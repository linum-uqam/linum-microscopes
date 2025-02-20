from abc import abstractmethod

from .abstract_device import AbstractDevice


class AbstractVibratome(AbstractDevice):
    frequency: float
    amplitude: float

    def __init__(self, config: dict):
        super().__init__(config)

    @property
    @abstractmethod
    def frequency(self) -> float:
        raise NotImplementedError("Property not implemented")

    @frequency.setter
    @abstractmethod
    def frequency(self, value: float):
        raise NotImplementedError("Property not implemented")

    @property
    @abstractmethod
    def amplitude(self) -> float:
        raise NotImplementedError("Property not implemented")

    @amplitude.setter
    @abstractmethod
    def amplitude(self, value: float):
        raise NotImplementedError("Property not implemented")

    @property
    @abstractmethod
    def is_vibrating(self):
        raise NotImplementedError("Property not implemented")

    @abstractmethod
    def start(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def stop(self):
        raise NotImplementedError("Method not implemented")

    def __del__(self):
        self.stop()
