# Desafio Final — Central de Atendimento

## A história

Você foi contratado(a) para criar o sistema de **atendimento de chamados de suporte** de uma empresa. Pessoas abrem chamados ("minha internet caiu", "o servidor parou"), a equipe atende **por ordem de chegada**, e o(a) chefe quer poder **desfazer** um atendimento marcado por engano, ver os pendentes **por urgência** e **achar qualquer chamado pelo número de protocolo**.

Boa notícia: você já conhece todas as ferramentas necessárias. Este desafio junta tudo o que aprendemos no curso.

| O que o sistema faz | Ferramenta que você vai usar |
|---|---|
| Atender por ordem de chegada | **Fila** (FIFO) |
| Desfazer o último atendimento | **Pilha** (LIFO/FILO) |
| Listar pendentes por urgência | **Ordenação** (Bubble, Selection ou Insertion) |
| Achar chamado pelo protocolo | **Busca binária** |
| Contar chamados por prioridade | **Recursão** |
| Menu e leitura de dados | Laço, condição, validação de entrada (já pronto) |

## O que já vem pronto

- O arquivo **`desafio_final.py`** com o menu completo e as funções vazias, cada uma com instruções em passos (`TODO`).
- O arquivo **`desafio_final_testes.py`**, que confere automaticamente se cada função funciona.

Você **só** precisa completar as 7 funções. Não é preciso mexer no menu.

## Como trabalhar

1. Coloque os dois arquivos na mesma pasta.
2. Complete as funções **na ordem** (Nível 1 → 4).
3. Depois de cada função, rode os testes:

```bash
python desafio_final_testes.py
```

4. Quando todos passarem (`9/9`), rode o programa e teste o menu "de verdade":

```bash
python desafio_final.py
```

> Os testes mostram o que está errado. Leia a mensagem de erro com calma: ela costuma dizer exatamente onde olhar.

## Os níveis

### Nível 1 — Fila (obrigatório)
Funções `abrir_chamado` e `atender_proximo`. O primeiro chamado aberto é o primeiro atendido.

### Nível 2 — Pilha (obrigatório)
Função `desfazer_atendimento`. O **último** chamado atendido é o **primeiro** a voltar, e volta para a **frente** da fila (ele já esperava, não pode perder a vez).

### Nível 3 — Ordenação
Função `ordenar_por_prioridade`. Escreva você mesmo(a) um algoritmo de ordenação. **Não vale `sorted()`** nem `.sort()`.
Desafio dentro do desafio: chamados de **mesma prioridade devem continuar na ordem de chegada**.

### Nível 4 — Busca binária e recursão
Funções `buscar_protocolo` (busca binária) e `contar_por_prioridade` (recursão, sem `for`, `while` nem `sum`).

### Bônus (opcional, vale pontos extras)

Escolha quantos quiser. Todos exigem alterar ou ampliar o programa:

1. **Prazo de atendimento:** cada chamado ganha um campo `tempo_espera`; o relatório mostra a média (use recursão para somar).
2. **Cancelar chamado:** nova opção no menu que remove um chamado pendente pelo protocolo (e faz o desfazer continuar funcionando).
3. **Furar a fila:** chamados de prioridade 3 vão para a frente da fila ao serem abertos.
4. **Salvar e carregar:** gravar os chamados em um arquivo de texto ao sair e recarregá-los ao abrir.
5. **Comparar algoritmos:** gerar 1.000 chamados aleatórios e comparar quantas comparações cada ordenação faz.


