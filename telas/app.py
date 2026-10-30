"""
Janela principal: menu lateral fixo + área onde as telas são exibidas.

Responsável: Pessoa 4
Este arquivo JÁ FUNCIONA: abre a janela e troca entre Home e Tarefas.
Cada tela é recriada toda vez que é aberta, então ela sempre mostra
os dados atualizados do JSON.
"""
import tkinter as tk

from telas.tela_home import TelaHome
from telas.tela_tarefas import TelaTarefas
from utils.constantes import (
    COR_FUNDO, COR_MENU_LATERAL, COR_MENU_TEXTO,
    LARGURA_MENU, TAMANHO_JANELA, TITULO_APP,
)


class App(tk.Tk):
    TELAS = {
        "Home": TelaHome,
        "Tarefas": TelaTarefas,
    }

    def __init__(self):
        super().__init__()
        self.title(TITULO_APP)
        self.geometry(TAMANHO_JANELA)
        self.configure(bg=COR_FUNDO)

        self.tela_atual = None
        self.nome_tela_atual = None
        self.botoes_menu = {}

        self._criar_menu_lateral()

        self.area_conteudo = tk.Frame(self, bg=COR_FUNDO)
        self.area_conteudo.pack(side="left", fill="both", expand=True)

        self.mostrar_tela("Home")

    def _criar_menu_lateral(self):
        menu = tk.Frame(self, bg=COR_MENU_LATERAL, width=LARGURA_MENU)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)  # mantém a largura fixa

        tk.Label(menu, text="Menu", bg=COR_MENU_LATERAL, fg=COR_MENU_TEXTO,
                 font=("Segoe UI", 14, "bold")).pack(pady=(20, 30))

        for nome in self.TELAS:
            botao = tk.Button(
                menu, text=nome, anchor="w", relief="flat", bd=0, highlightthickness=0,
                bg=COR_MENU_LATERAL, fg=COR_MENU_TEXTO,
                activebackground="#374151", activeforeground=COR_MENU_TEXTO,
                font=("Segoe UI", 11), padx=20, pady=8, cursor="hand2",
                command=lambda n=nome: self.mostrar_tela(n),
            )
            botao.pack(fill="x")
            self.botoes_menu[nome] = botao

    def mostrar_tela(self, nome):
        """Destroi a tela atual e cria a tela 'nome' ("Home" ou "Tarefas")."""
        if self.tela_atual is not None:
            self.tela_atual.destroy()

        classe_tela = self.TELAS[nome]
        self.tela_atual = classe_tela(self.area_conteudo, app=self)
        self.tela_atual.pack(fill="both", expand=True, padx=20, pady=20)
        self.nome_tela_atual = nome

        for n, botao in self.botoes_menu.items():
            botao.configure(bg="#374151" if n == nome else COR_MENU_LATERAL)

    def recarregar_tela(self):
        """Chame depois de criar/editar/excluir algo para atualizar a tela."""
        self.mostrar_tela(self.nome_tela_atual)
