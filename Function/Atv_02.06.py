from random import randint
import os
from termcolor import colored
import funcoes as fc

Q = int(input('Questão qual? '))
os.system ('cls')
if (Q ==1):
          print('-='*30)
          print('Questão 1')
          def calculadoraA(x,y,z):
                    return x*y*z

          x = int(input('\nInforme o valor de X '))
          y = int(input('Informe o valor de Y '))
          z = int(input('Informe o valor de Z '))
          print(colored(calculadoraA(x,y,z), 'green'))

if (Q ==2):
          print('-='*30)
          print('Questão 2')
          L= []

          def aleatorio():
                    return randint(0,100)

          for i in range(6):
                    L.append(aleatorio())
          L = sorted(L)
          print(colored(L, 'cyan'))
          print(f"Será o menor {colored(L[0], 'red')},  e o maior é {colored(L[5], 'blue')}") #se usar as aspas e o colored dentro, prestar atenção a utilização das aspas duplas
          
if (Q == 3):
          print('-='*30)
          print('Questão 3')
          def fatorial(n):
                    resultado = 1
                    for i in range(1, n+1):
                              resultado *= i
                    return resultado

          # Solicita ao usuário que digite um número
          numero = int(input("Digite um número para calcular o fatorial: "))

          # Calcula o fatorial do número digitado pelo usuário
          resultado = fatorial(numero)
          print(colored(resultado, 'red'))

if(Q == 4):
          print('-='*30)
          print('Questão 4')

          n = int(input('Até qual termo da Série vai querer ver?'))
          sequencia_fibo = fc.fibonacci(n)
          for i in range(n):
                    print(f'{i+1}° termo = {sequencia_fibo[i]}')

if(Q == 5):
    n = int(input('Digite um número '))
    fc.quant_num(n)

if(Q == 6):
    n = int(input('Digite um número '))
    fc.questao_2(n)

if(Q == 7):
    
    def questao_3():
        s = 0
        for i in range(3):
            s += float(input('Digite um número: '))
        return

    resultado = questao_3()
    print("O valor de s é:", resultado)


if(Q == 8):
    n = float(input('Digite um número '))
    def questao_4(n):
        if n> 0:
            print(colored('P', 'green'))
        else:
            print(colored('N', 'red'))
    questao_4(n)
    
if(Q == 9):
    def somaimposto(ti, custo):
        valor_final = custo*(ti/100)
        print(colored(valor_final+custo, 'green'))
    custo = float(input('Qual o valor do produto? '))
    ti = int(input('Quantos porcentos será o imposto sobre ele? '))
    os.system('cls')
    somaimposto(ti, custo)

if(Q == 10):
    def conversor(horas, minutos):
        if horas < 12:
            periodo = 'A.M'
        else:
            periodo = 'P.M'
            horas = horas - 12
        return horas, minutos, periodo
    def printar (horas_c, minutos_c, periodo):
        print(colored(f'\nA notação em 12 horas será: {horas_c}:{minutos_c} {periodo}', 'green'))
         
    while True:
        horas = int(input('Digite as horas (formato 24hrs) '))
        minutos = int(input('Digite os minutos que participara dessa conversão '))
        
        horas_c, minutos_c, periodo = conversor(horas, minutos)
        printar(horas_c, minutos_c,periodo)
        
        opcao = input("Deseja fazer outra conversão? (S/N): ").strip().upper()
        if opcao == 'N':
            break
        
        
        
if(Q == 11):
    def converter_notacao(horas, minutos):
        periodo = 'A.M.' if horas < 12 else 'P.M.'
        horas = horas % 12 if horas % 12 != 0 else 12
        return horas, minutos, periodo

    def imprimir_notacao(horas, minutos, periodo):
        print(f"A notação de 12 horas é: {horas}:{minutos:02d} {periodo}")

    while True:
        horas = int(input("Digite as horas (formato de 24 horas): "))
        minutos = int(input("Digite os minutos: "))

        horas_convertidas, minutos_convertidos, periodo = converter_notacao(horas, minutos)
        imprimir_notacao(horas_convertidas, minutos_convertidos, periodo)

        opcao = input("Deseja converter novamente? (S/N): ")
        if opcao.upper() != "S":
            break
