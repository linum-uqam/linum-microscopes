from abc import ABC, abstractmethod

from linum_microscopes.controllers import DeviceThread


class AbstractDevice(ABC):
    connected: bool
    thread: DeviceThread
    config: dict

    def __init__(self, config: dict):
        self.connected = False
        self.thread = DeviceThread()
        self.config = config

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
