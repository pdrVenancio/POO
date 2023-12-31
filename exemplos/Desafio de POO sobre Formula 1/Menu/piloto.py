import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
import model

class LimiteCadastroPiloto(tk.Toplevel):
    def __init__(self, controle, equipes):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Cadastrar piloto")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.framePais = tk.Frame(self)
        self.frameNumero = tk.Frame(self)
        self.frameEquipe = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameNome.pack()
        self.framePais.pack()
        self.frameNumero.pack()
        self.frameEquipe.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelPais = tk.Label(self.framePais, text="País: ")
        self.labelNumero = tk.Label(self.frameNumero, text="Número: ")
        self.labelEquipe = tk.Label(self.frameEquipe, text="Equipe: ")

        self.labelNome.pack(side="left")
        self.labelPais.pack(side="left")
        self.labelNumero.pack(side="left")
        self.labelEquipe.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputPais = tk.Entry(self.framePais, width=20)
        self.inputNumero = tk.Entry(self.frameNumero, width=20)

        # Combobox para escolher a equipe
        self.escolhaEquipe = tk.StringVar()
        self.comboEquipe = ttk.Combobox(self.frameEquipe, width=17, textvariable=self.escolhaEquipe, values=equipes)

        self.inputNome.pack(side="left")
        self.inputPais.pack(side="left")
        self.inputNumero.pack(side="left")
        self.comboEquipe.pack(side="left")

        # Botões
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter", font=('negrito', 9))
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear", font=('negrito', 9))
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraPilotos(tk.Toplevel):    #Tela com uma caixa de texto com as informações de todos os pilotos cadastrados
    def __init__(self, controle, pilotos):
        tk.Toplevel.__init__(self)
        self.geometry('600x550')
        self.title("Lista de pilotos cadastrados")
        self.controle = controle

        self.framePilotos = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framePilotos.pack()
        self.frameButton.pack()

        self.labelPilotos = tk.Label(self.framePilotos, text="Pilotos cadastrados")
        self.labelPilotos.pack(side="left")

        self.textPilotos = tk.Text(self.framePilotos, height=30, width=50)
        self.textPilotos.pack(side="left")
        self.textPilotos.insert(tk.END, pilotos)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaListaHandler)

