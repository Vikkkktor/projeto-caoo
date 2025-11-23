import tkinter as tk
from tkinter import  ttk, messagebox
import customtkinter as ctk
from PIL import Image
#from controller import Controller


class View():
    def __init__(self):
        self.root = tk.Tk()


        #self.controller = Controller(self)


        self.background = ctk.CTkFrame(self.root, fg_color="black")
        self.background.pack(fill=tk.BOTH, expand=True)
        self.background.grid_rowconfigure(0, weight=1)
        self.background.grid_columnconfigure(0, weight=1)


        self.telaInsercaoDados()
        self.telaDeResultado("gif")
       # self.telaDeEscolha()
       # self.telaDespensa()
       # self.telaReceitas()
       # self.telaModoPreparo()


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


        self.labelSaltoVertical = ctk.CTkLabel(self.containerForm, text="Salto Vertical", fg_color="black", text_color="white")
        self.labelSaltoVertical.grid(row=6, column= 1, padx=(0,15))
        self.entrySaltoVertical = ctk.CTkEntry(self.containerForm, placeholder_text = "26,5", placeholder_text_color = "black", justify = "center", height=30)
        self.entrySaltoVertical.grid(row=7, column= 1, padx=(0, 20), pady=(0, 30))  


        self.labelSaltoHorizontal = ctk.CTkLabel(self.containerForm, text="Salto Horizontal", fg_color="black", text_color="white")
        self.labelSaltoHorizontal.grid(row=6, column= 2, padx=(0,15))
        self.entrySaltoHorizontal = ctk.CTkEntry(self.containerForm, placeholder_text = "190", placeholder_text_color = "black", justify = "center", height=30)
        self.entrySaltoHorizontal.grid(row=7, column= 2, padx=(0, 20), pady=(0, 30))  


        self.labelVelociade = ctk.CTkLabel(self.containerForm, text="Velocidade", fg_color="black", text_color="white")
        self.labelVelociade.grid(row=6, column= 3, padx=(0,15))
        self.entryVelocidade = ctk.CTkEntry(self.containerForm, placeholder_text = "10km/h", placeholder_text_color = "black", justify = "center", height=30)
        self.entryVelocidade.grid(row=7, column= 3, padx=(0, 20), pady=(0, 30))  


        self.botaoEnviar = ctk.CTkButton(self.containerForm, text="Enviar", width=100, height=30, text_color="#FFFFFF", command=self.mostrarTelaDeResultado)
        self.botaoEnviar.grid(row=8, column=2, pady=(50))


    def mostrarTelaInsercaoDados(self):
        self.frame1.tkraise()
        self.root.geometry("800x500")

    
    def carregarGif(self, gif):
        self.gif = "charles-oliveira-ufc.gif"
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


  #  def efetuarLogin(self):
     #   emailOuNomeUsuario = self.entryEmailUsuarioLogin.get()
    #    senha = self.entrySenhaLogin.get()
      #  self.controller.efetuarLogin(emailOuNomeUsuario, senha)




