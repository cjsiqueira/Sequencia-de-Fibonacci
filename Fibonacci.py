# Sequencia-de-Fibonacci
#Apenas um exercício de Lógica em Python que apresenta os 10 primeiros termos da sequencia de Fibonacci e posteriormente pergunta ao usuário quantos a mais ele quer ver. 


c = 1
valor = 1
antecessor = 0
mais = 10
total = 0


while mais != 0 :
    total += mais 

    while c <= total :
        print (f'O {c} e {c + 1} termos da sequencia são: {antecessor} e {valor}.')



        antecessor = antecessor + valor 
        valor = valor + antecessor 
        c += 1

    print ('PAUSA')
    mais = int(input('Quantos termos a mais você quer ver?'))


print ('O programa acabou. OBRIGADO!')