class LimiteAlteraPiloto(tk.Toplevel):
    def __init__(self, controle, pilotos):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Alterar piloto")
        self.controle = controle

        self.pilotoAlterado = False

        self.framePiloto = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framePiloto.pack()
        self.frameButton.pack()

        self.labelPiloto = tk.Label(self.framePiloto, text="Piloto: ")
        self.labelPiloto.pack(side="left")

        self.escolhaPiloto = tk.StringVar()
        self.comboPiloto = ttk.Combobox(self.framePiloto, width=17, textvariable=self.escolhaPiloto, values=pilotos)
        self.comboPiloto.bind("<<ComboboxSelected>>", self.alterarPiloto)
        self.comboPiloto.pack(side="left")

    def alterarPiloto(self, event):
        if self.pilotoAlterado:
            return

        self.pilotoAlterado = True

        #Campos para alterar os dados do piloto
        self.frameNome = tk.Frame(self)
        self.framePais = tk.Frame(self)
        self.frameEquipe = tk.Frame(self)
        self.frameButton2 = tk.Frame(self)

        self.frameNome.pack()
        self.framePais.pack()
        self.frameEquipe.pack()
        self.frameButton2.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelPais = tk.Label(self.framePais, text="País: ")
        self.labelEquipe = tk.Label(self.frameEquipe, text="Equipe: ")

        self.labelNome.pack(side="left")
        self.labelPais.pack(side="left")
        self.labelEquipe.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputPais = tk.Entry(self.framePais, width=20)

        # Combobox para escolher a equipe
        self.escolhaEquipe = tk.StringVar()
        self.comboEquipe = ttk.Combobox(self.frameEquipe, width=17, textvariable=self.escolhaEquipe, values=self.controle.ctrlPrincipal.ctrlEquipe.getNomesEquipes())
        
        self.inputNome.pack(side="left")
        self.inputPais.pack(side="left")
        self.comboEquipe.pack(side="left")

        # Botões
        self.buttonSubmit = tk.Button(self.frameButton2, text="Enter", font=('negrito', 9))
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", self.controle.enterAlteraHandler)

        self.buttonFecha = tk.Button(self.frameButton2, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", self.controle.fechaAlteraHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlPiloto:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

        if not os.path.isfile("Cadastros/pilotos.pickle"):
            self.listaPilotos = []
        else:
            with open("Cadastros/pilotos.pickle", "rb") as f:
                self.listaPilotos = pickle.load(f)

    def cadastrarPiloto(self):
        equipes = self.ctrlPrincipal.ctrlEquipe.getNomesEquipes()   # Obtem os nomes das equipes
        self.limiteCadastro = LimiteCadastroPiloto(self, equipes)

    def enterHandler(self, event):
        nome = self.limiteCadastro.inputNome.get()
        pais = self.limiteCadastro.inputPais.get()

        #Exception para garantir que o número digitado seja inteiro
        try:
            numero = int(self.limiteCadastro.inputNumero.get())
        except ValueError:
            messagebox.showinfo('Alerta', 'Número inválido!')
            return
        
        equipe = self.limiteCadastro.escolhaEquipe.get()

        try:
            for e in self.ctrlPrincipal.ctrlEquipe.listaEquipes:    # Obtem a equipe do piloto
                if e.nome == equipe:
                    Equipe = e

            for piloto in self.listaPilotos:
                if piloto.numero == numero: #altera o piloto caso o número já esteja cadastrado
                    piloto.nome = nome
                    piloto.pais = pais
                    piloto.equipe = Equipe

                    self.limiteCadastro.mostraJanela('Sucesso', 'Piloto alterado com sucesso!')
                    self.clearHandler(event)
                    return

            self.listaPilotos.append(model.Piloto(nome, pais, numero, Equipe))
            self.listaPilotos.sort(key=lambda piloto: piloto.numero) # Ordena a lista de pilotos pelo número

            self.limiteCadastro.mostraJanela('Sucesso', 'Piloto cadastrado com sucesso!')
            self.clearHandler(event)
        except ValueError as error:
            self.limiteCadastro.mostraJanela('Erro', str(error))

    def clearHandler(self, event):
        self.limiteCadastro.inputNome.delete(0, len(self.limiteCadastro.inputNome.get()))
        self.limiteCadastro.inputPais.delete(0, len(self.limiteCadastro.inputPais.get()))
        self.limiteCadastro.inputNumero.delete(0, len(self.limiteCadastro.inputNumero.get()))

    def fechaHandler(self, event):
        self.limiteCadastro.destroy()

    def listarPilotos(self):
        pilotos = ''

        for piloto in self.listaPilotos:
            pilotos += str(piloto) + '\n\n'    # Adiciona os dados do piloto na string usando o método __str__

        self.limiteLista = LimiteMostraPilotos(self, pilotos)

    def fechaListaHandler(self, event):
        self.limiteLista.destroy()

    def salvaPilotos(self):
        if len(self.listaPilotos) != 0:
            with open("Cadastros/pilotos.pickle", "wb") as f:
                pickle.dump(self.listaPilotos, f)

    def getNomesPilotos(self):
        nomes = []

        for piloto in self.listaPilotos:
            str = f"{piloto.numero} - {piloto.nome}"
            nomes.append(str)

        return nomes
    
    def getListaPilotos(self):
        return self.listaPilotos
    
    def alterarPiloto(self):
        pilotos = self.getNomesPilotos()
        self.limiteAltera = LimiteAlteraPiloto(self, pilotos)

    def enterAlteraHandler(self, event):
        piloto = self.limiteAltera.escolhaPiloto.get()
        numero = piloto.split(' - ')[0]

        nome = self.limiteAltera.inputNome.get()
        pais = self.limiteAltera.inputPais.get()
        equipe = self.limiteAltera.escolhaEquipe.get()

        for piloto in self.listaPilotos:
            if piloto.numero == int(numero): #altera o piloto caso o número já esteja cadastrado
                # Verifica quais campos foram preenchidos
                try:
                    if nome != '':
                        piloto.nome = nome
                    elif pais != '':
                        piloto.pais = pais
                    elif equipe != '':
                        Equipe = self.ctrlPrincipal.ctrlEquipe.getEquipe(equipe)
                        if Equipe == None:
                            raise ValueError('Equipe não encontrada')
                        else:
                            piloto.Equipe = Equipe
                    else:
                        raise ValueError('Preencha pelo menos um campo')

                    self.limiteAltera.mostraJanela('Sucesso', 'Piloto alterado com sucesso!')
                    self.fechaAlteraHandler(event)
                    return
                except ValueError as error:
                    self.limiteAltera.mostraJanela('Erro', str(error))

    def fechaAlteraHandler(self, event):
        self.limiteAltera.destroy()