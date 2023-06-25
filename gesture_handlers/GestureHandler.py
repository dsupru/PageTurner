from time import sleep, time

# Base class for event handling
# Provides a common implementation of event handling
# Uses a lock as a way to prevent events firing in a rapid succession
class GestureHandler:
    def __init__(self, cooldownS):
        self.cooldownS = cooldownS
        self.inActionStartTime = 0

    # is overwritten in a child class
    def event_action(self):
        raise NotImplementedError

    def isReady(self):
        return self.inActionStartTime == 0 \
                or time() - self.inActionStartTime > self.cooldownS * 1000

    def event_callback(self, action_name):
        if self.isReady():
            self.inActionStartTime = time()
            self.event_action(action_name)

