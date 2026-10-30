"""
Gráficos Matplotlib dentro do Tkinter.

Responsável: Pessoa 4
As funções recebem o frame onde o gráfico vai aparecer e um dicionário
{rótulo: quantidade} vindo do estatisticas_service.

Uso:
    criar_grafico_barras(frame, {"A fazer": 3, "Em andamento": 1, ...}).pack(side="left")
"""
from matplotlib.figure import Figure  # noqa: F401
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # noqa: F401


def criar_grafico_barras(parent, dados):
    """
    Gráfico de barras: tarefas por status.
    Retorna o widget Tkinter (canvas.get_tk_widget()) para quem chamou dar pack/grid.

    Esqueleto:
        fig = Figure(figsize=(5, 3.5), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(list(dados.keys()), list(dados.values()))
        ax.set_title("Tarefas por status")
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        return canvas.get_tk_widget()

    Importante: use Figure (e não plt.figure) para não abrir janelas extras.
    """
    # TODO (Pessoa 4)
    raise NotImplementedError


def criar_grafico_pizza(parent, dados):
    """
    Gráfico de pizza: tarefas por tipo.
    Cuidado: se todos os valores forem 0, ax.pie dá erro/aviso.
    Nesse caso mostre um texto "Sem tarefas cadastradas".
    """
    # TODO (Pessoa 4)
    raise NotImplementedError
