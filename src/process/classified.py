import base64
from src.utils.config import ClassifiedConfig
class Classified:
    def __init__(self):
        hostile_words_encoded = ClassifiedConfig.HOSTILE_WORDS
        less_hostile_words_encoded = ClassifiedConfig.LESS_HOSTILE_WORDS

        self.hostile_words = self.decrypt_base64_string(hostile_words_encoded)
        self.less_hostile_words = self.decrypt_base64_string(less_hostile_words_encoded)

        print(self.hostile_words, self.less_hostile_words)

    def calculate_percents(self):
        bds_percent = None
        return bds_percent
    def is_bds_classified(self):
        is_bds = None
        return is_bds
    def threat_level(self):
        bds_threat_level = None
        return bds_threat_level

    @staticmethod
    def decrypt_base64_string(raw_str : str):
        base64_bytes = raw_str.encode('utf-8')
        decoded_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_bytes.decode("utf-8")
        return decoded_string

a = Classified()
