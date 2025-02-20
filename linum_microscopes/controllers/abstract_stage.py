from abc import abstractmethod

from .abstract_device import AbstractDevice


class AbstractStage(AbstractDevice):
    origin_position: list = [0.0, 0.0, 0.0]
    _position: list
    _speed: float
    _acceleration: float
    _state: str

    def __init__(self, config: dict, ):
        super().__init__(config)

    @property
    @abstractmethod
    def position(self) -> list:
        raise NotImplementedError("Method not implemented")

    @property
    @abstractmethod
    def speed(self) -> float:
        raise NotImplementedError("Method not implemented")

    @speed.setter
    @abstractmethod
    def speed(self, value: float):
        raise NotImplementedError("Method not implemented")

    @property
    @abstractmethod
    def acceleration(self) -> float:
        raise NotImplementedError("Method not implemented")

    @acceleration.setter
    @abstractmethod
    def acceleration(self, value: float):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def home(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def move_to(self, x: float = None, y: float = None, z: float = None, blocking: bool = False, speed: float = 500):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def move_by(self, dx: float = None, dy: float = None, dz: float = None, blocking: bool = False, speed: float = 500):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def abort(self):
        raise NotImplementedError("Method not implemented")
