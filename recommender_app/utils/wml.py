from recommender_app.config import WML_CREDENTIALS
from ibm_watson_machine_learning import APIClient

from recommender_app.config import WML_CREDENTIALS, WML_SPACE_UID

wml_client = APIClient(WML_CREDENTIALS)
wml_client.set.default_space(WML_SPACE_UID)

def score(deployment_uid, payload):

    return wml_client.deployments.score(deployment_uid, payload)
