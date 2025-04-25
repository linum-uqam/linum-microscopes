from abc import ABC, abstractmethod
from pathlib import Path

from linum_microscopes.controllers.abstract_camera import AbstractCamera
from linum_microscopes.controllers.abstract_stage import AbstractStage
from linum_microscopes.controllers.abstract_vibratome import AbstractVibratome


class AcquisitionStrategy(ABC):
    _data_path: Path = None

    def __init__(self, camera: AbstractCamera, vibratome: AbstractVibratome, stage: AbstractStage):
        self._camera = camera
        self._vibratome = vibratome
        self._stage = stage

    @property
    @abstractmethod
    def camera(self) -> AbstractCamera:
        raise NotImplementedError("Property not implemented")

    @camera.setter
    @abstractmethod
    def camera(self, value: AbstractCamera):
        raise NotImplementedError("Property not implemented")

    @property
    @abstractmethod
    def vibratome(self) -> AbstractVibratome:
        raise NotImplementedError("Property not implemented")

    @vibratome.setter
    @abstractmethod
    def vibratome(self, value: AbstractVibratome):
        raise NotImplementedError("Property not implemented")

    @property
    @abstractmethod
    def stage(self) -> AbstractStage:
        raise NotImplementedError("Property not implemented")

    @stage.setter
    @abstractmethod
    def stage(self, value: AbstractStage):
        raise NotImplementedError("Property not implemented")

    @abstractmethod
    def execute_strategy(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def execute_automated_strategy(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def single_acquisition(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def stop(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def initialise_data_path(self, path: str | Path):
        raise NotImplementedError("Method not implemented")

    @property
    def data_path(self) -> Path:
        return self._data_path

    @data_path.setter
    def data_path(self, value: str | Path):
        if isinstance(value, str):
            value = Path(value)
        self._data_path = value

    def is_running(self):
        return self.running

    def __del__(self):
        if self.running:
            self.stop()
