''' Manipulação de Texto em Python
    Funções importante para manipulação de texto:
        # Analise:
            - len(frase): retorna o tamanho de frase.
            
            - frase.count(char/string): retorna quantas vezes ele encontrou o char ou string
            colocado como parametro. Também pode ser da forma (char/string, inicio, fim),
            para procurar o char ou string em certos limites da frase.
            
            - frase.find(char/string): procura dentro de frase o char ou string colocado como
            parametro, e retorna a posição do primeiro char dentro de frase, caso não encontre
            ele retorna -1.
            
            - string/char in frase: analisa se existe uma palavra ou letra dentro de frase
            caso exista, retorna True, caso contrario, retorna False

        # Transformação:
            - frase.replace(str1, str2): busca dentro de frase a str1, e quando encontra 
            substitui pela str2, assim até o final de frase, NÃO ALTERANDO A FRASE EM SI.

            - frase.upper(): coloca todas as letras de frase em maiusculas, alterando a 
            frase em si.

            - frase.lower(): coloca todas as letras de frase em minusculas, alterando a 
            frase em si.

            - frase.capitalize(): coloca somente a primeira letra em maiuscula, deixando 
            todo o resto em minuscula.

            - frase.title(): coloca todas as palavras de frase com o primeiro char maiusculo

            - frase.strip(): retira todos os espaços excedentes tanto a direita quanto a 
            esquerda, também pode-se usar rstrip e lstrip, para retirar somente os espaços,
            a direita ou a esquerda, respectivamente.

        #Divisão:
            - frase.spli(): separa todos as palavras de frase por espaços, mas esse parametro
            pode ser alterado.

        #Junção:
            - string/char.join(frase): pega a lista frase, e junta todos os elementos da lista
            de usando a string ou o char colocado no inicio do comando
'''

