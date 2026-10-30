"""
Modal (janela pop-up) para criar ou editar disciplina.

Responsável: Pessoa 1
Uso:
    ModalDisciplina(parent, ao_salvar=funcao)                    # criar
    ModalDisciplina(parent, disciplina=obj, ao_salvar=funcao)    # editar

'ao_salvar' é uma função sem parâmetros chamada depois de salvar com sucesso
(normalmente para recarregar a tela que abriu o modal).
"""
import tkinter as tk
from tkinter import ttk, messagebox  # noqa: F401

from utils.constantes import MAX_NOME_DISCIPLINA  # noqa: F401

# from servicos import disciplina_service


class ModalDisciplina(tk.Toplevel):
    def __init__(self, parent, disciplina=None, ao_salvar=None):
        super().__init__(parent)
        self.disciplina = disciplina
        self.ao_salvar = ao_salvar

        self.title("Editar disciplina" if disciplina else "Nova disciplina")
        self.resizable(False, False)
        self.transient(parent)   # fica na frente da janela principal
        self.grab_set()          # bloqueia a janela principal enquanto aberto

        self._criar_campos()

    def _criar_campos(self):
        """
        - Label "Nome *" + ttk.Entry (preencher com disciplina.nome se for edição)
        - Botões "Cancelar" (self.destroy) e "Salvar" (self.salvar)
        Dica para limitar a 50 caracteres: use validatecommand no Entry,
        ou só deixe o serviço barrar com ValueError.
        """
        # TODO (Pessoa 1)
        pass

    def salvar(self):
        """
        try:
            criar_disciplina(nome) ou editar_disciplina(id, nome)
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro), parent=self)
            return
        messagebox.showinfo("Sucesso", "...", parent=self)
        if self.ao_salvar: self.ao_salvar()
        self.destroy()
        """
        # TODO (Pessoa 1)
        pass
