from abc import ABC, abstractmethod

class Elo:
    def __init__(self, model):
        self.next = None

    def set_next(self, next):
        self.next = next

    @abstractmethod
    def proc(self, data):
        pass

    def run(self, data):
        data = self.proc(data)

        if self.next is not None:
            return self.next.run(data)
        else:
            return data
