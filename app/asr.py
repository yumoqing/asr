import os, sys
import argparse
from appPublic.log import MyLogger, info, debug, warning
from appPublic.folderUtils import ProgramPath
from appPublic.jsonConfig import getConfig
from appPublic.registerfunction import RegisterFunction
from ahserver.configuredServer import ConfiguredServer
from ahserver.serverenv import ServerEnv
from whisper_model import WhisperFile
from asr_engine import generate

__version__ = '0.0.1'

if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog="Sage")
	parser.add_argument('-w', '--workdir')
	parser.add_argument('-p', '--port')
	args = parser.parse_args()
	print(args)
	workdir = args.workdir or os.getcwd()
	p = ProgramPath()
	config = getConfig(workdir, NS={'workdir':workdir, 'ProgramPath':p})
	if config.logger:
		logger = MyLogger(config.logger.name or 'sage',
							levelname=config.logger.levelname or 'debug',
							logfile=config.logger.logfile or None)
	else:
		logger = MyLogger('sage', levelname='debug')

	info(f'========sage version={__version__}========')
	# server = ConfiguredServer(auth_klass=MyAuthAPI, workdir=workdir)
	server = ConfiguredServer(workdir=workdir)
	rf = RegisterFunction()
	rf.register('generate', generate)
	g = ServerEnv()
	g.whisper_engine = WhisperFile()
	port = args.port or config.website.port or 8080
	port = int(port)
	server.run(port=port)

