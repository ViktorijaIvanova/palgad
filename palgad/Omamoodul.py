

def palkinim(palgad:int,inimesed:str)->int:
    """funktsioon eemaldab loendist elemendid
    """
    
    palk=int(input("sisetage palk: "))
    inimes=input("sisetage nimi inimesed: ")
    inimesed.remove(inimes)
    palgad.remove(palk)
    return inimesed, palgad


def keskpalga(palgad,inimesed):
    """funktsioon väljastab andmed antud indeksiga
    """
    palgad.index()
    palgad.index(palgad[1:3])
    inimesed.index()
    inimesed.index(inimesed[1:3])
    return keskpalga 
       