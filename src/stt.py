import json

from vosk import Model, KaldiRecognizer
import wave
from src.utils.config import SttConfig

class Stt:
    def __init__(self):
        model_path = SttConfig.MODEL_PATH
        self.model = Model(model_path)

    def convert_speach_to_text(self, file_path):
        wf = wave.open(file_path, "rb")
        rec = self._config_rec(wf)
        text = []
        while True:
            data = wf.readframes(4000)  # Read audio in chunks
            if len(data) == 0: break
            if rec.AcceptWaveform(data): text.append(json.loads(rec.Result())["text"])

        text.append(json.loads(rec.FinalResult())["text"])

        final_txt = ".\n".join(text)
        return final_txt

    def _config_rec(self, wf):
        rec = KaldiRecognizer(self.model, wf.getframerate())
        rec.SetWords(True)
        rec.SetPartialWords(True)
        return rec