from customtkinter import *  # Biblioteca tkinter melhorada
from PIL import Image, ImageDraw, ImageOps
import os
import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self):
        self.app_menu = CTk()
        self.app_menu.geometry('700x600')
        self.app_menu.title("🍕 Mokele y Mbembe 🍕")

        # Criar um CTkCanvas e associar uma scrollbar
        self.canvas = CTkCanvas(self.app_menu)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Usar o CTkScrollbar em vez do Scrollbar do tkinter, sem o 'orient'
        self.scrollbar = CTkScrollbar(self.app_menu, command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Configurar o Canvas com a scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Criar o frame de conteúdo dentro do Canvas
        self.frame_conteudo = CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_conteudo, anchor="nw")

        # Atualizar a scrollbar quando o conteúdo for maior que a tela
        self.frame_conteudo.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.tema_atual = StringVar(value="dark")
        set_appearance_mode(self.tema_atual.get())

        # Dicionário de pizzas
        self.pizzas = {
            "Calabresa": {
                "imagem": "PIZZA.jpg",
                "descricao": "🍕 Pizza Calabresa\n - Queijo, molho de tomate, calabresa e cebola.\n - 🍽️ Serve 2 a 3 pessoas\n - 💲 R$ 35,00\n - 👀 8 pedaços",
                "quantidade": 0
            },
            "Quatro Queijos": {
                "imagem": "PIZZA_4QUEIJOS.jpg",
                "descricao": "🧀 Pizza Quatro Queijos\n - Molho de tomate e bastante queijo.\n - 🍽️ Serve 2 a 3 pessoas\n - 💲 R$ 30,00\n - 👀 8 pedaços",
                "quantidade": 0
            },
            "Portuguesa": {
                "imagem": "portuguesa.png",
                "descricao": "🥚 Pizza Portuguesa\n - Presunto, ovos, ervilhas e cebola.\n - 🍽️ Serve 3 a 4 pessoas\n - 💲 R$ 40,00\n - 👀 8 pedaços",
                "quantidade": 0
            },
            "MOKELE Y MBEMBE": {
                "imagem": "MOKELE.png",
                "descricao": "🦖 Mokele Pizza\n - Carne de Mokele-Mbembe em rodelas, calabreso(lá ele), alho e sal.\n - 🍽️ Serve 3 a 4 pessoas\n - 💲 R$ 12,00\n - 👀 8 pedaços",
                "quantidade": 0
            },
            "Grêmio *PROMOÇÃO*": {
                "imagem": "gremio.png",
                "descricao": "⚽ Grêmio\n - queijo, bacon e mussarela AZUL. \n - 🍽 Serve 3 a 4 pessoas\n - 💲 R$2,00\n - 👀 8 pedaços",
                "quantidade": 0
            },
            "Montanhas Nevadas": {
                "imagem": "montanhas.png",
                "descricao": "⛰ Montanha Nevada\n - Rocha gigante e Neve. \n - 🍽 Serve 50 - 100 pessoas\n - 💲 R$2.274,00\n - 👀 uma montanha de pedaços",
                "quantidade": 0
            },
            "Estrela de Neutron": {
                "imagem": "estrela.png",
                "descricao": "🌟 Estrela de Neutron\n - Estrela de Neutron. \n - 🍽 Serve ∞ pessoas\n - 💲 R$250,00\n - 👀 pedaço pra disgraça",
                "quantidade": 0
            },
            "Hemisfério Norte": {
                "imagem": "hemisferio.png",
                "descricao": "🌎 Hemisfério Norte\n - Hemisfério Norte. \n - 🍽 Serve 6,4Bi de pessoas\n - 💲 R$1700,00\n - 👀 MUITOS PEDAÇOS",
                "quantidade": 0
            },
            "Sorvete de Mostarda": {
                "imagem": "sorvete.png",
                "descricao": "🍦 Sorvete de Mostarda\n - massa de pizza, chocolate, M&M e sorvete de mostarda.\n - 🍽️ Serve 3 a 4 pessoas\n - 💲 R$ 45,00\n - 👀 8 pedaços",
                "quantidade": 0
            },
            "Vegetação da Amazonia": {
                "imagem": "amazonia.png",
                "descricao": "🌴 Vegetação da Amazonia\n - massa de pizza, gergelim, camarão e planta da amazonia.\n - 🍽️ Serve 5 a 6 pessoas\n - 💲 R$ 548,00\n - 👀 8 pedaços",
                "quantidade": 0
            },
            "Pedra Sedimentar": {
                "imagem": "sedimentar.png",
                "descricao": "🗻 Pedra Sedimentar\n - pizza de calabres com 4 camadas.\n - 🍽️ Serve 8 a 10 pessoas\n - 💲 R$ 15,00\n - 👀 24 pedaços",
                "quantidade": 0
            },
            "Espanha": {
                "imagem": "espanha.png",
                "descricao": "💃 Espanha\n - molho de tomate, orégano, mussarela, peito de peru e tomate.\n - 🍽️ Serve 3 a 4 pessoas\n - 💲 R$ 411,00\n - 👀 24 pedaços",
                "quantidade": 0
            },
            "Espanha": {
                "imagem": "espanha.png",
                "descricao": "💃 Espanha\n - molho de tomate, orégano, mussarela, peito de peru e tomate.\n - 🍽️ Serve 3 a 4 pessoas\n - 💲 R$ 411,00\n - 👀 24 pedaços",
                "quantidade": 0
            },
            "Jalapão": {
                "imagem": "jalapao.png",
                "descricao": "🏞 ✨Jalapão\n - Creme de avelã, ferrero roucher, chocolate derretido e ouro comestível.\n - 🍽️ Serve 5 a 6 pessoas\n - 💲 R$ 3.221,00\n - 👀 24 pedaços",
                "quantidade": 0
            },
            
        }

        self.mostrar_imagens_cardapio()

    def carregar_imagem(self, nome_arquivo):
        """Carrega e retorna uma imagem redimensionada."""
        try:
            caminho_imagem = os.path.join("img/", nome_arquivo)
            img = Image.open(caminho_imagem)
            img = img.resize((150, 150))

            # Criar borda arredondada nas pontas
            img = self.aplicar_borda_arredondada(img)

            return CTkImage(light_image=img, size=(150, 150))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a imagem '{nome_arquivo}': {e}")
            return None

    def aplicar_borda_arredondada(self, img):
        """Aplica borda arredondada nas imagens"""
        largura, altura = img.size
        raio = 30  # Tamanho do raio da borda arredondada

        # Criar uma máscara com bordas arredondadas
        mask = Image.new('L', (largura, altura), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([0, 0, largura, altura], radius=raio, fill=255)

        # Aplicar a máscara à imagem
        img = ImageOps.fit(img, (largura, altura))
        img.putalpha(mask)

        return img

    def mostrar_imagens_cardapio(self):
        """Exibe todas as pizzas com suas imagens e descrições, sem quantidade ou botões"""
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()

        row = 0
        for nome_pizza, dados_pizza in self.pizzas.items():
            imagem = self.carregar_imagem(dados_pizza["imagem"])
            if imagem:
                imagem_label = CTkLabel(self.frame_conteudo, image=imagem, text="")
                imagem_label.image = imagem
                imagem_label.grid(row=row, column=0, padx=20, pady=20)

                info_label = CTkLabel(self.frame_conteudo, text=dados_pizza["descricao"], font=("Arial", 14), justify="left")
                info_label.grid(row=row, column=1, padx=20, sticky="w")

                row += 1

        def pedir_pizza(self):
            """Função chamada quando o botão 'Pedir Pizza' é pressionado"""
            pedido_resumo = "Resumo do Pedido:\n\n"
            for nome_pizza, dados_pizza in self.pizzas.items():
                if dados_pizza["quantidade"] > 0:
                    pedido_resumo += f"{nome_pizza}: {dados_pizza['quantidade']} unidade(s)\n"

            if pedido_resumo == "Resumo do Pedido:\n\n":
                messagebox.showinfo("Pedido", "Nenhuma pizza foi selecionada. Por favor, escolha as pizzas desejadas.")
            else:
                messagebox.showinfo("Pedido", pedido_resumo)

    def exibir_menu(self):
        self.app_menu.mainloop()

# Exibir o menu
menu = Menu()
menu.exibir_menu()
