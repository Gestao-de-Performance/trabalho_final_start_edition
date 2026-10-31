"""
Testes automaticos do desafio final.
Coloque este arquivo na mesma pasta do seu desafio_final.py e rode:
    python desafio_final_testes.py
"""

from collections import deque
import desafio_final as d

resultados = []


def teste(nome):
    def decorador(func):
        try:
            func()
            resultados.append((nome, True, ""))
        except Exception as erro:
            resultados.append((nome, False, f"{type(erro).__name__}: {erro}"))
        return func
    return decorador


def cenario():
    fila, todos, historico = deque(), [], []
    d.abrir_chamado(fila, todos, "Ana", "sem internet", 2)
    d.abrir_chamado(fila, todos, "Bruno", "tela azul", 3)
    d.abrir_chamado(fila, todos, "Carla", "trocar mouse", 1)
    d.abrir_chamado(fila, todos, "Davi", "servidor caiu", 3)
    return fila, todos, historico


@teste("Nivel 1: abrir chamado gera protocolos 1, 2, 3...")
def _():
    fila, todos, _h = cenario()
    assert [c["protocolo"] for c in todos] == [1, 2, 3, 4]
    assert len(fila) == 4
    assert todos[0]["status"] == "pendente"


@teste("Nivel 1: atender segue a ordem de chegada (FIFO)")
def _():
    fila, todos, h = cenario()
    assert d.atender_proximo(fila, h)["nome"] == "Ana"
    assert d.atender_proximo(fila, h)["nome"] == "Bruno"
    assert len(fila) == 2 and len(h) == 2
    assert todos[0]["status"] == "atendido"


@teste("Nivel 1: atender com fila vazia devolve None")
def _():
    assert d.atender_proximo(deque(), []) is None


@teste("Nivel 2: desfazer devolve o chamado para a FRENTE da fila")
def _():
    fila, todos, h = cenario()
    d.atender_proximo(fila, h)
    d.atender_proximo(fila, h)
    c = d.desfazer_atendimento(fila, h)
    assert c["nome"] == "Bruno"                 # ultimo atendido = primeiro a voltar
    assert fila[0]["nome"] == "Bruno"
    assert c["status"] == "pendente"
    assert len(h) == 1


@teste("Nivel 2: desfazer sem historico devolve None")
def _():
    assert d.desfazer_atendimento(deque(), []) is None


@teste("Nivel 3: ordena por prioridade (3 primeiro), estavel")
def _():
    fila, todos, h = cenario()
    nomes = [c["nome"] for c in d.ordenar_por_prioridade(fila)]
    assert nomes == ["Bruno", "Davi", "Ana", "Carla"], nomes


@teste("Nivel 3: ordenar NAO altera a fila original")
def _():
    fila, todos, h = cenario()
    d.ordenar_por_prioridade(fila)
    assert [c["nome"] for c in fila] == ["Ana", "Bruno", "Carla", "Davi"]


@teste("Nivel 4: busca binaria acha e nao acha protocolos")
def _():
    fila, todos, h = cenario()
    assert d.buscar_protocolo(todos, 3)["nome"] == "Carla"
    assert d.buscar_protocolo(todos, 1)["nome"] == "Ana"
    assert d.buscar_protocolo(todos, 4)["nome"] == "Davi"
    assert d.buscar_protocolo(todos, 99) is None
    assert d.buscar_protocolo([], 1) is None


@teste("Nivel 4: contagem recursiva por prioridade")
def _():
    fila, todos, h = cenario()
    assert d.contar_por_prioridade(todos, 3) == 2
    assert d.contar_por_prioridade(todos, 1) == 1
    assert d.contar_por_prioridade([], 3) == 0


ok = sum(1 for _, passou, _ in resultados if passou)
print()
for nome, passou, msg in resultados:
    print(("[OK]   " if passou else "[FALHA]"), nome, f"\n         {msg}" if msg else "")
print(f"\nResultado: {ok}/{len(resultados)} testes passaram.")
