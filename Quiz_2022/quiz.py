import os
from time import sleep
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
            'azul': '\033[34m',
            
            'magenta' :'\033[35m', 
            'ciano': '\033[36m',
            'grey': '\033[37m'}
##A primeira questão nas listas sempre será a correta
##Prof, não entendi bem as funções aí decidi deixar sem
##E aparentemente o CLS não está funcionando
QUESTAO = {
  "Sobre o multímetro, assinale a alternativa CORRETA sobre uma de suas funções= ":
      ["Verifica a tensão contínua ou alternada de determinado circuito elétrico.",
      "Serve para medir a temperatura ambiente.",
      "Não realiza testes de continuidade em circuitos elétricos.",
      "Serve para limpar componentes do computador deixando-os funcionais."],

  "Sobre placa mãe, é incorreto afirmar que? = ":
      ["A placa mãe é um circuito integrado formado por uma camada chamada de mesa epitaxial de silício.",
      "A placa-mãe nada mais é do que uma central de comunicação.",
        "A placa-mãe fica encaixada diretamente com o cabo da fonte que transporta a energia elétrica necessária pra ela funcionar.",
        "A placa mãe é basicamente composta por 7 camadas soldadas."],
  
    "Dos aplicativos abaixo, qual não funciona para programar? = ":
    ["duolingo",
    "portugol",
    "pycharm",
    "visual studio"],

    "Qual dos comandos abaixo não está presente na sintaxe de Python? = ":
    ["escreva",
    "str",
    "range",
    "random"],
    
    "Marque a alternativa incorreta ao fazer a manutenção no PC= ":
    ["Executar uma atualização de BIOS mal-sucedida.",
    "Executar um backup completo do sistema, antes de tudo.",
    "Executar o utilitário de verificação de disco (chkdsk).",
    "Executar todas as atualizações de aplicativos e drivers."],

    "Das alternativas seguintes, é correto afirmar que = ":
    [ "O HD é mais lento que a RAM e armazena dados permanentemente.",
    "Ao desmontar um computador é não existe a necessidade de usar ferramentas antiestática.",
    "Existem lacunas de ar entre o cooler e o processador que atrapalham a dissipação de calor. Para melhorar isso, é preciso aplicar álcool isopropílico ao unir os componentes.",
    "O cabo flat SATA possui 3 conexões: um preto, um azul e um vermelho."
    ],

    "O que é hot swapping? = ":
    ["Tecnologia que permite a remoção e substituição de componentes em equipamentos sem precisar desligá-los.",
    "Um dispositivo que permite a comunicação direta do usuário com o computador.",
    "Implica no processo de apagar totalmente o conteúdo do computador, reinstalando seu sistema operacional do zero.",
    "É o componente responsável por dar mais agilidade e velocidade no funcionamento geral do sistema. "
    ],
    "Qual desses dispositivos é um periférico de entrada de dados? = ":
    ["Teclado.",
    "Caixa de som.",
    "Monitor.",
    "Memória RAM."
    ]

}
QUESTAO2 = {
   "Qual das alternativas abaixo informa a função dos jumpers de configuração?= ":
    ["São utilizados para ativar, regular ou desativar funções específicas do sistema que não são acessíveis via software.",
    "São dispositivos capazes de armazenar informações para posterior consulta ou uso.",
    "Possuem função principal de transformar a corrente elétrica da rede, que chega em uma voltagem alta, para uma voltagem menor, que é a indicada para o hardware do computador.",
    "São um conjunto de linhas de comunicação que permitem a interligação entre dispositivos."],
  
   "Para que serve o método append? = ":
   ["Adicionar elemento ao final da lista",
   "Adicionar elemento ao inicio da lista",
   "Adicionar elemento ao meio da lista",
   "Somar as listas"],
  
   "Com qual tipo de memória é possível a leitura, gravação e regravação de dados, mas que, ao desligar o computador, esse tipo de memória perde todos esses dados? = ":
   ["RAM",
   "EPROM.",
    "ROM.",
    "PROM."],

    "Existem vários tipos de fontes de alimentação, porém, os dois mais utilizados são = ":
    ["AT e ATX",
    "TA e ATX.",
    "AT e TAX.",
    "TA e TAX."],

    "Qual desses itens abaixo é usado para manter a temperatura da CPU baixa e constante? = ":
    ["Pasta térmica.", 
   "Pasta de dente.",
    "Creme de cabelo.",
    "Pasta isolante."],
   
    "Pra que serve a BIOS e onde se encontra?":
    ["Controla e configura os dispositivos periféricos dentro da placa-mãe.",
    "Transfere energia para o computador na fonte de alimentação.",
    "Controla os dispositivos de saída dentro da placa-mãe.",
    "Serve pra configuar os dispositivos conectados dentro da CPU."
    ],
    "Qual a definição de Algoritmo? = ":
    ["Algoritmo é uma sequência lógica de instruções que devem ser seguidas para resolução de um problema",
    "Algoritmo é um programa de computador que segue uma sequência lógica de tarefas e variáveis",
    "Algoritmo é um problema lógico que para ser solucionado necessita de um programa baseado em tarefas",
    "Algoritmo é algo que tem ritmo que causa um problema em quem não tem coordenação motora, gerando um problema"

    ]


}
QUESTAO3 ={
   "Dentre as alternativas abaixo, qual alternativa possui apenas exemplos de aplicativos que utilizam o Big Data? = ":
   ["Netflix, Twitter e Instagram.", 
   "Netflix, Uber e Letras.",
    "Facebook, Livros e Uber.",
    "Whatsapp, Instagram e Pinturas."],
   
   "Em python, qual das palavras é reservada para uma estrutura condicional? = ":
    ["if", 
    "while", 
    "def", 
    "input"],
    
    "Um tipo de memória cujo conteúdo é gravado pelo fabricante, podendo ser lido, mas não modificado é denominado = ":
    ["ROM",
    "RAM.",
    "SDRAM.",
    "DDR."],
   
    "A corrente alternada (AC) é caracterizada por = ":
    ["Elétrons que se movem em uma direção depois em outra, rapidamente.", 
    "Elétrons que se movem em uma única direção.",
    "Elétrons que se movem em direções diferentes e depois estabilizam.",
    "Elétrons que se movem em uma única direção e depois alternam."],
 
    "Quais dessas manutenções pode ser considerada uma manutenção preventiva? = ":
    ["Limpeza da parte interna e externa do computador", 
    "Remoção de vírus e malwares", 
    "Uso de placas de diagnóstico na placa mãe", 
    "Redimensionar partições para melhor organização"]


}
cont = 0
contTT= 0
print("\nVamos começar O QUIZ!!!")
print("As perguntas ficam abaixo das alternativas ")
print("E selecione de 0 à 3 para escolher as alterativas")
print("Cuidado para não se confudir com as respostas")
print("\n")
def cadastro():
    nome=str(input("E iremos testar o seu cconhecimento em algoritmos e manutenção de sistemas mas antes de começarmos, Qual é o seu nome? "))
    print("Seja vem-vindo(a) ",nome)
    return nome
