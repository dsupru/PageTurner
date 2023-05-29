from .mediapipe_recognizer import MediaPipeRecognizer
from .base_recognizer import BaseRecognizer

def build_recognizer(kind, callback):
    if kind == 'hand_gesture':
        return MediaPipeRecognizer(callback)
    else:
        raise NotImplementedError('No other recognizers were implemented')

