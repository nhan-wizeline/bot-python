from wit import Wit
from response_parser import NLPResponseParser
from response_builder import ResposeBuilder

def send_human_message_to_npl_api(message_text):
    return client.message(message_text)

def wait_for_human_message():
    return input("[Human]: ")

# app start here
access_token = "6X32NHTQMGUJZ7POOKYQFGA3DKWOG7CK"
client = Wit(access_token)
response_parser = NLPResponseParser()
response_to_human = ResposeBuilder()

print("Welcome to chatbot with Python")
while True:
    message_text = wait_for_human_message()
    wit_response = send_human_message_to_npl_api(message_text)
    response_parser.parse_response(wit_response['entities'])

    print("[Stupid Bot]: " + response_to_human.build_message_response_to_human(response_parser, message_text))
    if("bye" in response_parser.entities):
        break

