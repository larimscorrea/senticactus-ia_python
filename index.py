import re

def load_words():
    file_path = 'words.txt'  # Caminho correto do arquivo
    dic_word_polarity = {}
    
    with open(file_path, 'r') as sentiwords:
        for line in sentiwords:
            pos_ponto = line.find('.')
            word = line[:pos_ponto]
            pol_pos = line.find('POL')
            polarity = line[pol_pos+7:pol_pos+9].replace(';', '')

            dic_word_polarity[word] = int(polarity)

    return dic_word_polarity

def analyze_sentiment():
    # Entrada do usuário
    comentario = input("Digite seu comentário: ")

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())

    sentilex = load_words()

    # Inicialização dos contadores
    count_positivo = 0
    count_negativo = 0
    count_neutro = 0

    # Contagem de polaridades baseadas no dicionário
    for palavra in palavras:
        if palavra in sentilex:
            polarity = sentilex[palavra]
            if polarity > 0:
                count_positivo += 1
            elif polarity < 0:
                count_negativo += 1
            else:
                count_neutro += 1

    # Verificação do sentimento
    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    elif count_positivo < count_negativo and count_neutro == 0:
        return "Negativo"
    else:
        return "Neutro ou Misturado"

# Saída esperada
sentimento = analyze_sentiment()
print("Sentimento:", sentimento)