# tela de cadastro e relacionados
    """def telaCadastro(self):
        self.frame2 = ctk.CTkFrame(self.background, fg_color="black")
        self.frame2.grid(row=0, column=0, sticky="nsew")


        self.containerCadastroTopo = ctk.CTkFrame(self.frame2, fg_color="black")
        self.containerCadastroTopo.pack(fill=tk.X, expand=True)


        self.containerCadastroForm = ctk.CTkFrame(self.frame2, fg_color="black")
        self.containerCadastroForm.pack(fill=tk.BOTH, expand=True)


        self.labelNomePagina = tk.Label(self.containerCadastroTopo, text="Cadastre-se", fg_color="black", fg="white")
        self.labelNomePagina.pack()


        self.labelNomeUsuario = tk.Label(self.containerCadastroForm,width=20, text="Nome de Usuário", fg_color="black", fg="#FFFFFF")
        self.labelNomeUsuario.pack()    


        self.entryNomeUsuario = tk.Entry(self.containerCadastroForm,width=20)
        self.entryNomeUsuario.pack(pady=(0,5))


        self.labelEmail = tk.Label(self.containerCadastroForm,width=20, text="Email", fg_color="black", fg="#FFFFFF")
        self.labelEmail.pack()    


        self.entryEmailCadastro = tk.Entry(self.containerCadastroForm,width=20)
        self.entryEmailCadastro.pack(pady=(0,5))  


        self.labelSenha = tk.Label(self.containerCadastroForm,width=20, text="Senha", fg_color="black", fg="#FFFFFF")
        self.labelSenha.pack()


        self.entrySenhaCadastro = tk.Entry(self.containerCadastroForm,width=20)
        self.entrySenhaCadastro.pack()


        self.botaoCadastrar = tk.Button(
                                    self.containerCadastroForm,
                                    text="Cadastrar",
                                    width=10,  
                                    command=self.efetuarCadastro)
        self.botaoCadastrar.pack(pady=(40,0))




      def mostrarTelaCadastro(self):
        self.frame2.tkraise()
        self.root.geometry("400x455")
       


    def efetuarCadastro(self):
        email = self.entryEmailCadastro.get()
        nomeUsuario = self.entryNomeUsuario.get()
        senha = self.entrySenhaCadastro.get()
        self.controller.efetuarCadastro(email, nomeUsuario, senha)




# tela de escolha e relacionados
    def telaDeEscolha(self):
        self.frame3 = ctk.CTkFrame(self.background, fg_color="black")
        self.frame3.grid(row=0, column=0, sticky="nsew")


        self.containerTopo = ctk.CTkFrame(self.frame3, fg_color="black")
        self.containerTopo.pack(fill=tk.X, expand=True)


        self.containerBotoes = ctk.CTkFrame(self.frame3, fg_color="black")
        self.containerBotoes.pack(fill=tk.BOTH, expand=True)


        self.labelBoasVindas = tk.Label(self.containerTopo, text=" ", fg_color="black", fg="white", font=(20) )
        self.labelBoasVindas.pack()


        self.botaoDespensa = tk.Button(self.containerBotoes,
                                    text="DESPENSA",
                                    width=50,
                                    height=3,
                                    command=self.mostrarIngredientesSalvos)
        self.botaoDespensa.pack(pady=(0,50))


        self.botaoReceitas = tk.Button(self.containerBotoes,
                                    text="RECEITAS",
                                    width=50,
                                    height=3,
                                    command=self.controller.mostrarReceitas
                                   )
        self.botaoReceitas.pack()




    def mostrarTelaDeEscolha(self, nomeUsuario):
        self.labelBoasVindas.config(text=(f"Bem Vindo {nomeUsuario.upper()}"))
        self.frame3.tkraise()
        self.root.geometry("600x600")




    def voltarParaTelaEscolha(self):
        self.controller.voltarParaTelaEscolha()




# tela despensa e relacionados
    def telaDespensa(self):
        self.frame4 = ctk.CTkFrame(self.background, fg_color="black")
        self.frame4.grid(row=0, column=0, sticky="nsew")


        self.containerTopo = ctk.CTkFrame(self.frame4, fg_color="black")
        self.containerTopo.pack(fill=tk.X, side=tk.TOP)


        self.containerAdicionarIngredientes = ctk.CTkFrame(self.frame4, fg_color="black")
        self.containerAdicionarIngredientes.pack(anchor="n", fill=tk.BOTH, pady=(2,0))
       
        self.containerIngredientesSalvos = ctk.CTkFrame(self.frame4, fg_color="black")
        self.containerIngredientesSalvos.pack(fill=tk.BOTH, expand=True)


        self.botaoVoltar = tk.Button(self.containerTopo,
                                    text="⟵",
                                    font=(20),
                                    relief="flat",
                                    fg_color="black",
                                    activebackground="black",
                                    bd=0,
                                    highlightthickness=0,
                                    fg="white",
                                    command=self.voltarParaTelaEscolha)
        self.botaoVoltar.pack(side=tk.LEFT)


        self.labelNomePagina = tk.Label(self.containerTopo, text="Despensa", fg_color="black", fg="white", font=(20))
        self.labelNomePagina.pack()


        self.labelNomeIngrediente = tk.Label(self.containerAdicionarIngredientes,width=17, text="Nome do Ingrediente:", fg_color="black",fg="#FFFFFF", font=(5))
        self.labelNomeIngrediente.pack(pady=(30,0), padx=(100,0), side="left", anchor="n")


        self.entryNomeIngrediente = tk.Entry(self.containerAdicionarIngredientes,width=20)
        self.entryNomeIngrediente.pack(pady=(33, 0), padx=10,side="left", anchor="n")


        self.labelQtdIngrediente = tk.Label(self.containerAdicionarIngredientes,width=5, text="QTD:", fg_color="black", fg="#FFFFFF", font=(5))
        self.labelQtdIngrediente.pack(pady=(30,0), side="left", anchor="n")


        self.entryQtdIngrediente = tk.Entry(self.containerAdicionarIngredientes,width=5)
        self.entryQtdIngrediente.pack(pady=(33, 0), padx=10,side="left", anchor="n")


        self.botaoAdicionar = tk.Button(self.containerAdicionarIngredientes,
                                        text="Adicionar",
                                        fg="black",
                                        height=1,
                                        width=10,  
                                        command=self.adicionarIngredientes
                                        )
        self.botaoAdicionar.pack(pady=(30, 0), padx=(0, 100))


        self.labelIngredientes = tk.Label(self.containerIngredientesSalvos, text="Ingredientes Salvos", fg_color="black", fg="white", font=(20))
        self.labelIngredientes.pack(pady=(50,0))


        self.containerIngredientesSalvos = ctk.CTkFrame(self.containerIngredientesSalvos, fg_color="black")
        self.containerIngredientesSalvos.pack(pady=(25,0), anchor="center")




    def mostrarTelaDespensa(self):
        self.frame4.tkraise()
        self.root.geometry("700x700")




    def limparIngredientes(self):
        for widget in self.containerIngredientesSalvos.winfo_children():
            widget.destroy()




    def adicionarIngredientes(self):
        nomeIngrediente = self.entryNomeIngrediente.get()
        qtdIngrediente = self.entryQtdIngrediente.get()
        self.controller.adicionarIngredientes(nomeIngrediente, qtdIngrediente)
       
        self.mostrarIngredientesSalvos()




    def mostrarIngredientesSalvos(self):
        self.controller.mostrarIngredientesSalvos()




    def ingredientesSalvosFormat(self, nomeIngrediente, qtdIngrediente):
        linha = ctk.CTkFrame(self.containerIngredientesSalvos, fg_color="black")
        linha.pack(fill=tk.X, pady=2, padx=20)


        linha.columnconfigure(0, weight=1)
        linha.columnconfigure(1, weight=0)
        linha.columnconfigure(2, weight=0)
       
        labelIngredientesSalvosNome = tk.Label(linha, text=nomeIngrediente, fg_color="black", fg="white", font=(15), anchor="w")
        labelIngredientesSalvosNome.grid(row=0, column=0, sticky="w")
        labelIngredientesSalvosQuantidade = tk.Label(linha, text=str(qtdIngrediente), fg_color="black", fg="white", font=(15))
        labelIngredientesSalvosQuantidade.grid(row=0, column=1, padx=100)


        botaoRemover = tk.Button(linha,
                                text="X",
                                fg_color="red",
                                fg="white",
                                width=2,
                                command=lambda nomeIngredienteRemovido=nomeIngrediente: self.removerIngrediente(nomeIngredienteRemovido)
                                )
        botaoRemover.grid(row=0, column=2)




    def mostrarDespensaVazia(self):
        labelVazio = tk.Label(self.containerIngredientesSalvos, text="Nenhum Ingrediente Salvo!", fg_color="black", fg="white", font=(20))
        labelVazio.pack()




    def removerIngrediente(self, nomeIngredienteRemovido):
        self.controller.removerIngrediente(nomeIngredienteRemovido)
 


# tela de receitas e relacionados
    def telaReceitas(self):
        self.frame5 = ctk.CTkFrame(self.background, fg_color="black")
        self.frame5.grid(row=0, column=0, sticky="nsew")


        self.containerTopo = ctk.CTkFrame(self.frame5, fg_color="black")
        self.containerTopo.pack(fill=tk.X, side=tk.TOP)


        self.containerReceitas = ctk.CTkFrame(self.frame5, fg_color="black")
        self.containerReceitas.pack(fill=tk.BOTH, expand=True)


        self.botaoVoltar = tk.Button(self.containerTopo,
                                    text="⟵",
                                    font=(20),
                                    relief="flat",
                                    fg_color="black",
                                    activebackground="black",
                                    bd=0,
                                    highlightthickness=0,
                                    fg="white",
                                    command=self.voltarParaTelaEscolha)
        self.botaoVoltar.pack(side=tk.LEFT)  


        style = ttk.Style()
        temaAtual = style.theme_use("clam")
               
        style.configure("Treeview",
                    background="black",        
                    foreground="white",        
                    rowheight=25,
                    fieldbackground="black",  
                    borderwidth=0,            
                    relief="flat")  


        style.configure("Treeview.Heading",
                    background="black",        
                    foreground="white",        
                    font=(10),                  
                    borderwidth=0,            
                    relief="flat")  


        self.listaReceitas = ttk.Treeview(self.containerReceitas, columns=("Receitas", "ID"), show="headings")
        self.listaReceitas.heading("Receitas", text="Receitas")
        self.listaReceitas.column("Receitas", anchor=tk.CENTER, width=700, stretch=tk.NO)
        self.listaReceitas.heading("ID", text="ID")
        self.listaReceitas.column("ID", width=0, stretch=tk.NO)
        self.listaReceitas.pack(fill=tk.BOTH, expand=True)
       


        self.listaReceitas.bind("<Double-1>", self.mostrarTelaModoPreparo)
       


    def mostrarTelaReceitas(self, receitas):
        self.frame5.tkraise()
        self.root.geometry("700x700")


        for item in self.listaReceitas.get_children():
            self.listaReceitas.delete(item)
        for receita in receitas:
            nome = receita.get("title")
            idReceita = receita.get("id")
            self.listaReceitas.insert("", "end", values=(nome, idReceita))
        self.frame5.grid(row=0, column=0, sticky="nsew")




    def voltarParaTelaReceitas(self):
        self.frame5.tkraise()
        self.root.geometry("700x700")




    def telaModoPreparo(self):
        self.frame6 = ctk.CTkFrame(self.background, fg_color="black")
        self.frame6.grid(row=0, column=0, sticky="nsew")


        self.containerTopo = ctk.CTkFrame(self.frame6, fg_color="black")
        self.containerTopo.pack(fill=tk.X, side=tk.TOP)


        self.containerIngredientesUsados = ctk.CTkFrame(self.frame6, fg_color="black")
        self.containerIngredientesUsados.pack(fill=tk.X)


        self.containerModoPreparo = ctk.CTkFrame(self.frame6, fg_color="black")
        self.containerModoPreparo.pack(fill=tk.BOTH, expand=True)


        self.botaoVoltar = tk.Button(self.containerTopo,
                                    text="⟵",
                                    font=(20),
                                    relief="flat",
                                    fg_color="black",
                                    activebackground="black",
                                    bd=0,
                                    highlightthickness=0,
                                    fg="white",
                                    command=self.voltarParaTelaReceitas)
        self.botaoVoltar.pack(side=tk.LEFT)


        self.labelNomeReceita = tk.Label(self.containerTopo, text="", fg_color="black", fg="white", font= ("bold",15))
        self.labelNomeReceita.pack()    


        self.labelIngredientesUsados = tk.Label(self.containerIngredientesUsados, text="", fg_color="black", fg="white", font=(10))
        self.labelIngredientesUsados.pack(pady=10)  


        self.textModoPreparo = tk.Text(self.containerModoPreparo, fg_color="black", fg="white", font=(10),wrap="word",bd=0,highlightthickness=0,relief="flat")
        self.textModoPreparo.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)  


        self.barraRolagemModoPreparo = ttk.Scrollbar(self.containerModoPreparo, command=self.textModoPreparo.yview)
        self.barraRolagemModoPreparo.pack(side=tk.RIGHT, fill=tk.Y)


        self.textModoPreparo.config(yscrollcommand=self.barraRolagemModoPreparo.set)




    def mostrarTelaModoPreparo(self, event):
        self.frame6.tkraise()
        self.root.geometry("1300x800")


        itemSelecionado = self.listaReceitas.focus()
        valoresLinha = self.listaReceitas.item(itemSelecionado, "values")
        self.idReceita =  valoresLinha[1]


        self.dadosLimposReceita = self.controller.buscarModoPreparo(self.idReceita)
        self.nomeReceita = self.dadosLimposReceita.get("Nome")
        self.ingredientes = self.dadosLimposReceita.get("Ingredientes")
        self.modoPreparo = self.dadosLimposReceita.get("Instrucoes")


        self.labelNomeReceita.config(text=self.nomeReceita)
        self.labelIngredientesUsados.config(text=self.ingredientes)
        self.textModoPreparo.config(state=tk.NORMAL)
        self.textModoPreparo.delete(1.0, tk.END)
        self.textModoPreparo.insert(tk.END, self.modoPreparo)
        self.textModoPreparo.config(state=tk.DISABLED)




    def mostrarCadastroSucesso(self):
        messagebox.showinfo("Cadastro concluído", "Usuário cadastrado com sucesso!")




    def mostrarMensagemErro(self, nomePagina, mensagem):
        messagebox.showerror(nomePagina, mensagem)




    def mostrarMensagemAviso(self, nomePagina, mensagem):
        messagebox.showwarning(nomePagina, mensagem)"""


View()

