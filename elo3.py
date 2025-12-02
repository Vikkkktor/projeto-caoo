from elo import Elo

class Elo3(Elo):
    def processamento(self, dados):
        self.arteMarcialSugerida = dados
        self.caminhoGif = ""

        if self.arteMarcialSugerida == "Wrestling":
            self.caminhoGif = "gifs/khabib.gif"
            self.estiloSugerido = "Grappling"
        elif self.arteMarcialSugerida == "Jiu-Jitsu":
            self.caminhoGif = "gifs/charles.gif"
            self.estiloSugerido = "Grappling"
        elif self.arteMarcialSugerida == "Boxe":
            self.caminhoGif = "gifs/poatan.gif"      
            self.estiloSugerido = "Striking"
        elif self.arteMarcialSugerida == "Muay Thai/Karate":
            self.caminhoGif = "gifs/prates.gif"
            self.estiloSugerido = "Striking"


        return self.arteMarcialSugerida, self.estiloSugerido, self.caminhoGif