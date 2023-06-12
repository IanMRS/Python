from random import randint
import os
from termcolor import colored
import funcoes as fc

cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
        'azul': '\033[34m',
        'magenta' :'\033[35m', 
        'ciano': '\033[36m',
        'grey': '\033[37m'}

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
            periodo = 'A'
        else:
            periodo = 'P'
            horas = horas - 12
        return horas, minutos, periodo
    def printar (horas_c, minutos_c, periodo):
        print(colored(f'\nA notação em 12 horas será: {horas_c}:{minutos_c} {periodo}.M', 'green'))
         
    while True:
        horas = int(input('Digite as horas (formato 24hrs) '))
        minutos = int(input('Digite os minutos que participara dessa conversão '))
        
        horas_c, minutos_c, periodo = conversor(horas, minutos)
        printar(horas_c, minutos_c,periodo)
        
        opcao = input("Deseja fazer outra conversão? (S/N): ").strip().upper()
        if opcao == 'N':
            break
        
if(Q == 11):
    total = valor_deTodas = 0
    
    def valorPagamento (prestacao,dias):
        valor_final = prestacao+(prestacao*((3+(dias/10))/100))
        return valor_final
        
        
        
    while True:   
        prestacao = float(input('\n\nQual o valor da prestação? '))
        if prestacao == 0:
            break
        dias = float(input('Quantos dias teve de atraso? '))
        
        
        os.system('cls')
        valor_final = valorPagamento(prestacao,dias)
        total +=1
        valor_deTodas += valor_final
        print(f'\nValor a ser pago será {cores["ciano"]}R$ {valor_final}{cores["limpa"]}')
    print(colored('-=', 'red')*20)
    print(colored('RELATORIO DO DIA', 'red'))
    print(colored('-=', 'red')*20)
    print(f'Quantidade de prestações foi {cores["ciano"]}{total}{cores["limpa"]}')
    print(f'E o valor de todas as de prestações foi {cores["ciano"]}R$ {valor_deTodas}{cores["limpa"]}')
        
        
