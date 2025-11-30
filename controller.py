from model import Model
class Controller():
    def __init__(self, view):
        self.model = Model()
        self.view = view

    def enviarDados(self):
        abdominais, arremessoMB, flexibilidade, velocidade, saltoHorizontal, saltoVertical = self.view.enviarDados()
        self.resultado = self.model.ReceberDados([abdominais, arremessoMB, flexibilidade, velocidade, saltoHorizontal, saltoVertical])
        self.receberDados()
        self.view.mostrarTelaDeResultado()
        

    def receberDados(self):
        self.estilo = self.resultado[0]
        self.arteMarcial = self.resultado[1]
        self.caminhoGif = self.resultado[2]

        self.view.atualizarPagina(self.arteMarcial, self.estilo, self.caminhoGif)
        