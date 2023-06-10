def fibonacci(n):
          if n <=0:
                    return []
          elif n ==1:
                    return [0]
          elif n == 2:
                    return [0,1]
          else: 
                    sequencia = [0,1]
                    while len(sequencia) < n:
                              sequencia.append(sequencia[-1] + sequencia[-2])
                    return sequencia

def quant_num(n):
    for i in range(1,n+1):
        print(f'{i} '*i)

def questao_2(n):
    L = []
    for i in range(1, n+1):
        L.append(i)
        lista = ' '.join(map(str, L))
        print(lista)


