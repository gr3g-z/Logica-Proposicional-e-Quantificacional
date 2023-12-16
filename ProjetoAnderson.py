from nltk.sem import Expression
from nltk.test.setup_fixt import check_binary
from nltk import *
from nltk.sem.drt import DrtParser
from nltk.sem import logic
logic._counter._value = 0
import re
import spacy


Base_de_crenças = {}
read_expr = Expression.fromstring
# Carregar o modelo de linguagem do spaCy para português
nlp = spacy.load("pt_core_news_sm")

def lematizar_palavra(palavra):
    # Função para lematizar uma palavra usando spaCy
    doc = nlp(palavra)
    return doc[0].lemma_

def converter_para_minusculas(frase):
    return frase.lower()

def corresponder_frase(frase):
    frase = converter_para_minusculas(frase)
    # Definindo o padrão para "S é P" e "S não é P"
    padrao_eh = re.compile(r'(\w+) é (\w+)')
    padrao_nao_eh = re.compile(r'(\w+) não é (\w+)')
    padrao_todo_eh = re.compile(r'todo (\w+) é (\w+)')
    padrao_todos_sao = re.compile(r'todos os (\w+) são (\w+)')
    padrao_todos_sao2 = re.compile(r'todos (\w+) são (\w+)')
    padrao_todo_nao_eh = re.compile(r'todo (\w+) não é (\w+)')
    padrao_todos_nao_sao = re.compile(r'todos os (\w+) não são (\w+)')
    padrao_algum_eh = re.compile(r'algum (\w+) é (\w+)')
    padrao_algum_nao_eh = re.compile(r'algum (\w+) não é (\w+)')
    padrao_nenhum_eh = re.compile(r'nenhum (\w+) é (\w+)')
    padrao_nenhum_nao_eh = re.compile(r'nenhum (\w+) não é (\w+)')
    padrao_toda_eh = re.compile(r'toda (\w+) é (\w+)')
    padrao_todas_sao = re.compile(r'todas as (\w+) são (\w+)')
    padrao_todas_sao2 = re.compile(r'todas (\w+) são (\w+)')
    padrao_toda_nao_eh = re.compile(r'toda (\w+) não é (\w+)')
    padrao_todas_nao_sao = re.compile(r'todas as (\w+) não são (\w+)')
    padrao_alguma_eh = re.compile(r'alguma (\w+) é (\w+)')
    padrao_alguma_nao_eh = re.compile(r'alguma (\w+) não é (\w+)')
    padrao_nenhuma_eh = re.compile(r'nenhuma (\w+) é (\w+)')
    padrao_nenhuma_nao_eh = re.compile(r'nenhuma (\w+) não é (\w+)')

    # Verificando se a frase corresponde ao padrão "Toda S é P"
    correspondencia_toda_eh = padrao_toda_eh.match(frase)
    if correspondencia_toda_eh:
        sujeito, propriedade = correspondencia_toda_eh.groups()
        return f"all x.({lematizar_palavra(sujeito)}(x) -> {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Todas as S são P"
    correspondencia_todas_sao = padrao_todas_sao.match(frase)
    if correspondencia_todas_sao:
        sujeito, propriedade = correspondencia_todas_sao.groups()
        return f"all x.({lematizar_palavra(sujeito)}(x) -> {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Todas S são P"
    correspondencia_todas_sao2 = padrao_todas_sao2.match(frase)
    if correspondencia_todas_sao2:
        sujeito, propriedade = correspondencia_todas_sao2.groups()
        return f"all x.({lematizar_palavra(sujeito)}(x) -> {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Toda S não é P"
    correspondencia_toda_nao_eh = padrao_toda_nao_eh.match(frase)
    if correspondencia_toda_nao_eh:
        sujeito, propriedade = correspondencia_toda_nao_eh.groups()
        return f"-exists x.({lematizar_palavra(sujeito)}(x) & {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Todas as S não são P"
    correspondencia_todas_nao_sao = padrao_todas_nao_sao.match(frase)
    if correspondencia_todas_nao_sao:
        sujeito, propriedade = correspondencia_todas_nao_sao.groups()
        return f"-exists x.({lematizar_palavra(sujeito)}s(x) & {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Alguma S é P"
    correspondencia_alguma_eh = padrao_alguma_eh.match(frase)
    if correspondencia_alguma_eh:
        sujeito, propriedade = correspondencia_alguma_eh.groups()
        return f"exists x.({lematizar_palavra(sujeito)}(x) & {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Alguma S não é P"
    correspondencia_alguma_nao_eh = padrao_alguma_nao_eh.match(frase)
    if correspondencia_alguma_nao_eh:
        sujeito, propriedade = correspondencia_alguma_nao_eh.groups()
        return f"exists x.({lematizar_palavra(sujeito)}(x) & -{lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Nenhuma S é P"
    correspondencia_nenhuma_eh = padrao_nenhuma_eh.match(frase)
    if correspondencia_nenhuma_eh:
        sujeito, propriedade = correspondencia_nenhuma_eh.groups()
        return f"-exists x.({lematizar_palavra(sujeito)}(x) & {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Nenhuma S não é P"
    correspondencia_nenhuma_nao_eh = padrao_nenhuma_nao_eh.match(frase)
    if correspondencia_nenhuma_nao_eh:
        sujeito, propriedade = correspondencia_nenhuma_nao_eh.groups()
        return f"-exists x.({lematizar_palavra(sujeito)}(x) & -{lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "S é P"
    correspondencia_eh = padrao_eh.match(frase)
    if correspondencia_eh:
        sujeito, propriedade = correspondencia_eh.groups()
        return f"{lematizar_palavra(propriedade)}({lematizar_palavra(sujeito)})"

    # Verificando se a frase corresponde ao padrão "S não é P"
    correspondencia_nao_eh = padrao_nao_eh.match(frase)
    if correspondencia_nao_eh:
        sujeito, propriedade = correspondencia_nao_eh.groups()
        return f"-{lematizar_palavra(propriedade)}({lematizar_palavra(sujeito)})"

    # Verificando se a frase corresponde ao padrão "Todo S é P"
    correspondencia_todo_eh = padrao_todo_eh.match(frase)
    if correspondencia_todo_eh:
        sujeito, propriedade = correspondencia_todo_eh.groups()
        return f"all x.({lematizar_palavra(sujeito)}(x) -> {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Todos os S são Ps"
    correspondencia_todos_sao = padrao_todos_sao2.match(frase)
    if correspondencia_todos_sao:
        sujeito, propriedade = correspondencia_todos_sao.groups()
        return f"all x.({lematizar_palavra(sujeito)}(x) -> {lematizar_palavra(propriedade)}(x))"
    
    # Verificando se a frase corresponde ao padrão "Todos S são Ps"
    correspondencia_todos_sao2 = padrao_todos_sao.match(frase)
    if correspondencia_todos_sao2:
        sujeito, propriedade = correspondencia_todos_sao2.groups()
        return f"all x.({lematizar_palavra(sujeito)}(x) -> {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Todo S não é P"
    correspondencia_todo_nao_eh = padrao_todo_nao_eh.match(frase)
    if correspondencia_todo_nao_eh:
        sujeito, propriedade = correspondencia_todo_nao_eh.groups()
        return f"-exists x.({lematizar_palavra(sujeito)}(x) & {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Todos os S não são Ps"
    correspondencia_todos_nao_sao = padrao_todos_nao_sao.match(frase)
    if correspondencia_todos_nao_sao:
        sujeito, propriedade = correspondencia_todos_nao_sao.groups()
        return f"-exists x.({lematizar_palavra(sujeito)}s(x) & {lematizar_palavra(propriedade)}s(x))"

    # Verificando se a frase corresponde ao padrão "Algum S é P"
    correspondencia_algum_eh = padrao_algum_eh.match(frase)
    if correspondencia_algum_eh:
        sujeito, propriedade = correspondencia_algum_eh.groups()
        return f"exists x.({lematizar_palavra(sujeito)}(x) & {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Algum S não é P"
    correspondencia_algum_nao_eh = padrao_algum_nao_eh.match(frase)
    if correspondencia_algum_nao_eh:
        sujeito, propriedade = correspondencia_algum_nao_eh.groups()
        return f"exists x.({lematizar_palavra(sujeito)}(x) & -{lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Nenhum S é P"
    correspondencia_nenhum_eh = padrao_nenhum_eh.match(frase)
    if correspondencia_nenhum_eh:
        sujeito, propriedade = correspondencia_nenhum_eh.groups()
        return f"-exists x.({lematizar_palavra(sujeito)}(x) & {lematizar_palavra(propriedade)}(x))"

    # Verificando se a frase corresponde ao padrão "Nenhum S não é P"
    correspondencia_nenhum_nao_eh = padrao_nenhum_nao_eh.match(frase)
    if correspondencia_nenhum_nao_eh:
        sujeito, propriedade = correspondencia_nenhum_nao_eh.groups()
        return f"-exists x.({lematizar_palavra(sujeito)}(x) & -{lematizar_palavra(propriedade)}(x))"

    # Se a frase não corresponder a nenhum padrão conhecido
    return "Padrão não reconhecido."

