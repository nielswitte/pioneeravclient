from pioneeravclient import *
import config

pioneer = PioneerAvClient.factory(config.TYPE, config.HOST, config.PORT)

pioneer.setVolUp()