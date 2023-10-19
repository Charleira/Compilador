import pickle

# Variáveis globais
linha = ''
posicao = 0
caractere = ''
tabela_tokens = []

class Token:
    def __init__(self):
        self.lexema = ''
        self.simbolo = ''

    def map_reserved(self, lexema):
        reserved_mapping = {
            "programa": "sprograma",
            "início": "sinício",
            "fim": "sfim",
            "procedimento": "sprocedimento",
            "funcao": "sfuncao",
            "se": "sse",
            "entao": "sentao",
            "senao": "ssenao",
            "enquanto": "senquanto",
            "faca": "sfaca",
            "escreva": "sescreva",
            "leia": "sleia",
            "var": "svar",
            "inteiro": "sinteiro",
            "booleano": "sbooleano",
            "verdadeiro": "sverdadeiro",
            "falso": "sfalso",
            "div": "sdiv",
            "e": "se",
            "ou": "sou",
            "nao": "snao"
        }

        self.simbolo = reserved_mapping.get(lexema, 'sidentificador')

def ler_caractere():
    global caractere, posicao, linha
    if posicao < len(linha):
        caractere = linha[posicao]
        posicao += 1
    else:
        caractere = ''  # Fim da linha

def trata_atribuicao():
    global caractere, token
    token.lexema = caractere
    ler_caractere()
    if caractere == "=":
        token.lexema += caractere
        token.simbolo = 'satribuicao'
        ler_caractere()
    else:
        token.simbolo = 'sdoispontos'

def trata_operador_aritmetico():
    global caractere, token
    token.lexema = caractere
    if caractere == "+":
        token.simbolo = 'sadicao'
    elif caractere == "-":
        token.simbolo = 'ssubtracao'
    elif caractere == "*":
        token.simbolo = 'smultiplicacao'
    ler_caractere()

def trata_operador_relacional():
    global caractere, token
    token.lexema = caractere
    if caractere == "!":
        ler_caractere()
        if caractere == "=":
            token.lexema += caractere
            token.simbolo = 'sdif'
            ler_caractere()
        else:
            token.simbolo = 'snao'
    elif caractere in {"<", ">"}:
        if caractere == "<":
            token.simbolo = 'smenor'
        elif caractere == ">":
            token.simbolo = 'smaior'
        ler_caractere()
        if caractere == "=":
            token.lexema += caractere
            if token.simbolo == 'smenor':
                token.simbolo = 'smenorig'
            elif token.simbolo == 'smaior':
                token.simbolo = 'smaiorig'
            ler_caractere()

def trata_pontuacao():
    global caractere, token
    token.lexema = caractere
    if caractere == ";":
        token.simbolo = 'sponto_virgula'
    elif caractere == ",":
        token.simbolo = 'svirgula'
    elif caractere == "(":
        token.simbolo = 'sabre_parenteses'
    elif caractere == ")":
        token.simbolo = 'sfecha_parenteses'
    elif caractere == ".":
        token.simbolo = 'sponto'
    ler_caractere()

def trata_identificador_palavra_reservada():
    global caractere, token
    id_ = caractere  # Alterei o nome da variável para evitar conflito com a função id() do Python.
    ler_caractere()
    while caractere.isalpha() or caractere.isdigit() or caractere == "_":
        id_ += caractere
        ler_caractere()
    token.lexema = id_
    token.map_reserved(id_)  # Use map_reserved to map reserved words to symbols

def trata_digito():
    global caractere, token
    num = caractere
    ler_caractere()
    while caractere.isdigit():
        num += caractere
        ler_caractere()
    token.lexema = num
    token.simbolo = 'snumero'

def pega_token():
    global tabela_tokens, caractere, token
    token = Token()  # Inicializar o token corretamente
    ler_caractere()  # Adicionei essa linha para garantir que a leitura comece corretamente no início

    if caractere.isdigit():
        trata_digito()
    elif caractere.isalpha():
        trata_identificador_palavra_reservada()
    elif caractere == ":":
        trata_atribuicao()
    elif caractere in {"+", "-", "*"}:
        trata_operador_aritmetico()
    elif caractere in {"!", "<", ">", "="}:
        trata_operador_relacional()
    elif caractere in {";", ",", "(", ")", "."}:
        trata_pontuacao()

    tabela_tokens.append(token)


with open('teste_10.txt', 'r') as f:
    for linha in f:
        # Processar cada linha do arquivo
        posicao = 0
        while posicao < len(linha):
            pega_token()

    # Salvar a tabela de tokens em um arquivo
with open('tabela_tokens.txt', 'w') as f:
    for token in tabela_tokens:
        f.write(f"Lexema: {token.lexema}, Símbolo: {token.simbolo}\n")