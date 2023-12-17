# alfabeto_especial = ['a', 'á', 'à', 'â', 'ã', 'ä', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f', 'g', 'h', 'i', 'í', 'ì', 'î', 'ï', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ò', 'ô', 'õ', 'ö', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù', 'û', 'ü', 'v', 'w', 'x', 'y', 'ý', 'ÿ', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', ',', '.', ';', ':', '?', '/', '<', '>', '[', ']', '{', '}', '|', '"', "'", '`', '^', '~']
logo = '''
oooooooooooo           oooo                       oooooo     oooo                       oooo      .   
`888'     `8           `888                        `888.     .8'                        `888    .o8   
 888          .ooooo.   888 .oo.    .ooooo.         `888.   .8'    .oooo.   oooo  oooo   888  .o888oo 
 888oooo8    d88' `"Y8  888P"Y88b  d88' `88b         `888. .8'    `P  )88b  `888  `888   888    888   
 888    "    888        888   888  888   888          `888.8'      .oP"888   888   888   888    888   
 888       o 888   .o8  888   888  888   888           `888'      d8(  888   888   888   888    888 . 
o888ooooood8 `Y8bod8P' o888o o888o `Y8bod8P'            `8'       `Y888""8o  `V88V"V8P' o888o   "888" 
                                                                                                                                                
'''

alfabeto_especial = ['>', ';', 'm', '(', 'f', '*', 'o', ':', '{', '$', 'û', 'w', 'b', 'á', 'ã', '`', '.', ',', 'c', '6', 'j', 'õ', 'ò', 's', 'ù', 'ç', 'î', '#', '8', 'è', '}', '4', '2', 'k', 'ó', '5', '7', '"', '0', 'n', "'", '~', '@', 'y', 't', 'ô', 'ö', '<', '!', '?', 'i', 'g', 'í', ']', 'à', 'ä', 'h', '9', 'l', 'ë', '/', ')', 'a', '-', '1', 'ÿ', '+', 'p', 'e', 'â', 'ê', 'z', 'ú', '_', '|', '&', 'ï', '3', 'ì', 'd', 'v', '%', 'ü', '[', '=', '^', 'é', 'q', 'ý', 'r', 'x', ' ', 'u']

tamanho_alfabeto = len(alfabeto_especial)

def caesar_cypher(direcao, texto, deslocamento):
    mensagem = ""
    if direcao == "decodificar":
        deslocamento *= -1
    for caractere in texto:
        if caractere in alfabeto_especial:
            nova_posicao = alfabeto_especial.index(caractere) + deslocamento
            if nova_posicao > tamanho_alfabeto or nova_posicao < 0:
                nova_posicao = nova_posicao % tamanho_alfabeto
            mensagem += alfabeto_especial[nova_posicao]
        else:
            mensagem += caractere
              
    print(f"Mensagem: {mensagem}")
    
print(f"\033[36m{logo}\033[0m")


terminar = False
while not terminar:
    direcao = ""
    while direcao not in ["codificar", "decodificar"]:
        direcao = input("Digite 'codificar' para criptografar, digite 'decodificar' para descriptografar:\n").lower()
        if direcao not in ["codificar", "decodificar"]:
            print("Opção inválida")
    texto = input("Digite sua mensagem:\n").lower()
    deslocamento = int(input("Digite o número de deslocamento:\n"))

    caesar_cypher(direcao, texto, deslocamento)
        
    continuar = input("Deseja continuar? 'sim' ou 'nao': ").lower()
    if continuar == "nao":
        terminar = True
