objetfichier=open('frenchssaccent.dic','r')
lexique=[]
for e in objetfichier:
    lexique.append(e)
objetfichier.close()

for i in range(len(lexique)):
    lexique[i]=lexique[i].replace('\n','')

dico={'a':1,'e':1,'i':1,'l':1,'n':1,'o':1,'r':1,'s':1,'t':1,'u':1,'d':2,'g':2,'m':2,'b':3,'c':3,'p':3,'f':4,'h':4,'v':4,'j':8,'q':8,'k':10,'w':10,'x':10,'y':10,'z':10,'':0,'?':0}

def score(mot):
    somme=0
    for i in mot:
        somme+=dico[i]
    return somme
        
def max_score(lettres):
    motMax=''
    scor=0
    for mot in lettres:
        if score(mot)>score(motMax):
            motMax=mot                      #on ne regarde pas si le mot est possible
            scor=score(motMax)
    return motMax,scor

assert max_score(['rte', 'ver', 'ce', 'etc', 'cet', 'ex', 'cr', 'et', 'ter', 'te', 'ct']) == ('ex', 11)