import json
import pytest
from homeAutomation.server.main import app


@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client


def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')


def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))


def test_publish_1(client):
    response = client.get('/')
    assert b'Server is up' in response.data


def test_publish_2(client):
    example_response = {'responseId': '3d######-####-####-####-############-######d2',
                        'queryResult': {'queryText': 'Turn on lights',
                                        'parameters': {},
                                        'allRequiredParamsPresent': True,
                                        'fulfillmentMessages': [
                                            {'text': {'text': ['']}}
                                        ], 'outputContexts': [{
                                                                  'name': 'projects/nodemcu-#####/agent/sessions/3c######-####-####-####-##########42/contexts/__system_counters__',
                                                                  'parameters': {'no-input': 0.0, 'no-match': 0.0}}],
                                        'intent': {
                                            'name': 'projects/nodemcu-#####/agent/intents/88######-####-####-####-##########b6',
                                            'displayName': 'Turn on or off led'}, 'intentDetectionConfidence': 1.0,
                                        'languageCode': 'en'}, 'originalDetectIntentRequest': {'payload': {}},
                        'session': 'projects/nodemcu-#####/agent/sessions/3c######-####-####-####-##########42'}

    response = post_json(client, '/', example_response)
    assert response.status_code == 200
    assert json_of_response(response)['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] == "The lights are on"

def test_publish_3(client):
    example_response = {'responseId': '3d######-####-####-####-############-######d2',
                        'queryResult': {'queryText': 'Turn off lights',
                                        'parameters': {},
                                        'allRequiredParamsPresent': True,
                                        'fulfillmentMessages': [
                                            {'text': {'text': ['']}}
                                        ], 'outputContexts': [{
                                                                  'name': 'projects/nodemcu-#####/agent/sessions/3c######-####-####-####-##########42/contexts/__system_counters__',
                                                                  'parameters': {'no-input': 0.0, 'no-match': 0.0}}],
                                        'intent': {
                                            'name': 'projects/nodemcu-#####/agent/intents/88######-####-####-####-##########b6',
                                            'displayName': 'Turn on or off led'}, 'intentDetectionConfidence': 1.0,
                                        'languageCode': 'en'}, 'originalDetectIntentRequest': {'payload': {}},
                        'session': 'projects/nodemcu-#####/agent/sessions/3c######-####-####-####-##########42'}

    response = post_json(client, '/', example_response)
    assert response.status_code == 200
    assert json_of_response(response)['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] == "The lights are off"

def test_publish_4(client):
    example_response = {'responseId': '3d######-####-####-####-############-######d2',
                        'queryResult': {'queryText': 'lights',
                                        'parameters': {},
                                        'allRequiredParamsPresent': True,
                                        'fulfillmentMessages': [
                                            {'text': {'text': ['']}}
                                        ], 'outputContexts': [{
                                                                  'name': 'projects/nodemcu-#####/agent/sessions/3c######-####-####-####-##########42/contexts/__system_counters__',
                                                                  'parameters': {'no-input': 0.0, 'no-match': 0.0}}],
                                        'intent': {
                                            'name': 'projects/nodemcu-#####/agent/intents/88######-####-####-####-##########b6',
                                            'displayName': 'Turn on or off led'}, 'intentDetectionConfidence': 1.0,
                                        'languageCode': 'en'}, 'originalDetectIntentRequest': {'payload': {}},
                        'session': 'projects/nodemcu-#####/agent/sessions/3c######-####-####-####-##########42'}

    response = post_json(client, '/', example_response)
    assert response.status_code == 200
    assert json_of_response(response)['payload']['google']['richResponse']['items'][0]['simpleResponse']['textToSpeech'] == "Do you want to turn on or off the lights"