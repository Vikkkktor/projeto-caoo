import tkinter as tk
from tkinter import  ttk, messagebox
import customtkinter as ctk
from PIL import Image
from controller import Controller


class View():
    def __init__(self):
        self.root = tk.Tk()

        self.controller = Controller(self)


        self.background = ctk.CTkFrame(self.root, fg_color="black")
        self.background.pack(fill=tk.BOTH, expand=True)
        self.background.grid_rowconfigure(0, weight=1)
        self.background.grid_columnconfigure(0, weight=1)


        self.telaInsercaoDados()
        self.telaDeResultado("gif")

        self.mostrarTelaInsercaoDados()

        self.root.mainloop()


# tela inicial/de inserção 
    def telaInsercaoDados(self):
        self.root.title("DMMA")
        self.frame1 = ctk.CTkFrame(self.background, fg_color="black")
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame1.grid_columnconfigure(0, weight=1)


        self.containerTopo = ctk.CTkFrame(self.frame1, fg_color="black")
        self.containerTopo.grid(row=1, column=0, sticky="nsew")
        self.containerTopo.grid_columnconfigure(0, weight=1)


        self.containerForm = ctk.CTkFrame(self.frame1, fg_color="black")
        self.containerForm.grid(row=2, column=0, sticky="nsew")
        self.containerForm.grid_columnconfigure(0, weight=1)
        self.containerForm.grid_columnconfigure(4, weight=1)

        self.labelNomePagina = ctk.CTkLabel(self.containerTopo, text="INSIRA SEUS DADOS", fg_color="black", text_color="white", font=("Candara", 20, "bold"), justify="center" )
        self.labelNomePagina.grid(row=0, column= 0, padx=(0, 0), pady=(60, 0))


        self.labelAbdominais = ctk.CTkLabel(self.containerForm, text="Abdominais", fg_color="black", text_color="white")
        self.labelAbdominais.grid(row=4, column= 1, padx=(0, 15), pady=(50, 0))
        self.entryAbdominais = ctk.CTkEntry(self.containerForm, placeholder_text = "23", placeholder_text_color = "black", justify = "center", height=30)
        self.entryAbdominais.grid(row=5, column= 1, padx=(0, 20), pady=(0, 30))  


        self.labelArremessoMB = ctk.CTkLabel(self.containerForm, text="Arremessos MB", fg_color="black", text_color="white")
        self.labelArremessoMB.grid(row=4, column= 2, padx=(0,15), pady=(50, 0))
        self.entryArremessoMB = ctk.CTkEntry(self.containerForm, placeholder_text = "5,1", placeholder_text_color = "black", justify = "center", height=30)
        self.entryArremessoMB.grid(row=5, column= 2, padx=(0, 20), pady=(0, 30))  


        self.labelFlexibilidade = ctk.CTkLabel(self.containerForm, text="Flexibilidade", fg_color="black", text_color="white")
        self.labelFlexibilidade.grid(row=4, column= 3, padx=(0,15), pady=(50, 0))
        self.entryFlexibilidade = ctk.CTkEntry(self.containerForm, placeholder_text = "52", placeholder_text_color = "black", justify = "center", height=30)
        self.entryFlexibilidade.grid(row=5, column= 3, padx=(0, 20), pady=(0, 30))  

       
        self.labelVelociade = ctk.CTkLabel(self.containerForm, text="Velocidade", fg_color="black", text_color="white")
        self.labelVelociade.grid(row=6, column= 3, padx=(0,15))
        self.entryVelocidade = ctk.CTkEntry(self.containerForm, placeholder_text = "10km/h", placeholder_text_color = "black", justify = "center", height=30)
        self.entryVelocidade.grid(row=7, column= 3, padx=(0, 20), pady=(0, 30))  


        self.labelSaltoVertical = ctk.CTkLabel(self.containerForm, text="Salto Vertical", fg_color="black", text_color="white")
        self.labelSaltoVertical.grid(row=6, column= 1, padx=(0,15))
        self.entrySaltoVertical = ctk.CTkEntry(self.containerForm, placeholder_text = "26,5", placeholder_text_color = "black", justify = "center", height=30)
        self.entrySaltoVertical.grid(row=7, column= 1, padx=(0, 20), pady=(0, 30))  


        self.labelSaltoHorizontal = ctk.CTkLabel(self.containerForm, text="Salto Horizontal", fg_color="black", text_color="white")
        self.labelSaltoHorizontal.grid(row=6, column= 2, padx=(0,15))
        self.entrySaltoHorizontal = ctk.CTkEntry(self.containerForm, placeholder_text = "190", placeholder_text_color = "black", justify = "center", height=30)
        self.entrySaltoHorizontal.grid(row=7, column= 2, padx=(0, 20), pady=(0, 30))  


        self.botaoEnviar = ctk.CTkButton(self.containerForm, text="Enviar", width=100, height=30, text_color="#FFFFFF", command=self.controller.enviarDados)
        self.botaoEnviar.grid(row=8, column=2, pady=(50))


    def mostrarTelaInsercaoDados(self):
        self.frame1.tkraise()
        self.root.geometry("800x500")

    
    def carregarGif(self, gif):
        self.gif = "gifs/charles-oliveira-ufc.gif"
        self.meta = Image.open(self.gif)

        self.frames = self.meta.n_frames

        self.imagens = []
        for i in range(self.frames):
            self.obj = tk.PhotoImage(file=self.gif, format=f"gif -index {i}")
            self.imagens.append(self.obj)


    def animacao(self, frameAtual=0):
        self.imagem = self.imagens[frameAtual]

        self.labelGif.configure(image=self.imagem)
        self.frameAtual = frameAtual + 1

        if self.frameAtual == self.frames:
            self.frameAtual = 0

        self.loop = self.root.after(40, lambda: self.animacao(self.frameAtual))


    def telaDeResultado(self, gif):
        self.frame2 = ctk.CTkFrame(self.background, fg_color="black")
        self.frame2.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure(0, weight=0)
        self.frame2.grid_rowconfigure(1, weight=0)
        self.frame2.grid_rowconfigure(2, weight=0)
        self.frame2.grid_rowconfigure(3, weight=1)
        self.frame2.grid_rowconfigure(4, weight=0)

        self.containerTopo = ctk.CTkFrame(self.frame2, fg_color="black")
        self.containerTopo.grid(row=0, column=0, sticky="nsew")

        self.containerGif = tk.Frame(self.frame2, bg="black")
        self.containerGif.grid(row=1, column=0, sticky="nsew")

        self.containerArteMarcial = ctk.CTkFrame(self.frame2, fg_color="black")
        self.containerArteMarcial.grid(row=2, column=0, sticky="nsew")

        self.containerBotao = ctk.CTkFrame(self.frame2, fg_color="black")
        self.containerBotao.grid(row=4, column=0, sticky="se")
        
        self.labelNomePagina = ctk.CTkLabel(self.containerTopo, 
         text="Sua área recomendada é o *AREA RECOMENDADA*",
         fg_color="black", 
         text_color="white", 
         font=("Candara", 20, "bold"),
         justify="center" )
        self.labelNomePagina.pack(pady=(40))

        self.labelGif = tk.Label(self.containerGif, bg="black")
        self.labelGif.pack(pady=(0,40))

        self.carregarGif(gif)
        self.animacao()
    
        self.labelArteMarcial = ctk.CTkLabel(self.containerArteMarcial, 
         text="Arte Marcial: *ARTE MARCIAL RECOMENDADA*", 
         fg_color="black", 
         text_color="white", 
         font=("Candara", 20, "bold"), 
         justify="center" )
        self.labelArteMarcial.pack()

        self.botaoGrafico = ctk.CTkButton(self.containerBotao, text="Grafico", width=100, height=30, text_color="#FFFFFF", command="")
        self.botaoGrafico.pack()

    def mostrarTelaDeResultado(self):
        self.frame2.tkraise()
        self.root.geometry("800x500")

    def enviarDados(self):
        return self.entryAbdominais.get(), self.entryArremessoMB.get(), self.entryFlexibilidade.get(), self.entryVelocidade.get(), self.entrySaltoHorizontal.get(), self.entrySaltoVertical.get()


View()

