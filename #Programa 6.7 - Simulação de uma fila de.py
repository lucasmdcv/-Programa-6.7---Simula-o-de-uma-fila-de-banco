#Programa 6.7 - Simulação de uma fila de banco
último = 10
fila = list(range(1, último + 1))
while True :
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):")
    if operação == 'A':
        if len(fila) > 0 :
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido')
        else:
            print('fila vazia, ninguém pode atender')
    elif operação == 'F' :
        último += 1 #incrementa o ticket do novo cliente
        fila.append(último)
    elif operação == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")