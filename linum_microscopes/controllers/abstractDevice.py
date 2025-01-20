#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Abstract Device Class and Thread"""

import time
from pathlib import Path

from PySide6.QtCore import QThread, Signal
import logging


logging.basicConfig(
    format=f"%(levelname)s - %(asctime)s [{Path(__file__).name}:%(lineno)s | %(funcName)s()] %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S")

class AbstractDeviceThread(QThread):
    actions = []
    sig_stage_action_done = Signal(str)
    sig_current_action = Signal(str)

    def __init__(self, parent=None, frequency: float = 1 / 30.0):
        super().__init__(parent=parent)
        self.frequency = frequency
        self._busy = False

    def addAction(self, name: str, action, *args, **kwargs):
        if name == "abort":
            self.actions.clear()
        self.actions.append({"name": name,
                             "action": action,
                             "args": args,
                             "kwargs": kwargs}
                            )
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
