def analisador_lexical(teste):
    lista_tokens = []
    
    with open(teste, 'r') as arquivo:
        caractere = arquivo.read(1)  # Lê o próximo caractere do arquivo
        while caractere:
            while (caractere == "{" or caractere == " ") and not caractere.isspace():
                if caractere == "{":
                    temp_token = "{"
                    caractere = arquivo.read(1)
                    while caractere != "}" and caractere:
                        temp_token += caractere
                        caractere = arquivo.read(1)
                    temp_token += "}"
                    lista_tokens.append(("TipoToken", temp_token))  # Insere na lista de tokens
                while caractere.isspace() and not caractere.isspace():
                    caractere = arquivo.read(1)
            
            if not caractere.isspace() and caractere != "":
                temp_token = caractere
                # Aqui você precisaria implementar a lógica para pegar o token completo
                lista_tokens.append(("TipoToken", temp_token))  # Insere na lista de tokens
            
            caractere = arquivo.read(1)
    
    return lista_tokens

if __name__ == "__main__":
    nome_arquivo = "teste.txt"  # Substitua pelo nome do seu arquivo de entrada
    lista_de_tokens = analisador_lexical(nome_arquivo)
    for token in lista_de_tokens:
        print(token)
