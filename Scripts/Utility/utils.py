import os
import __root__
from Configuration import configreader
from Scripts.Utility.Log.logger import Logger

# Read the configurations
config_file = os.path.join(__root__.path(), "Configuration/service.yml")
configuration = configreader.read_configuration(config_file) # parsing the "service.yml"
logger = Logger(configuration).log_obj