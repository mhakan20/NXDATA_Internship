NUME_LUNI={1:'ianuarie',2:"februarie",3:"martie",4:"aprilie",5:"mai",6:"iunie",7:"iulie",8:"august",
      9:'septembrie',10:'octombrie',11:'noiembrie',12:"decembrie"}
#pentru usurinta nu am definit toate judetele
NUME_JUDETE={1:'Alba',2:'Iasi',3:"Maramures",4:"Bucuresti"}
VALIDATE_CODE=[2,7,9,1,4,6,3,5,8,2,7,9]


def validator(entry_CNP):
    CNP=[int(x) for x in str(entry_CNP)]
    person={'sex':'','an_nasterii':0,'luna_nasterii':'','ziua_nasterii':0,'judet':'','NNN':0}
    an1=0
    an2=0
    luna=0
    zi=0
    judet=0
    #aflare sex
    if CNP[0] % 2 == 0:
        person["sex"]='F'
    else:
        person["sex"]='M'

    #aflare an nastere
    if CNP[0] < 3:
        an1 = 19
    elif CNP[0] < 5:
        an1 = 18
    elif CNP[0] < 7:
        an1 = 20
    else:
        an1 = 19
    an2=CNP[1] * 10 + CNP[2]
    person['an_nasterii']=an1 * 100 + an2

    #aflare luna nastere
    luna = CNP[3] * 10 + CNP[4]
    person["luna_nasterii"]=NUME_LUNI[luna]

    #aflare zi nastere
    zi=CNP[5] * 10 + CNP[6]
    person['ziua_nasterii']=zi

    #aflare nume judet
    judet=CNP[7] * 10 + CNP[8]
    person['judet']=NUME_JUDETE[judet]

    #aflare NNN
    nnn=CNP[9] * 100 + CNP[10] * 10 + CNP[11]
    person['NNN'] = nnn

    print("Informatii Persoana:")
    print(person)

    #validare
    sum=0
    for i in range(len(VALIDATE_CODE)):
        sum+=CNP[i]*VALIDATE_CODE[i]
    rest = sum % 11
    if rest == 10:
        c=1
    else :
        c=rest

    if c == CNP[12]:
        return True
    else:
        return False



CNP=1700425021118

if validator(CNP):
    print ("valid")
else:
    print("invalid")

