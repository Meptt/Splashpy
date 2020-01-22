import os

CONF_PATH = os.getcwd() + "settigs.conf"

with open(CONF_PATH) as configuration:
    conf = configuration.read()
    print(conf)