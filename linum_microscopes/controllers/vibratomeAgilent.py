from pymeasure.instruments.agilent import Agilent33220A
import pyfirmata2

id = "USB0::0x0957::0x0407::MY44013298::INSTR"

"""Function Generator Controller (JDS6600)"""
import time
from linum_microscopes.config import config
from linum_microscopes.controllers.abstractDevice import AbstractDeviceThread
import logging
from tqdm.auto import tqdm
import random
import numpy as np

import serial

# TODO: Set the default signal when starting the generator
# TODO: convert the EN undocumented commands (see the chinese doc)
# TODO: add property to know if the vibratome is running
# FIXME: we often have serial write timeout errors

SERIAL_PORT = "USB0::0x0957::0x0407::MY44013298::INSTR"
ARDUINO_SERIAL_PORT = "COM6"


class Vibratome:
    def __init__(self, port: str = SERIAL_PORT):
        # Connect to the stage xyz and wake it up
        self.device = Agilent33220A(SERIAL_PORT)
        self._enabled = False

        # Initializing the arduino board used to enable/disable the voicecoil driver
        self.board = pyfirmata2.Arduino(ARDUINO_SERIAL_PORT)
        self.disable()

        # Connect to the function generator device
        self.device = Agilent33220A(port)
        self.config = dict()

        # Configure the device with default parameters
        self.device.shape = "SINUSOID"
        self.set_frequency(30.0)
        self.set_amplitude(1.0)

    def __del__(self):
        self.stop_blade()
        self.device.shutdown()
        self.board.exit()

    def update_config(self):
        self.config['enabled'] = self._enabled
        # self.config['channel_1'] = dict()
        # self.config['channel_1']['waveform'] = self.get_waveform()
        # self.config['channel_1']['frequency'] = self.get_frequency()
        # self.config['channel_1']['amplitude'] = self.get_amplitude()
        # self.config['channel_1']['phase'] = self.get_phase()
        # self.config['channel_1']['duty_cycle'] = self.get_duty_cycle()
        # self.config['channel_1']['bias'] = self.get_bias()


    def start_blade(self):
        self.enable()
        self.device.output = True
        self._enabled = True

    def stop_blade(self):
        self.disable()
        self.device.output = False
        self._enabled = False

    # def set_waveform(self, waveform: str, channel: int = 1):
    #     """Set the waveform of the function generator.
    #     Parameters
    #     ----------
    #     waveform : str
    #         The waveform to set. Available waveforms are:
    #         - 'sine'
    #         - 'square'
    #         - 'pulse'
    #         - 'triangular'
    #         - 'partial_sine'
    #         - 'CMOS'
    #         - 'dc'
    #         - 'half_wave'
    #         - 'full_wave'
    #         - 'noise'
    #         - 'exponential'
    #         - 'exponential_decay'
    #         - 'multi-tone'
    #         - 'sinc'
    #         - 'lorenz'
    #     channel : int
    #         The channel to set the waveform to.
    #     """
    #     # TODO: add option for arbitrary waveform between 101 to 160
    #     assert waveform in AVAILABLE_WAVEFORMS, f"Waveform {waveform} not available. Available waveforms: {AVAILABLE_WAVEFORMS}"
    #     assert channel in [1, 2], f"Channel {channel} not available. Available channels: {[1, 2]}"
    #
    #     # Prepare the command
    #     if channel == 1:
    #         channel_code = 21
    #     else:
    #         channel_code = 22
    #     command = f":w{channel_code}={AVAILABLE_WAVEFORMS.index(waveform)}.\r\n"
    #     response = self.write_command(command)
    #     assert response == ":ok", "Something went wrong!"

    # def get_waveform(self) -> str:
    #     command = ":r21=."
    #     response = self.write_command(command)
    #     response = response.replace(":r21=", "").strip(".\r\n")
    #     waveform_ch1 = AVAILABLE_WAVEFORMS[int(response)]
    #     command = ":r22=."
    #     response = self.write_command(command)
    #     response = response.replace(":r22=", "").strip(".\r\n")
    #     waveform_ch2 = AVAILABLE_WAVEFORMS[int(response)]
    #
    #     return waveform_ch1, waveform_ch2

    def set_frequency(self, frequency: float):
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
        self.device.frequency = frequency

    def get_frequency(self, channel: int=1):
        """Get the frequency of the function generator.
        Returns
        -------
        frequency : float
            The frequency of the function generator.
        unit : str
            The unit of the frequency.
        """
        return self.device.frequency

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
        rsp = self.write_command(command)

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

    def set_amplitude(self, value: float):
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
        assert 0 <= value <= 10, "Value must be between 0 and 10V"
        self.device.amplitude = value

    def get_amplitude(self):
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
        return self.device.amplitude

    def enable(self):
        """Enable the vibratome."""
        self.board.digital[2].write(1)
        self._enabled = True

    def disable(self):
        """Disable the vibratome."""
        self.board.digital[2].write(0)
        self._enabled = False

    @property
    def is_vibrating(self) -> bool:
        """Return True if the vibratome is vibrating."""
        return self._enabled and self.device.output

    # def set_phase(self, phase: float):
    #     """Set the phase (in degrees) of channel 1.
    #     Parameters
    #     ----------
    #     phase : float
    #         The phase to set in degrees (between 0 and 360).
    #     """
    #     assert 0 <= phase <= 360, "Phase must be between 0 and 360"
    #     phase = int((phase % 360) * 10)
    #     command = f":w31={phase}."
    #     response = self.write_command(command)
    #     assert response == ":ok", "Something went wrong!"
    #
    # def get_phase(self) -> float:
    #     """Get the phase in degrees (between 0 and 360)."""
    #     base = ":r31="
    #     command = base + '.'
    #     response = self.write_command(command)
    #     response = int(response.replace(base, "").strip(".\r\n"))
    #     phase = response / 10.0
    #     return phase

