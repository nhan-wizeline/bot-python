class NLPResponseParser:
    def __init__(self):
        self.entities = list()
        self.entities_values = list()
        self.intent = None

    def parse_response(self, wit_response_entities):

        self.entities = []
        self.entities_values = []
        self.intent = None

        for k, v in wit_response_entities.items():
            if (k == "intent"):
                try:
                    self.intent = wit_response_entities['intent'][0]['value']
                except:
                    self.intent = None
            else:
                for entity in wit_response_entities[k]:
                    self.entities_values.append(entity['value'])
                    self.entities.append(k)

    def __str__(self):
        return "intent: {}, entities {}, values: {}".format(self.intent, str(self.entities), str(self.entities_values))