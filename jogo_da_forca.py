palavra_secreta = 'python'
letras_digitadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ').lower()

    if len(letra_digitada) != 1:
        print('Digite apenas uma letra.')
        continue

    tentativas += 1
    letras_digitadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)
    print(f'{letra_digitada} está na palavra secreta' if letra_digitada in palavra_secreta else f'{letra_digitada} não está na palavra secreta.')

    if palavra_formada == palavra_secreta:
        print(f'Parabéns, você ganhou! A palavra era {palavra_secreta}.')
        print(f'Número de tentativas: {tentativas}')
        break
