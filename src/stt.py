import json
from pathlib import Path
from vosk import Model, KaldiRecognizer
import wave
from src.utils.config import SttConfig
from src.utils.logger import Logger

class Stt:
    def __init__(self):
        model_path = SttConfig.MODEL_PATH
        self.model = Model(model_path)
        self.logger = Logger().get_logger()

    def transcription(self, file_path):
        wf = wave.open(file_path, "rb")
        rec = self._config_rec(wf)
        text = []
        while True:
            data = wf.readframes(4000)  # Read audio in chunks
            if len(data) == 0: break
            if rec.AcceptWaveform(data): text.append(json.loads(rec.Result())["text"])

        text.append(json.loads(rec.FinalResult())["text"])

        final_txt = ".\n".join(text)
        self._log_transcript_worked(file_path)
        return final_txt

    def _config_rec(self, wf):
        rec = KaldiRecognizer(self.model, wf.getframerate())
        rec.SetWords(True)
        rec.SetPartialWords(True)
        return rec

    def _log_transcript_worked(self, file_path):
        file_name = Path(file_path).name
        self.logger.info(f"'{file_name}' file transcript fully!")
