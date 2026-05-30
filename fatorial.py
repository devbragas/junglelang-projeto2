print("Digite um numero para calcular o fatorial:")
entrada = input()
numero = int(entrada)
resultado = 1
um = 1
while numero > 1:
    temp = resultado
    copia_numero = numero
    copia_numero = copia_numero - um
    while copia_numero > 0:
        resultado = resultado + temp
        copia_numero = copia_numero - um
    numero = numero - um
print("O fatorial selvagem desse numero eh:")
print(resultado)