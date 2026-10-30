"""
Modal para criar ou editar tarefa.

Responsável: Pessoa 1
Uso:
    ModalTarefa(parent, ao_salvar=funcao)                 # criar
    ModalTarefa(parent, tarefa=obj, ao_salvar=funcao)     # editar
"""
import tkinter as tk
from tkinter import ttk, messagebox  # noqa: F401
from datetime import datetime  # noqa: F401

from utils.constantes import (  # noqa: F401
    TIPOS, STATUS_SELECIONAVEIS, CORES_TAREFA,
    MAX_NOME_TAREFA, MAX_DESCRICAO_TAREFA, FORMATO_DATA_TELA,
)

# from servicos import tarefa_service, disciplina_service


class ModalTarefa(tk.Toplevel):
    def __init__(self, parent, tarefa=None, ao_salvar=None):
        super().__init__(parent)
        self.tarefa = tarefa
        self.ao_salvar = ao_salvar

        self.title("Editar tarefa" if tarefa else "Nova tarefa")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        self._criar_campos()
        if tarefa:
            self._preencher_campos()

    def _criar_campos(self):
        """
        Campos (use grid com 2 colunas: label | campo):
        - Nome *        ttk.Entry
        - Tipo *        ttk.Combobox(values=TIPOS, state="readonly")
        - Prazo *       Tkinter não tem calendário nativo. Opções:
                          a) ttk.Entry no formato DD/MM/AAAA (FORMATO_DATA_TELA)
                          b) 3 Combobox: dia / mês / ano
        - Descrição     ttk.Entry (máx. MAX_DESCRICAO_TAREFA)
        - Status *      ttk.Combobox(values=STATUS_SELECIONAVEIS, state="readonly")
        - Cor           ttk.Combobox(values=list(CORES_TAREFA.keys()))
        - Disciplina *  ttk.Combobox com os nomes de disciplina_service.listar_disciplinas()
                        (guarde um dicionário nome -> id)
        Botões: Cancelar | Salvar

        Se não houver nenhuma disciplina cadastrada, avise o usuário
        que ele precisa criar uma disciplina primeiro.
        """
        # TODO (Pessoa 1)
        pass

    def _preencher_campos(self):
        """No modo edição, coloca os valores de self.tarefa nos campos."""
        # TODO (Pessoa 1)
        pass

    def _ler_prazo(self):
        """
        Converte o texto digitado para datetime.date.
        datetime.strptime(texto, FORMATO_DATA_TELA).date()
        Se o formato estiver errado, lance ValueError("Data inválida. Use DD/MM/AAAA.")
        """
        # TODO (Pessoa 1)
        pass

    def salvar(self):
        """
        try:
            prazo = self._ler_prazo()
            tarefa_service.criar_tarefa(...) ou editar_tarefa(self.tarefa.id, ...)
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro), parent=self)
            return
        messagebox.showinfo("Sucesso", "...", parent=self)
        if self.ao_salvar: self.ao_salvar()
        self.destroy()
        """
        # TODO (Pessoa 1)
        pass
