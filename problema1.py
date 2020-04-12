
# in cadrul acestei abordari se considera pozitiile [end:start] ale frazei initiale
def problema_1(phrase, changes):
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

phrase="Lorem Ipsum este pur si simplu o macheta pentru text a industriei tipografice. "
changes=[[17,20,"cu siguranta"],
         [33,40,"emblema"],
         [66,77,"informatice"]
         ]
#modificare fraza
final=problema_1(phrase,changes)
print(final)


#eliminarea sectiunii "si simplu"
print(final.find("si simplu"))
final_phrase=final[:final.find("si simplu ")] + final[final.find("si simplu ")+len("si simplu "):]
print(final_phrase)

