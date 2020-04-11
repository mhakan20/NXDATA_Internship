
# in cadrul acestei abordari se considera pozitiile [end:start] ale frazei initiale
def problema_1_1(phrase, changes):
    """

    :param fraza initiala
    :param schimbarile dorite
    :return: fraza finala

    Rolul functiei este de a modifica o fraza in functie de cuvintele dorite.
    Se selecteaza portiunile date ca parametru si ulterior se modifica cu cuvintele dorite.
    """
    words_to_change=[]
    for i, val in enumerate(changes):
        start=val[0]
        end=val[1]
        words_to_change.append(phrase[start:end])
    print(words_to_change)
    for i, word in enumerate(words_to_change):
        phrase=phrase.replace(word,changes[i][2])
    return phrase

#in aceasta abordare se considera ca pozitiile [start:end] sunt dinamice
#dinamicitatea consta in faptul ca reprezinta pozitiile cuvintelor in fraza ce a primit deja modificarile anterioare
def problema_1_2(phrase,changes):
    for val in changes:
        phrase="".join((phrase[:val[0]],val[2],phrase[val[1]:]))
    return phrase

phrase="Lorem Ipsum este pur si simplu o macheta pentru text a industriei tipografice. "
changes=[[17,20,"cu siguranta"],
         [34,40,"emblema"],
         [63,77,"informatice"]
         ]

final=problema_1_1(phrase,changes)
print(final)
final2=problema_1_2(phrase,changes)
print(final2)
