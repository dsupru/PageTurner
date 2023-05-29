from .GestureHandler import GestureHandler
from .PyAutoGuiHandler import PyAutoGuiGestureHandler
from .GestureHandler import GestureHandler

def build_gesture_handler(handler_type, cooldownS) -> GestureHandler:
    if handler_type == 'arrows':
        return PyAutoGuiGestureHandler(cooldownS)
    else:
        raise NotImplementedError('No other handler were implemented')
    
