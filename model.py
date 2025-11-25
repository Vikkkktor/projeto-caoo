from elo_01 import Elo_01
from elo_02 import Elo_02
from elo_03 import Elo_03

class Model:
    def __init__(self):
        self.e0 = Elo_01(self)
        self.e1 = Elo_02(self)
        self.e2 = Elo_03(self)

        self.e0.set_next(self.e1)
        self.e1.set_next(self.e2)

    def receberDados(self, dados):
        resposta = self.e0.run(dados)
        return resposta