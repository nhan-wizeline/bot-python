from response_parser import NLPResponseParser
import json
from urllib.request import urlopen, Request

class ResposeBuilder:
    def __init__(self):
        self.response_to_human = ""

    def build_message_response_to_human(self, response_parser, message_text):
        self.response_to_human = ""

        if (response_parser.intent != None):
            if (response_parser.intent.lower() == "get_price"):  # cryptocurrency
                coin_buy_price = 0
                if ('cryptocurrency' in response_parser.entities):
                    block_chain_ticker_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
                    block_chain_price = json.load(urlopen(block_chain_ticker_url))

                    for cryptocurrency_name in response_parser.entities_values:
                        if (message_text.lower().find(str(cryptocurrency_name).lower()) > -1):
                            for coins in block_chain_price:
                                if (coins['name'].lower() == cryptocurrency_name.lower()):
                                    coin_buy_price = coins['price_usd']
                                    self.response_to_human += "{} price is {} USD; ".format(cryptocurrency_name,
                                                                                            coin_buy_price)

            elif (response_parser.intent.lower() == ""):  # place holder for game/dota
                pass

            elif (response_parser.intent.lower() == ""):  # place holder for others
                pass

        else:  # no intent
            if ('greetings' in response_parser.entities and "bye" not in response_parser.entities):
                self.response_to_human = "Hi, I am Stupid bot, how may I help you?"

            elif ('bye' in response_parser.entities):
                self.response_to_human = "Thank you and bye for now"

            else:
                self.response_to_human = "Sorry I do not understand your message, our support team will contact you asap!"


        return self.response_to_human