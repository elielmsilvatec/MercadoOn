import PySimpleGUI as sg

# Definir email e senha corretos
email_correto = 'eliel@email.com'
senha_correta = '123'

# Layout da janela
layout = [
    [sg.Text('MercadoON', key='-TEXTO-', font=('Helvetica', 50), justification='center', pad=((0, 0), (50, 20)))],
    [sg.Text('Email:'), sg.Input(key='-EMAIL-', size=(30, 1))],
    [sg.Text('Senha:'), sg.Input(key='-SENHA-', password_char='*', size=(30, 1))],
    [sg.Button('Login')]
]

# Configurar a aparência da janela
sg.theme('DarkBlue3')  # Define o tema da janela
sg.set_options(font=('Helvetica', 14))  # Define a fonte global

# Criar janela
janela = sg.Window('Tela de Login', layout, finalize=True)

# Loop de eventos
while True:
    evento, valores = janela.read()

    # Fechar a janela se o usuário clicar no 'X' de fechar
    if evento == sg.WINDOW_CLOSED:
        break

    # Verificar se o email e a senha estão corretos
    if evento == 'Login':
        email = valores['-EMAIL-']
        senha = valores['-SENHA-']

        if email == email_correto and senha == senha_correta:
            sg.popup('Logado')
        else:
            sg.popup('Usuário ou senha incorreto')

# Fechar a janela ao finalizar
janela.close()
