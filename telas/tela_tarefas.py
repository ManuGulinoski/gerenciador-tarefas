"""
Tela Tarefas.

Responsável: Pessoa 3
Usa os serviços da Pessoa 1 (tarefas/disciplinas), o filtro da Pessoa 2
e abre o ModalTarefa da Pessoa 1.
Layout de cima para baixo:
    Título + [Criar tarefa]
    Filtros: Disciplina | Tipo | Status | Prioridade | Prazo | [Limpar]
    Lista de CardTarefa (com barra de rolagem)
"""
import tkinter as tk
from tkinter import ttk, messagebox  # noqa: F401

from utils.constantes import (  # noqa: F401
    COR_FUNDO, OPCAO_TODOS, TIPOS, STATUS_TODOS, PRIORIDADES, FILTROS_PRAZO,
)

# Descomente conforme for implementando:
# from servicos import tarefa_service, disciplina_service, filtro_service
# from telas.modais.modal_tarefa import ModalTarefa
# from telas.componentes.card_tarefa import CardTarefa


class TelaTarefas(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=COR_FUNDO)
        self.app = app

        topo = tk.Frame(self, bg=COR_FUNDO)
        topo.pack(fill="x")
        tk.Label(topo, text="Tarefas", bg=COR_FUNDO,
                 font=("Segoe UI", 18, "bold")).pack(side="left")
        ttk.Button(topo, text="+ Criar tarefa",
                   command=self.abrir_modal_criar).pack(side="right")

        self._criar_filtros()

        # Área onde os cards são desenhados
        self.lista_frame = tk.Frame(self, bg=COR_FUNDO)
        self.lista_frame.pack(fill="both", expand=True, pady=10)

        self.atualizar_lista()

    # ------------------------------------------------------------------
    def _criar_filtros(self):
        """
        5 ttk.Combobox (state="readonly"), cada um começando em OPCAO_TODOS.
        - Disciplina: nomes vindos de disciplina_service.listar_disciplinas()
          (guarde um dicionário nome -> id para converter depois)
        - Tipo: [OPCAO_TODOS] + TIPOS
        - Status: [OPCAO_TODOS] + STATUS_TODOS
        - Prioridade: [OPCAO_TODOS] + PRIORIDADES
        - Prazo: [OPCAO_TODOS] + FILTROS_PRAZO
        Em cada combobox: .bind("<<ComboboxSelected>>", lambda e: self.atualizar_lista())
        """
        # TODO (Pessoa 3)
        tk.Label(self, text="[filtros aqui]", bg=COR_FUNDO).pack(anchor="w", pady=10)

    def _valores_dos_filtros(self):
        """
        Lê os combobox e devolve um dicionário pronto para
        filtro_service.filtrar_tarefas(**filtros).
        OPCAO_TODOS vira None.
        """
        # TODO (Pessoa 3)
        return {}

    # ------------------------------------------------------------------
    def atualizar_lista(self):
        """
        1. Apaga os cards antigos (for w in self.lista_frame.winfo_children(): w.destroy())
        2. tarefas = filtro_service.filtrar_tarefas(**self._valores_dos_filtros())
        3. Para cada tarefa, cria um CardTarefa passando as funções de callback.
        4. Se a lista estiver vazia, mostra "Nenhuma tarefa encontrada".
        Dica de rolagem: Canvas + Scrollbar + Frame interno.
        """
        # TODO (Pessoa 3)
        pass

    # ------------------------------------------------------------------
    # Ações (chamadas pelos botões e pelos ícones dos cards)
    # ------------------------------------------------------------------
    def abrir_modal_criar(self):
        """ModalTarefa(self, ao_salvar=self.atualizar_lista)"""
        # TODO (Pessoa 3)
        messagebox.showinfo("Em construção", "Modal de tarefa ainda não implementado.")

    def editar(self, tarefa):
        """ModalTarefa(self, tarefa=tarefa, ao_salvar=self.atualizar_lista)"""
        # TODO (Pessoa 3)
        pass

    def excluir(self, tarefa):
        """
        if messagebox.askyesno("Excluir", f"Excluir a tarefa '{tarefa.nome}'?"):
            tarefa_service.excluir_tarefa(tarefa.id)
            messagebox.showinfo("Sucesso", "Tarefa excluída!")
            self.atualizar_lista()
        """
        # TODO (Pessoa 3)
        pass

    def concluir(self, tarefa):
        """tarefa_service.concluir_tarefa(...) + pop-up de sucesso + atualizar_lista()"""
        # TODO (Pessoa 3)
        pass
