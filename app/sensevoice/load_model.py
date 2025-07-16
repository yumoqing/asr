from ahserver.serverenv import ServerEnv
from appPublic.worker import awaitify
from appPublic.jsonConfig import getConfig, get_definition
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

class SenseVoiceBase:
    def __init__(self):
        model_dir = get_definition('sensevoice_path')
        self.model = AutoModel(model=model_dir)
    
    def _stt(self, x):
        pass
    stt = awaitify(_stt)

class SenseVoiceFile(SenseVoiceBase):
    def _stt(self, filepath):
        res = this.model.generate(input=filepath,language="auto",
                use_itn=True,
                batch_size_s=60
        )
        return rich_transcription_postprocess(res[0]["text"])
