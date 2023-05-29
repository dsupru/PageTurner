from threading import Lock
from time import sleep

# Uses a lock as a way to prevent events firing in a rapid succession
class GestureHandler:
    def __init__(self, cooldownS):
        self.gesturelock = Lock()
        self.cooldownS = cooldownS

    def event_action(self):
        raise NotImplementedError

    def event_callback(self):
        locked = self.gestureLock.acquire(
                blocking=False,
                timeout=self.cooldownS
        )

        if locked:
            self.event_action()
            sleep(self.cooldownS)
            self.gesturelock.release()

