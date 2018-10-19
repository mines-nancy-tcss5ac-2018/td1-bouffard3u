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

dico={'a':1,'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'m':2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10,'':0}

def score(mot):
    somme=0
    for i in mot:
        somme+=dico[i]
    return somme
        
def max_score(lettres,lexique):
    motMax=''
    scor=0
    for mot in lexique:
        if score(mot)>score(motMax):
            if motPossible(mot,lettres):
                motMax=mot
                scor=score(motMax)
    return motMax,scor

#assert max_score(('j', 'e', 'u', 'x', 's', 'y', 'w', 'i'),lexique)=='sexy',22