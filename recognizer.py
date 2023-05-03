import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class Recognizer:
    model_path = './hand_landmarker.task'
    BaseOptions = mp.tasks.BaseOptions
    HandLandmarker = mp.tasks.vision.HandLandmarker
    HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
    HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
    VisionRunningMode = mp.tasks.vision.RunningMode

    def __init__(self, process_results_callback):
        self.options = Recognizer.HandLandmarkerOptions(
            base_options= Recognizer.BaseOptions(model_asset_path=Recognizer.model_path),
            running_mode=Recognizer.VisionRunningMode.LIVE_STREAM,
            result_callback=process_results_callback)
        self.recognizer = Recognizer.HandLandmarker.create_from_options(self.options)

    def recognize(self, image, timestamp_ms):
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        self.recognizer.detect_async(mp_image, int(timestamp_ms))

