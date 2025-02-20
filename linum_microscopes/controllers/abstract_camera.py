from abc import abstractmethod

from .abstract_device import AbstractDevice

class AbstractCamera(AbstractDevice):

    def __init__(self, config: dict):
        super().__init__(config)

    @abstractmethod
    def save_data(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def return_data(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_camera_settings(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def set_camera_settings(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def set_acquisition_mode(self):
        raise NotImplementedError("Method not implemented")
