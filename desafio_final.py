"""
DESAFIO FINAL - Central de Atendimento
Aluno(a): ____________________

Complete as funcoes marcadas com TODO, de cima para baixo (Nivel 1 ao 4).
O menu no final do arquivo ja esta pronto: NAO precisa mexer nele.

Para conferir seu progresso, rode:   python desafio_final_testes.py
Para usar o programa de verdade:     python desafio_final.py
"""

from collections import deque


# ---------------------------------------------------------------
# NIVEL 1 - FILA: abrir e atender chamados
# ---------------------------------------------------------------
def criar_chamado(protocolo, nome, descricao, prioridade):
    """Ja pronta: cada chamado e um dicionario."""
    return {
        "protocolo": protocolo,
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,      # 1 = baixa, 2 = media, 3 = alta
        "status": "pendente",
    }


def abrir_chamado(fila, todos, nome, descricao, prioridade):
    """
    TODO:
    1. O protocolo e o proximo numero: len(todos) + 1
    2. Crie o chamado com criar_chamado(...)
    3. Coloque o chamado no FIM da fila e tambem na lista 'todos'
    4. Devolva o chamado criado
    """
    pass


def atender_proximo(fila, historico):
    """
    TODO:
    1. Se a fila estiver vazia, devolva None
    2. Retire o chamado da FRENTE da fila (dica: popleft)
    3. Mude o status dele para "atendido"
    4. Empilhe o chamado no 'historico' (dica: append)
    5. Devolva o chamado atendido
    """
    pass


# ---------------------------------------------------------------
# NIVEL 2 - PILHA: desfazer o ultimo atendimento
# ---------------------------------------------------------------
def desfazer_atendimento(fila, historico):
    """
    TODO:
    1. Se o 'historico' estiver vazio, devolva None
    2. Desempilhe o ultimo chamado do 'historico' (dica: pop)
    3. Mude o status de volta para "pendente"
    4. Coloque-o na FRENTE da fila (dica: appendleft)
    5. Devolva o chamado
    """
    pass


# ---------------------------------------------------------------
# NIVEL 3 - ORDENACAO: lista de pendentes por prioridade
# ---------------------------------------------------------------
def ordenar_por_prioridade(chamados):
    """
    TODO: devolva uma NOVA lista com os chamados em ordem de prioridade,
    do maior (3) para o menor (1).
    Regras:
    - NAO use sorted() nem .sort(): implemente Bubble, Selection ou Insertion.
    - NAO altere a lista recebida (comece com: v = list(chamados)).
    - Chamados com a mesma prioridade mantem a ordem de chegada.
      (Pense: qual comparacao garante isso? < ou <= ?)
    """
    pass


# ---------------------------------------------------------------
# NIVEL 4 - BUSCA BINARIA e RECURSAO
# ---------------------------------------------------------------
def buscar_protocolo(todos, protocolo):
    """
    TODO: busca binaria na lista 'todos' (ela ja esta em ordem de protocolo,
    porque os protocolos sao criados em sequencia: 1, 2, 3...).
    Devolva o chamado encontrado ou None. NAO use um laco 'for' que
    percorra a lista inteira.
    """
    pass


def contar_por_prioridade(chamados, prioridade, i=0):
    """
    TODO: conte, RECURSIVAMENTE, quantos chamados tem a prioridade dada.
    Proibido usar for, while ou sum(). Dicas:
    - Caso base: se i >= len(chamados), nao ha mais nada a contar (0).
    - Passo recursivo: (1 se o chamado i tem a prioridade, senao 0)
                       + contar_por_prioridade(chamados, prioridade, i + 1)
    """
    pass


# ---------------------------------------------------------------
# INTERFACE (menu)
# ---------------------------------------------------------------
def ler_inteiro(mensagem, minimo, maximo):
    while True:
        texto = input(mensagem)
        if texto.isdigit() and minimo <= int(texto) <= maximo:
            return int(texto)
        print(f"Digite um numero entre {minimo} e {maximo}.")


def mostrar(chamado):
    print(f"#{chamado['protocolo']:03d} | prioridade {chamado['prioridade']} | "
          f"{chamado['nome']}: {chamado['descricao']} [{chamado['status']}]")


def menu():
    fila, todos, historico = deque(), [], []
    while True:
        print("\n=== CENTRAL DE ATENDIMENTO ===")
        print("1) Abrir chamado")
        print("2) Atender proximo")
        print("3) Desfazer ultimo atendimento")
        print("4) Listar pendentes por prioridade")
        print("5) Buscar por protocolo")
        print("6) Relatorio")
        print("0) Sair")
        op = ler_inteiro("Escolha: ", 0, 6)

        if op == 0:
            print("Ate a proxima!")
            break
        elif op == 1:
            nome = input("Nome: ")
            desc = input("Descricao: ")
            prio = ler_inteiro("Prioridade (1-3): ", 1, 3)
            mostrar(abrir_chamado(fila, todos, nome, desc, prio))
        elif op == 2:
            c = atender_proximo(fila, historico)
            print("Atendendo:" if c else "Fila vazia.")
            if c:
                mostrar(c)
        elif op == 3:
            c = desfazer_atendimento(fila, historico)
            print("Devolvido a fila:" if c else "Nada para desfazer.")
            if c:
                mostrar(c)
        elif op == 4:
            pendentes = ordenar_por_prioridade(fila)
            if not pendentes:
                print("Nenhum chamado pendente.")
            for c in pendentes:
                mostrar(c)
        elif op == 5:
            p = ler_inteiro("Protocolo: ", 1, 10**6)
            c = buscar_protocolo(todos, p)
            mostrar(c) if c else print("Protocolo nao encontrado.")
        elif op == 6:
            print(f"Total aberto: {len(todos)} | Pendentes: {len(fila)} | "
                  f"Atendidos: {len(historico)}")
            for p in (3, 2, 1):
                print(f"Prioridade {p}: {contar_por_prioridade(todos, p)}")


if __name__ == "__main__":
    menu()
