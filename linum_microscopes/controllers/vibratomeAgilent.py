from pymeasure.instruments.agilent import Agilent33220A
import pyfirmata2

id = "USB0::0x0957::0x0407::MY44013298::INSTR"

"""Agilent Function Generator Controller (33220A) used for the vibratome"""

import time
from linum_microscopes.controllers.abstractDevice import AbstractDeviceThread
from tqdm.auto import tqdm
import random
import numpy as np

SERIAL_PORT = "USB0::0x0957::0x0407::MY44013298::INSTR"
ARDUINO_SERIAL_PORT = "COM6"


class Vibratome:
    def __init__(self, port: str = SERIAL_PORT):
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
        self.config = dict()
        self.config['enabled'] = self._enabled
        self.config['frequency'] = self.get_frequency()
        self.config['amplitude'] = self.get_amplitude()

    def start_blade(self):
        self.enable()
        self.device.output = True

    def stop_blade(self):
        self.disable()
        self.device.output = False

    def set_frequency(self, frequency: float):
        """Set the frequency of the function generator.
        Parameters
        ----------
        frequency : float
            The frequency to set in Hz
        """
        self.device.frequency = frequency

    def get_frequency(self):
        """Get the frequency of the function generator.
        Returns
        -------
        frequency : float
            The frequency of the function generator in Hz
        """
        return self.device.frequency

    def set_amplitude(self, value: float):
        """Set the amplitude of the function generator.
        Parameters
        ----------
        value : float
            The amplitude to set in volts (half of the waveform range)
        """
        assert 0 <= value <= 10, "Value must be between 0 and 10V"
        self.device.amplitude = value

    def get_amplitude(self):
        """Get the amplitude of the function generator.
        Returns
        -------
        value : float
            The amplitude of the function generator in volts.
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
    def configuration(self) -> dict:
        self.device.update_config()
        return self.device.config


def test_vibratome(n_tests: int = 25, sleep_time: float = 0.1, enabled=True, disabled=False):
    # Initialize the vibratome
    vibratome = Vibratome()
    n_fails = 0
    freq = 30.0  # Hz
    amplitude = 2.5  # V

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
    # return error_rate_disabled, error_rate_enabled


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
