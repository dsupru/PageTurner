class BaseRecognizer:
    def __init__(self):
        pass

    def recognize(self, image, timestamp_ms):
        raise NotImplementedError