class VibratomeThread(AbstractDeviceThread):
    def __init__(self):
        super().__init__()
        self.device = Vibratome()
    def start_blade(self):
        name = "Starting the blade"
        action = self.device.start_blade
        self.addAction(name, action, force=True)

    def stop_blade(self):
        name = "Stopping the blade"
        action = self.device.stop_blade
        self.addAction(name, action, force=False)

    @property
    def is_vibrating(self):
        return NotImplementedError

    @property
    def configuration(self) -> dict:
        self.device.update_config()
        return self.device.config

def test_vibratome(n_tests: int=25, sleep_time: float=0.1, enabled=True, disabled=False):
    # Initialize the vibratome
    vibratome = Vibratome()
    n_fails = 0
    freq = 30.0 # Hz
    amplitude = 2.5 # V

    if disabled:
        # Testing the communication with a disabled generator
        for _ in tqdm(range(n_tests), desc="Disabled vibratome test"):
            try:
                _ = vibratome.get_frequency()
                time.sleep(sleep_time)
            except Exception as e:
                print(f"Something went wrong! ({e})")
                n_fails += 1
        error_rate_disabled = n_fails / n_tests
        message = f"Disabled generator error rate (# fail/# tests): {n_fails}/{n_tests} ({n_fails / n_tests * 100:.2f}%)"

        print(message)

    # Testing the communication with an enabled generator
    if enabled:
        vibratome.set_amplitude(amplitude)
        vibratome.set_frequency(freq)
        vibratome.start_blade()
        n_fails = 0
        for _ in tqdm(range(n_tests), desc="Enabled vibratome test"):
            this_wait_time = random.uniform(0, sleep_time)
            try:
                _ = vibratome.get_frequency()
                time.sleep(this_wait_time)
            except Exception as e:
                print(f"Something went wrong (wait time: {this_wait_time:.3e}s)! ({e})")
                n_fails += 1
        message = f"Enabled generator error rate (# fail/# tests): {n_fails}/{n_tests} ({n_fails / n_tests * 100:.2f}%)"
        error_rate_enabled = n_fails / n_tests
        print(message)


    del vibratome
    #return error_rate_disabled, error_rate_enabled




def test():
    with Agilent33220A(id) as device:
        # Make a beep
        device.beep()

        # Get the frequency
        print(f"The frequency is: {device.frequency} Hz")

        # Check the output status
        print(f"The output is : {device.output}")

        # Configure the vibratome
        device.shape = "SINUSOID"  # Sets a sine waveform
        device.amplitude = 2  # Set amplitude of 1 V
        device.offset = 0  # Set the amplitude to 0 V
        device.frequency = 30.0  # Sets the frequency to 30Hz
        device.output = True

        time.sleep(10)

        device.output = False


def calibrate_resonance_frequency(start_freq: float, stop_freq: float, step: float, amplitude: float, on_time: float=2, off_time: float=0.5):
    # Initialize the vibratome
    vibratome = Vibratome()
    vibratome.set_amplitude(amplitude)

    frequencies = np.arange(start_freq, stop_freq, step)
    for freq in tqdm(frequencies, desc="Frequency test"):
        vibratome.device.beep()
        vibratome.set_frequency(freq)
        vibratome.start_blade()
        time.sleep(on_time)
        vibratome.stop_blade()
        time.sleep(off_time)


    del vibratome