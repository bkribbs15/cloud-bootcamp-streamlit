import os
from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))

RESOURCES_FOLDER = os.path.join(CONFIG_PATH, 'resources')