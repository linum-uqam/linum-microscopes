from abc import ABC, abstractmethod

class AbstractCamera(ABC):

    def __init__(self):
        pass

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
