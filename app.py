import os
from datetime import datetime

def responder_ao_utente(texto: str) -> str:
    comando: str = texto.lower()

    # Linhas 7 a 22 comentadas conforme pedido
    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #     return 'Olá tudo bem!'
    # if comando == 'como estás':
    #     return 'Estou bem, obrigado!'
    # if comando == 'como te chamas?':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # Linhas 24 a 37 descomentadas
    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        'horas': f'São: {datetime.now():%H:%M} horas',
        'data': f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        # Novas interações:
        'qual é a tua cor favorita?': 'Gosto do verde.',
        'qual é o teu desporto preferido?': 'Gosto muito de futebol.',
        'qual é a capital de portugal?': 'Lisboa .',
        'quem és?': 'Sou um assistente virtual criado para conversar contigo.',
        'o que fazes?': 'Respondo às tuas perguntas simples.',
        'qual é o teu animal favorito?': 'Adoro gatos, são muito curiosos.',
        'ajuda-me': 'Claro, pergunta o que quiseres.',
        'qual é o teu filme favorito?': 'Gosto de filmes de terror.',
        'qual é a tua música favorita?': ' jazz.',
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'

def iniciar_chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    nome_utilizador: str = input('Assistente: Como te chamas? ')
    print(f'Assistente: Olá, {nome_utilizador}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta = responder_ao_utente(user_input)
        print(f'Assistente: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('\nVolte sempre!\n')

if __name__ == "__main__":
    iniciar_chat()