asdfg= cadastro()

for i, x in QUESTAO.items():
    correta = x[0]
    sorteio = sorted(x)
    print("\n")
    for label, x in enumerate(sorteio):
        print(f'{cores["magenta"]} {label}). {x} {cores["limpa"]}')   
    Q_label=-1 
    rt=0 
    while Q_label not in [0,1,2,3]:
        Q_label = int(input(f'{i} '))
        if Q_label in [0,1,2,3]:
            qq = sorteio[Q_label]
            sleep(1)
            if (qq == correta):
                cont += 1
                print("Acertou")
                rt=0
                break
            elif(qq!= correta):
                print("Errou")
                print(f'Certa é {correta}')
                break
        print(f'{cores["vermelho"]}Alternaiva inexistente{cores["limpa"]}')
    
contTT=cont
r=0
print(f'\n{asdfg} tem até o momento acertou {cores["ciano"]} {cont} {cores["limpa"]}. ')
if(cont<3):
    print("E isso é mal, mas boa sorte, porque iremos aumentar o nível")
else:
    print("Você está indo bem, vamos para o próximo level")
while(r!=1):
    r=int(input('Está pronto? Digite 1 para prosseguir, e nesse nível se acerta ganha 2 ponto, mas perde 1 se errar '))
    os.system('cls') or None 
cont=0
for i, x in QUESTAO2.items():
    correta = x[0]
    sorteio = sorted(x)
    print("\n")
    for label, x in enumerate(sorteio):
        print(f'{cores["magenta"]} {label}). {x} {cores["limpa"]}')
    Q_label=-1 
while Q_label not in [0,1,2,3]:
    Q_label = int(input(f'{i} '))
    if Q_label in [0,1,2,3]:
        qq = sorteio[Q_label]
        sleep(1)
        if (qq == correta):
            cont += 2
            print("Acertou")
            break
             
        elif(qq!= correta):
            cont-=1
            print("Errou")
            print(f'Certa é {correta}')
            break
    print(f'{cores["vermelho"]}Alternaiva inexistente{cores["limpa"]}')

      
contTT+=cont

print(f'\n{asdfg} você tem {cores["ciano"]}{cont}{cores["limpa"]} acertos, e no total {cores["ciano"]}{contTT}{cores["limpa"]} acertos')
if(cont<4):
    print("\nNesse nivel foi meio ruim e no")
elif(cont>=4):
    print("\nNesse nível foi bom e no")
if(contTT<7):
    print(" geral, está errando muito, boa sorte na prox fase")
elif(contTT>=7):
    print(" geral está indo bem, vamos para o próximo level")
cont=0
r=0
while(r!=1):
    r=int(input('Está pronto? Digite 1 para prosseguir e nesse nível, se acertar ganha 3 pontos, mas perde 2 se errar '))
    os.system('cls') or None
      
for i, x in QUESTAO3.items():
    correta = x[0]
    sorteio = sorted(x)
    print("\n")
    for label, x in enumerate(sorteio):
        print(f'{cores["magenta"]} {label}). {x} {cores["limpa"]}')
    Q_label=-1  
    while Q_label not in [0,1,2,3]:
        Q_label = int(input(f'{i} '))
        if Q_label in [0,1,2,3]:
            qq = sorteio[Q_label]
            sleep(1)
            if (qq == correta):
                cont += 3
                print("Acertou")
                break
            elif(qq!= correta):
                print("Errou")
                print(f'Certa é {correta}')
                break
                cont-=2
    print(f'{cores["vermelho"]}Alternaiva inexistente{cores["limpa"]}')
     
contTT+=cont
print(f'\n{asdfg} você tem {cores["ciano"]}{cont}{cores["limpa"]} acertos, e no total {cores["ciano"]}{contTT}{cores["limpa"]} acertos')

if(cont<9):
   print("\nNesse nivel foi meio ruim e ")
elif(cont>=9):
   print("\nNesse nível foi bom e ")
if(contTT<15):
  print("  você falhou no quiz de Ian, que pena")
elif(contTT>=15):
  print("  você passou no quiz de Ian, parabéns")