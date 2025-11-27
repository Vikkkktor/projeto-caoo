from model import Model
class Controller():

    def __init__(self, view):
        self.model = Model()
        self.view = view

    def enviarDados(self):
        abdominais, arremessoMB, flexibilidade, saltoHorizontal, saltoVertical, velocidade = self.view.enviarDados()
        retorno = self.model.receberDados([abdominais, arremessoMB, flexibilidade, saltoHorizontal, saltoVertical, velocidade])
        print(retorno)