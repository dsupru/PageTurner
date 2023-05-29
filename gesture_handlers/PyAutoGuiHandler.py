import pyautogui
from .GestureHandler import GestureHandler

class PyAutoGuiGestureHandler(GestureHandler):
    def __init__(self, cooldownS):
        super().__init__(cooldownS)

    def event_action(self, action_name):
        if action_name == 'Thumb_Up':
            pyautogui.press('right')
        elif action_name == 'Pointing_Up':
            pyautogui.press('left')

