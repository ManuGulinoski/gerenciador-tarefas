"""
Tela Home - Desempenho.

Responsável: Pessoa 4
Layout de cima para baixo:
    [Criar v]                       (menu com "Disciplina" e "Tarefa")
    "Frase motivacional" - Autor
    [Total] [Concluídas] [Atrasadas] [Para hoje]
    [Gráfico de barras]  [Gráfico de pizza]
"""
import tkinter as tk
from tkinter import ttk  # noqa: F401

from utils.constantes import COR_FUNDO

# Descomente conforme for implementando:
# from servicos import estatisticas_service, frase_service
# from telas.modais.modal_disciplina import ModalDisciplina
# from telas.modais.modal_tarefa import ModalTarefa
# from telas.componentes.card_big_number import CardBigNumber
# from telas.componentes.graficos import criar_grafico_barras, criar_grafico_pizza


class TelaHome(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=COR_FUNDO)
        self.app = app  # use self.app.recarregar_tela() após salvar algo

        tk.Label(self, text="Desempenho", bg=COR_FUNDO,
                 font=("Segoe UI", 18, "bold")).pack(anchor="w")

        self._criar_botao_criar()
        self._criar_frase()
        self._criar_big_numbers()
        self._criar_graficos()

    def _criar_botao_criar(self):
        """
        Botão "Criar ▾" que abre um menu com "Disciplina" e "Tarefa".
        Dica: ttk.Menubutton + tk.Menu(tearoff=0) com menu.add_command(...)
        "Disciplina" abre ModalDisciplina(self, ao_salvar=self.app.recarregar_tela)
        "Tarefa"     abre ModalTarefa(self, ao_salvar=self.app.recarregar_tela)
        """
        # TODO (Pessoa 4)
        pass

    def _criar_frase(self):
        """Label com frase_service.buscar_frase() -> (frase, autor)."""
        # TODO (Pessoa 4)
        tk.Label(self, text="[frase motivacional aqui]", bg=COR_FUNDO,
                 font=("Segoe UI", 11, "italic")).pack(anchor="w", pady=10)

    def _criar_big_numbers(self):
        """
        Linha com 4 CardBigNumber usando estatisticas_service.big_numbers().
        Dica: um Frame com os cards lado a lado (pack side="left" ou grid).
        """
        # TODO (Pessoa 4)
        tk.Label(self, text="[4 cards big numbers aqui]",
                 bg=COR_FUNDO).pack(anchor="w", pady=10)

    def _criar_graficos(self):
        """
        Dois gráficos lado a lado:
        criar_grafico_barras(frame, estatisticas_service.contagem_por_status())
        criar_grafico_pizza(frame, estatisticas_service.contagem_por_tipo())
        """
        # TODO (Pessoa 4)
        tk.Label(self, text="[gráfico de barras]   [gráfico de pizza]",
                 bg=COR_FUNDO).pack(anchor="w", pady=10)
