from abc import ABC, abstractmethod

from .device_thread import DeviceThread


class AbstractDevice(ABC):
    connected: bool
    _thread: DeviceThread
    config: dict

    def __init__(self, config: dict):
        self.connected = False
        self.config = config
        self.init_thread()

    @property
    def thread(self) -> DeviceThread:
        return self._thread

    @thread.setter
    def thread(self, value: DeviceThread):
        self._thread = value

    def init_thread(self):
        self._thread = DeviceThread()

    @abstractmethod
    def connect(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError("Method not implemented")

    def add_to_queue(self, name: str, action, *args, **kwargs):
        if name == "abort":
            self.thread.clear_queue()
        action = {"name": name,
                  "action": action,
                  "args": args,
                  "kwargs": kwargs}
        self.thread.add_to_queue(action)

    def is_connected(self):
        return self.connected

    def __del__(self):
        if self.connected:
            self.disconnect()
        self.thread.stop()
