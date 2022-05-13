from os import path


class Configure:

    def __init__(self):
        self._API_KEY = 'ZJPghmU5njjfV5x7Fogzgf44BKuxPsHuBElzJAWkiJlaDEaH69YsgQsfd8xZAz4T'
        self._API_SECRET = 'uSkzoCcBM4qdSY362TPpb3Sf5okB3ydPrAw8JHHT9twBSpOQyIz9fQESzxaCksmR'

        self.path = path.dirname(__file__) + "\endpoints.txt"
        #self._available_endpoints = self.load_available_endpoints()
        self.available_symbols = ['BTCUSDT',
                                  'ETHUSDT',
                                  'BNBUSDT',
                                  'SOLUSDT',
                                  'ADAUSDT',
                                  'XRPUSDT',
                                  'DOTUSDT',
                                  'LINKUSDT',
                                  'XMRUSDT',
                                  'LTCUSDT'
                                        ]
        self.available_intervals = [
            "1m",
            "5m",
            "15m",
            "1h",
            "4h",
            "1d",
            "1W"
        ]


    def load_available_endpoints(self):
        temp = []
        with open(self.path, "r") as file:
            for line in file.readlines():
                temp.append(line)
        return temp


    @property
    def API_KEY(self):
        return self._API_KEY

    @property
    def API_SECRET(self):
        return self._API_SECRET

    @property
    def available_endpoints(self):
        return self._available_endpoints

    def get_api_key(self):
        return self.API_KEY

    def get_api_secret(self):
        return self.API_SECRET

    def get_all_data(self):
        pass


