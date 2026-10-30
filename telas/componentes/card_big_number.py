"""
Card com um número grande (usado na Home).

Responsável: Pessoa 4
Uso:
    CardBigNumber(frame, titulo="Total de tarefas", valor=12).pack(side="left", padx=8)
"""
import tkinter as tk


class CardBigNumber(tk.Frame):
    def __init__(self, parent, titulo, valor, cor_valor="#111827"):
        super().__init__(parent, bg="white", bd=1, relief="solid", padx=16, pady=12)

        # TODO (Pessoa 4) - estilize como preferirem
        tk.Label(self, text=str(valor), bg="white", fg=cor_valor,
                 font=("Segoe UI", 24, "bold")).pack(anchor="w")
        tk.Label(self, text=titulo, bg="white", fg="#6B7280",
                 font=("Segoe UI", 10)).pack(anchor="w")
