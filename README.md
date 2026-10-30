# Gerenciador de Tarefas Acadêmicas

Sistema desktop em Python + Tkinter para cadastrar disciplinas e tarefas,
acompanhar prazos e ver o desempenho em gráficos.

## Como rodar

```bash
pip install -r requirements.txt
python main.py
```

No estado inicial do esqueleto, a janela já abre com o menu lateral e troca
entre **Home** e **Tarefas**. O resto está marcado com `# TODO (Pessoa N)`.

## Arquitetura em camadas

```
telas/        ->  servicos/  ->  models/ + repositorio/  ->  dados/dados.json
(Tkinter)         (regras)       (classes)  (lê/salva JSON)
```

Regras da equipe:

1. **As setas só apontam para baixo.** Tela chama serviço; serviço chama repositório.
2. **Só `repositorio/armazenamento.py` abre o JSON.**
3. **Serviços não importam `tkinter`.** Erros de validação viram `raise ValueError("mensagem")`;
   a tela captura com `try/except` e mostra no `messagebox`.
4. **Nada de texto solto.** "Prova", "A fazer", "Urgente" etc. vêm sempre de `utils/constantes.py`.
5. **"Atrasada" e prioridade não são salvas.** São calculadas por `tarefa.status_atual()` e `tarefa.prioridade()`.
6. **A tarefa guarda `disciplina_id`**, não o nome da disciplina.

## Divisão de responsabilidades

| Pessoa | Parte | Arquivos |
|---|---|---|
| 1 | Disciplinas e tarefas | `models/`, `servicos/disciplina_service.py`, `servicos/tarefa_service.py`, `telas/modais/modal_disciplina.py`, `telas/modais/modal_tarefa.py` |
| 2 | Base, dados, filtros e qualidade | `utils/constantes.py`, `repositorio/armazenamento.py`, `servicos/filtro_service.py`, `dados/dados.json`, GitHub, Trello, testes |
| 3 | Tela de tarefas | `telas/tela_tarefas.py`, `telas/componentes/card_tarefa.py` |
| 4 | Home e estrutura | `main.py`, `telas/app.py`, `telas/tela_home.py`, `servicos/estatisticas_service.py`, `servicos/frase_service.py`, `telas/componentes/graficos.py`, `telas/componentes/card_big_number.py` |

Pastas extras: `estudos/` (exercícios da trilha de Tkinter), `testes/` (scripts de teste) e
`dados/gerar_exemplo.py` (recria dados de exemplo com prazos a partir de hoje).

Para achar sua parte: pesquise `TODO (Pessoa 1)` (ou 2, 3, 4) no VS Code com `Ctrl+Shift+F`.

### Ordem sugerida

1. **Pessoa 2** termina `armazenamento.py` e os dados de exemplo até 31/10 (todos dependem deles).
2. **Pessoa 1** termina `dias_restantes`, `status_atual` e `prioridade` em `models/tarefa.py` até 01/11.
3. Depois disso, todos trabalham em paralelo.
4. Integração e testes juntos no final.

O cronograma completo, por pessoa e por data, está no documento da equipe.

Enquanto uma parte não está pronta, quem depende dela pode testar com dados
escritos à mão no `dados/dados.json`.

## Fluxo no Git

```bash
git checkout main
git pull                              # pega o que os outros já subiram
git checkout -b feature/nome-da-tarefa
# ... trabalha, testa ...
git add .
git commit -m "Implementa filtros da tela de tarefas"
git push -u origin feature/nome-da-tarefa
# abre Pull Request no GitHub -> outra pessoa revisa -> merge na main
```

- Nunca dar push direto na `main`.
- Commits pequenos e com mensagem clara.
- Um cartão do Trello por User Story; o nome da branch pode citar o cartão.

## Formato do JSON

```json
{
  "disciplinas": [{"id": "a1b2", "nome": "Cálculo"}],
  "tarefas": [
    {"id": "c3d4", "nome": "Lista 3", "tipo": "Exercício",
     "prazo": "2026-11-05", "disciplina_id": "a1b2",
     "status": "A fazer", "descricao": "", "cor": null}
  ]
}
```

## Tecnologias

Python 3, Tkinter / ttk / messagebox, json, datetime, uuid, requests (API ZenQuotes),
Matplotlib + FigureCanvasTkAgg, Git/GitHub, Trello.
