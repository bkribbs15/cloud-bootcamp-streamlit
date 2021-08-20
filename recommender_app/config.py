import os
from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))

RESOURCES_FOLDER = os.path.join(CONFIG_PATH, 'resources')

WML_SERVICE_URL =  os.getenv('WML_SERVICE_URL', 'https://us-south.ml.cloud.ibm.com')
WML_SERVICE_API_KEY = os.getenv('WML_SERVICE_API_KEY')
WML_SPACE_UID = os.getenv('WML_SPACE_UID')

WML_CREDENTIALS = {
    "url": WML_SERVICE_URL,
    "apikey": WML_SERVICE_API_KEY
}

WML_DEPLOYMENT_ID = os.getenv('WML_DEPLOYMENT_ID')
