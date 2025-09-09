import base64
from src.utils.config import ClassifiedConfig
from collections import Counter
class Classified:
    def __init__(self):
        hostile_words_encoded = ClassifiedConfig.HOSTILE_WORDS
        less_hostile_words_encoded = ClassifiedConfig.LESS_HOSTILE_WORDS

        self.hostile_words = self.decrypt_base64_string(hostile_words_encoded)
        self.less_hostile_words = self.decrypt_base64_string(less_hostile_words_encoded)

        print(self.hostile_words, self.less_hostile_words)

    def classified(self, text : str):
        danger_percents = self.calculate_percents()
        is_bds = self.is_indicted(danger_percents)
        bds_threat_level = self.threat_level(is_bds, danger_percents)

    def calculate_percents(self):
        bds_percent = None
        return bds_percent

    @staticmethod
    def is_indicted(danger_percents : float) -> bool:
        if danger_percents > ClassifiedConfig.INDICTED_LEVEL: return True
        else: return False

    @staticmethod
    def threat_level(_is_bds, _danger_percents):
         if _is_bds:
             if _danger_percents > ClassifiedConfig.HIGH_LEVEL: return ClassifiedConfig.HIGH
             else: return ClassifiedConfig.MEDIUM
         return ClassifiedConfig.NONE



    @staticmethod
    def decrypt_base64_string(raw_str : str):
        base64_bytes = raw_str.encode('utf-8')
        decoded_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_bytes.decode("utf-8")
        return decoded_string

    def study(self):
        listi1 = ["12345", "12345", "12345", "23456", "67890"]
        listi2 = ["12345", "67890", "aaaaa", "bbbbb"]
        a = list(set(listi1) & set(listi2))
        counter1 = Counter(listi1)
        sum = {}
        for part in a:
            count1 = counter1.get(part, 0)
            sum[part] = count1
        print(sum)

if __name__ == "__main__":
    a = Classified()
    a.study()