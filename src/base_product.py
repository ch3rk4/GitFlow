from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass