#!/usr/bin/python3
def ler_arquivo(nome: str) -> list:
    '''Função que retorna conteudo de um arquivo'''
    try:
        with open(nome, 'r') as arq:
            return arq.readlines()
    except Exception as e:
        return ['Erro: {}'.format(e)]

def escrever_arquivo(nome: str, conteudo: list) -> bool:
    try:
        with open(nome, 'a') as arq:
            conteudo = [x+'\n' for x in conteudo]
            arq.writelines(conteudo)
            return True
    except Exception:
            return False

def contar_linhas(nome: str) -> int:
        '''Função para contar linhas de um arquivo'''
        return len(ler_arquivo(nome))
nomes = ['daniel', 'pedro']
print(escrever_arquivo('texto.txt', nomes))
