import requests, os
vermelho = '\033[41m'
verde = '\033[42m'
nulo = '\033[0m'
verde1 = '\033[32m'
vermelho1 = '\033[31m'
azul = '\033[0;30;34m'
rosa = '\033[0;30;35m'
amarelo = '\033[33m'

print(f'''                           ▄───▄
██████╗░██╗██████╗░██████╗░█▀█▀█
██╔══██╗██║██╔══██╗██╔══██╗█▄█▄█
{azul}██║░░██║██║██████╔╝██████╦╝─███──▄▄
██║░░██║██║██╔══██╗██╔══██╗─████▐█─█
{vermelho1}██████╔╝██║██║░░██║██████╦╝─████───█
╚═════╝░╚═╝╚═╝░░╚═╝╚═════╝░─▀▀▀▀▀▀▀{nulo}
by: SL{azul}AY{vermelho1}ER{nulo}''')
alvo = input('Site: ')

with open ('DBwordlist.txt', 'r') as file:
    wordlist = file.readlines()

    for word in wordlist:
        url_final = f'{alvo}/{word.strip()}'
        req = requests.get(url_final)
        code = req.status_code
        if code == 200:
            print(f'{verde1}•{nulo} {code} {url_final}')
        elif code == 404:
            print(f'{vermelho1}•{nulo} {code} {url_final}')