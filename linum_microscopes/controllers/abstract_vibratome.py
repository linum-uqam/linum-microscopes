from abc import ABC, abstractmethod


class AbstractVibratome(ABC):
    frequency: float
    amplitude: float

    def __init__(self):
        pass

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
