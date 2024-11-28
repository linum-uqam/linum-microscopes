#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Function Generator Controller (JDS6600)"""
import time

# Communication protocol: https://joy-it.net/files/files/Produkte/JT-JDS6600/JT-JDS6600-Communication-protocol.pdf
# http://www.junteks.com/
# User Manual: http://68.168.132.244/JDS6600_EN_manual.pdf
# Communication protocol and software link: http://68.168.132.244/DDS_Setup.rar

import serial

# TODO: Set the default signal when starting the generator
# TODO: convert the EN undocumented commands (see the chinese doc)
# TODO: add property to know if the vibratome is running

SERIAL_PORT = "COM8"
AVAILABLE_WAVEFORMS = ['sine', 'square', 'pulse', 'triangular', 'partial_sine', 'CMOS', 'dc',
                       'half_wave', 'full_wave', 'noise', 'exponential', 'exponential_decay',
                       'multi-tone', 'sinc', 'lorenz']


class FunctionGeneratorJDS6600:
    def __init__(self, port: str = SERIAL_PORT):
        # Connect to the stage xyz and wake it up
        self.serial = serial.Serial(
            port=port,
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )

    def __del__(self):
        self.serial.close()

    def write_command(self, command: str) -> str:
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()

        # Prepare the command
        command_encoded = command
        if not command_encoded.endswith("\r\n"):
            command_encoded += "\r\n"
        command_encoded = str.encode(command_encoded)

        # Send the command and wait for a response
        self.serial.write(command_encoded)
        time.sleep(0.05)  # Wait a few milliseconds for the response to be ready

        # Read the response
        response = self.serial.readline().strip().decode("utf-8")
        return response

    def arm(self):
        """Arm the vibratome"""
        self.set_waveform("pulse", channel=2)
        self.set_frequency(1.0, channel=2)
        self.set_amplitude(5.0, channel=2)
        self.set_duty_cycle(100, channel=2)
        self.enable(channel_1=False, channel_2=True)

    def unarm(self):
        """Unarm the vibratome"""
        self.set_waveform("pulse", channel=2)
        self.set_frequency(1.0, channel=2)
        self.set_amplitude(5.0, channel=2)
        self.set_duty_cycle(0, channel=2)
        self.enable(channel_1=False, channel_2=True)

    def set_waveform(self, waveform: str, channel: int = 1):
        """Set the waveform of the function generator.
        Parameters
        ----------
        waveform : str
            The waveform to set. Available waveforms are:
            - 'sine'
            - 'square'
            - 'pulse'
            - 'triangular'
            - 'partial_sine'
            - 'CMOS'
            - 'dc'
            - 'half_wave'
            - 'full_wave'
            - 'noise'
            - 'exponential'
            - 'exponential_decay'
            - 'multi-tone'
            - 'sinc'
            - 'lorenz'
        channel : int
            The channel to set the waveform to.
        """
        # TODO: add option for arbitrary waveform between 101 to 160
        assert waveform in AVAILABLE_WAVEFORMS, f"Waveform {waveform} not available. Available waveforms: {AVAILABLE_WAVEFORMS}"
        assert channel in [1, 2], f"Channel {channel} not available. Available channels: {[1, 2]}"

        # Prepare the command
        if channel == 1:
            channel_code = 21
        else:
            channel_code = 22
        command = f":w{channel_code}={AVAILABLE_WAVEFORMS.index(waveform)}.\r\n"
        response = self.write_command(command)
        assert response == ":ok", "Something went wrong!"

    def get_waveform(self) -> str:
        command = ":r21=."
        response = self.write_command(command)
        response = response.replace(":r21=", "").strip(".\r\n")
        waveform_ch1 = AVAILABLE_WAVEFORMS[int(response)]
        command = ":r22=."
        response = self.write_command(command)
        response = response.replace(":r22=", "").strip(".\r\n")
        waveform_ch2 = AVAILABLE_WAVEFORMS[int(response)]

        return waveform_ch1, waveform_ch2

    def set_frequency(self, frequency: float, channel: int = 1, unit: str = "Hz"):
        """Set the frequency of the function generator.
        Parameters
        ----------
        frequency : float
            The frequency to set.
        channel : int
            The channel to set the frequency. Either 1 or 2
        unit: str
            Frequency unit. Available units are: 'Hz', 'KHz', 'MHz', 'mHz' and 'uHz'.
        """
        AVAILABLE_UNITS = ["Hz", "KHz", "MHz", "mHz", "uHz"]
        assert channel in [1, 2], "Channel must be 1 or 2"
        assert unit in AVAILABLE_UNITS, "Unit must be one of {}".format(AVAILABLE_UNITS)

        # Prepare the command
        command = ""
        if channel == 1:
            command += ":w23="
        else:
            command += ":w24="

        # Add the frequency and the unit
        if unit == 'Hz':
            command += f"{int(frequency / 0.01)},{AVAILABLE_UNITS.index(unit)}."
        elif unit == 'KHz':
            command += f"{int(frequency * 1e3 / 0.01)},{AVAILABLE_UNITS.index(unit)}."
        elif unit == 'MHz':
            command += f"{int(frequency * 1e6 / 0.01)},{AVAILABLE_UNITS.index(unit)}."
        else:
            command += f"{int(frequency / 0.01)},{AVAILABLE_UNITS.index(unit)}."
        response = self.write_command(command)
        assert response == ":ok", "Something went wrong!"

    def get_frequency(self):
        """Get the frequency of the function generator.
        Returns
        -------
        frequency : float
            The frequency of the function generator.
        unit : str
            The unit of the frequency.
        """
        command = ":r23=."
        response = self.write_command(command)
        response = response.replace(":r23=", "").strip(".\r\n").split(",")
        frequency = int(response[0]) * 0.01
        unit = ["Hz", "KHz", "MHz", "mHz", "uHz"][int(response[1])]
        if unit == 'KHz':
            frequency /= 1e3
        elif unit == 'MHz':
            frequency /= 1e6
        return frequency, unit

    def enable(self, channel_1: bool = True, channel_2: bool = False):
        """Enable the output of the function generator.
        Parameters
        ----------
        channel_1 : bool
            Enable the output of channel 1.
        channel_2 : bool
            Enable the output of channel 2.
        """
        command = f":w20={int(channel_1)},{int(channel_2)}."
        _ = self.write_command(command)

    def disable(self, channel_1: bool = True, channel_2: bool = True):
        """Disable the output of the function generator.
        Parameters
        ----------
        channel_1 : bool
            Disable the output of channel 1.
        channel_2 : bool
            Disable the output of channel 2.
        """
        command = f":w20={int(not channel_1)},{int(not channel_2)}."
        _ = self.write_command(command)

    def set_amplitude(self, value: float, channel: int = 1):
        """Set the amplitude of the function generator.
        Parameters
        ----------
        value : float
            The amplitude to set in volts (half of the waveform range)
        channel : int
            The channel to set the range. Either 1 or 2
        Notes
        -----
        * The signal generator displays the range instead of the amplitude.
        """
        assert channel in [1, 2], "Channel must be 1 or 2"
        assert 0 <= value <= 10, "Value must be between 0 and 10V"

        # Prepare the command
        command = ""
        if channel == 1:
            command += ":w25="
        else:
            command += ":w26="

        # Add the value
        command += f"{int(value * 2 / 0.001)}."
        response = self.write_command(command)
        assert response == ":ok", "Something went wrong!"

    def get_amplitude(self, channel: int = 1):
        """Get the amplitude of the function generator.
        Parameters
        ----------
        channel : int
            The channel to get the range. Either 1 or 2
        Returns
        -------
        value : float
            The amplitude of the function generator in volts.
        Notes
        -----
        * The signal generator displays the range instead of the amplitude.
        """
        assert channel in [1, 2], "Channel must be 1 or 2"

        command = ""
        if channel == 1:
            base = ":r25="
        elif command == 2:
            base = ":r26="
        command += base
        command += "."

        response = self.write_command(command)
        response = response.replace(base, "").strip(".\r\n")
        value = int(response) * 0.001 / 2
        return value

    def set_duty_cycle(self, duty_cycle: float, channel: int = 1):
        """Set the duty cycle (between 0.0 and 100.
        Parameters
        ----------
        duty_cycle : float
            The duty cycle to set, between 0.0 and 100.
        channel : int
            The channel to set the range. Either 1 or 2
        """
        assert channel in [1, 2], "Channel must be 1 or 2"
        assert 0 <= duty_cycle <= 100, "duty_cycle must be between 0 and 100"
        if channel == 1:
            command = f":w29={int(duty_cycle * 10)}."
        else:
            command = f":w30={int(duty_cycle * 10)}."
        response = self.write_command(command)
        assert response == ":ok", "Something went wrong!"

    def get_duty_cycle(self, channel: int = 1) -> float:
        """Get the duty cycle of the function generator.
        Parameters
        ----------
        channel : int
            The channel to get the range. Either 1 or 2
        Returns
        -------
        duty_cycle : float
            The duty cycle between 0.0 and 100.0
        """
        assert channel in [1, 2], " Channel must be 1 or 2"
        if channel == 1:
            base = ":r29="
        else:
            base = ":r30="
        command = base + "."
        response = self.write_command(command)
        response = response.replace(base, "").strip(".\r\n")
        duty_cycle = float(response) / 10.0
        return duty_cycle

    def set_bias(self, value: float, channel: int = 1):
        """Set the offset of the function generator.
        Parameters
        ----------
        value : float
            The bias to set in volts, between -9.99V and 9.99V
        channel: int
            The channel to set the range. Either 1 or 2.
        """
        assert channel in [1, 2], "Channel must be 1 or 2"
        assert -9.99 <= value <= 9.99, "Value must be between -9.99V and 9.99V"
        bias = int(value * 100 + 1000)
        if channel == 1:
            command = f":w27={bias}."
        elif channel == 2:
            command = f":w28={bias}."
        response = self.write_command(command)
        assert response == ":ok", "Something went wrong!"

    def get_bias(self, channel: int = 1) -> float:
        """Get the bias of the function generator.
        Parameters
        ----------
        channel : int
            The channel to get the range. Either 1 or 2
        Returns
        -------
        bias : float
            The bias of the function generator in volts.
        """
        assert channel in [1, 2], "Channel must be 1 or 2"
        if channel == 1:
            base = ":r27="
        else:
            base = ":r28="
        command = base + "."
        response = self.write_command(command)
        response = int(response.replace(base, "").strip(".\r\n"))
        bias = (response - 1000) / 100
        return bias

    def set_phase(self, phase: float):
        """Set the phase (in degrees) of channel 1.
        Parameters
        ----------
        phase : float
            The phase to set in degrees (between 0 and 360).
        """
        assert 0 <= phase <= 360, "Phase must be between 0 and 360"
        phase = int((phase % 360) * 10)
        command = f":w31={phase}."
        response = self.write_command(command)
        assert response == ":ok", "Something went wrong!"

    def get_phase(self) -> float:
        """Get the phase in degrees (between 0 and 360)."""
        base = ":r31="
        command = base + '.'
        response = self.write_command(command)
        response = int(response.replace(base, "").strip(".\r\n"))
        phase = response / 10.0
        return phase