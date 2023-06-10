def dados(nome, idade=None):
          if(idade is not None):
                    return(print(f'O {nome} tem {idade} anos.'))
          else:
                    return(print(f'O {nome} tem idade desconhecida.'))
dados('João')




def Excalculadora(x,y):
          return{'\nsoma': x+y, 'subtração':x-y}
resultados = Excalculadora(3,5)

for key in resultados:
          print(f'{key}: {resultados[key]}')
          
          
def fatorial(n):
resultado = 1
for i in range(1, n+1):
          resultado *= i
return resultado

# Solicita ao usuário que digite um número
numero = int(input("Digite um número para calcular o fatorial: "))

# Calcula o fatorial do número digitado pelo usuário
resultado = fatorial(numero)
print(resultado)          
