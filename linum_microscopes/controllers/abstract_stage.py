from abc import ABC, abstractmethod

from PySide6.QtCore import Signal


class AbstractStage(ABC):
    origin_position: list
    _position: list
    _speed: float
    _acceleration: float
    _state: str
    sig_stage_action_done = Signal(str)
    sig_current_action = Signal(str)
    sig_stage_position = Signal(float, float, float)

    def __init__(self):
        pass

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
    def move_to(self, x: float, y: float, z: float = None, blocking: bool = False):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def move_by(self, dx: float, dy: float, dz: float = None, blocking: bool = False):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def abort(self):
        raise NotImplementedError("Method not implemented")
