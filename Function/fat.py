cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
        'azul': '\033[34m',
        'magenta' :'\033[35m', 
        'ciano': '\033[36m',
        'grey': '\033[37m'}


def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# Solicita ao usuário que digite um número
numero = int(input("Digite um número para calcular o fatorial: "))

# Calcula o fatorial do número digitado pelo usuário
resultado = fatorial(numero)

# Exibe o resultado na tela
print(f"O fatorial de {cores['amarelo']}{numero}{cores['limpa']} é igual a {cores['ciano']}{resultado}{cores['limpa']}")