import base64
from src.utils.config import ClassifiedConfig
from collections import Counter
from src.process.tokenize import Tokenize
from trying import sum_commons


class Classified:
    def __init__(self):
        hostile_words_encoded = ClassifiedConfig.HOSTILE_WORDS
        less_hostile_words_encoded = ClassifiedConfig.LESS_HOSTILE_WORDS


        self.hostile_words = self.decrypt_base64_string(hostile_words_encoded)
        self.less_hostile_words = self.decrypt_base64_string(less_hostile_words_encoded)



    def classified(self, text : str) -> dict:
        metadate_expansion = {}
        danger_percents = self.calculate_percents(text)
        is_bds = self.is_indicted(danger_percents)
        bds_threat_level = self.threat_level(is_bds, danger_percents)

        metadate_expansion[ClassifiedConfig.BDS_PERCENT] = danger_percents
        metadate_expansion[ClassifiedConfig.IS_BDS] = is_bds
        metadate_expansion[ClassifiedConfig.BDS_THREAT_LEVEL] = bds_threat_level

        return metadate_expansion

    def calculate_percents(self, text):
        def count_commons_optimized(text, keywords) -> int:
            """

            :param text:
            :param keywords:
            :return:
            """
            tokenize_text = Tokenize(text).clean(" ")
            tokenize_keywords = Tokenize(keywords).clean(",")


            uniques_words = list(set(tokenize_text)&set(tokenize_keywords))
            counter = Counter(text)
            sum_commons = 0
            for word in uniques_words:
                    sum_commons += counter.get(word, 0)
            return sum_commons
        def count_commons(raw_text : str, keywords : str) -> int:
            sum_commons = 0
            for word in keywords:
                sum_commons += raw_text.count(word)
            return sum_commons
        def _sum_unique_words(text : str) -> int:
            split_text = text.split(",")
            set_text = set(split_text)
            return len(set_text)

        hostile_sum = count_commons(raw_text=text, keywords=self.hostile_words)
        less_hostile_sum = count_commons(raw_text=text, keywords=self.less_hostile_words) * 2
        sum_commons = hostile_sum + less_hostile_sum

        bds_percent = sum_commons / _sum_unique_words(text) * 100
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