objetfichier=open('frenchssaccent.dic','r')
lexique=[]
for e in objetfichier:
    lexique.append(e)
objetfichier.close()

for i in range(len(lexique)):
    lexique[i]=lexique[i].replace('\n','')
    
def motPossible(mot,lettres):
    L=[e for e in lettres]
    for e in mot:
        if e in L:
            L.remove(e)
        else:
            return False
    return True

def solve(lettres,lexique):
    motMax=''
    for mot in lexique:
        if len(mot)>len(motMax):
            if motPossible(mot,lettres):
                motMax=mot
    return motMax

assert solve(('b', 'p', 'd', 'w', 's', 'y', 'w', 'i'),lexique)=='bis'