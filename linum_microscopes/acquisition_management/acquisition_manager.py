from .acquisition_strategy import AcquisitionStrategy


class AcquisitionManager:
    strategy: AcquisitionStrategy = None

    def __init__(self, strategy: AcquisitionStrategy):
        self.strategy = strategy

    def acquire(self):
        self.strategy.execute_strategy()

    def acquire_automated(self):
        self.strategy.execute_automated_strategy()

    def stop(self):
        self.strategy.stop()

    def __del__(self):
        self.stop()
