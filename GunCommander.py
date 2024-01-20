import random
import string

def gerar_senha(tamanho=12):
                                    
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def gerar_nome():
    nomes = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hank']
    sobrenomes = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson']
       
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    
    return f'{nome} {sobrenome}'





print('''\033[1;36;40m    ###                 ##            #####     ###                         ##       ###
  ##  ##                ##            ##  ##     ##                        ##      ##  ##
 ##         ####    ######    ####   ##  ##     ##       #####    ##### #######   ##       ##   ##  ## ###
##        ##   ##  ##  ##   ##   ##  #####      ##     ##   ##   ##       ##     ##        ##   ##  ###  ##
##       ##    ## ##   ##  ########  ##  ##    ##     ##    ##    ##     ##      ## ####  ##   ##   ##   ##
##  ##   ##   ##  ##  ##   ##       ##  ##     ##     ##  ###      ##    ##      ##  ##   ##  ###  ##   ##
 ###      ####     #####    ####    #####     ####     ### ##  #####      ###     ####     ### ##  ##   ##''')
print('')
print('''\033[1;31;40m
1-gerar_senhas
2-gerar_Nomes''')
print('')

var1 = int(input('>'))

if var1 == 1:
    senha = gerar_senha()
    print(senha)

if var1 == 2:
    nome = gerar_nome()
    print(nome)