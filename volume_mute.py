from pioneeravclient import *
import config

pioneer = PioneerAvClient.factory(config.TYPE, config.HOST, config.PORT)

if pioneer.getMute() == "MUT1" :
	pioneer.mute()
else :
	pioneer.unmute()