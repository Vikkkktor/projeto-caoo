from model import Model
class Controller():
    def __init__(self, view):
        self.model = Model()
        self.view = view

    def enviarDados(self):
        abdominais, arremessoMB, flexibilidade, velocidade, saltoHorizontal, saltoVertical = self.view.enviarDados()
        retorno = self.model.receberDados([abdominais, arremessoMB, flexibilidade, velocidade, saltoHorizontal, saltoVertical])
        print(retorno)