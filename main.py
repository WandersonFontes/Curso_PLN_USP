import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist

# corpus = nltk.corpus.mac_morpho
# print("-"*10 + "Treinamento PLN" + "-"*10+"\n")

# Retornar palavras
# print(f"Valores - {corpus.words()}")

# Retornar palavras com tag's
# print(f"Palavras com Tag - {corpus.tagged_words()}")


# Retornar sentenças
# print(f"Sentença - {corpus.sents()}")

# Tokenização
# print(f"Tokens: {corpus.word_tokenize()}")

# Retornar palavras com tag's
# print(f"Senteças com Tag - {nltk.tagged_sents()}")

# Tokenização
f = open("ipsum.txt", "r")
txt = f.read()

tokens = nltk.word_tokenize(txt)
print(f'Tokens texto ou frase por completo: {tokens}')

# Regex para pegar apenas as palavras sem a pontuação nem números.
pattern = RegexpTokenizer(r'[a-zA-Z]\w+')

stopwords = nltk.corpus.stopwords.words("portuguese")
print(f'Stop Words: {stopwords}')

# Compreensão para colocar o token em caixa baixa e remover stopwords (a,e,i,o,u,ai,ei,eu,oi,ui...)
tokensPatternLower = [i.lower() for i in pattern.tokenize(txt) if i not in stopwords]
print(f'Tokens sem pontução, usando o padrão REGEX: \n{tokensPatternLower}')

# Contador de frenquência de tokens
frenquecia = FreqDist(tokensPatternLower)
print(frenquecia.most_common())

# Dez tokens mais frequente
dezTokens = frenquecia.most_common(10)





