import time
import sys

def efeito_digitacao(texto, delay=0.1):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def digitar(texto, delay=0.05):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delay)
    print()

historico = []

temperatura = None
energia = None
comunicacao = None

def inserir_dados():
    temperatura = float(input("Digite a temperatura da nave: "))
    print()

    energia = float(input("Digite o nível de energia da nave em %: "))
    print()

    comunicacao = int(input("""
    0 = Afetado
    1 = Operando 
    Digite os status de comunicação: """))
    print()

    leitura = [temperatura, energia, comunicacao]
    historico.append(leitura)

    return temperatura, energia, comunicacao

    efeito_digitacao("Carregando informações...", delay=0.08)
    print()

def visualizar_status(temperatura, energia, comunicacao):
    if temperatura is None:
        print("Nenhum dado foi inserido ainda.")
        return
        print()

    efeito_digitacao("STATUS ATUAL DA NAVE")
    print(f"Temperatura: {temperatura}")
    print(f"Nível de energia: {energia}%")

    if comunicacao == 0:
        print("Comunicação: Afetada")
    else:
        print("Comunicação: Operando")
    print()

def executar_analise(temperatura, energia, comunicacao):
    if temperatura is None:
        print("Insira os dados antes de executar a análise.")
        return
        print()

    efeito_digitacao("Carregando informações...", delay=0.08)
    print()

    print("Temperatura:")
    if temperatura >= 80:
        digitar("Alerta de superaquecimento")
    elif temperatura <= 20:
        digitar("Alerta de temperatura muito baixa")
    else:
        digitar("Temperatura normal")
    print()

    print("Energia:")
    if energia <= 10:
        digitar("Nível de energia crítico")
    elif energia <= 20:
        digitar("Economia de energia")
    else:
        digitar("Energia Estável")
    print()

    print("Comunicação:")
    if comunicacao == 0:
        digitar("Falha de comunicação")
    else:
        digitar("Comunicação estável")

def mostrar_historico():
    if len(historico) == 0:
        print("Nenhuma leitura foi registrada ainda.")
        return
        print()

    print("HISTÓRICO DAS LEITURAS")

    for i, leitura in enumerate(historico):
        temperatura = leitura[0]
        energia = leitura[1]
        comunicacao = leitura[2]

        print(f"Leitura {i + 1}:")
        print(f"Temperatura: {temperatura}")
        print(f"Energia: {energia}%")

        if comunicacao == 0:
            print("Comunicação: Afetada")
        else:
            print("Comunicação: Operando")
print()

while True:
    print()
    print("""MENU DO SISTEMA DA NAVE
    1 - Inserir dados
    2 - Visualizar status
    3 - Executar análise
    4 - Histórico das leituras
    5 - Encerrar sistema""")
    print()
    opcao = int(input("Escolha uma opção: "))
    print()

    if opcao == 1:
        temperatura_nave, nivel_energia, comunicacao = inserir_dados()

    elif opcao == 2:
        visualizar_status(temperatura_nave, nivel_energia, comunicacao)

    elif opcao == 3:
        executar_analise(temperatura_nave, nivel_energia, comunicacao)

    elif opcao == 4:
        mostrar_historico()

    elif opcao == 5:
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")