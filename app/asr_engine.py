import os
import time
from traceback import print_exc
import base64
import wave
from appPublic.log import info, debug, warning, error, exception, critical
from appPublic.dictObject import DictObject
from appPublic.folderUtils import temp_file
from ahserver.serverenv import ServerEnv
from aiohttp.web import StreamResponse
from ahserver.globalEnv import realpath

def save_base64_wav(base64_data, output_file,sample_rate=16000, num_channels=1):
    # Decode the base64 data
    wav_data = base64.b64decode(base64_data)

    # Open a new WAV file for writing
    with wave.open(output_file, 'wb') as wf:
        # Set the parameters of the WAV file
        wf.setnchannels(num_channels)  # Mono channel
        wf.setsampwidth(2)  # 16-bit sample width
        wf.setframerate(sample_rate)  # 44.1 kHz sample rate
        # Write the decoded data to the WAV file
        wf.writeframes(wav_data)

async def generate(request, kw):
	params_kw = kw.get('params_kw', DictObject())
	info(f'{params_kw=}')
	model = params_kw.model
	audio_file = params_kw.audio_file
	if not audio_file:
		audio = params_kw.audio
		if audio is None:
			return {
				'status':'error',
				'message':'audio is null'
			}
		audio_file = temp_file(suffix='.wav')
		save_base64_wav(audio, audio_file)
	else:
		audio_file = realpath(audio_file)

	engine = None
	g = ServerEnv()
	if model=='whisper':
		engine = g.whisper_engine

	if engine is None:
		return {
			'status':'error',
			'message':f'model={model} is not defined'
		}
	try:
		t1 = time.time()
		dic = await engine.stt(audio_file)
		t2 = time.time()
		os.remove(audio_file)
		ret = {
			"status":"ok",
			"time_cost":t2-t1,
			"content":dic['text'],
			"segments":dic['segments'],
			"language":dic['language']
		}
		info(f'{dic=}, {ret=}')
		return ret
	except Exception as e:
		exception(f'{e}')
		print_exc()
		return {
			'status':'error',
			'message':f'{e}'
		}

g = ServerEnv()
g.generate = generate
