from elo import Elo
import re
# Normaliza os dados
class Elo1(Elo):
    def processamento(self, dados):
        for i in range(len(dados)):
            texto = str(dados[i]).replace(',', '.')
            dadoLimpo = re.sub(r'[^\d.]', '', texto)
            dados[i] = float(dadoLimpo)
        
        explosao = dados[4] * dados[5] 

        dados = [
            dados[0],
            dados[1], 
            dados[2], 
            dados[3], 
            explosao  
        ]

        return dados