# Testes

Scripts simples com `assert` para testar serviços e modelos.
Rode sempre a partir da pasta do projeto, sem o `.py`:

    python -m testes.teste_tarefa

Os testes gravam no dados.json. Depois de testar, restaure os dados de exemplo:

    python -m dados.gerar_exemplo
