import re

def trata_comentario_e_consome_espacos(line):
    # Remove comentários e espaços em branco da linha
    line = re.sub(r'\/\/.*', '', line)  # Remove comentários de linha
    line = re.sub(r'\s+', ' ', line)    # Substitui múltiplos espaços por um único espaço
    return line.strip()

def pega_token(token):
    # Implemente a lógica para identificar tokens aqui
    # Neste exemplo, consideramos que um token é uma palavra separada por espaços
    return token

def analisador_lexical(calculadora):
    tokens = []
    
    with open(calculadora, 'r') as arquivo:
        for linha in arquivo:
            linha = trata_comentario_e_consome_espacos(linha)
            if linha:
                palavras = linha.split(' ')
                for palavra in palavras:
                    token = pega_token(palavra)
                    tokens.append(token)
    
    return tokens

if __name__ == "__main__":
    nome_arquivo = "seuarquivo.txt"  # Substitua pelo nome do seu arquivo de entrada
    lista_de_tokens = analisador_lexical(nome_arquivo)
    print(lista_de_tokens)
