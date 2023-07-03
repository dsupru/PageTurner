import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from .base_recognizer import BaseRecognizer

class MediaPipeRecognizer(BaseRecognizer):
    model_path = './gesture_recognizer.task'
    BaseOptions = mp.tasks.BaseOptions
    GestureRecognizer = mp.tasks.vision.GestureRecognizer
    GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
    GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
    VisionRunningMode = mp.tasks.vision.RunningMode

    def __init__(self, process_results_callback):
        self.process_results_callback = process_results_callback
        def processed_callback(result, output_image, timestamp_ms: int):
            if result != None and result.gestures != []:
                action = result.gestures[0][0].category_name
                self.process_results_callback(action)

        self.options = MediaPipeRecognizer.GestureRecognizerOptions(
            base_options= MediaPipeRecognizer.BaseOptions(model_asset_path=MediaPipeRecognizer.model_path),
            running_mode=MediaPipeRecognizer.VisionRunningMode.LIVE_STREAM,
            result_callback=processed_callback)
        self.recognizer = MediaPipeRecognizer.GestureRecognizer.create_from_options(self.options)

    def recognize(self, image, timestamp_ms):
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        self.recognizer.recognize_async(mp_image, int(timestamp_ms))

