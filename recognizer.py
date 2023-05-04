import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class Recognizer:
    model_path = './gesture_recognizer.task'
    BaseOptions = mp.tasks.BaseOptions
    GestureRecognizer = mp.tasks.vision.GestureRecognizer
    GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
    GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
    VisionRunningMode = mp.tasks.vision.RunningMode

    def __init__(self, process_results_callback):
        self.options = Recognizer.GestureRecognizerOptions(
            base_options= Recognizer.BaseOptions(model_asset_path=Recognizer.model_path),
            running_mode=Recognizer.VisionRunningMode.LIVE_STREAM,
            result_callback=process_results_callback)
        self.recognizer = Recognizer.GestureRecognizer.create_from_options(self.options)

    def recognize(self, image, timestamp_ms):
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        self.recognizer.recognize_async(mp_image, int(timestamp_ms))

