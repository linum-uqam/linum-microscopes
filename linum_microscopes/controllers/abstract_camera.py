from abc import abstractmethod

import numpy as np

from .abstract_device import AbstractDevice

class AbstractCamera(AbstractDevice):

    def __init__(self, config: dict):
        super().__init__(config)

    @abstractmethod
    def save_data(self ,path: str):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def return_data(self) -> np.ndarray:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_camera_settings(self) -> dict:
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def set_camera_settings(self, settings: dict):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def set_acquisition_mode(self, mode: str):
        raise NotImplementedError("Method not implemented")
