from abc import ABC, abstractmethod


class IAgent(ABC):
    @abstractmethod
    def buy_order(self, symbol, interval, amount):
        pass

    @abstractmethod
    def sell_order(self, symbol, interval, amount):
        pass