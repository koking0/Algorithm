from threading import Semaphore


class H2O:
    def __init__(self):
        self.hydrogenSema = Semaphore(2)
        self.oxygenSema = Semaphore(1)
        self.oxygenSema.acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogenSema.acquire()
        releaseHydrogen()
        if self.hydrogenSema._value == 0:
            self.oxygenSema.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygenSema.acquire()
        releaseOxygen()
        self.hydrogenSema.release()
        self.hydrogenSema.release()
