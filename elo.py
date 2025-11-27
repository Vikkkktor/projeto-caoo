from abc import ABC, abstractmethod

class Elo:
    def __init__(self, model):
        self.next = None

    def set_next(self, next):
        self.next = next

    @abstractmethod
    def processamento(self, data):
        pass

    def run(self, data):
        data = self.processamento(data)

        if self.next is not None:
            return self.next.run(data)
        else:
            return data
