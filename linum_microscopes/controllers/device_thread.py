import logging
import time

from PySide6.QtCore import QThread, Signal


class DeviceThread(QThread):
    actions: list
    frequency: float
    _busy: bool
    sig_stage_action_done: Signal = Signal(str)
    sig_current_action: Signal = Signal(str)

    def __init__(self, parent=None, frequency: float = 1 / 30.0):
        super().__init__(parent=parent)
        self.frequency = frequency
        self.actions = []

    def add_to_queue(self, action: dict):
        self.actions.append(action)

    def clear_queue(self):
        self.actions.clear()

    def process_next_action(self):
        if len(self.actions) == 0:
            return

        current_action = self.actions.pop(0)
        action = current_action["action"]
        name = current_action["name"]
        args = current_action["args"]
        kwargs = current_action["kwargs"]

        msg = f"Processing: {name}"
        logging.info(msg)
        self.sig_current_action.emit(msg)

        # Processing the action
        self._busy = True
        action(*args, **kwargs)
        self._busy = False

        # Post action processing
        self.sig_stage_action_done.emit(action)

    def run(self):
        while not self.isInterruptionRequested():
            self.process_next_action()
            time.sleep(self.frequency)

    def stop(self):
        self.requestInterruption()
        self.wait()

    @property
    def is_busy(self):
        return self._busy