def Criar_base_de_crenca(chave, base = Base_de_crenças):
    base[chave] = []
    return base

def Obter_strings_da_chave(chave, base=Base_de_crenças):
    if chave in base:
        lista_strings = base[chave]
        return lista_strings
    else:
        print(f"A chave '{chave}' não existe no dicionário.")
        return None
    
def Validação_informacional_crença(chave, base= Base_de_crenças):
    lista_crenças = Obter_strings_da_chave(chave, base) #Equivalente ao [p1,p2,p3...pn]
    nova_crença = input('Adicioniar crença: ') #Equivalente ao C
    nova_crença_ = corresponder_frase(nova_crença)
    nova_crença_ = read_expr(nova_crença_)
    lista_nltk = []
    expressões_lidas = []
    if lista_crenças == None:
       print('Base de crenças vazia')
    else:
       for i in range (len(lista_crenças)):
         crença = lista_crenças[i]
         crença_nltk = corresponder_frase(crença)
         lista_nltk.append(crença_nltk)
       for valor in lista_nltk:
         variavel = read_expr(valor)
         expressões_lidas.append(variavel)

    if TableauProver().prove(nova_crença_, []) == True:
       string= 'Sua crença não será adicionada na base por ser uma Tautologia'
       return string
    if TableauProver().prove(-nova_crença_, []) == True:
       string= 'Sua crença não será adicionada na base por ser uma Contradição'
       return string
    if TableauProver().prove(nova_crença_, expressões_lidas) == True:
       string= 'Sua crença não será adicionada na base por ser redundante e não trazer valor informacional'
       return string
    if TableauProver().prove(-nova_crença_, expressões_lidas) == True:
       resultados_false = []

       for i in range(len(expressões_lidas)):
            lista_temp = expressões_lidas.copy()
            p_atual = lista_temp.pop(i)
            resultado = TableauProver().prove(-nova_crença_, lista_temp)
            if resultado == False:
                resultados_false.append((lista_crenças[i]))
       print("Crenças que contradizem com nova crença:", resultados_false)
       lista_final= substituir_variavel(resultados_false, nova_crença)

       for t in range(len(resultados_false)):
            a = base[chave]
            a.remove(resultados_false[t])

       for s in range(len(lista_final)):
            base[chave].append(lista_final[s])

       print("Lista final após substituições:", lista_final)
       return base

    else:
       base[chave].append(nova_crença)
       string= 'Sua crença foi adicionada a base de crenças'
       return string, base
    

def substituir_variavel(variaveis, substituicao):
    # Função para substituir um elemento escolhido pelo usuário na lista
    # Você pode personalizar essa função conforme necessário

    # Se substituicao for uma string, permitir que o usuário escolha
    if isinstance(substituicao, str):
        a= print(f"Escolha uma variável para '{substituicao}' substituir: {variaveis}")
        escolha = input("digite o número correspondente: ")
        try:
            escolha = int(escolha)
            if escolha < 1 or escolha > len(variaveis):
                raise ValueError("Índice fora do intervalo.")
        except ValueError:
            print("Escolha inválida.")
            return variaveis
    # Se substituicao for um número, usar diretamente
    elif isinstance(substituicao, int):
        escolha = substituicao
    else:
        print("Tipo de substituicao não suportado.")
        return variaveis

    # Criar uma nova lista para evitar modificar a original
    nova_variaveis = variaveis.copy()

    # Realizar a substituição na nova lista
    nova_variaveis[escolha - 1] = substituicao
    return nova_variaveis
