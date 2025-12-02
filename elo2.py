from elo import Elo

class Elo2(Elo):
    def __init__(self, model):
     super().__init__(model)

    def processamento(self, dados):
        razaoUsuario = self.model.CalcularRazao([dados])[0]
        vetorSG = self.model.escala.transform([razaoUsuario])
        self.model.usuarioVetorGeral = vetorSG
        grupoSG = self.model.kmeansGeral.predict(vetorSG)[0]

        if grupoSG == self.model.idGrappler:              
              vetorGrappler = self.model.escalaGrappler.transform([razaoUsuario])
              subGrupo = self.model.kmeansGrappler.predict(vetorGrappler)[0]
              
              if subGrupo == self.model.idWrestling:
                  resultadoFinal = "Wrestling"
              else:
                  resultadoFinal = "Jiu-Jitsu"
          
        else:              
              vetorStriker = self.model.escalaStriker.transform([razaoUsuario])
              subGrupo = self.model.kmeansStriker.predict(vetorStriker)[0]
              
              if subGrupo == self.model.idBoxe:
                  resultadoFinal = "Boxe"
              else:
                  resultadoFinal = "Muay Thai/Karate"

        return resultadoFinal