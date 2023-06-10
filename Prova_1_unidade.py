from asyncio import events
from multiprocessing.sharedctypes import Value
import PySimpleGUI as sg

funcionarios = {"Ana": {"senha": "1112", "endereço": "Rua Salvador, 99 - Centro", "Telefone": "73911111111","Salário": "1200", "Função":"Docier"},
"Pedro": {"senha": "1122", "endereço": "Rua Salvador, 100 - Centro", "Telefone": "73911111112","Salário": "1200", "Função":"Padeiro"},
"Asafe": {"senha": "1222", "endereço": "Rua Salvador, 101 - Centro", "Telefone": "73911111122","Salário": "1300", "Função":"Caixa"}}

layout = [
    [sg.Text('')],
    [sg.Text('Boas-Vindas à Padaria Pão Bom', justification='center')],
    [sg.Column([
    [sg.Button('Login', size=(20,1))], 
    [sg.Button('Cadastrar', size=(20,1))],
    [sg.Button('Fechar', size=(20,1))],], justification='center')],
    [sg.Text('')],
]
window = sg.Window('Tela Principal', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =='Fechar':
        break
    if event == 'Login':
        nome = sg.popup_get_text('Digite o seu usuário')
        if nome in funcionarios:
            password = sg.popup_get_text('Digite a sua senha')
            if password in funcionarios[nome]['senha']:
                sg.popup(f'Sucesso no Login! \n \n Bom Trabalho {nome}')
                layout_prin = [
                    [sg.Text('')],
                    [sg.Text('MENU DE OPÇÕES', justification='center')],
                    [sg.Column([
                    [sg.Button('OK', size=(20,1))],
                    [sg.Button('Cancelar', size=(20,1))],], justification='center')],
                ]
                prin_window = sg.Window('Tela Principal', layout_prin)
                while True:
                    event, values = prin_window.read()
                    if event == sg.WIN_CLOSED or event =='Cancelar':
                        break
                    if event == 'OK':
                        layout = [
                            [sg.Button('Realizar Compras')],
                            [sg.Button('Atualizar Dados')],
                            [sg.Button('Gerenciar folhas de pagamento')]
                        ]
                        window1 = sg.Window('Tela Principal', layout)


                        while True:
                            event, values = window1.read()
                            if event == sg.WIN_CLOSED or event =='Cancelar':
                                break
            
            else: 
                sg.popup_error('Senha errada')
        else:
            sg.popup_error('Usuario não encontrado')
    if event == 'Cadastrar':
        valores = []
        campos = ["nome", "senha", "endereço", "Telefone", "Salário", "Função"]
        for i in range(6):
            preenchimento = sg.popup_get_text(f'{campos[i]} da nova pessoa', title='Novo Funcionario')
            if preenchimento != None:
                valores.append(preenchimento)
            else:
                break
        if len(valores) == 6:
            funcionarios[valores[0]] = {"senha": valores[1], "endereço": valores[2], "Telefone":valores[3], "Salário": valores[4], "Função": valores[5]}
            confirmacao = sg.popup_ok_cancel(f'{valores[0]}, seu nome foi adicionado com sucesso!')
            if confirmacao == 'cancel':
                pass