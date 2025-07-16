from ahserver.serverenv import ServerEnv
from appPublic.worker import awaitify
from appPublic.log import info, debug, warning, error, exception, critical

from ahserver.globalEnv import get_definition
import numpy as np
import base64
import whisper

# 编码
def base64_encode(text):
	text_bytes = text.encode('utf-8')
	encoded_bytes = base64.b64encode(text_bytes)
	encoded_text = encoded_bytes.decode('utf-8')
	return encoded_text

# 解码
def base64_decode(encoded_text):
	encoded_bytes = encoded_text.encode('utf-8')
	decoded_bytes = base64.b64decode(encoded_bytes)
	decoded_text = decoded_bytes.decode('utf-8')
	return decoded_text

class WhisperBase:
	def __init__(self):
		model_name = get_definition('whisper_model')
		self.model = whisper.load_model(model_name)

	def _stt(self, filepath):
		e = Exception(f'{filepath=} WhisperBase can not use')
		exception(f'{e=}')
		raise e


class WhisperFile(WhisperBase):
	def _stt(self, filepath):
		return self.model.transcribe(filepath)
	
	stt = awaitify(_stt)

class WhisperBase64(WhisperBase):
	def _stt(self, audio):
		audiolist = audio.values()
		nparr = np.array(audiolist, dtype=np.float32)
		nparr=np.vstack(nparr).astype(np.float)
		"""
		
		raw = base64_decode(audio_base64)
		ndarr = np.frombuffer(raw, dtype=np.float32)
		"""
		info(f'ndarr={nparr}')
		return self.model.transcribe(nparr)

	stt = awaitify(_stt)
