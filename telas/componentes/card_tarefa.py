"""
Card de uma tarefa na tela Tarefas.

Responsável: Pessoa 3
O card só DESENHA. Quando o usuário clica em um ícone, ele chama a função
recebida no construtor; quem decide o que fazer é a TelaTarefas.

Uso:
    CardTarefa(frame, tarefa, nome_disciplina,
               ao_editar=self.editar, ao_excluir=self.excluir,
               ao_concluir=self.concluir).pack(fill="x", pady=4)
"""
import tkinter as tk

from utils.constantes import FORMATO_DATA_TELA  # noqa: F401


class CardTarefa(tk.Frame):
    def __init__(self, parent, tarefa, nome_disciplina,
                 ao_editar, ao_excluir, ao_concluir):
        super().__init__(parent, bg="white", bd=1, relief="solid", padx=12, pady=8)
        self.tarefa = tarefa

        # TODO (Pessoa 3) - mostrar:
        # - nome
        # - prazo (tarefa.prazo.strftime(FORMATO_DATA_TELA))
        # - status (tarefa.status_atual())
        # - disciplina (nome_disciplina)
        # - tipo
        # - prioridade (tarefa.prioridade()) - opcional, mas fica bonito
        # - faixa colorida à esquerda se tarefa.cor existir
        #
        # Ícones: use texto ou os símbolos ✎ ✕ ✓ (evite emojis como 🗑,
        # que podem não aparecer no Tkinter do Windows):
        #   command=lambda: ao_editar(tarefa)
        #   command=lambda: ao_excluir(tarefa)
        #   command=lambda: ao_concluir(tarefa)
        # Dica: esconda/desabilite o ✓ se a tarefa já estiver concluída.
        pass
