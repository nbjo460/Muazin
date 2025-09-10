import string



class Tokenize:
    """

    """
    def __init__(self, _processed_str : str):
        self.processed_str = _processed_str

    def clean(self, split_by = ","):
        """
        Apply all the clean options, to one func.
        :return: str
        """
        self.processed_str = self.split(split_by)
        self.processed_str = self.lower_str()
        self.processed_str = self.remove_punctuation()
        self.processed_str = self.remove_special_symbols()
        return self.processed_str

    def split(self, split_by):
        return self.processed_str.split(split_by)

    def lower_str(self):
        processed_list_words = []
        for word in self.processed_str:
            word.lower()
            processed_list_words.append(word)
        return processed_list_words

    def remove_punctuation(self):
        processed_list_words = []
        translator = str.maketrans("", "", string.punctuation)
        for word in self.processed_str:
            word.translate(translator)
            processed_list_words.append(word)
        return processed_list_words

    def remove_special_symbols(self):
        import re
        processed_list_words = []
        for word in self.processed_str:
            edited_word = re.sub(r'\W+', ' ', word)
            processed_list_words.append(edited_word)
        return processed_list_words
