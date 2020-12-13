'''''''''''''''''''''''''''''''''''''''''''''
MECCANICA DEI SOLIDI; Programma riguardante:
 CINEMATICA,STATICA,LINEA TERMO-ELASTICA
             2 dimensioni
'''''''''''''''''''''''''''''''''''''''''''''
#############################################√ ∛ ∜ ⓥ,㊀,ⓛ,㊇, 
'''Importazioni'''
import copy
import sympy as sym
import mpmath
#from mpmath import *
#from sympy import solve
mpmath.mp.dps = 5; mpmath.mp.pretty = True
pi=sym.pi
import numpy
#from sympy import sqrt
from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False, no_global=True)
from sympy.matrices import *
init_printing(use_unicode=True)
import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
colori = {'Viola':'BUILTIN','Marrone':'console','Rosso':'COMMENT','Nero':'TODO','RossoAcceso':'stderr','Blu':'stdout','Verde':'STRING','Arancione':'KEYWORD','Errore':'ERROR','Warning': 'ERROR'}
def MostraColori():
    for i in colori:
        color.write(i+'\n',colori[i])
def colorwrite(*c):
    if len(c) == 1:
        a,b = c[0],'Nero'
    else:
        a,b = c[0],c[1]
    for i in a:
        if i != "'":
            color.write(i,colori[b])
#q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14 = sym.symbols('q1 q2 q3 q4 q5 q6 q7 q8 q9 q10 q11 q12 q13 q14')
##############################################
'''Simboli'''
#lunghezze:
l        =  sym.symbols('l',positive=True)
L        =  sym.symbols('L',positive=True)
r        =  sym.symbols('r',positive=True)
R        =  sym.symbols('R',positive=True)
#cedimenti normali/tangenti
δ        =  sym.symbols('δ')
delta    =  sym.symbols('δ')
d        =  sym.symbols('δ')
#cedimenti angolari
φ        =  sym.symbols('φ')
csi      =  sym.symbols('φ')
c        =  sym.symbols('φ')
#deformazioni termiche
θ        =  sym.symbols('θ', positive=True)
teta     =  sym.symbols('θ', positive=True)
t1       =  sym.symbols('θ1',positive=True)
t2       =  sym.symbols('θ2',positive=True)
t3       =  sym.symbols('θ3',positive=True)
t4       =  sym.symbols('θ4',positive=True)
α        =  sym.symbols('α', positive=True)#coef. dilataz. term.
alfa     =  sym.symbols('α', positive=True)#coef. dilataz. term.
h        =  sym.symbols('h', positive=True)#spessore
h1       =  sym.symbols('h1', positive=True)#spessore1
h2       =  sym.symbols('h2', positive=True)#spessore2
h3       =  sym.symbols('h3', positive=True)#spessore3
θ1,θ2,θ3,θ4 = t1,t2,t3,t4
#ascissa curvilinea
ξ        =  sym.symbols('ξ',positive=True)
#rigidezze:
A        =  sym.symbols('A',positive=True)#chiamo Ar per non confonderla?
C        =  sym.symbols('C',positive=True)
B        =  sym.symbols('B',positive=True)
#costante elastica
k        =  sym.symbols('k',positive=True)
#azioni distribuite:
p        =  sym.symbols('p',positive=True)
#azioni esterne:
F        =  sym.symbols('F',positive=True)
N        =  sym.symbols('N',positive=True)
T        =  sym.symbols('T',positive=True)
M        =  sym.symbols('M',positive=True)
#Condizioni al contorno:
C1        =  sym.symbols('C1')
C2        =  sym.symbols('C2')
C3        =  sym.symbols('C3')
C4        =  sym.symbols('C4')
#f = sym.symbols('f', real=True, nonzero=True)
##############################################
'''Liste utili'''
numeri     = ['0','1','2','3','4','5','6','7','8','9']
lettere    = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cerchiati  = ['ⓝ',' ⓣ','Ⓝ','Ⓣ','ⓐ','ⓔ']
simboli    = [l,R,δ,delta,d,φ,csi,c,teta,θ,ξ]#...
##############################################
#FUNZIONI ESSENZIALI E RICORRENTI:
'''Algebra (3D):'''
def prodottoscalare(*ab):
    c = 0
    if len(ab) == 1:
        a = ab[0]
        for i in a:
            c += i
        return c
    a,b=ab[0],ab[1]
    for i in range(len(a)):
        c += a[i]*b[i]
    return c
def prodottovettoriale(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def somma(a,b):
    c = [0,0,0]
    for i in range(len(a)):
        c[i] = a[i] + b[i]
    return c
def sottrazione(a,b):
    c = [0,0,0]
    for i in range(len(a)):
        c[i] = a[i] - b[i]
    return c
def prodottorigacolonna(a,b):
    c = [0,0,0]
    for i in range(len(a)):
        c[i] = a[i] * b[i]
    return c

'''Algebra (nD):'''
def nsomma(a,b):
    c = []
    if len(a) == len(b):
        for i in range(len(a)):
            c.append([])
            c[i] = a[i] + b[i]
    else:
        print('len(a)!=len(b)')
    return c
def nsottrazione(a,b):
    c = []
    if len(a) == len(b):
        for i in range(len(a)):
            c.append([])
            c[i] = a[i] - b[i]
    else:
        print('len(a)!=len(b)')
    return c
def nprodottorigacolonna(*ab):
    if len(ab) == 1:
        c = []
        for i in ab[0]:
            c.append(i)
        return c
    ab = ab[0]
    a,b = ab[0],ab[1]
    c = []
    if len(a) == len(b):
        for i in range(len(a)):
            c.append([])
            c[i] = a[i] * b[i]
    else:
        print('len(a)!=len(b)')
    return c
'''Geometria (3D):'''
def distanza(a,b):
    d = ((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**0.5
    d = sym.nsimplify(d)
    return d
def direzione(c,d):
#per adesso funziona solo per ambienti bidimensionali -> penso che possa essere generalizzato SENZA cambiare alcunchè del codice previa verifica di quale coordinata non vari fra i due punti :)
#N.B.: y = sym.atan(x) => x e (-pi/2,pi/2)
#CONVENZIONI SCELTE:
#1) 0 <= α <= 360
#2) segmento AB -> parte in A, finisce in B
#3) Le lunghezze devono chiamarsi l...   
    a,b = [0,0,0],[0,0,0]
    for i in range(len(a)):
        a[i] = c[i]/l
        b[i] = d[i]/l
    Δx = b[0]-a[0]
    Δy = b[1]-a[1]
    #Δz = a[2]-b[2]
    if Δy == 0:
        if Δx > 0:
            α = 0
        elif Δx < 0:
            α = 180
        else:
            print('Mi stai chiedendo la direzione della retta che ha come estremi lo stesso punto.')
            print("Ne segue che l'input immesso rappresenti un punto e non una retta che, in quanto tale, non ha associata alcuna direzione.")
            print('Input:',c,d)
            '''
            print('Che angolo vuoi che ti ritorno?')
            m = float(input())
            return m
            '''
            return False
    elif Δx == 0:
        if Δy > 0:
            α = 90
        else:
            α = 270
    else:
        if Δy/Δx > 0:
            if Δx > 0:
                α = gradi(sym.atan(Δy/Δx))
            else:
                α = 180 + gradi(sym.atan(Δy/Δx))
        else:
            α = gradi(sym.atan(Δy/Δx))  
            if Δx > 0:
                α = 360 + gradi(sym.atan(Δy/Δx))
            else:
                α = 180 + gradi(sym.atan(Δy/Δx))
    return α

'''Calcolo combinatorio''' #N.B.: i seguenti binomiali NON riportano il numero di combinazioni ma le combinazioni stesse
#per far si che le funzioni a seguire abbiano l'input scritto sempre correttamente indipendentemente dal contesto in cui vengono chiamate
def fattoriale(x):
    if x == 0:
       return 1
    else:
       return x * fattoriale(x-1)

def controllo_binomiale(n):
    b = []
    if type(n) == int:
        for i in range(n):
            b.append(str(i+1))
    else:
        if type(n[0]) == str:
            for i in n:
                b.append(str(i))
    return b

#coefficiente binomiale (n,2)
def binomiale_2(n):
    b = controllo_binomiale(n)
    n = len(b)
    c = []
    a = 0
    while a < n:
        d = copy.deepcopy(b)
        f = d[a:]
        e = []
        for i in f:
            if i != d[a]:
                c.append(d[a]+i)
        a += 1
    return c

#n deve essere un intero, amplia la def se necessario. (parto da 0 e non da 1 come in Sum)
def sistema_input_binomiale(n):
    if type(n) not in [int,list]:
        print('Sono sistema_input_binomiale.')
        print("L'input deve essere un o intero o una lista di str/flo/int/sym...")
        return False
    D,Di = {},{}
    b,bi = [],[]
    lista = []
    m = n
    if type(n) == list:
        m = len(n)
    #puoi anche eliminare i seguenti i casi n<=26,52 mantenendo l'else:
    #la loro prensenza semplifica la stampa nel testaggio
    if m <= 26:
        for i in range(97,97+m):
            lista.append(chr(i))
    elif m <= 52:
        for i in range(65,91):
            lista.append(chr(i))
        for i in range(97,97-26+m):
            lista.append(chr(i))
    else:
        for i in range(m):
            lista.append(chr(i))
    if type(n) == int:
        n = []
        for i in range(m):
            n.append(i)
    for i in range(len(n)):
        D[lista[i]]  = n[i]
        Di[n[i]] = lista[i]
        b.append(lista[i])
        bi.append(n[i])
    return [D,Di,b,bi]
       
#E' sum_binomiale ampliato,ma con un imput che non puo essere messo in Tipologia_Vincoli[...], n può ora essere > 9 (<26 ma facilmente aumentabile) MA deve essere intero (in caso puoi ampliare anche questa def)
def Liste_binomiali(n):#chr(i): 0<=i<=65535; a,..,z <=> 97,...,122; A,...Z <=> 65,...,90
    I = sistema_input_binomiale(n)
    if type(n) == list:
        n = len(n)
    D,Di,b,bi = I[0],I[1],I[2],I[3]
    r = []
    r.append(b)
    B = b
    for k in range(n-1):
        c = []
        w = []
        for C in b[:-1]:
            e = []
            c.append([])
            for i in B:
                for j in C:
                    if i > j[-1]:
                        c[-1].append(j+i)
                        w.append(j+i)
        r.append(w)
        b = c
    r.reverse()
    R = []
    for i in r:
        R.append([])
        for j in i:
            R[-1].append([])
            for k in j:
                R[-1][-1].append(D[k])
    return R

#real binomiale(n,k) con output combinazioni e non cardinalità
def Binomiale(n,k):
    B = Liste_binomiali(n)
    B.reverse()
    B = B[k-1]
    #verifica:
    if type(n) != int:
        n = len(n)
    c = fattoriale(n)/(fattoriale(k)*fattoriale(n-k))
    if len(B) == c:
        return B
    else:
        print('len(output) =',len(B))
        print('binom.(n,k) =',c)
        return False
    
#sommatoria coefficienti binomiali (n,i): lista di n liste ciascuna corrispondente a n-i
def sum_binomiale(n):
    r = []
    b = controllo_binomiale(n)
    n = len(b)
    r.append(b)
    B = b
    for k in range(n-1):
        c = []
        w = []
        for C in b[:-1]:
            e = []
            c.append([])
            for i in B:
                for j in C:
                    if int(i) > int(j[-1]):
                        c[-1].append(j+i)
                        w.append(j+i)
        r.append(w)
        b = c
    r.reverse()
    return r

#dizionario di 2^(n-1) elementi (esclude binomiale(n,1)) che associa ad ogni insieme di n elementi i suoi n(n-1)/2 elementi 'binomializzati'
def dizionale(n):
    b = controllo_binomiale(n)
    n = len(b)
    Db = {}
    bs = elenca(sum_binomiale(n)[:-2])
    for i in bs:
        Db[i] = binomiale_2(i)
    return Db

'''Visualizzatori'''
def stampamatrice2(A):#sym.pprint(A)
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = sym.nsimplify(A[i][j])
    L = []
    for i in range(len(A)):
        M = []
        for j in range(len(A[i])):
            M.append([])
        L.append(M)
    l = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if len(str(A[i][j])) > l:
                l = len(str(A[i][j]))
    for i in range(len(A)):
        for j in range(len(A[i])):
            L[i][j] = ' '*(l-len(str(A[i][j])))+str(A[i][j])
    return L
#raramente la matrice è cosi grande da non entrare nello schermo... in caso usa questa def:
def stampamatrice(A):#sym.pprint(A)
    for i in range(len(A)):
        for j in range(len(A[i])):
            ##################################
            A[i][j] = sym.nsimplify(A[i][j])
            ##################################
    L = []
    for i in range(len(A)):
        M = []
        for j in range(len(A[i])):
            M.append([])
        L.append(M)
    l = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            a = sta(A[i][j])
            if len(a) > l:
                l = len(a)
    for i in range(len(A)):
        for j in range(len(A[i])):
            a = sta(A[i][j])
            L[i][j] = ' '*(l-len(a))+a
    return L
#stampavettore([-R*q3 + q1, R*q3 + q2, 0]) -> (-R*q3 + q1)e1 + (R*q3 + q2)e2
def stampavettore(a):
    st = []
    c  = 0
    for i in a:
        c+=1
        if i != 0:
            st.append('('+str(i)+')e'+str(c))
    sta = ''
    c   = len(st)-1
    for i in st:
        if st[c] == i:
            sta += i
        else:
            sta += i+' + '
    return sta

def sstampavettore(a):
    st = []
    c  = 0
    for i in a:
        c+=1
        if i != 0:
            color.write('(',colori['Viola'])
            color.write(str(i),colori['Blu'])
            color.write(')e'+str(c),colori['Viola'])
            if c == 1:
                if ss(a[1]) != 0 or ss(a[2]) != 0:
                    color.write(' + ',colori['Blu'])
            elif c == 2:
                if ss(a[2]) != 0:
                    color.write(' + ',colori['Blu'])
    return ' '

def stampavettore2(*A):
    a = A[0]
    if len([*A]) != 2:
        st = []
        c = 0
        for i in a:
            c += 1
            if i != 0:
                st.append('('+str(i)+')e'+str(c))
        sta = ''
        c   = len(st)-1
        for i in st:
            if st[c] == i:
                sta += i
            else:
                sta += i+' + '
        return sta
    else:
        l1,l2 = A[1][0],A[1][1]
        st = []
        c = 0
        for i in a:
            c += 1
            if i != 0:
                st.append('('+str(i)+')'+' '*([1,l1,l2][c-1]-len(str(i)))+'e'+str(c))
            else:
                st.append(' '*([1,l1,l2][c-1]+4))
        sta = ''
        c   = len(st)-1
        for i in st:
            if st[c] == i:
                sta += i
            else:
                sta += i+' + '
        return sta


'''Gradi <=> Radianti'''
def gradi(x):
    x=180*x/pi
    return x
def rad(x):
    x=x*pi/180
    return x
'''Spezza punti'''
def spezza(l):
    L = []
    for i in range(len(l)):
        if i == len(l)-1:
            if i == 0:
                return [l]
            else:
                if l[i] in lettere:
                    L.append(l[i])
                    break
        if l[i] in lettere and l[i+1] in lettere:
            L.append(l[i])
        elif l[i] in lettere and l[i+1] in numeri:
            L.append(l[i]+l[i+1])
    return L

##############################################
#FUNZIONI NON ESSENZIALI MA RICORRENTI:
'''Estetica'''
def VIN_():
    return(['Carrello','Pendolo/Biella','Pantografo/Tecnigrafo','Cerniera','Pattino/Glifo','Incastro','Molla'])
'''True-False'''
def si_o_no():
    cc = 0
    while cc == 0:
        cc = 1
        risp = input().lower()
        if len(risp) == 0:
            return False
        if risp not in ['si','no']:
            print('La risposta deve essere o si o no. Rispondi di nuovo:')
            print('Digitare invio equivale a digitare "no".')
            cc = 0
    if risp == 'si':
        return True
    else:
        return False
'''Elenca Liste di liste e Dizionari'''
def elenca(a):
    L = []
    if type(a) == list:
        for i in a:
            for j in i:
                L.append(j)
    elif type(a) == dict:
        for i in a:
            L.append(i)
    return L
def elenca_senza_duplicati(a):#usata una sola volta...
    L = []
    if type(a) == list:
        for i in a:
            for j in i:
                if j not in L:
                    L.append(j)
    elif type(a) == dict:
        for i in a:
            if i not in L:
                L.append(i)
    return L
##############################################
#FUNZIONI SYM INVERSE: Ritornato Liste (o Liste di liste) di stringhe, così che siano pronte per la stampa
#ELIMINATI TUTTI I PEZZI IN CUI VENGONO USATE (sostituite con le funzioni sym apposite)
'''M = Matrix(A) => A = ConvertitoreMatriceLista(M) se A è quadrata'''
def ConvertitoreMatriceLista(M):#M = M.tolist()
    #solo per M quadrate
    v = int(len(M)**0.5)
    W = []
    for i in M:
        W.append([sym.sympify(i)])
    for i in range(len(W)):
        W[i] = [sym.sympify(str(W[i])[1:-1]).evalf(5)]
    K = []
    for i in range(v):
        V = []
        for j in range(v):
            V.append([])
        K.append(V)
    for i in range(v):
        for j in range(v):
            K[i][j] = W[j+v*i]
    for i in range(len(K)):
        for j in range(len(K[i])):
            K[i][j] = sym.sympify(str(K[i][j])[1:-1]).evalf(5)
    #K = K.tolist(A)
    return K
'''V = Matrix(q) => q = ConvertitoreVettoreLista(V)'''#M.tolist())
def ConvertitoreVettoreLista(V):#a = list(map(lambda x:x[0],a.tolist())) -> quando?
    for i in V:
        Q.append([sym.sympify(i)])
    for i in range(len(Q)):
        Q[i] = [sym.sympify(str(Q[i])[1:-1]).evalf(5)]
    #Q = V.tolist()
    return Q
'''V = lista di str => V2 = lista di sym'''
def SymVettore(V):
    V2 = []
    for i in V:
        if i.strip() == '0':
            V2.append(sym.sympify(i).evalf(1))
        else:
            V2.append(sym.sympify(i).evalf(5))
    return V2
#unica funzione che PUO SERVIRE, ma non l'ho ancora usata
def DelistaVettore(a):
    b = list(map(lambda x:x[0],a.tolist()))
    return b
##############################################
#CORREZIONE INCOMPATIBILITA' IMPORTAZIONI: SYMPY-COPY: n.b.: ss() crea un terzo simbolo, o lo si fa a tutto o da errore (credo)
def ss(a):
    a = sym.simplify(sym.sympify(str(a)).evalf(5))
    b = str(a)
    if 'e-' in b:
        if b.count(' ') == 0:
            return 0
    return a

##############################################
##############################################
#FUNZIONI DI SUPPORTO PER PREPARA:
'''FUNZIONI CON SOLO INPUT: Pr '''
#################################
###Pr = ['ABC', 'CDE', 'CFEG']###
#################################

#lista -> lista
#tutti i punti di Pr senza numero
#['A', 'B', 'C', 'D', 'E', 'F', 'G']
def punti_(Pr):
    return elenca_senza_duplicati(Pr)

#lista -> lista di liste
#tutti i punti di Pr numerati e divisi per corpo
#[['A1', 'B1', 'C1'], ['C2', 'D2', 'E2'], ['C3', 'F3', 'E3', 'G3']]
def P_(Pr):
    P = []
    n = len(Pr)
    for i in range(n):
        P.append([])
        for j in range(len(Pr[i])):
            P[-1].append(Pr[i][j]+str(i+1))
    return P

#lista -> lista di liste
#tutti i punti di Pr non numerati e divisi per corpo
#[['A', 'B', 'C'], ['C', 'D', 'E'], ['C', 'F', 'E', 'G']]
def Pu_(Pr):
    P = []
    n = len(Pr)
    for i in range(n):
        P.append([])
        for j in range(len(Pr[i])):
            P[-1].append(Pr[i][j])
    return P

#lista -> lista
#tutti i punti di Pr con numero. Quelli di raccordo fra più corpi son ripetuti ma con numeri differenti
#['A1', 'B1', 'C1', 'C2', 'D2', 'E2', 'C3', 'F3', 'E3', 'G3']
def punti_numerati(Pr):
    n = len(Pr)
    puntinumerati = []
    for i in range(n):
        for j in range(len(Pr[i])):
            puntinumerati.append(Pr[i][j]+str(i+1))
    return puntinumerati

#lista -> lista di liste
#lista di liste -> lista di liste
#come P ma i punti hanno il numero solo se sono di raccordo= 
#=tutti i punti di Pr numerati con relativo numero solo in caso di punti di raccordo e divisi per corpo (lista di liste)
#P             = [['A1', 'B1', 'C1'], ['C2', 'D2', 'E2'], ['C3', 'F3', 'E3', 'G3']]
#puntinumerati = [ 'A1', 'B1', 'C1',   'C2', 'D2', 'E2',   'C3', 'F3', 'E3', 'G3']
#[['A', 'B', 'C1'], ['C2', 'D', 'E2'], ['C3', 'F', 'E3', 'G']]
def PU_(Pr):
    P  = P_(Pr)
    PU = []
    for i in P:
        PU.append([])
        for j in i:
            PU[-1].append(j)
    puntinumerati = punti_numerati(Pr)
    M1 = []
    for i in puntinumerati:
        M1.append(i[:-1])
    M2 = []
    for i in M1:
        if M1.count(i) == 1:
            M2.append(i)
    n = len(Pr)
    for i in range(n):
        for j in range(len(PU[i])):
            if PU[i][j][:-1] in M2:
                PU[i][j] = PU[i][j][:-1]
    return PU

#lista -> lista
#lista di liste -> lista
#lista dei punti di PU
#PU = [['A', 'B', 'C1'], ['C2', 'D', 'E2'], ['C3', 'F', 'E3', 'G']]
#['A', 'B', 'C1', 'C2', 'D', 'E2', 'C3', 'F', 'E3', 'G']
def PUNTI_(Pr):
    PU = PU_(Pr)
    return elenca(PU)
##############################################
'''FUNZIONE DI SUPPORTO PER IL DIZIONARIO COORDINATE'''
#Aggiunge a D = {} i punti numerati (+L0 per i nodi)
#P = [['A1', 'B1', 'C1'], ['C2', 'D2', 'E2'], ['C3', 'F3', 'E3', 'G3']]
#{'A':[-l,l,0],...} -> {'A':[-l,l,0],'A1':[-l,l,0],...}
def AggiornaDizionario(D,Pr):
    C = {}
    for i in D:
        C[i+'0'] = D[i]
    P = P_(Pr)
    for i in P:
        for j in i:
            if j not in D:
                D[j] = D[j[0]]
    D = dict(D, **C);
    return D
##############################################
'''FUNZIONI DI SUPPORTO CON INPUT: vin (o vin e Pr)'''
########################################################################
##vin = [['A','G'], [], [], ['C', 'E2E3', 'C1C2', 'C2C3'], [], [], []]##
########################################################################
def stampavincoli():
    print()
    print('                                           n = numero di aste, condizioni imposte:        ')
    print('                                          assoluto (se n=1):              relativo:       ')#?assoluto e relativo. corretto?
    print('                                             asta-terra                  asta-asta/2      ')
    print('VINCOLI SEMPLICI:                                                                         ')
    print('Carrello:                V(P) n = δn             2n-1             1 se n=1, 2n-3 se n > 1 ')
    print()
    print('Pendolo/Biella:   [V(Q)-V(P)] n = δn             2n-1             1 se n=1, 2n-3 se n > 1 ')##credo sia superfluo scrivere in funzione di n. Se n>1 è un carrello...
    print()
    print('Pantografo:              |θ(P)| = φ                1                         1            ')
    print()
    print('VINCOLI DOPPI:                                                                            ')
    print('Cerniera                 V(P) n = δn              2n                     2(n-1)           ')
    print('                         V(P) t = δt                                                      ')
    print()
    print('Pattino/Glifo            V(P) n = δn               2                         2            ')
    print('                         |θ(P)| = φ                                                       ')
    print()
    print('VINCOLI TRIPLI:                                                                           ')
    print('Incastro:                V(P) n = δn               3                         3            ')
    print('                         V(P) t = δt                                                      ')
    print('                         |θ(P)| = φ                                                       ')
    print('MOLLE:')
    print('                         V(P) n = δn             2n-1             1 se n=1, 2n-3 se n > 1 ')
    print()
    
#Aggiunge a vin i numeri ad ogni lettera fatta eccezione per i 'nodi' (ossia i vincoli sia interni che esterni)
#[['A1', 'G3'], [], [], ['C', 'E2E3'], [], [], []]
def numeravincoli(vin,Pr):
    V = copy.deepcopy(vin)
    PUNTI = PUNTI_(Pr)
    puntinumerati = punti_numerati(Pr)
    Pu = Pu_(Pr)
    for i in range(len(vin)):
        for j in range(len(vin[i])):
            if len(vin[i][j]) == 1:
                if vin[i][j] in PUNTI:
                    for k in puntinumerati:
                        if k[0] == vin[i][j]:
                            m = k[1]
                    V[i][j] = vin[i][j]+m
            elif len(vin[i][j]) == 2:
                if vin[i][j][1] not in ['1','2','3','4','5','6','7','8','9']:#Aggiunta postuma
                    vrel = ''
                    for k in vin[i][j]:
                        for t in range(len(Pu)):
                            if k in Pu[t]:
                                vrel += k+str(t+1)
                    V[i][j] = vrel
    #se len(vin[i][j]) == 1 ma quel punto è di raccordo e non ci sono nodi => P1P2.. ora non lo fa :(
    #nel caso di vincoli relativi legati a nodi -> sostituisco con 0 il numero: es:A1A2A3B1->A0B1,A1A2B1B2 -> A0B0,etc.
    for i in range(len(V)):
        for j in range(len(V[i])):
            if len(V[i][j]) > 4:
                a,b = V[i][j],int(len(V[i][j])/2)-1
                cc = 0
                for k in range(b):
                    if V[i][j][2*k] == V[i][j][2*k+2]:
                        a = a[:2*k+1+cc]+a[2*k+2+cc:]
                        cc -= 1
                b = a.count(a[0])
                if b > 1:
                    a = a[b-1:]
                    a = a[0]+'0'+a[2:]
                b = a.count(a[-2])
                if b > 1:
                    a = a[:-1]
                    a = a+'0'
                    a = a[:2]+a[-2]+a[-1]
                V[i][j] = a
    return V

#Ritorna una dizionario che ha come chiave i punti ove vi sono vincoli contemporaneamente assoluti e relativi
#Var[punto] = [elenco dei numeri dei corpi che si raccordano in quel punto, posizione i (vin[i]), posizione j (vin[i][j])]
#{'C': [['1','2','3'], 3, 0]}]
#Pr  = ['ABC', 'CDE', 'CFEG']
#vin = [['A', 'G' ], [], [], ['C', 'E2E3'], [], [], []]
def Var_(vin,Pr):
    #vin = numeravincoli(vin,Pr)#?? '#' ci va o no?
    puntinumerati = punti_numerati(Pr)
    Var  = {}
    for i in range(len(vin)):
        for j in range(len(vin[i])):
            s = len(spezza(vin[i][j]))
            if s == 1:
                if len(vin[i][j]) == 1:
                    m = vin[i][j]
                    Var[vin[i][j]] = [[],i,j]
    for i in Var:
        for j in puntinumerati:
            if j[0] == i:
                Var[i][0].append(j[1])
    for i in Var:
        Var[i][0].sort()
    return Var
       
#'Apre' un nodo dividendolo in somma di vincoli. 
#vin = [['A1', 'G3'], [], [], ['C', 'E2E3'], [], [], []]
#[['A1', 'F3'], [], [], ['C', 'C1C2', 'C2C3', 'E2E3'], [], [], []]
def riducinodi(vin,Pr):#se ci sono 3 (4) corpi e il nodo è collegato solo a 2 (3) di essi, riporta un risultato errato
    vin = numeravincoli(vin,Pr)
    Var = Var_(vin,Pr)#{'C': [['1','2','3',] 3, 0]}
    for k in Var:
        s = Var[k][0]
        i = Var[k][1]
        j = Var[k][2]
        if i == 0:
            for h in range(len(s)-1):
                vin[3].append(k+s[h]+k+s[h+1])
        elif i == 3:
            for h in range(len(s)-1):
                vin[3].insert(1+j+h,k+s[h]+k+s[h+1])
            #[['A1', 'F3'], [], [], ['C', 'C1C2', 'C2C3', 'E2E3'], [], [], []]
    for i in vin[3]:
        if len(i) == 1:
            vin[3][vin[3].index(i)] = vin[3][vin[3].index(i)]+'0'
    for i in vin[0]:
        if len(i) == 1:
            vin[0][vin[0].index(i)] = vin[0][vin[0].index(i)]+'0'
    return vin

#Al fine di poter chiamare altre volte riducinodi() senza dover stampare tutto piu volte
def stampariducinodi(vin,Pr):
    vin = riducinodi(vin,Pr)
    Var = Var_(vin,Pr)
    for k in Var:
        s = Var[k][0]
        i = Var[k][1]
        j = Var[k][2]
        if i == 0:
            print('\nIn',k,'vi è un carrello che funge sia da vincolo interno che esterno ed eroga dunque 1 condizione di vincolo assoluta e',2*len(s)-2,'relative.')
            print('Lo scompongo in',len(s),'vincoli secondo il seguente schema: (ti servirà saperlo per quando ti chiederò gli angoli)')
            print(vin[i][j],'   -> carrello esterno')
            for h in range(len(s)-1):
                print(k+s[h]+k+s[h+1],'-> cerniera interna')
        elif i == 3:
            print('\nIn',k,'vi è una cerniera che funge sia interno che esterno ed eroga dunque 2 condizioni di vincolo assoluto e',2*len(s)-2,'relative.')
            print('Lo scompongo in',len(s),'vincoli. Es: D -> D1D2+D2D3+D = cerniera+cerniera+cerniera. Ti servirà saperlo per quando ti chiederò gli angoli.')
            print(vin[i][j],'   -> cerniera esterna')
            for h in range(len(s)-1):
                print(k+s[h]+k+s[h+1],'-> cerniera interna')
        else:
            print('Sono stampariducinodi(vin,Pr). Deve esserci un errore.\n\n\n')
    print()
            
#rende semplici tutti i vincoli e li distingue con un 'etichetta':
#S  = [[normali],[tangenti],[angolari],[elastici]]
#riducinodi(vin) = [['A1', 'G3'], [], [], ['C', 'E2E3', 'C1C2', 'C2C3'], [], [], []]
#[['A1Ⓝ', 'G3Ⓝ', 'CⓃ', 'E2E3Ⓝ', 'C1C2Ⓝ', 'C2C3Ⓝ'], ['CⓉ', 'E2E3Ⓣ', 'C1C2Ⓣ', 'C2C3Ⓣ'], [], []]
def semplificavincoli(V,Pr):#'ⓝ','ⓣ','Ⓝ','Ⓣ','ⓐ','ⓔ'
    S   = [[], [], [], []]
    for i in range(len(V)):
        for j in range(len(V[i])):
            if i in [0,1,3,4,5]:
                S[0].append(V[i][j]  +'ⓝ')
            if i in [2,4,5]:
                S[2].append(V[i][j]  +'ⓐ')
            if i in [3,5]:
                S[1].append(V[i][j]  +'ⓣ')
            if i in [6]:
                S[3].append(V[i][j]  +'ⓔ')
    return S
###################################################################################################
###################################################################################################
'''FUNZIONI INPUT()'''
#Pr  = ['ABC', 'CGE', 'CDEG']
#vin = [['A', 'G' ], [], [], ['C', 'E2E3'], [], [], []]


#Pr = ['ABC', 'CDE', 'CFEG']
def chiedimi_i_punti(n):
    print('Scrivimi tutti i punti del corpo indicato:')
    Pr = []
    for i in range(n):
        Pr.append([])
        cc = 0
        while cc == 0:
            cc = 1
            p = input('Punti corpo n.'+str(i+1)+':\n').strip().upper()
            if len(p) == 0:
                cc = 0
            for h in p:
                if h not in lettere:
                    cc = 0
            if cc == 0:
                print('La risposta deve contenere solo lettere e nessuno spazio fra loro. Te lo richiedo.')
        Pr[i] = p
    return Pr

#P = ['A1','B1','C1','C2','D2','E2','C3','F3','E3','G3']
def sistemaP(Pr):
    return punti_numerati(Pr)

def chiedimi_le_coordinate(Pr):
    punti = punti_(Pr)
    print('Per ogni punto che ti verrà chiesto, specificane la posizione X e Y:')
    print("Se sbagli a digitare, scrivi 'ricomincia' o 'ripeti'.")
    print("La lunghezza caratteristica è 'l'. Se preferisci scrivi solo interi.")
    cc = 0
    while cc == 0:
        cc = 1
        D  = {}
        for i in punti:
            x = input(str(i)+'x: ')
            if x.lower() in ['ricomincia','ripeti']:
                cc = 0
                print('Ricominciamo da capo con le coordinate dei punti:')
                break
            else:
                if len(x) == 0:
                    x = '0'
                elif x == '-':
                    x = '-l'
                elif x == '+':
                    x = 'l'
                elif 'l' not in x:
                    x = x+'*l'
            y = input(str(i)+'y: ')
            if y.lower()  in ['ricomincia','ripeti']:
                cc = 0
                print('Ricominciamo da capo con le coordinate dei punti:')
                break
            else:
                if len(y) == 0:
                    y = '0'
                elif y == '-':
                    y = '-l'
                elif y == '+':
                    y = 'l'
                elif 'l' not in y:
                    y = y+'*l'
                x = sym.sympify(x)
                y = sym.sympify(y)
                D[i] = [x,y,0]
                print()
    return D

def chiedimi_i_collegamenti(Pr):
    punti = punti_(Pr)
    print('Per ognuno dei punti che ti indicherò, scrivimi con quali altri punti è collegato (senza spazi ne numeri).')
    dd = 0
    while dd == 0:
        dd = 1
        Relazioni = {}
        for i in punti:
            if dd == 1:
                cc = 0
                while cc == 0:
                    cc = 1
                    risp = input(i+':  ').upper()
                    while len(risp) == 0:
                        print('La risposta può contenere solo',str(punti)+'. Ripeti')
                        risp = input(i+':  ').upper()
                    if risp.lower() in ['ricomincia','ripeti']:
                        print('Ricominciamo da capo con i collegamenti.')
                        dd,cc = 0,1
                    if dd == 1:
                        for j in risp:
                            if j not in punti:
                                cc = 0
                                print('La risposta può contenere solo',str(punti)+'. Ripeti')
                                break
            rel = []
            h = 0
            for k in risp:
                rel.append(k)
            Relazioni[i] = rel
    return Relazioni#{'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D', 'G'], 'D': ['C', 'E'], 'E': ['D', 'F', 'G'], 'F': ['E'], 'G': ['E', 'C']}
#Pr = ['ABCDF','EF']
#{'A': ['B'], 'B': ['A', 'E', 'C'], 'C': ['B', 'D', 'F'], 'D': ['C'], 'F': ['C', 'E'], 'E': ['B', 'F']}


def sistema_relazioni(Relazioni,Pr):
    Pu = Pu_(Pr)#[['A',  'B',  'C' ], ['C',  'D',  'E' ], ['C',  'F',  'E',  'G' ]]
    #Creiamo una lista di liste ove ogni sottolista, rappresentativa di un corpo, contiene tutti i collegamenti fra aste di quel corpo.
    #es1 Relazioni = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D', 'G'], 'D': ['C', 'E'], 'E': ['D', 'F', 'G'], 'F': ['E'], 'G': ['E', 'C']}
    #--> Obiettivo = [['AB','BC'],['CG','GE'],['CD','DE','EF']]#gli elementi di ogni sottolista non saranno necessariamente nell'ordine indicato
    n = len(Pr)
    Collegamenti = []
    for i in range(n):
        Collegamenti.append([])
        for j in Relazioni:
            if j in Pu[i]:
                for k in Relazioni[j]:
                    if k in Pu[i]:
                        if (j+k and k+j) not in Collegamenti[i]:
                            Collegamenti[i].append(j+k)
    return Collegamenti
    #Collegamenti = [['AB', 'BC'], ['CG', 'EG'], ['CD', 'DE', 'EF']]
def sistema_collegamenti(Collegamenti):
    #Collegamenti = [['AB', 'BC'], ['CG', 'EG'], ['CD', 'DE', 'EF']]
    #Collegamenti = [['AB','BC','CD','CE'],['FE','EG']]
    #Collegamenti = [['AB','BC','CD','CE'],['FE','EG','EH']]# -> test
    Link = {}
    ee = []
    for i in Collegamenti:
        e = []
        for j in i:
            for k in j:
                e.append(k)
        ee.append(e)
    #ee1 = [['A', 'B', 'B', 'C'], ['C', 'G', 'E', 'G'], ['C', 'D', 'D', 'E', 'E', 'F']]
    E = []
    for i in ee:
        e = []
        for j in i:
            if i.count(j) == 1:
                e.append(j)
        E.append(e)
    #len(E1[i]) '= [2,2,2]'   #if len(E[i]) in [1,2] => non serve chiedere i contributi
    #len(E2) = [3,2]
    for i in range(len(Collegamenti)):
        if len(Collegamenti[i]) == 1:
            E[i] = 0
    #E[i] = 0 -> vi è una sola trave
    #len(E[i]) = n -> 0 -> ci sono n estremi liberi
    #len(E[i]) = 2 -> le travi sono tutte collegate 'in fila' (ci sono 2 estremi liberi)
    cc = 0
    for i in range(len(Collegamenti)):
        if E[i] == 0:
            Link[Collegamenti[i][0]] = []
        elif len(E[i]) == 2:
            #ordiniamo Collegamenti[i] cosicchè le travi siano in giusta progressione
            R = []
            R2 = []
            for j in Collegamenti[i]:
                if j[0] == E[i][0]:
                    R.append(j)
                    R2.append(j)
                    R2.append(j[1]+j[0])
                elif j[1] == E[i][0]:
                    R.append(j[1]+j[0])
                    R2.append(j)
                    R2.append(j[1]+j[0])
            d = 1
            while d < len(Collegamenti[i]):
                for j in Collegamenti[i]:
                    if j not in R2:
                        if j[0] == R[-1][1]:
                            R.append(j)
                            R2.append(j)
                            R2.append(j[1]+j[0])
                            d += 1
                        elif j[1] == R[-1][1]:
                            R.append(j[1]+j[0])
                            R2.append(j)
                            R2.append(j[1]+j[0])
                            d += 1
            Collegamenti[i] = R
            #aggiungiamo i contributi
            for h in Collegamenti[i]:
                Link[h] = []
            for h in range(len(Collegamenti[i])):
                f = len(Collegamenti[i])-h-1
                while f > 0:
                    f -= 1
                    Link[Collegamenti[i][len(Collegamenti[i])-h-1]].append(Collegamenti[i][f])
        else:
            if cc == 0:
                cc = 1
                print('Mi serve conoscere le condizioni al contorno per quando dovrò calcolare le sollecitazioni dei sistemi ausiliari.')
                print('Ti mostrerò innanzitutto una legenda che associa ad ogni travi di uno specifico corpo un numero,')
                print('in questo modo, invece delle lettere delimitanti la trave, potrai rispondermi con il numero ad essa associata.')
                print('Successivamente ti farò due domande, la prima riguarda i versi delle travi (la trave AB ha la direzione del vettore che parte in A e termina in B);')
                print('la seconda riguarda invece i contributi da sommare ad ogni trave: questi NON saranno cumulativi, quindi se le travi sono: AB(->1),BC(->2),CD(->3), per la trave CD dovrai digitare: 12.')
                print('Ad ogni domanda dovrai rispondere con i numeri relativi le travi senza spazi (e non con i punti che le delimitano), o, per passare alla domanda successiva, con il numero 0 o premendo invio.')
                print("E' molto raro che accada, per cui verifica prima bene gli input immessi, ma, se considero un collegamento di troppo, digita 'elimina'.")
            for h in range(len(Collegamenti[i])):
                print(Collegamenti[i][h],'-->',h+1)
            risp = input('Versi delle travi. Quale trave deve avere verso opposto?\n')
            if risp.lower() in ['elimina','del','cancella']:
                print('Ok, quali collegamenti devo eliminare?')#L rimane fregato cosi :(
                risp = input()
                soso = []
                for k in risp:
                    soso.append(k)
                soso.sort()
                risp = ''
                for k in soso:
                    risp = risp+k
                tt = -1
                for k in risp:
                    tt += 1
                    del Collegamenti[i][int(k)-1+tt]
                print('Eliminati. Te lo richiedo:')
                for h in range(len(Collegamenti[i])):
                    print(Collegamenti[i][h],'-->',h+1)
                print('Quale trave deve avere verso opposto?')
                risp = input()
            for k in risp:
                if k != '0':
                    Collegamenti[i][int(k)-1] = Collegamenti[i][int(k)-1][1]+Collegamenti[i][int(k)-1][0]
            for h in Collegamenti[i]:
                Link[h] = []
            print('Contributi per le condizioni al contorno:')
            for h in range(len(Collegamenti[i])):
                risp = input(Collegamenti[i][h]+':\n')
                for k in risp:
                    if k != '0':
                        Link[Collegamenti[i][h]].append(Collegamenti[i][int(k)-1])
    return Link
#print(sistema_collegamenti())
#Collegamenti = [['AB', 'BC'], ['CG', 'EG'], ['CD', 'DE', 'EF']]# -> Link = {'AB': [], 'BC': ['AB'], 'CG': [], 'GE': ['CG'], 'CD': [], 'DE': ['CD'], 'EF': ['DE', 'CD']}
#Collegamenti = [['ED','CD','EF','FG'],['FE','EG']]
#Collegamenti = [['AB','BC','CD','CE'],['FE','EG']]# -> {'AB': [], 'BC': ['AB'], 'CD': ['AB', 'BC', 'EC'], 'EC': [], 'FE': [], 'EG': ['FE']} n.b.: lista di prova, non presa da un esercizio
#print(sistema_collegamenti(Collegamenti))

def Sistema_Link(Link,Pr):
    n = len(Pr)
    Pu = Pu_(Pr)#[['A','B','C'], ['C','G','E'], ['C','D','E','F']]
    L = []
    for i in range(n):
        L.append({})
    for i in Link:
        c = 0
        for j in range(len(Pu)):
            if i[0] in Pu[j]:
                if i[1] in Pu[j]:
                    L[j][i] = Link[i]
    return L
#Pr  = ['ABC', 'CGE', 'CDEF']
#Link = {'AB': [], 'BC': ['AB'], 'CG': [], 'GE': ['CG'], 'CD': [], 'DE': ['CD'], 'EF': ['DE', 'CD']}
#print(Sistema_Link(Link,Pr))

#vin = [['A', 'G' ], [], [], ['C', 'E2E3'], [], [], []]
def chiedimi_i_vincoli():
    print('Per ognuno dei vincoli che ti indicherò, dimmi, uno alla volta, in quale punto è presente. Per andare avanti digita invio.')
    print('Non usare mai spazi ne numeri (a meno che strettamente necessari). Devi cioè darmi le informazioni MINIME per la comprensione del testo')
    print('Nel caso di cerniera, se questa coinvolge tutti i corpi che confluiscono in quel punto, digita solo la lettera;')
    print('alternativamente digita lettra+numeri relativi ai corpi coinvolti')
    print("Se sbagli a digitare, scrivi 'ricomincia' o 'ripeti'.")
    VIN = VIN_()
    vin = [[],[],[],[],[],[],[]]
    c = 0
    d = 0
    while c < 7:
        d += 1
        risp = input(VIN[c]+' n.'+str(d)+':\n').strip().upper()
        if risp == '':
            c += 1
            d = 0
        elif risp in ['RICOMINCIA','RIPETI']:
            print("Ok, ricominciamo.")
            c = 0
            d = 0
            vin = [[],[],[],[],[],[],[]]
        else:
            vin[c].append(risp)
    return vin

#V = ['A1Ⓝ', 'G3Ⓝ', 'CⓃ','C1C2Ⓝ', 'C2C3Ⓝ','C1C2Ⓣ', 'C2C3Ⓣ', 'E2E3Ⓝ', 'E2E3Ⓣ'] (non in quest'ordine)
def sistemavin(vin,Pr):
    VIN = ['carrello','pendolo/biella','pantografo/tecnigrafo','cerniera','pattino/glifo','incastro','molla']
    #vin = ??
    V = numeravincoli(vin,Pr)
    #V = [['A1', 'F3'], [], [], ['C', 'E2E3'], [], [], []]
    stampariducinodi(vin,Pr)
    V = riducinodi(vin,Pr)
    #V = [['A1', 'F3'], [], [], ['C', 'E2E3', 'C1C2', 'C2C3'], [], [], []]
    V = semplificavincoli(V,Pr)
    #V = [['A1Ⓝ', 'F3Ⓝ', 'CⓃ', 'E2E3Ⓝ', 'C1C2Ⓝ', 'C2C3Ⓝ'], ['CⓉ', 'E2E3Ⓣ', 'C1C2Ⓣ', 'C2C3Ⓣ'], [], []]
    V = elenca(V)
    #V = ['A1Ⓝ', 'F3Ⓝ', 'CⓃ', 'E2E3Ⓝ', 'C1C2Ⓝ', 'C2C3Ⓝ', 'CⓉ', 'E2E3Ⓣ', 'C1C2Ⓣ', 'C2C3Ⓣ']
    return V

def chiedimi_angoli_e_cedimenti(vin,Pr,D):#lower()?#ripeti/ricomincia#invio invece che 0#filtro cedimenti
    vin = riducinodi(vin,Pr)
    VIN = VIN_()#['carrello','pendolo/biella','pantografo/tecnigrafo','cerniera','pattino/glifo','incastro','molla']
    print('Rispondi alle seguenti domande. Esprimi gli angoli in gradi. Sappi che:')
    print('a pendoli e molle esterne aumenterò autonomamente gli angoli di (+/-)180 gradi per considerare le reaz.vinc. tiranti e non comprimenti')
    print('Se una cerniera è esterna, digita solo il punto in cui è applicata, altrimenti PNPN')
    print("Se commetti un errore, digita 'ripeti' o 'ricomincia'")
    cc = 0
    while cc == 0:
        cc = 1
        DA,Mol  = {},{}
        for i in range(len(vin)):
            if i in [0]:#Carrello
                for j in vin[i]:
                    if cc == 1:
                        print(VIN[i],'in',j+':')
                        m = input('Angolo normale-orizzonte\n')
                        if m.lower() not in ['ricomincia','ripeti']:
                            if len(m) == 0:
                                m = 0
                                if i == 1:
                                    m = 180
                            else:
                                m = sym.sympify(m)
                                if i == 1:
                                    if m  >= 180:
                                        m -= 180
                                    else:
                                        m += 180
                            DA[j+'ⓝ'] = m
                        else:
                            cc = 0
                            print('Ok, ricominciamo.')
            elif i in [1]:#Pendolo(/Biella)
                for j in vin[i]:
                    dd = 0
                    if len(j) == 4:
                        if j[0] != j[2]:
                            di = direzione(D[j[0]],D[j[2]])
                            di += 180
                            if di >= 360:
                                di -= 360
                            DA[j+'ⓝ'] = di
                        else:
                            dd = 1
                    else:
                        dd = 1
                    if dd == 1:
                        if cc == 1:
                            print(VIN[i],'in',j+':')
                            m = input('Angolo normale-orizzonte\n')
                            if m.lower() not in ['ricomincia','ripeti']:
                                if len(m) == 0:
                                    m = 180
                                else:
                                    m = sym.sympify(m)
                                    if i == 1:
                                        m += 180
                                        if m  >= 360:
                                            m -= 360
                                DA[j+'ⓝ'] = m
                            else:
                                cc = 0
                                print('Ok, ricominciamo.')
            elif i in [2]:#Pantografo(/Tecnigrafo)
                for j in vin[i]:
                    DA[j+'ⓐ'] = 0
            elif i in [3]:#Cerniera
                for j in vin[i]:
                    if len(j) == 4:
                        DA[j+'Ⓝ'],DA[j+'Ⓣ'] = 90,0
                    elif len(j) == 2:
                        DA[j+'ⓝ'],DA[j+'ⓣ'] = 90,0
            elif i in [4]:#Pattino(/Glifo)
                for j in vin[i]:
                    if cc == 1:
                        DA[j+'ⓐ'] = 0
                        print(VIN[i],'in',j+':')
                        m = input('Angolo normale-orizzonte\n')
                        if m.lower() not in ['ricomincia','ripeti']:
                            if len(m) == 0:
                                m = 0
                                if i == 1:
                                    m = 180
                            else:
                                m = sym.sympify(m)
                                if i == 1:
                                    if m  >= 180:
                                        m -= 180
                                    else:
                                        m += 180
                            DA[j+'ⓝ'] = m
                        else:
                            cc = 0
                            print('Ok, ricominciamo.')
            elif i in [5]:#Incastro
                for j in vin[i]:
                    DA[j+'㊈'],DA[j+'㊆'],DA[j+'㊅'] = 90,0,0
            #Legge di Hocke: F = k Δx -> il 'cedimento' della molla è Δx = F/k. Lo inserisco solo nei lavori virtuali. Verifica!
            elif i == 6:#Molle
                for j in vin[i]:
                    if cc == 1:
                        dd = 0
                        print(VIN[i],'in',j+':')
                        if len(j) == 4:
                            if j[0] != j[2]:
                                di = direzione(D[j[0]],D[j[2]])
                                di += 180
                                if di >= 360:
                                    di -= 360
                                DA[j+'ⓔ'] = di
                            else:
                                dd = 1
                        else:
                            dd = 1
                        if dd == 1:
                            m = input('Angolo normale-orizzonte\n')
                            if m.lower() not in ['ricomincia','ripeti']:
                                if len(m) == 0:
                                    m = 180
                                else:
                                    m = sym.sympify(m)
                                    if i == 1:
                                        m += 180
                                        if m  >= 360:
                                            m -= 360
                                DA[j+'ⓔ'] = m
                            else:
                                cc = 0
                                print('Ok, ricominciamo.')
                        m = input('Costante elastica\n')
                        if len(m) == 0:
                            Mol[j] = sym.sympify(k)
                        else:
                            Mol[j] = sym.sympify(m)
    DC = {}
    for i in DA:
        DC[i] = 0
    ln = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    eln = elenca(ln)
    dac = elenca(DA)
    print('Ti sto per mostrare tutti i gradi di vincolo ottenuti, ciascuno dei quali associato ad una lettera.')
    print('Digita le lettere relative a tutti i vincoli che presentano un cedimento, non usare spazi.')
    cc = -1
    for i in DA:
        cc += 1
        print(eln[cc]+')',i,' '*(5-len(i)),'Angolo:',DA[i])
    m = input().lower()
    for i in m:
        print('Cedimento',str(dac[ln[i]])+':')
        mc = input()
        DC[dac[ln[i]]] = sym.sympify(mc)
    return [DA,DC,Mol]

#NEL CASO CINEMATICO NON CONOSCO LINK, PER CUI QUESTA DEF VA MODIFICATA. LA VERSIONE CON Pr ANZICCHE LINK E' SALVATA IN LINEA TERMO-ELASTICA DEEP-DEEP
def chiedimi_i_cedimenti_termici(Link,vin1,D):
    PenAss,PenRel = [],[]
    epa = ''
    for i in vin1:
        if len(i) == 2:
            PenAss.append(i)
            epa += i+', '
        else:
            PenRel.append(i)
    epa = epa[:-2]
    num = len(PenAss)
    T,T2 = {},{}
    print('Vi sono deformazioni di natura termica?')
    risp  = si_o_no()
    if risp == False:
        return [T,T2]
    if num > 0:
        if num == 1:
            print("Vi è un pendolo esterno:",epa+":")
        else:
            print('Vi sono','n',"pendoli esterni:",epa+". Te li mostrerò uno alla volta; per ciascuno di questi:")
        print("digita invio se non vi sono azioni di natura termica su di esso, altrimenti rispondi con la lunghezza del pendolo.")
        for i in PenAss:
            lung = input('Lunghezza '+str(i)+': ')
            if len(lung) > 0:
                if lung == '1':
                    lung = sym.sympify(l)
                else:
                    lung = sym.sympify(lung)
                T2[i] = lung
                #NON CREDO SIA POSSIBILE UN PENDOLO ABBIA DUE T DISTINTE. NON CONSIDERO QUESTA IPOTESI
    for i in PenRel:
        T2[i] = distanza(D[i[0]],D[i[2]])
    if len(PenRel)+len(PenAss) > 0:
        print('Ve ne sono anche al di fuori dei pendoli?')
        risp = si_o_no()
        if risp == False:
            return [T,T2]#NO!! NON PUOI CONOSCERE ALFA E TETA!! AGGIUNGERLE!
    print('Sto per mostrarti tutti i tratti di trave presenti nel tuo sistema ciascuno associato ad una lettera.')
    print('Scrivi, senza spazi, le lettere corrispondenti ai tratti che presentano azioni di natura termica:')
    ln = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    eln = elenca(ln)
    for i in range(len(Link)):
        print(eln[i]+')',Link[i])
    m = input()
    Tra = []
    for i in m:
        Tra.append(Link[ln[i]])
    if len(Tra) != 0:
        print('Vi è un unico valore Θ>0 di temperatura?')
        risp = si_o_no()
        if risp == True:
            for i in Tra:
                T[i] = [t1,t1,h]
        else:
            print('Per ognuno dei tratti che ti indicherò, indicami il valore della temperatura (uniforme) della trave')
            print('Se la trave separa due ambienti(?) a temperatura uniforme ma diversa, indicami i valori delle due temperature (senza spazi) nella stessa risposta.')
            print('La convenzione per la risposta è la seguente: t1,t2,t3 nel caso di tempratura singola e titj (con i,j in 1,2,3 e i!=j) nel caso di due temperature distinte.')
            for i in Tra:
                cc = 1
                risp = input(str(i)+': ')
                while risp not in ['t1','t2','t3','t1t2','t2t3','t1t3']:
                    print('La risposta deve essere una fra: t1,t2,t3,t1t2,t2t3,t1t3')
                    print('Rispondi di nuovo')
                    risp = input()
                if len(risp) == 2:
                    r = sym.sympify(risp)
                    T[i] = [r,r,h]
                else:
                    r1,r2 = sym.sympify(risp),sym.sympify(risp)
                    T[i] = [r1,r1,h]
            '''
            #controlla se T[i][0] != T[i][1] per ogni i
            print("Sto supponendo tutte le travi abbiano o stesso spessore h.")
            print('Se è corretto premi invio, senno digita qualsiasi altra cosa.')
            risp = input()
            if len(risp) != 0:
                print('NON LO SCRIVO PERCHE TANTO NON è MAI CAPITATO. Al massimo cambia a mano, i simboli sono gia pronti.(h1,h2,h3)')
            STESSO DISCORSO PER ALFA
            '''
    return [T,T2]


###AAA: UNA FORZA PUO ESSERE APPLICATA A META' DI UN ASTA. COME SCRITTO SOTTO QUESTA IPOTESI VIENE CONSIDERATA SOLO IN AZIONI_DISTRIBUITE (che fra l'altro ora come ora non è funzionante).
###quindi: AGGIORNAMI!! (fallo come ultima cosa, dopo l'ultimo passaggio completato correttamente!)
#Puo invece convenire inserire in fra i punti quelli di applicazione di tali forze cosi queste agiscano sempre agli estremi.
#In questo modo si semplifica notevolmente la programmazione delle parti finali ma nello stampare gli stati di sollecitazione considera qualche trave di troppo (non è errore, ma non è un ragionamento 'umano')
def chiedimi_le_azioni_concentrate():#migliorabile ma funzionante
    Papp   = []
    print('Vi sono azioni esterne "concentrate"?')#
    risp = si_o_no()
    if risp == True:
        AzioniX = []
        AzioniY = []
        AzioniM = []
        PappX   = {}#PuntoX -> ValoreX
        PappY   = {}
        PappM   = {}
        print('Rispondi alle seguenti domande, premi invio per passare alla domanda successiva.')
        print('Rispondi, alla prima domanda, indicando il punto e non le coordinate dello stesso.')
        print('Rispondi, alla seconda domanda, rispettando le maiuscole!')
        print('Ti chiederò, prima le forze, prima tutte quelle lungo le X e poi tutte quelle lungo le Y, e dopo i momenti.')
        print('Scrivi correttamente i segni, ricorda che un momento è positivo se il suo verso è antiorario')
        cc = 0
        while cc == 0:
            m1 = input('Punto di applicazione azione esterna direzione X n.'+str(len(AzioniX)+1)+':\n').upper()
            if m1 == '':
                cc = 1
            else:
                AzioniX.append(m1)
                m2 = input('Valore:\n')
                #while m2[-1] not in ['F','T','N','p']:#
                    #print("L'ultimo carattere della risposta deve appartenere a:",['F','T','N','p'],". Ripeti")#
                    #m2 = input().upper()
                PappX[m1] = sym.sympify(m2)
        cc = 0
        while cc == 0:
            m1 = input('Punto di applicazione azione esterna direzione Y n.'+str(len(AzioniY)+1)+':\n').upper()
            if m1 == '':
                cc = 1
            else:
                AzioniY.append(m1)
                m2 = input('Valore:\n')
                #while m2[-1] not in['F','T','N','p']:
                    #print("L'ultimo carattere della risposta deve appartenere a:",['F','T','N','p'],". Ripeti")
                    #m2 = input().upper()
                PappY[m1] = sym.sympify(m2)
        cc = 0
        while cc == 0:
            m1 = input('Punto di applicazione momento esterno n.'+str(len(AzioniM)+1)+':\n').upper()
            if m1 == '':
                cc = 1
            else:
                AzioniM.append(m1)
                m2 = input('Valore:\n')
                PappM[m1] = sym.sympify(m2)
        Papp   = [PappX,PappY,PappM]
    return Papp

def chiedimi_le_azioni_distribuite():
    DPapp = {}
    ADP  = {}  
    print('Vi sono azioni esterne "distribuite"?')
    risp = si_o_no()
    if risp == True:
        DPappX = {}
        DPappY = {}
        print('Rispondi alle seguenti domande, premi invio per passare alla domanda successiva.')
        print('Se un azione distribuita riguarda più corpi, dividila fra essi come fossero più azioni distribuite.')
        print('Quando ti chiedo i punti rispondi elencando ordinatamente (senza spazi nè numeri) tutti i punti che riguardano quella specifica azione distribuita')
        cc = 0
        while cc == 0:
            m1 = input('Punti X: azione n.'+str(len(DPappX)+1)+'\n').upper()
            if m1 == '':
                cc = 1
            else:
                mm1 = input('Valore iniziale:  ')
                mm2 = input('Valore finale:    ')
                DPappX[m1[0]+m1[-1]] = [sym.sympify(mm1),sym.sympify(mm2)]
                ADP[m1[0]+m1[-1]] = m1
        while cc == 1:
            m1 = input('Punti Y: azione n.'+str(len(DPappY)+1)+'\n').upper()
            if m1 == '':
                cc = 0
            else:
                mm1 = input('Valore iniziale:  ')
                mm2 = input('Valore finale:    ')
                DPappY[m1[0]+m1[-1]] = [sym.sympify(mm1),sym.sympify(mm2)]
                ADP[m1[0]+m1[-1]] = m1
        DPapp   = [DPappX,DPappY]
    return [DPapp,ADP]

def chiedimi_le_sostituzioni():
    Sub = {}
    print('Fra i dati è indicata una qualche relazione fra alcuni prametri?')
    risp = si_o_no()
    if risp == True:
        print('Esplicita un parametro dalla relazione indicata, indicami prima quel parametro e poi a cosa è uguale:')
        print('Quando hai finito di indicarmi le relazioni, digita invio per andare avanti.')
        c = ' '
        while len(c) != 0:
            c = input('Parametro: ')
            if len(c) != 0:
                r = input('Valore in funzione degli altri parametri: ')
                Sub[sym.sympify(c)] = sym.nsimplify(sym.sympify(r))
    return Sub

def chiedimi_le_rigidezze(L):#Aggiustare:
    ACB = {}
    for i in L:
        ACB[i[1]+i[0]], ACB[i] = [0,0,B], [0,0,B]
    print("Mi serve conoscere le rigidezze a flessione (B), scorrimento angolare (C), allungamento (A).")
    print("In genere l'unico termine non trascurabile nell'ipotesi dei lavori virtuali è B.")
    print("Se in questo caso, come di solito avviente, ti interessa conoscere solo B (che è uniforme), digita invio.")
    m = input()
    if len(m) == 0:
        return ACB
    #print('Il tuo sistema è costituito dalle seguenti travi:\n',L)
    print("Mi serve conoscere le rigidezze delle varie travi.")
    print("In generale valgono le seguenti considerazioni:")
    print('B) La rigidezza a flessione B è omogenea e uguale per ogni trave e porta contributi non trascurabili.')
    print('C) La rigidezza allo scorrimento angolare C -> ∞ nel caso di trave snella (ipotesi di Eulero-Bernoulli), ovvero se la lunghezza ha dimensione prevalente rispetto quelle della sezione.')
    print("A) La rigidezza assiale all'allungamento A porta anch'essa contributo nullo se le azioni esterne sono esclusivamente trasversali.")
    print("Così facendo nell'ipotesi dei lavori virtuali solo i termini con B danno un contributo non nullo.")
    print("Nell'esercizio in questione valgono queste considerazioni?")
    risp = si_o_no()
    if risp == False:
        print('Queste sono le travi presenti nel tuo sistema:\n',L)
        print('Quali di queste hanno A non trascurabile?')
    return ACB
###################################################################################################
###################################################################################################
#FUNZIONE PREPARA(n), ove n = numero corpi
#migliorabile con revisione dei dati
#Attenzione: esame: 12/04/13 Link,L,.. danno un asta di troppo
#Attenzione: esame: 28/10/11, es.n.: 1; AD è un pendolo (interno) e non una trave... se non te ne accorgi puoi creare una funz. di controllo input...
def prepara(n):
    #'''
    stampa = [True,False][1]
    
    Pr = chiedimi_i_punti(n)
    if stampa == True:
        print('    Pr  =',Pr,'\n')
    Di = chiedimi_le_coordinate(Pr)
    D = AggiornaDizionario(Di,Pr)
    if stampa == True:
        print('    Pr  =',Pr)
        print('    D   =',D,'\n')
    Relazioni = chiedimi_i_collegamenti(Pr)
    Collegamenti = sistema_relazioni(Relazioni,Pr)
    Link = sistema_collegamenti(Collegamenti)
    L = Sistema_Link(Link,Pr)
    if stampa == True:
        print('    Pr   =',Pr)
        print('    D    =',D)
        print('    Link =',Link,)
        print('    L    =',L,'\n')
    vin = chiedimi_i_vincoli()#numero?
    if stampa == True:
        print('    Pr   =',Pr)
        print('    D    =',D)
        print('    Link =',Link,)
        print('    L    =',L)
        print('    vin  =',vin)
    #'''
    #Qua a volte ci inceppa...

    DAC = chiedimi_angoli_e_cedimenti(vin,Pr,D)
    DA,DC,Mol = DAC[0],DAC[1],DAC[2]
    if stampa == True:
        print('    Pr   =',Pr)
        print('    D    =',D)   
        print('    Link =',Link)
        print('    L    =',L)
        print('    vin  =',vin)
        print('    DA   =',DA)
        print('    DC   =',DC)
        print('    Mol  =',Mol,'\n')
    TT2 = chiedimi_i_cedimenti_termici(elenca(Link),vin[1],D)
    CT,CT2 = TT2[0],TT2[1]
    if stampa == True:
        print('    Pr   =',Pr)
        print('    D    =',D)
        print('    Link =',Link)
        print('    L    =',L)
        print('    vin  =',vin)
        print('    DA   =',DA)
        print('    DC   =',DC)
        print('    Mol  =',Mol)
        print('    CT   =',CT)
        print('    CT2  =',CT2,'\n')
    AC = chiedimi_le_azioni_concentrate()
    if stampa == True:
        print('    Pr   =',Pr)
        print('    D    =',D)
        print('    Link =',Link)
        print('    L    =',L)
        print('    vin  =',vin)
        print('    DA   =',DA)
        print('    DC   =',DC)
        print('    Mol  =',Mol)
        print('    CT   =',CT)
        print('    CT2  =',CT2)
        print('    AC   =',AC,'\n')
    ad = chiedimi_le_azioni_distribuite()
    AD, ADP = [ad[0],ad[1]]
    if stampa == True:
        print('    Pr   =',Pr)
        print('    D    =',D)
        print('    Link =',Link)
        print('    L    =',L)
        print('    vin  =',vin)
        print('    DA   =',DA)
        print('    DC   =',DC)
        print('    Mol  =',Mol)
        print('    CT   =',CT)
        print('    CT2  =',CT2)
        print('    AC   =',AC)
        print('    AD   =',AD)
        print('    ADP  =',ADP,'\n')
    ACB = chiedimi_le_rigidezze(elenca(Link))
    if stampa == True:
        print('    Pr   =',Pr)
        print('    D    =',D)
        print('    Link =',Link)
        print('    L    =',L)
        print('    vin  =',vin)
        print('    DA   =',DA)
        print('    DC   =',DC)
        print('    Mol  =',Mol)
        print('    CT   =',CT)
        print('    CT2  =',CT2)
        print('    AC   =',AC)
        print('    AD   =',AD)
        print('    ADP  =',ADP)
        print('    ACB  =',ACB,'\n')
    Sub = chiedimi_le_sostituzioni()    
    #[Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
    color.write('\n\nDati da inserire come input nel programma:\n')
    print('Pr  =',Pr)
    print('vin =',vin)
    print('DA  =',DA)
    print('DC  =',DC)
    print('L   =',L)
    print('AC  =',AC)
    print('AD  =',AD)
    print('ADP =',ADP)
    print('Mol =',Mol)
    print('CT  =',CT)
    print('CT2 =',CT2)
    print('Sub =',Sub)
    print('ACB =',ACB)
    print('D   =',D)
    print('SC  =',-1)
    print('AZC =',"'?'")	

#prepara(1)
#prepara(2)
#prepara(3)
#numerocorpi = 
#prepara(numerocorpi)
###################################################################################################
#FUNZIONI USATE PER LA CINEMATICA E CHE CI RIGIOCHIAMO PER LA LINEA TERMO-ELASTICA:
'''Associa ad ogni punto del corpo la relativa velocità funzione dei parametri lagrangiani scelti arbitrariamente'''
def DizionarioVelocità(P,D):
    n = len(P)
    punti = elenca(P)
    Lag = []
    for i in P:
        Lag.append(i[0])
    #creazione simboli: parametri lagrangiani (qi)
    q = []
    for i in range(3*n):
        q.append(sym.sympify(sym.symbols('q'+str(i+1))))
    #creazione di 2 liste dei punti preceduti da V e θ
    Vpunti, θpunti = [], []
    for i in punti:
        Vpunti.append('V'+str(i))
        θpunti.append('θ'+str(i))
    for i in Lag:
        if i not in punti:
            Vpunti.append('V'+str(i))
            θpunti.append('θ'+str(i))
    #Inizio creazione LagraDizio: come DizionarioVelocità, ma separa le velocità traslazioni da quelle angolari in base alla lettera precedente il punto (V o θ) e non assegna le velocità angolari ai punti che non sono poli
    LagraDizio = {}
    DizionarioVelocità = {}
    #Velocità dei punti scelti come poli
    k = -1
    for i in range(len(Lag)):
        k += 1
        poV = 'V'+str(Lag[i])
        poθ = 'θ'+str(Lag[i])
        posV = Vpunti.index(poV)
        posθ = θpunti.index(poθ)
        LagraDizio[Vpunti[posV]] = [q[k],q[k+1],0]
        LagraDizio[θpunti[posθ]] = [0,0,q[k+2]]
        k += 2
    #Velocità dei punti rimanenti
    distanza = {}
    for i in range(len(P)):
        for j in range(len(P[i])):
            if P[i][j] not in Lag:
                dist = sottrazione(D[P[i][j]],D[Lag[i]])
                distanza[str(D[P[i][j]])+str(D[Lag[i]])] = dist
                poV  = LagraDizio['V'+str(Lag[i])]
                poθ  = LagraDizio['θ'+str(Lag[i])]
                Vpu  = 'V'+str(P[i][j])
                LagraDizio[Vpu] = somma(poV,prodottovettoriale(poθ,dist))                
    #stampo tutte le velocità dei punti (meno di quelli 'lagrangiani'):
    for i in range(len(P)):
        for j in range(len(P[i])):
            if P[i][j] not in Lag:
                poV  = 'V'+str(Lag[i])
                poθ  = 'θ'+str(Lag[i])
                Vpu  = 'V'+str(P[i][j])
    #creazione DizionarioVelocità (output)   
    DizionarioVelocità = {}
    for i in LagraDizio:
        if i[0] == 'V':
            DizionarioVelocità[i[1:]] = [0,0,0]
    for i in LagraDizio:
        if i[0] == 'V':
            DizionarioVelocità[i[1:]] = somma(DizionarioVelocità[i[1:]],LagraDizio[i])
    for i in DizionarioVelocità:
        j = int(i[-1])-1
        DizionarioVelocità[i] = somma(DizionarioVelocità[i],LagraDizio['θ'+Lag[j]])
    return [DizionarioVelocità,LagraDizio]

def Stampa_DizionarioVelocità(P,D):
    n = len(P)
    punti = elenca(P)
    Lag = []
    for i in P:
        Lag.append(i[0])
    q = []
    for i in range(3*n):
        q.append(sym.sympify(sym.symbols('q'+str(i+1))))
    Vpunti, θpunti = [], []
    for i in punti:
        Vpunti.append('V'+str(i))
        θpunti.append('θ'+str(i))
    for i in Lag:
        if i not in punti:
            Vpunti.append('V'+str(i))
            θpunti.append('θ'+str(i))            
    LagraDizio = {}
    a,b,c,d,e = 'Rosso','Nero','Blu','Viola','Arancione'
    color.write('Parametri lagrangiani scelti e velocità associata:\n')
    k = -1
    for i in range(len(Lag)):
        k += 1
        #V(A1) = q1e1 + q2e2
        color.write('V(',colori[e])
        color.write(str(Lag[i]),colori[b])
        color.write(')'+' '*(2-len(str(Lag[i]))),colori[e])
        color.write(' = ',colori[c])
        color.write(str(q[k]),colori[c])
        color.write('e1',colori[d])
        color.write(' + ',colori[c])
        color.write(str(q[k+1]),colori[c])
        color.write('e2\n',colori[d])
        #Θ(A1) = q3e3
        color.write('Θ(',colori[e])
        color.write(str(Lag[i]),colori[b])
        color.write(')'+' '*(2-len(str(Lag[i]))),colori[e])
        color.write(' = ',colori[c])
        color.write(str(q[k+2]),colori[c])
        color.write('e3\n\n',colori[d])
        poV = 'V'+str(Lag[i])
        poθ = 'θ'+str(Lag[i])
        posV = Vpunti.index(poV)
        posθ = θpunti.index(poθ)
        LagraDizio[Vpunti[posV]] = [q[k],q[k+1],0]
        LagraDizio[θpunti[posθ]] = [0,0,q[k+2]]
        k += 2
    distanza = {}
    for i in range(len(P)):
        for j in range(len(P[i])):
            if P[i][j] not in Lag:
                dist = sottrazione(D[P[i][j]],D[Lag[i]])
                distanza[str(D[P[i][j]])+str(D[Lag[i]])] = dist
                poV  = LagraDizio['V'+str(Lag[i])]
                poθ  = LagraDizio['θ'+str(Lag[i])]
                Vpu  = 'V'+str(P[i][j])
                LagraDizio[Vpu] = somma(poV,prodottovettoriale(poθ,dist))                
    color.write('Velocità degli altri punti del corpo:\n')
    for i in range(len(P)):
        for j in range(len(P[i])):
            if P[i][j] not in Lag:
                #a,b,c,d,e = 'Rosso','Nero','Blu','Viola','Arancione'
                poV  = 'V'+str(Lag[i])
                poθ  = 'θ'+str(Lag[i])
                Vpu  = 'V'+str(P[i][j])
                #V(B1) = V(A1)+ θ(A1) x A1B1
                color.write('V(',colori[a])
                color.write(str(P[i][j]),colori[b])
                color.write(')'+' '*(2-len(str(P[i][j]))),colori[a])
                color.write(' = ',colori[c])
                color.write('V(',colori[c])
                color.write(str(Lag[i]),colori[c])
                color.write(')'+' '*(2-len(str(Lag[i]))),colori[c])
                color.write('  + ',colori[c])
                color.write('θ(',colori[c])
                color.write(str(Lag[i]),colori[c])
                color.write(')'+' '*(2-len(str(Lag[i]))),colori[c])
                color.write(' x ',colori[c])
                color.write(str(Lag[i])+str(P[i][j])+'\n',colori[c])
                #V(B1) = (q1)e1 + (q2)e2 + {(q3)e3 x [(-l)e2]}
                color.write('V(',colori[a])
                color.write(str(P[i][j]),colori[b])
                color.write(')'+' '*(2-len(str(P[i][j]))),colori[a])
                color.write(' = ',colori[c])
                sstampavettore(LagraDizio[poV])
                color.write(' + {',colori[c])
                sstampavettore(LagraDizio[poθ])
                color.write(' x [',colori[c])
                sstampavettore(distanza[str(D[P[i][j]])+str(D[Lag[i]])])
                color.write(']}\n',colori[c])
                #V(B1) = (l*q3 + q1)e1 + (q2)e2
                color.write('V(',colori[a])
                color.write(str(P[i][j]),colori[b])
                color.write(')'+' '*(2-len(str(P[i][j]))),colori[a])
                color.write(' = ',colori[c])
                sstampavettore(LagraDizio[Vpu])
                print('\n')
                
#Convenzione: nel caso di un 'nodo', assegno l'eq. di vincolo esterno al punto appartenente al corpo con numero identificativo minore (arbitrario)
def MatriceCinematica(DV,DA):
    vincoli = elenca(DA)
    punti   = elenca(DV)
    #cerco l'eventuale "nodo 'dichiarato'"  senza scomodare P
    #nodi[punto] -> numero identificatico minore fra quelli dei corpi che hanno in comune quel punto (scelta arbitraria)
    nodi = {}
    for i in vincoli:
        if len(i) == 2:
            if i[0] not in nodi:
                nodi[i[0]] = -10
    for i in nodi:
        for j in vincoli:
            if len(j) == 5 and j[0] == i:
                s = spezza(j[:-1])
                for k in s:
                    if -int(k[1]) > nodi[i]:
                        nodi[i] = int(k[1])
    for i in nodi:
        nodi[i] = str(nodi[i])
    #sistemo DV nel caso in cui vi sia un vincolo relativo riguardante un nodo (es: A0B2)
    #lo generalizzo tramite spezza che non so come modificherò i nodi non dichiarati in futuro
    DNR = {}
    for i in DA:
        s = spezza(i)
        for j in s:
            if j[1] == '0':
                DNR[j[0]] = []
    for i in DV:
        if i[0] in DNR:
            DNR[i[0]].append(i[1])
    for i in DNR:
        DNR[i].sort()
        DNR[i] = DNR[i][0]
    NR = []
    for i in DNR:
        NR.append(i+DNR[i])
    for i in copy.deepcopy(DV):
        if i in NR:
            DV[i[0]+'0'] = DV[i]
    #Calcolo matrice cinematica in forma di lista -> Al
    Al = []
    C  = []
    for i in vincoli:
        s = spezza(i[:-1])
        e = i[-1]
        if e in ['ⓝ','ⓣ','ⓔ','Ⓝ','Ⓣ','㊈','㊆']:
            if len(s) == 1:
                j = s[0]
                if len(j) == 1:
                    vi = j + nodi[j]
                    ci = j + e
                else:
                    vi =  j
                    ci =  j + e
                ve = DV[vi]
                ve = prodottorigacolonna(ve,[1,1,0])
                co = [sym.cos(rad(DA[ci])).evalf(5),sym.sin(rad(DA[ci])).evalf(5),0]
                eq = prodottoscalare(ve,co).evalf(5)
                Al.append([eq])
            else:
                ve = sottrazione(DV[s[0]],DV[s[1]])
                ve = prodottorigacolonna(ve,[1,1,0])
                co = [sym.cos(rad(DA[i])).evalf(5),sym.sin(rad(DA[i])).evalf(5),0]
                eq = prodottoscalare(ve,co).evalf(5)
                Al.append([eq])
        elif e in ['ⓐ','㊅']:
            if len(s) == 1:
                j = s[0]
                if len(j) == 1:
                    eq = prodottoscalare(DV[j+nodi[j]],[0,0,1])
                    Al.append([eq])
                else:
                    eq = prodottoscalare(DV[j],[0,0,1])
                    Al.append([eq])
            else:
                eq = prodottoscalare(sottrazione(DV[s[0]],DV[s[1]]),[0,0,1])
                Al.append([eq])
    #Scrittura di A in forma matriciale -> Am -> gli tolgo cioè i parametri lagrangiani
    #alcune delle parti che seguono (quelle di pulizia), funzionano solo se qi è scritto come ultimo termine, dopo numeri e lunghezze varie! 
    #creo Am vuota dopo avere ricavato il numero di parametri lagrangiani = 3*n
    n = 0
    for i in punti:
        if int(i[-1]) > n:
            n = int(i[-1])
    Am = []
    for i in range(len(Al)):
        F = []
        for j in range(3*n):
            F.append(0)
        Am.append(F)
    #porto Al dentro Am
    dd = -1
    for i in Al:
        dd += 1
        i = str(i)[1:-1]
        qq = i.count('q')
        ee = -1
        u = i
        for j in range(qq):
            ee += 1
            cc  = 0
            indice = u.index('q')
            t = int(u[indice+1])-1
            Am[dd][t] = sym.sympify(u[:indice+2])
            u = u[indice+3:]
    #Approssimo ogni termine di Am (alla 5a cifra decimale)
    for i in range(len(Am)):
        for j in range(len(Am[i])):
            if Am[i][j] != 0:
                Am[i][j] = Am[i][j]#.evalf(5)
    #creo la forma finale di A, senza parametri lagrangiani 
    A = []
    for i in range(len(Am)):
        M = []
        for j in range(len(Am[i])):
            M.append(Am[i][j])
        A.append(M)
    for i in range(len(Am)):
        for j in range(len(Am[i])):
            if str(Am[i][j]) == '0':
                A[i][j] = '0'
            else:
                if len(str(Am[i][j]).strip()) == 2:
                    A[i][j] = 1
                elif len(str(Am[i][j]).strip()) == 3:
                    A[i][j] = -1
                else:
                    A[i][j] = (str(Am[i][j])[:-3])###########
    #RiSymmo A -> penso qualche parte appena sopra sia fatta per le lunghe ma di base sticazzi.
    for i in range(len(A)):
        for j in range(len(A[i])):
            if Am[i][j] != 0:
                A[i][j] = sym.sympify(A[i][j]).evalf(5)
            else:
                A[i][j] = sym.sympify(A[i][j]).evalf(1)
    return A

#Cerco di capire se vi possano essere bug nella m.c. A
def controlla_righe_identiche(A,DA):
    M = copy.deepcopy(A)
    L,W = [],[]
    D = elenca(DA)
    d = {}
    cc,gg = 1, 0
    for i in range(len(A)):
        B = copy.deepcopy(A)
        del B[i]
        if A[i] in B:
            L.append(i)
    if len(L) > 0:
        d = {}
        for i in L:
            d[i] = []
        for i in L:
            for j in range(len(A)):
                if i != j:
                    if A[i] == A[j]:
                        d[i].append(j)
        U = []
        for i in d:
            U.append([])
            U[-1].append(i)
            for j in d[i]:
                U[-1].append(j)
        W = []
        for i in U:
            i.sort()
            if i not in W:
                W.append(i)
        '''
        print()
        color.write(' '*15+'ATTENZIONE:'+' '*17,colori['Warning'])
        print()
        print(' '*10,'Matrice Cinematica:')
        As = stampamatrice(A)
        for t in range(len(As)):
            print(D[t],' '*(7-len(D[t])),As[t])
        '''
        color.write('N.B.: ',colori['RossoAcceso'])
        print("La matrice cinematica contiene equazioni identiche fra loro. Nello specifico:")
        for i in W:
            color.write('Equazione: ',colori['Nero'])
            color.write(str(A[i[0]])+'\n',colori['Blu'])
            for j in i:
                color.write('Vincolo:   ',colori['Viola'])
                color.write(D[j]+" (Riga "+str(j+1)+')\n',colori['Blu'])
        '''
        print('Possono capitare casi (tendenzialmente iperstatici) in cui ciò si verifichi (ad es: doppio incastro esterno allo stesso corpo), ma sono rari.')
        print("Proseguo ugualemente l'esercizio, ma assicurati che sia corretto questo risultato, guardando il sistema in esame ed eventualmente l'input inserito.\n")
        '''
        print('Ciò implica che almeno uno dei gradi di vincolo relativo le equazioni ripetute andrà rilassato.\n')

def Stampa_Equazioni_di_Vincolo_Omogenea(A,DA):
    vincoli = elenca(DA)
    v = len(vincoli)
    q = []
    for i in range(len(A[0])):
        q.append(sym.sympify(sym.symbols('q'+str(i+1))))
    B = []
    for i in A:
        B.append(prodottoscalare(i,q))
    color.write("\nEquazioni imposte dai vincoli nell'omogenea associata:\n")
    for i in range(v):
        print(vincoli[i]+':  '+' '*(5-len(vincoli[i])),'{',B[i],'= 0')

def Stampa_MatriceCinematica(A,DA):
    De = []
    for i in DA:
        De.append(i)
    As = stampamatrice(A)
    color.write('\nMatrice Cinematica:\n')
    for i in range(len(As)):
        j = sta(As[i])
        colorwrite(De[i]+': '+' '*(5-len(De[i]))+j+'\n','Blu')
        print()
        
def AssegnaCedimentiTermici(DCi,CT2):
    ect = elenca(CT2)
    if len(ect) > 0:
        DC = {}
        aa = elenca(DCi)
        cc = -1
        for i in DCi:
            DC[i] = DCi[i]
            if i[:-1] in CT2:
                if i[-1] in ['ⓝ','Ⓝ']:
                    DC[i] += CT2[i[:-1]]
        return DC
    else:
        return DCi

def Stampa_AssegnaCedimentiTermici(DCi,CT2):
    ect = elenca(CT2)
    eec = ''
    for i in ect:
        eec += i+', '
    eec = eec[:-2]
    if len(ect) > 0:
        color.write('AGGIORNAMENTO CEDIMENTI:\n',colori['Arancione'])
        aa = elenca(DCi)
        print('Prima di iniziare lo svolgimento è bene fare una considerazione:')
        l1,l2,l3,l4,l5,l6,l7,l8,l9 = '','i',' una','e','a','è','','un','o'
        if len(ect) > 1:
            l1,l2,l3,l4,l5,l6,l7,l8,l9 = 'l','o','no','i','e','sono','d','dei','i'
        print('i'+l1,'vincol'+l2,eec,'presenta'+l3,'deformazion'+l4,'di natura termica;')
        print('quest'+l5,l6,'assimilabil'+l4,'a'+l7,l8,'cediment'+l9)
        print('Si ha pertanto che:')
        cc = -1
        for i in DCi:
            cc += 1
            if i[:-1] in CT2:
                if i[-1] in ['ⓝ','Ⓝ']:
                    color.write('Cedimento'+' '*(5-len(i))+' '+str(i)+': ')
                    print(DCi[i],'-->',DCi[i]+CT2[i[:-1]])
        print()

###################################################################################################
###################################################################################################
#FUNZIONI PER LINEATERMOELASTICA():
def Stampa_classifica_gradi_di_libertà(n):
    print('Confrontiamo gradi di libertà e di vincolo per farci una prima idea della possibile classificazione cinematica e statica del sistema in esame:\n')
    color.write('Gradi di libertà:\n')
    if n == 1:
        print('Il sistema è composto da un solo corpo posto in uno spazio ambiente bidimensionale.')
    else:
        print('Il sistema è composto da',n,'corpi posti in uno spazio ambiente bidimensionale.')
    print('Numero gradi di libertà: 3x'+str(n),'=',3*n)

def Stampa_classifica_vincoli(vin,Pr):
    color.write('Gradi di vincolo:\n')
    n = len(Pr)
    V = numeravincoli(vin,Pr)
    elenco = elenca(V)
    if n == 1:
        print('Il corpo presenta',len(elenco),'dispositivi di vincolo che erogano in totale',len(elenca(semplificavincoli(V,Pr))),'condizioni di vincolo.')
    else:
        Vinterni = 0
        Vesterni = 0
        Vint_est = 0
        for i in elenco:
            if len(i) == 1:
                Vint_est += 1
            elif len(i) == 2:
                Vinterni += 1
            else:
                Vesterni += 1
        V = riducinodi(V,Pr)
        V = semplificavincoli(V,Pr)
        V = elenca(V)
        ve,vi,vie = [],[],[]
        for i in V:
            if len(i) == 2:
                vie.append(i)
            elif len(i) == 3:
                ve.append(i)
            else:
                vi.append(i)
        GVI = 0
        GVE = 0
        for i in V:
            if len(i) in [2,3]:
                GVE += 1
            else:
                GVI += 1
        vee,vii,vei = '','',''
        for i in ve:
            vee += i+'       '
        for i in vi:
            vii += i+'     '
        for i in vie:
            vei += i+'        '
        '''
        VIN = VIN_()
        VIN[1],VIN[2],VIN[4] = VIN[1][:VIN[1].index('/')],VIN[2][:VIN[2].index('/')],VIN[1][:VIN[4].index('/')]
        #Carrello       Pendolo        Pantografo     Cerniera       Pendolo        Incastro       Molla
        dv = {}
        cc = -1
        V = riducinodi(vin,Pr)
        for i in VIN:
            cc += 1
            dv[i+'i'] = []
            dv[i+'e'] = []
            dv[i+'a'] = []
            for j in V[cc]:
                print(j)
                if len(j) == 1:
                    dv[i+'i'].append(j)
                if len(j) == 2:
                    dv[i+'e'].append(j)
                elif len(j) == 4:
                    dv[i+'a'].append(j)
        for i in dv:
            print(i,dv[i])
        input()
        '''
        color.write('\nVincoli totali:  ',colori['RossoAcceso'])
        color.write(str(Vinterni+Vesterni+Vint_est),colori['Blu'])
        #color.write(' '*22)
        #for i in VIN:
        #    color.write(i+' '*(20-len(i)),colori['Viola'])
        print('\nVincoli interni:',Vinterni)
        print('Vincoli esterni:',Vesterni)
        if Vint_est != 0:
            print('Vincoli sia interni che esterni:',Vint_est)
        color.write('\nGradi di vincolo totali:  ',colori['RossoAcceso'])
        color.write(str(GVI+GVE)+'\n',colori['Blu'])
        color.write('Gradi di vincolo interni: '+str(GVI),colori['Blu'])
        color.write('  -------->  ',colori['Nero'])
        color.write(vii+'\n',colori['Viola'])
        color.write('Gradi di vincolo esterni: '+str(GVE),colori['Blu'])
        color.write('  -------->  ',colori['Nero'])
        color.write(vee+'\n',colori['Viola'])
        if Vint_est != 0:
            color.write('Vincoli sia interni che esterni: '+str(len(vie)),colori['Blu'])
            color.write('  ->  ',colori['Nero'])
            color.write(vei+'\n',colori['Viola'])
        
    
def Stampa_classifica_sistema(LI,GV):
    color.write('\nClassificazione candidata:\n')
    n = LI/3
    if GV > LI:
        print('gradi di vincolo =',GV,'<',LI,'= gradi di libertà')
        print('Il sistema è candidato ad essere iperstatico, ovvero cinematicamente indeterminato e staticamente impossibile.\n')
    elif GV == LI:
        print('gradi di vincolo =',GV,'=',LI,'= gradi di libertà')
        print('Il sistema è candidato ad essere isostatico, ovvero cinematicamente e staticamente univocamente determinato.\n')
    else:
        print('gradi di vincolo =',GV,'>',LI,'= gradi di libertà')
        print('Il sistema è candidato ad essere ipostatico (o labile), ovvero cinematicamente impossibile e staticamente indeterminato.\n')

def rank(A):
    return len(Matrix(A).rref()[1])

def Stampa_Analisi_Rango(A,DA):
    color.write('Rango Matrice Cinematica e classificazione reale:')
    n = len(A[0])/3
    D = elenca(DA)
    v = len(D)
    rid = v - 3*n
    if 3*n == rank(A):##CASO RANK(A) = MAX
        print('\nIl rango della matrice cinematica è massimo;')
        print('vi sono quindi',int(3*n),'gradi di vincolo indipendenti.')
        if rid == 0:
            print('Il sistema è cineticamente e staticamente univocamente determinato.')#guarda 12/01/12
        elif rid > 0:
            lettera = 'a.'
            if rid > 1:
                lettera = 'e.'
            print('Il sistema è cinematicamente impossibile e staticamente indeterminato.')
            print('Presenta',int(rid),'ridondanz'+str(lettera),'\n')
        else:
            print('Il sistema è cinematicamente indeterminato e staticamente impossibile')
            print('essendovi',int(-rid),'conponenti di spostamente non controllate dai vincoli.')
    else:#CASO RANK(A) < MAX
        print('\nIl rango della matrice cinematica non è massimo, pertanto')
        print('il problema cinematico e quello statico sono singolari.')
        print()
        print("L’esistenza di una soluzione dipenderà direttamente")
        print("dalle caratteristiche assunte l’insieme di azioni esterne attive")
        print("rispetto alla configurazione assunta dal sistema all’istante considerato.")
        print()
        print('Il problema cinematico e quello statico risultano quindi intrinsecamente legati, infatti:')
        print('•) Il problema cinematico ammette soluzione solo se')
        print('sono note le condizioni di compatibilià cinematica,')
        print('la cui determinazione è possibile solo se il problema statico è risolvibile.')
        print('•) Il problema statico ammette soluzione solo se')
        print("la potenza spesa dalle azioni esterne sugli atti di modo compatibili")
        print("con i dispositivi di vincolo, pensati fissi all'istante considerato, è nulla.")
    if rid > 0:
        print('Per la determinazione dei diagrammi finali delle azioni di contatto,')
        print('procedo con il metodo delle forze dopo opportuna scelta dei vincoli da rilassare.')
        print('Effetuiamo quindi una preventiva analisi dei dispositivi di vincolo per individuare quali siano effettivamente linearmente dipenendenti.')


#sfrutta le definizioni di 'calcolo combinatorio' scritte ad inizio programma per unire corpi iso/iper-statici internamente a partire dal dizionario dei ranghi dei binomiali(n,2) dei corpi possibili
def Unisci_Corpi(w,n):
    C = []
    for i in copy.deepcopy(w):
        if w[i] < 3:
            del w[i]
    w = elenca(w)
    D = dizionale(n)
    for i in D:
        W = []
        l = len(i)-1
        c = 0
        for j in D[i]:
            if j in w:
                W.append(j)
                c += 1
            if c == l:
                C.append(i)
                for k in W:
                    del w[w.index(k)]
    for i in w:
        C.append(i)
    e = []
    for i in C:
        for j in i:
            if j not in e:
                e.append(j)
    for i in range(1,n+1):
        if str(i) not in e:
            C.append(str(i))
    C.sort()
    return C
    

#Non so se sopra ho considerato il caso del pendolo Zerato (nodo)
def Tipologia_Vincoli_Rilassare(Pr,DA,D):
#N.B.: dà problemi se ci sono piu di 9 corpi (non importante a meno che non intendi svolgere un traliccio come un termoelastico)
    n,v = len(Pr),elenca(DA)
    #RICONOSCIMENTO CORPI INTERNAMENTE ISOSTATICI
    vi = []
    for i in v:
        if len(i) == 5:
            vi.append(i)
    w = {}
    c  = binomiale_2(n)
    for i in c:
        u = {}
        u[i] = []
        for j in vi:
            if i[0] == j[1]:
                if i[1] == j[3]:
                    u[i].append(j)
        e = []
        for j in u:
            for h in u[j]:
                if h[0]+h[1] not in e:
                    e.append(h[0]+h[1])
                if h[2]+h[3] not in e:
                    e.append(h[2]+h[3])
        DV = DizionarioVelocità(P_(Pr),D)[0]
        dv = {}
        da = {}
        for j in u:
            for h in u[j]:
                if h in DA:
                    da[h] = DA[h]
        for j in u:
            for h in u[j]:
                if h[0]+h[1] in DV:
                    dv[h[0]+h[1]] = DV[h[0]+h[1]]
                if h[2]+h[3] in DV:
                    dv[h[2]+h[3]] = DV[h[2]+h[3]]    
        A = MatriceCinematica(dv,da)
        for i in u:
            w[i] = rank(A)
    b = Unisci_Corpi(w,n)
    #VINCOLI INTERNI:
    di  = {}
    din = {}
    #Gradi di vincolo interno e rango dei corpi che si comportano come ne fossero un unico
    for i in b:
        if len(i) > 1:
            dd = []
            for j in i:
                dd.append(j)
            vi2 = []
            for j in vi:
                if j[1] in dd:
                    if j[3] in dd:
                        vi2.append(j)
            #Forse la prima parte di quanto segue è un passaggio di verifica della corretteza della parte soprastante. Se cosi fosse puoi eliminare questa sottoparte dal seguito, bug non ce ne dovrebbero essere più :)
            DE = {}
            for r in vi2:
                DE[r] = DA[r]
            lista = []
            for r in vi2:
                if r[0:2] not in lista:
                    lista.append(r[0:2])
                if r[2:-1] not in lista:
                    lista.append(r[2:-1])
            DV = DizionarioVelocità(P_(Pr),D)[0]
            DEV = {}
            for r in DV:
                if r in lista:
                    DEV[r] = DV[r]
            ddi = rank(MatriceCinematica(DEV,DE))
            di[i]  = ddi
            din[i] = len(vi2)
            #Verifico l'assenza bug
            if ddi != (len(i)-1)*3:
                color.write('ATTENZIONE: rank(Aint)_corpi_'+str(i)+' != 3*(numero_corpi - 1)!\n',colori['Errore'])
    #N.B.: Da ora in avanti, in questa def, corpi internamente isostatici verranno considerati come un corpo unico
    #Gradi di vincolo interno e rango fra corpi distinti
    c = binomiale_2(b)
    for i in b:
        for f in c:
            din[f] = 0
            u = {}
            u[i] = []
            for j in vi:
                if f[0] == j[1]:
                    if f[1] == j[3]:
                        u[i].append(j)
                        din[f] += 1
            e = []
            for j in u:
                for h in u[j]:
                    if h[0]+h[1] not in e:
                        e.append(h[0]+h[1])
                    if h[2]+h[3] not in e:
                        e.append(h[2]+h[3])
            dv = {}
            da = {}
            for j in u:
                for h in u[j]:
                    if h in DA:
                        da[h] = DA[h]
            for j in u:
                for h in u[j]:
                    if h[0]+h[1] in DV:
                        dv[h[0]+h[1]] = DV[h[0]+h[1]]
                    if h[2]+h[3] in DV:
                        dv[h[2]+h[3]] = DV[h[2]+h[3]]    
            A = MatriceCinematica(dv,da)
            for i in u:
                di[f] = rank(A)
    #VINCOLI ESTERNI
    ve = []
    vv = []
    for i in v:
        if len(i) <= 3:
            ve.append(i)
            vv.append(i)
    #sistemo, ahimè, cose inerenti i nodi (credo)
    ca = {}
    for i in vv:
        if len(i) == 2:
            ca[i] = []
            del ve[ve.index(i)]
            for p in Pu_(Pr):
                if i[0] in p:
                    ca[i].append(i[0]+str(Pu_(Pr).index(p)+1)+i[1])
    co = {}
    for i in ca:
        co[i] = []
        for j in ca[i]:
            co[i].append(j[1])
    for i in b:
        if len(i) > 1:
            e = []
            for j in i:
                e.append(j)
            for j in ca:
                gg = 1
                for h in ca[j]:
                    for t in e:
                        if t not in co[j]:
                            gg = 0
                if gg == 1:
                    a = e[0]
                    for h in ca[j]:
                        if h[1] == a:
                            ve.append(h)
        else:
            for j in ca:
                for h in ca[j]:
                    if h[1] == i:
                        ve.append(h)
    u  = {}
    for i in b :
        u[i] = []
        for j in i:
            for h in ve:
                if h[1] == j:
                    u[i].append(h)
    u2 = copy.deepcopy(u)
    for i in ca:
        for j in ca[i]:
            for h in u2:
                for t in u2[h]:
                    if t == j:
                        elenco = []
                        for q in u[h]:
                            if q == t:
                                elenco.append(i)
                            else:
                                elenco.append(q)
                        u[h] = elenco
    #Riscrivo Pr e D (e 'u' e DA). Ora infatti posso avere qualche corpo in meno e mi serve dare in pasto a DV il 'nuovo' sistema
    #P -> Pi
    P = P_(Pr)
    P2 = []
    e = []
    for i in b:
        e.append(i)
    for i in e:
        P2.append([])
        for j in i:
            for k in P[int(j)-1]:
                P2[-1].append(k)
    lista = []
    doppi = []
    for i in range(len(P2)):
        lista.append([])
        doppi.append([])
        for j in P2[i]:
            if j[0] not in lista[-1]:
                lista[-1].append(j[0])
            else:
                doppi[-1].append(j)
    Pi = []
    cc = 0
    for i in P2:
        cc += 1
        Pi.append([])
        for j in i:
            if j not in doppi[cc-1]:
                Pi[-1].append(j[0]+str(cc))
    #D -> Di
    Di = {}
    Di2 = {}
    for i in D:
        if len(i) == 1:
            Di2[i] = D[i]
            Di[i]  = D[i]
    for i in range(len(Pi)):
        for j in Di2:
            Di[j+str(i+1)] = Di2[j]
    da = {}
    for j in u:
        for h in u[j]:
            if h in DA:
                da[h[0]+j[0]+h[-1]] = DA[h]
    #u,u2 -> U,U2 -> u,u2 (roba sui nodi)
    U,U2 = {},{}
    for i in u:
        U[i],U2[i] = [],[]
        for j in u[i]:
            if len(j) == 2:
                U[i].append(j)
                U2[i].append(j[0]+i[0]+j[-1])
            else:
                U[i].append(j[0]+i[0]+j[-1])
                U2[i].append(j[0]+i[0]+j[-1])
    u,u2 = U,U2
    DV = DizionarioVelocità(Pi,Di)[0]
    dv = {}
    for j in u2:
        for h in u2[j]:
            if h[0]+h[1] in DV:
                dv[h[0]+h[1]] = DV[h[0]+h[1]]
    #Dizionari Vincoli esterni
    de = {}
    for i in u2:
        dv2 = {}
        da2 = {}
        for h in u2[i]:
            dv2[h[:-1]] = dv[h[:-1]]
            da2[h] = da[h]
        A = MatriceCinematica(dv2,da2)
        de[i] = rank(A)
    den = {}
    for i in b:
        den[i] = 0
        for j in i:
            for h in ve:
                if h[1] == j:
                    den[i] += 1
    return [de,den,di,din]


def EscludiIncludi(CV,DA,Pr):
    de,den,di,din = CV[0],CV[1],CV[2],CV[3]
    V,Pu = elenca(DA),Pu_(Pr)
    #Vi,Ve:
    Vi,Ve = [],[]
    for i in V:
        if len(i) in [2,3]:
            Ve.append(i)
        elif len(i) == 5:
            Vi.append(i)
    No = []
    for i in V:
        if len(i) == 2:
            No.append(i)
    #Diz. Nodi: per conoscerne quali corpi condividono il nodo
    DN = {}
    for i in No:
        DN[i] = []
        for j in range(len(Pu)):
            if i[0] in Pu[j]:
                DN[i].append(j+1)
    #Cerco corpi uniti
    Cu = []
    for i in de:
        if len(i) > 1:
            Cu.append([])
            for j in i:
                Cu[-1].append(j)
    #Salvo i vincoli colleganti tali corpi in un dizionario:
    VCu = {}
    for j in Cu:
        u = ''
        for k in j:
            u += k
        VCu[u] = []
    for i in Vi:
        for j in Cu:
            if i[1] in j:
                if i[3] in j:
                    VCu[u].append(i)
    #Capisco se il sistema è, almeno apparentemente, isostatico esternamente (cc = 1)
    cc = 1
    for i in den:
        if den[i] != 3:
            cc = 0    
    #Capisco se il sistema è realmente isostatico esternamente (gg = 1)
    gg = 1
    for i in de:
        if de[i] != 3:
            gg = 0
    #Dizionario che associa ai corpi i corrispettivi vincoli interni:
    bilis,bidiz = [],{}
    for i in de:
        bilis.append(i)
    if len(bilis) > 1:
        bilis = Binomiale(bilis,2)
        for i in bilis:
            bidiz[i[0]+i[1]] = i
    DVi = {}
    for i in di:
        DVi[i] = []
    for i in di:
        if i not in bidiz:
            e = []
            for j in i:
                e.append(j)
            for j in Vi:
                if j[1] in e:
                    if j[3] in e:
                        DVi[i].append(j)
        else:
            e = []
            for j in bidiz[i]:
                e.append([])
                for k in j:
                    e[-1].append(k)
            for j in Vi:
                if j[1] in e[0]:
                    if j[3] in e[1]:
                        DVi[i].append(j)
    #Dizionario che associa ai corpi i corrispettivi vincoli esterni:
    DVe = {}
    for i in de:
        DVe[i] = []
    for i in Ve:
        for j in de:
            for k in j:
                if len(i) == 3:
                    if k == i[1]:
                        DVe[j].append(i)
                elif len(i) == 2:
                    if i not in DVe[j]:
                        DVe[j].append(i)
    #Riempio escludi,includi:
    N,S = {},{}
    for i in de:
        if de[i] == den[i]:
            if de[i] > 0:
                N[i+'e'] = DVe[i]
        else:
            S[i+'e'] = DVe[i]
    for i in di:
        if di[i] == din[i]:
            if di[i] > 0:
                N[i+'i'] = DVi[i]
        else:
            S[i+'i'] = DVi[i]
    #Se R e S mi escludessero tutti i vincoli => C'è un G.D.V. angolare interno che si comporta da esterno:
    return [N,S,VCu,DVe,DVi]#DVe,DVi non necessari (specie DVi)

'''
per la def sotto in caso di test:
    print('V   =',V)
    print('de  =',de)
    print('den =',den)
    print('di  =',di)
    print('din =',din)
'''
#Non so se sopra ho considerato il caso del pendolo Zerato (nodo)
def Stampa_Informazioni_Vincoli_Rilassare(CV,VD):
    de,den,di,din = CV[0],CV[1],CV[2],CV[3]
    VCu,DVe,DVi = VD[2],VD[3],VD[4] #DVi non utilizzato
    #per dopo, ma anche per sapere se stampare
    cc = 1
    for i in den:
        if den[i] != 3:
            cc = 0    
    gg = 1
    for i in de:
        if de[i] != 3:
            gg = 0
    if len(VCu) > 0 or 1 in [cc,gg]:
        color.write('\nClassificazione dei vincoli interni ed esterni considerando i ranghi degli orlati della matrice cinematica per ogni corpo:\n')
        
    for i in VCu:
        corpi = ''
        for j in i:
            corpi = corpi+' e '+j
        corpi = corpi[3:]
        q = corpi.count('e')
        corpi = corpi.replace(' e',',',q-1)
        print('I corpi',corpi,'sono caratterizzati da',din[i],'gradi di vincolo interni:')
        print(str(VCu[i])[1:-1]+'.')#vin ?
        print('La matrice cinematica a questi associata ha rango pari a',str(di[i])+'.')
        print('Poichè affinchè',len(i),'corpi si comportino come un unico in termini di atto di moto rigido')
        print('il rango della matrice cinematica associata alle equazioni di vincolo interne deve essere pari a',str(di[i])+',')
        color.write('si ha che i corpi '+corpi+' si comportano in questo senso, ',colori['Blu'])
        if di[i] == din[i]:
            color.write(' e che tali corpi sono fra loro internamente isostatici.',colori['Blu'])
        else:
            a = din[i]-di[i]
            verbo,lettera,lettere2,lettera3 = 'sia','e','à','o'
            if a > 1:
                verbo,lettera,lettere2,lettera3 = 'siano','i','anno','i'
            print(" e che all'interno di tale sistema vi",verbo,a,'vincol'+lettera3,'linearmente dipendent'+lettera,'dagli altri')
            print('e che quindi',a,'fra i gradi di vincolo mostrati andr'+lettere2,'rilassat'+lettera3,'nella scelta del sistema ausiliare isostatico estraibile.')
        print()
    if cc == 1:
        corpi = ''
        for i in de:
            corpi = corpi+' e '+i
        corpi = corpi[3:]
        q = corpi.count('e')
        corpi = corpi.replace(' e',',',q-1)
        print('I vincoli esterni sono in numero minimo per garantire atto di moto rigido al sistema.')
        if gg == 1:
            print('I vincoli ridondanti andranno dunque cercati esclusivamente fra quelli interni.')
            print("Dall'analisi degli stessi (corpi",corpi+") emerge infatti che le matrici cinematiche ad essi associate hanno tutte rango massimo, ovvero 3.")
        else:
            print('Ciò nonostante alcuni di questi sono linearmente dipendenti da altri, quindi il sistema risulta essere esternamente ipostatico e ridondante.')
    #se S e N mi escludono tutti i vincoli devo recuperare il G.D.V. angolare interno che è assimilabile ad uno esterno.
    
    
def Ricapitola_Classificazione(cv,vd,A):
    de,den,di,din,R,S = cv[0],cv[1],cv[2],cv[3],vd[0],vd[1]
    color.write('\nRicapitolando i risultati ottenuti:\n')
    l = len(A[0])
    v = 0
    for i in A:
        v += 1
    r = rank(A)
    print('Gradi  di libertà:  ',l)
    print('Gradi  di vincolo:  ',v)
    print('Rango matr.cinem.:  ',r)
    if v-r >= 0:
        print('Vincoli ridonanti:  ',v-r)
    print()
    In = {}
    if l == r:
        print('RANK(A) = MAX')
        if v > l:
            print('Sistema iperstatico: cinematicamente impossibile e staticamente indeterminato')
        elif v == l:
            print('Sistama isostatico:  cinematicamente e staticamente univocamente determinato')
        else:
            print('Sistema ipostatico:  cinematicamente indeterminato e staticamente impossibile')
    else:
        print('RANK(A) < MAX')
        print('Problema singolare')
    #if l == r:
    if 1 == 1:
        ss,rr = 0,0
        for i in S:
            if len(str(S[i])) > ss:
                ss = len(str(S[i]))
        for i in R:
            if len(str(R[i])) > rr:
                rr = len(str(R[i]))
        s = 0
        for i in di:
            if len(str(i))>s:
                s = len(str(i))
        x2,x3 = int(ss/2)-6,int(rr/2)-8
        e = elenca(di)
        if len(e) > 0:#n = 3
            color.write('\n'+' '*(2)+'G.V. interni'+' '*(2),colori['Rosso'])#12
            color.write('totali   ',colori['Viola'])#6+n
            color.write('indipendenti   ',colori['Viola'])#12+n
            color.write('classificazione:   ',colori['Viola'])#16+n
            color.write('n.ridondanze:',colori['Viola'])#13+n
            color.write(' '*x2+' dove cercare:'+' '*x2,colori['Marrone'])#16
            color.write(' '*x3+' dove non cercare:\n',colori['Marrone'])#20
            for i in e:
                a = din[i]-di[i]#n.ridondanze
                if di[i] == 3:  
                    if din[i] == di[i]:
                        frase = ' isostatico'
                    elif din[i] > di[i]:
                        frase = 'iperstatico'
                    else:
                        frase = ' ipostatico'
                else:
                    frase = '     ∅     '
                x = ' '
                if i+'i' in S:
                    In[i+'i'] = a
                    for t in S[i+'i']:
                        x += t+','
                    x = x[:-1]
                    si = ' '*(rr-len(x))+x+' '*(rr-int(len(x)/2))
                else:
                    si = ' '*(2*x2)+'     ∅    '+' '*(2*x2)
                x = ' '
                if i+'i' in R:
                    for t in R[i+'i']:
                        x += t+','
                    x = x[:-1]
                    ri = str(x)
                else:
                    ri = '∅'
                x1 = s-len(str(i))
                color.write('   Corpo '+' '*x1+str(i)+':    ')
                print(din[i],' '*(10-len(str(din[i]))),di[i],' '*9,frase,' '*(21-len(frase)),a,si,ri)
        s = 0
        for i in di:
            if len(str(i))>s:
                s = len(str(i))
        e = elenca(de)
        if len(e) > 0:
            color.write('\n'+' '*(2)+'G.V. interni'+' '*(2),colori['Rosso'])#12
            color.write('totali   ',colori['Viola'])#6+n
            color.write('indipendenti   ',colori['Viola'])#12+n
            color.write('classificazione:   ',colori['Viola'])#16+n
            color.write('n.ridondanze:',colori['Viola'])#13+n
            color.write(' '*x2+' dove cercare:'+' '*x2,colori['Marrone'])#16
            color.write(' '*x3+' dove non cercare:\n',colori['Marrone'])#20
            for i in e:
                a = den[i]-de[i]
                frase = ''
                if de[i] == 3:  
                    if den[i] == de[i]:
                        frase = ' isostatico'
                    elif den[i] > de[i]:
                        frase = 'iperstatico'
                    else:
                        frase = ' ipostatico'
                else:
                    frase = '    ∅    '
                x = ' '
                if i+'e' in S:
                    In[i+'e'] = a
                    for t in S[i+'e']:
                        x += t+','
                    x = x[:-1]
                    se = ' '*(rr-len(x))+x+' '*(rr-int(len(x)/2))
                else:
                    se = ' '*(2*x2)+'     ∅    '+' '*(2*x2)
                x = ' '
                if i+'e' in R:
                    for t in R[i+'e']:
                        x += t+','
                    x = x[:-1]
                    re = str(x)
                else:
                    re = '∅'
                x1 = s-len(str(i))
                color.write('   Corpo '+' '*x1+str(i)+':    ')
                print(den[i],' '*(10-len(str(den[i]))),de[i],' '*9,frase,' '*(21-len(frase)),a,se,re)#-len(se)
    print()
    
def SistemaSiNo(VD,DA):
    N0,S0 = VD[0],VD[1]
    D = elenca(DA)
    N = []
    for i in N0:
        for j in N0[i]:
            if j not in N:
                N.append(D.index(j))
    S = []
    for i in S0:
        S.append([])
        for j in S0[i]:
            if D.index(j) not in N:
                S[-1].append(D.index(j))
    S.sort()
    N.sort()
    return [S,N]


def TrovaRidondanze(A,DA):
    L1,De,v,r = [],elenca(DA),len(A),rank(A)
    ridondanze = v-r
    if ridondanze == 0:
        print('Non sono presenti ridondanze (torno una lista vuota)')
        #print('\n\n\n\n\n\n\n\n.')
        return []
    L0 = []
    for i in range(v):
        L0.append(i)
    B = Binomiale(v,r)
    for i in range(len(B)):
        C = []
        for j in range(len(B[i])):
            C.append(A[B[i][j]])
        if rank(C) == r:
            L1.append(B[i])
    L = []
    for i in L1:
        L.append([])
        for k in L0:
            if k not in i:
                L[-1].append(k)
    L.sort()
    for i in L:
        i.sort()
    return L

def IntRelCelati(LP,SN):
    S,N = SN[0],SN[1]
    CE = []
    LF = copy.deepcopy(LP)
    for i in LF:
        for j in i:
            if j in N:
                CE.append(LP[LP.index(i)])
                break
    return CE

def Stampa_IntRelCelati(CE,DA):
    D = elenca(DA)
    if len(CE) > 0:
        TE = []
        for i in CE:
            for j in i:
                if D[j][-1] in ['ⓐ','㊅']:
                    if len(D[j]) == 5:
                        if D[j] not in TE:
                            TE.append(D[j])
        if len(TE) != 0:
            e = TE[0]
            l1,l2,l3,l4 = 'a','e','',  'o'
            if len(TE) > 1:
                e = ''
                for i in TE:
                    e = e + ' e ' + i
                e = e[3:]
                q = e.count('e')
                e = e.replace(' e',',',q-1)
                l1,l2,l3,l4 = 'e','i','no','i'
            color.write('Nonostante quanto mostrato, da una analisi più attenta ci si accorge che',colori['Blu'])
            color.write('l'+l1+' condizion'+l2+' di vincolo '+e+' si comporta'+l3+' sia come c.d.v. contemporaneamente intern'+l1+' ed estern'+l1+' e quindi è invece possibile rilassarl'+l1+'.\n\n',colori['Blu'])
        
def Stampa_RilassamentiPossibili(LP,DA,DC,vin,Pr):
    ############################################
    print(vin)
    vin = riducinodi(numeravincoli(vin,Pr),Pr)
    print(vin)
    ############################################
    D   = elenca(DA)
    VIN = VIN_()
    #stampo le possibili liste
    print("Le possibili scelte di sistemi ausiliari isostatici estraibili")
    print("si ottengono dal rilassamento delle condizioni di vincolo presenti in una delle seguenti liste:")
    for i in range(len(LP)):
        color.write('Lista n.'+str(i+1)+'\n')
        for j in range(len(LP[i])):
            for k in range(len(vin)):
                if D[LP[i][j]][:-1] in vin[k]:
                    z = k
            print(D[LP[i][j]],'-'*(21-len(VIN[z])+5-len(str(D[LP[i][j]])))+'>',VIN[z],'(Angolo:'+' '*(4-len(str(DA[D[LP[i][j]]]))),str(DA[D[LP[i][j]]])+'°;','Cedimento:',' '*(3-len(str(DC[D[LP[i][j]]]))),str(DC[D[LP[i][j]]])+')',)
       
    
def ScegliRilassamento(LP,DA):
    if len(LP) != 1:#se LP = []?
        risposte_int = []
        risposte_str = []
        for i in range(len(LP)):
            risposte_int.append(int(i+1))
            risposte_str.append(str(i+1))
        print('\nQuali condizioni di vincolo intendi rilassare fra le',len(LP),'proposte?')
        print('Rispondi con il numero asscoiato alle liste proposte.')
        cc = 0
        while cc == 0:
            cc = 1
            risp = input()
            if len(risp) == 0:
                LF = LP[0]
            elif risp not in risposte_str:
                cc = 0
                print('Le scelte proposte sono',str(len(LP))+'.')
                print('Ne segue che la risposta deve appartenere a:',risposte_int)
                print('Per cui rispondi nuovamente con una delle possibili risposte indicate.')
        LF = LP[int(risp)-1]
    else:
        LF = LP[0]
        print("Vi è una unica possibilità di rilassamento per l'estrazione di un sistema estraibile isostatico.")
    #################
    if len(LP) == 0:
        color.write('Sono ScegliRilassamento(LP,DA). LP = []\n\n\n\n\n',colori['Errore'])
        print('Provo a dare una lista vuova,vediamo che succede...')
        LF = []
    #################
    return LF

def Mostra_Rilassamento(LF,DA):
    D = elenca(DA)
    l1,l2 = 'e','a'
    if len(LF) > 1:
        l1,l2 = 'i','e'
    color.write('\nCondizion'+l1+'di vincolo rilassat'+l2+':\n')
    for i in LF:
        print(D[i]) 

def RilassaMatriceCinematica(A,LF):
    AR = copy.deepcopy(A)
    gg = 0
    for i in LF:
        del AR[i+gg]
        gg -= 1
    return AR

def RilassaInput(DA,DC,LF,Pr):
    D = RilassaIncastri(DA,DC,LF)
    DA2,DC2 = D[0],D[1]
    D = RilassaCerniere(DA2,DC2,LF,Pr)
    return D

def RilassaCerniere(DA,DC,LF,Pr):
    et = {'Ⓝ':'ⓝ','Ⓣ':'ⓣ'}#'㊈','㊆','㊅'
    V = elenca(DA)
    #R = elenco vincoli rilassati
    R = []
    for i in LF:
        R.append(V[i])
    #N = elenco punti con nodo (post-rilassamento)
    N2 = {}
    for i in V:
        s = spezza(i)
        for j in s:
            if j[0] not in N2:
                N2[j[0]] = 0
    for i in V:
        if i[-1] in ['Ⓝ','Ⓣ']:
            N2[i[0]] += 1
    for i in N2:
        N2[i] = int(N2[i]/2)
    li = []
    for i in R:
        if i[-1] in ['Ⓝ','Ⓣ']:
            if i[:-1] not in li:
                N2[i[0]] -= 1
                li.append(i[:-1])
    N = []
    for i in N2:
        if N2[i] > 0:
            N.append(i)
    #Dp[punto] = lista dei corpi che possiedono quel punto
    P = P_(Pr)
    Dp = {}
    for i in P:
        for j in i:
            if j[0] not in Dp:
                Dp[j[0]] = []
            Dp[j[0]].append(j[1])
    #DR
    DR = {}
    for i in R:
        if i[-1] in ['Ⓝ','Ⓣ']:
            if i[0] in N:
                DR[i] = [DA[i],DC[i]]
            else:
                DR[i[:-1]+et[i[-1]]] = [DA[i],DC[i]]
        else:
            if '0' not in i:
                DR[i] = [DA[i],DC[i]]
            else:
                w = ''
                s = spezza(i)
                for j in s:
                    if j[1] == '0':
                        w += j[0]
                        if j[0] not in N:
                            #assegno la condizione al corpo dal < numero identificativo
                            w += Dp[j[0]][1]
                        else:
                            w += j[1]
                    else:
                        w += j
                w += i[-1]
                DR[w] = [DA[i],DC[i]]
    #DAR,DCR 
    DAR,DCR = {},{}
    for i in V:
        if i not in R:
            if i[-1] in ['Ⓝ','Ⓣ']:
                if i[0] in N:
                    DAR[i] = DA[i]
                    DCR[i] = DC[i]
                else:
                    DAR[i[:-1]+et[i[-1]]] = DA[i]
                    DCR[i[:-1]+et[i[-1]]] = DC[i]
            else:
                if '0' not in i:
                    DAR[i] = DA[i]
                    DCR[i] = DC[i]
                else:
                    w = ''
                    s = spezza(i)
                    for j in s:
                        if j[1] == '0':
                            w += j[0]
                            if j[0] not in N:
                                #assegno la condizione al corpo dal < numero identificativo
                                w += Dp[j[0]][1]
                            else:
                                w += j[1]
                        else:
                            w += j
                    w += i[-1]
                    DAR[w] = DA[i]
                    DCR[w] = DC[i]
    return [DAR,DCR,DR]

def RilassaIncastri(DA,DC,LF):
    et = {'㊈':'Ⓝ','㊆':'Ⓣ'}#'㊈','㊆','㊅'
    DAR,DCR,DR = {},{},{}
    V = elenca(DA)
    #R = elenco vincoli rilassati
    R2 = []
    for i in LF:
        R2.append(V[i])
    R = []
    for i in R2:
        if i[-1] in ['㊅']:#['㊈','㊆','㊅']:
            if len(i) == 5:
                if i[:-1] not in R:
                    R.append(i[:-1])
    for i in DA:
        if i[-1] in ['㊈','㊆']:
            if i[:-1] in R:
                DAR[i[:-1]+et[i[-1]]] = DA[i]
                DCR[i[:-1]+et[i[-1]]] = DC[i]
            else:
                DAR[i] = DA[i]
                DCR[i] = DC[i]
        else:
            DAR[i] = DA[i]
            DCR[i] = DC[i]
    return [DAR,DCR,R]


'''
pezzo tolto (sia alle cerniere, che spezzandole non va messo 0, sia a DR che resta come è e non tocca il nodo (lo tocca due volte annullandosi))
                    #Scelta arbitraria?
                    DAR[i[:3]+'0'+i[-1]] = DA[i]
                    DCR[i[:3]+'0'+i[-1]] = DC[i]
                    #DAR[i[0]+'0'+i[2:-1]+et[i[-1]]] = DA[i]
                    #DCR[i[0]+'0'+i[2:-1]+et[i[-1]]] = DC[i]
'''

#spezza gli ['Ⓝ','Ⓣ'] in due vincoli
def RisolviNodi(DAR2,DCR2):
    #SE DR HA UN NODO CHE RIMANE NODO.... DOVREBBE POTER ESSERE SPEZZATO IN RISOLVINODI... MA COSI AGGIUNGO UN RILASSAMENTO...
    DAR,DCR = {},{}
    for i in DAR2:
        if i[-1] not in ['Ⓝ','Ⓣ']:
            DAR[i] = DAR2[i]
            DCR[i] = DCR2[i]
        else:
            t = i[-1]
            s = spezza(i)
            for j in s:
                DAR[j+t] = DAR2[i]
                DCR[j+t] = DCR2[i]
    return [DAR,DCR]

#es eq: {0      =  λ(C1ⓝ) + λ(F0Ⓝ) + λ(G3ⓝ) => F0N va cambiata di segno... oppure F0n
def CalcolaBilancioEsterno(DAR,DR,AC,AD,D):
    #0) PREPARAZIONE: liste dei vincoli esterni (i rilassati in RVe, gli altri in Ve)
    Ve,VRe = [],[]
    for i in DAR:
        if i[-1] in ['Ⓝ','Ⓣ']:
            if i[1] == '0':
                Ve.append(i)
        elif len(i) < 5:
            Ve.append(i)
    for i in DR:
        if len(i) < 5:
            VRe.append(i)
    #1) CREO LA MATRICE VUOTA (di zeri) IN CUI ANDRO' AD INSERIRE (le proiezioni) DELLE REAZIONI VINCOLARI
    E = []
    for i in range(3):
        M = []
        for j in range(len(Ve)):
            M.append(0)
        E.append(M)
    #2) RIEMPIO EQUAZIONI senza azioni esterne o forze campionatrici
    for i in Ve:
        m = Ve.index(i)
        if i[-1] in ['ⓝ','ⓣ','ⓔ','㊈','㊆']:
            E[0][m] += sym.cos(rad(DAR[i]))#.evalf(5)
            E[1][m] += sym.sin(rad(DAR[i]))#.evalf(5)
            E[2][m] += sym.sympify(prodottovettoriale(D[i[0]],[sym.cos(rad(DAR[i])).evalf(5),sym.sin(rad(DAR[i])).evalf(5),0])[2])
        elif i[-1] in ['Ⓝ','Ⓣ']:
            E[0][m] -= sym.cos(rad(DAR[i]))#.evalf(5)
            E[1][m] -= sym.sin(rad(DAR[i]))#.evalf(5)
            E[2][m] -= sym.sympify(prodottovettoriale(D[i[0]],[sym.cos(rad(DAR[i])).evalf(5),sym.sin(rad(DAR[i])).evalf(5),0])[2])
        elif i[-1] in ['ⓐ','㊅']:
            E[2][m] += 1
    #CREO LA LISTA DEI VETTORI RISULTATO:
    Z = []
    for i in range(len(elenca(DR))+1):
        M = []
        for i in range(3):
            M.append(0)
        Z.append(M)
    #RIEMPIO LA LISTA N.0 (SISTEMA 0)
    #E) Azioni esterne:
    if len(AC) != 0:
        ACxy = [AC[0],AC[1]]
        for h in range(2):
            for i in ACxy[h]:
                Z[0][h] -= ACxy[h][i]
                Z[0][2] -= sym.sympify(prodottovettoriale(D[i],[[ACxy[h][i],0,0],[0,ACxy[h][i],0]][h])[2])
        ACm  =  AC[2]
        for i in ACm:
            Z[0][2] -= ACm[i]
    #D) Azioni distribuite:
    ###NON funziona (credo) nel caso di aste inclinate (sottoposte ad AD)
    #il suo problema è che nel BE va fatto tutto rispetto l'origine
    if len(AD) != 0:
        ADx, ADy = AD[0], AD[1]
        for i in ADx:
            #ADx = {'BD': [p,p]}
            segno = +1
            if ADx[i][0] < 0:
                segno = -1
            Z[0][0] -= abs(sym.integrate(   ADx[i][0]+ξ*(ADx[i][1]-ADx[i][0])/(D[i[1]][1]-D[i[0]][1]), (ξ,abs(D[i[0]][1]),abs(D[i[1]][1]))))*segno
            #Z[0][2] += sym.integrate(ξ*(ADx[i][0]+ξ*(ADx[i][1]-ADx[i][0])/(D[i[1]][1]-D[i[0]][1])),(ξ,abs(D[i[0]][1]),abs(D[i[1]][1])))#*sym.sin(rad(-90+direzione(D[i[0]],D[i[1]])))
            if D[i[1]][1]-D[i[0]][1] < 0:
                segno *= -1
            Z[0][2] += abs(sym.integrate(ξ*(ADx[i][0]+ξ*(ADx[i][1]-ADx[i][0])/(D[i[1]][1]-D[i[0]][1])),(ξ,D[i[0]][1],D[i[1]][1])))*segno
        for i in ADy:
            segno = +1
            if ADy[i][0] < 0:
                segno = -1
            Z[0][1] -= abs(sym.integrate(   ADy[i][0]+ξ*(ADy[i][1]-ADy[i][0])/(D[i[0]][0]-D[i[1]][0]), (ξ,abs(D[i[0]][0]),abs(D[i[1]][0]))))*segno
            if D[i[1]][0] - D[i[0]][0] < 0:
                segno *= -1                
            Z[0][2] -= abs(sym.integrate((D[i[0]][0]+ξ)*(ADy[i][0]+ξ*(ADy[i][1]-ADy[i][0])/(D[i[1]][0]-D[i[0]][0])),(ξ,D[i[0]][0],D[i[1]][0])))*segno#*sym.cos(rad(direzione(D[i[0]],D[i[1]]))) FUNZIONANTE!
            #Z[0][2] -= sym.integrate(prodottovettoriale([D[i[0]][0]+ξ,D[i[0]][1],0],(0,(ADy[i][0]+ξ*(ADy[i][1]-ADy[i][0])/(D[i[1]][0]-D[i[0]][0])),0))[2],(ξ,D[i[0]][0],D[i[1]][0]))
            #(Xa + x)(p0 + x(pf-pi)/(Xb-Xa))sin(a) dx, Xa<x<Xb
            #Z[0][2] -= sym.integrate(ξ*(ADy[i][0]+ξ*(ADy[i][1]-ADy[i][0])/(D[i[0]][0]-D[i[1]][0])),(ξ,abs(D[i[0]][0]),abs(D[i[1]][0])))*cos(rad(direzione(D[i[0]],D[i[1]]))) (tanto tempo fa)
            
    #3-J) RIEMPIO TUTTI GLI ALTRI SISTEMI con i valori delle azioni campionatrici
    for i in VRe:
        m = VRe.index(i)+1
        if i[-1] in ['Ⓝ','Ⓣ','ⓝ','ⓣ','ⓔ','㊈','㊆','㊅']:
            Z[m][0] -= sym.cos(rad(DR[i][0]))#.evalf(5)
            Z[m][1] -= sym.sin(rad(DR[i][0]))#.evalf(5)
            Z[m][2] -= sym.sympify(prodottovettoriale(D[i[0]],[sym.cos(rad(DR[i][0])).evalf(5),sym.sin(rad(DR[i][0]).evalf(5)),0])[2])
        elif i[-1] in ['ⓐ','㊅']:
            Z[m][2] -= l
    #4) ESTETICA: semplificazioni
    for i in range(len(E)):
        for j in range(len(E[i])):
            E[i][j] = sym.nsimplify(E[i][j])
    for i in range(len(Z)):
        for j in range(len(Z[i])):
            Z[i][j] = sym.nsimplify(Z[i][j])
    return [E,Z,Ve]#,VRe]

def Stampa_BilancioEsterno(BE,DAR,DR,S2):
    E,Z,V = BE[0],BE[1],BE[2]
    Vn = Dati_V_MBM(DAR,V)
    S  = Dati_S_MBM(S2,Vn)
    ReSym = Crea_ReSym(V)
    DRE = elenca(DR)
    ER = []
    for i in E:
        ER.append(prodottoscalare(i,ReSym))
    cc = 0
    for i in range(len(Z)):
        for j in range(len(ER)):
            if len(str(Z[i][j])) > cc:
                cc = len(str(Z[i][j]))
    print('Riportandoli sotto forma di equazioni:')
    color.write('\nBilancio esterno\n',colori['Rosso'])
    for i in range(len(Z)):
        if i == 0:
            color.write('Sistema '+str(i)+': ',colori['Viola'])
            color.write('(sistema dei carichi esterni)\n')
        else:
            color.write('Sistema '+str(i)+': ',colori['Viola'])
            color.write('(relativo a '+str(DRE[i-1])+')\n')
        for j in range(len(ER)):
            print('{'+str(Z[i][j])+' '*(cc-len(str(Z[i][j])))+' =  '+str(ER[j]))
        color.write('Soluzione:\n',colori['Verde'])
        for j in range(len(ReSym)):
            print(ReSym[j],' '*(8-len(str(ReSym[j]))),'=  ',S[i][j])
        print()
    
def CalcolaBilancioNodi(DAR,DR,AC,AD,D):
    #0) TROVO I NODI e ci associo i vincoli tramite un dizionario:
    N = []
    for i in DAR:
        if i[-1] in ['Ⓝ','Ⓣ']:
            if i[0] not in N:
                N.append(i[0])                
    DN = {}
    for i in N:
        DN[i] = []
        for j in DAR:
            s = spezza(j)
            for k in s:
                if k[0] == i:
                    if j[-1] not in ['ⓐ','㊅']:
                        DN[i].append(j)
                    break
    #1) MANDO OGNI NODO A BilancioNodo E SALVO QUI I RISULTATI in un dizionario[punto-nodo]=[E,Z]:
    R = {}
    for i in DN:
        R[i] = BilancioNodo(i,DN[i],DR,DAR,AC,D)
    #DN[lettra nodo] -> [v1,v2,...];#R[lettera nodo] -> [E,Z]
    return [DN,R]
        
def BilancioNodo(N,V,DR,DAR,AC,D):
    #1) CREO LA MATRICE VUOTA (di zeri) IN CUI ANDRO' AD INSERIRE (le proiezioni) DELLE REAZIONI VINCOLARI
    E = []
    for i in range(2):
        M = []
        for j in range(len(V)):
            M.append(0)
        E.append(M)
    #2) RIEMPIO EQUAZIONI senza azioni esterne o forze campionatrici
    for i in V:
        segno = 1
        if i[-1] in ['Ⓝ','Ⓣ']:
            segno = -1
        if len(i) == 5:
            if i[3] == '0':
                segno *= -1
        m = V.index(i)
        E[0][m] += segno*sym.cos(rad(DAR[i])).evalf(5)
        E[1][m] += segno*sym.sin(rad(DAR[i])).evalf(5)
    #CREO LA LISTA DEI VETTORI RISULTATO:
    Z = []
    for i in range(len(elenca(DR))+1):
        M = []
        for i in range(2):
            M.append(0)
        Z.append(M)
    #RIEMPIO LA LISTA N.0 (SISTEMA 0)
    #E) Azioni esterne:
    if len(AC) != 0:
        ACxy = [AC[0],AC[1]]
        for h in range(2):
            for i in ACxy[h]:
                if i == N:
                    print('\n\n')
                    color.write('Modificami',colori['Errore'])
                    print()
                    print(i)
                    print('\n\n')
                    Z[0][h] -= ACxy[h][i]
    #3-J) RIEMPIO TUTTI GLI ALTRI SISTEMI con i valori delle azioni campionatrici
    cc = 0
    for i in DR:
        cc += 1
        if i[-1] in ['Ⓝ','Ⓣ','ⓝ','ⓣ','ⓔ']:
            if i[0] == N:
                '''
                Z[cc][0] += sym.cos(rad(DR[i][0])).evalf(5)
                Z[cc][1] += sym.sin(rad(DR[i][0])).evalf(5)
        #caso molle/pendoli/simili legati a nodi
                '''
                gg = -1
                for j in spezza(i):
                    gg += 1
                    segno = +1
                    #if i[-1] in ['Ⓝ','Ⓣ']:
                    #    segno *= -1
                    if len(i) == 5:
                        if j[1] == '0':
                            if gg == 1:
                                segno *= -1
                            Z[cc][0] -= segno*sym.cos(rad(DR[i][0])).evalf(5)
                            Z[cc][1] -= segno*sym.sin(rad(DR[i][0])).evalf(5)
                    else:
                         Z[cc][0] -= segno*sym.cos(rad(DR[i][0])).evalf(5)
                         Z[cc][1] -= segno*sym.sin(rad(DR[i][0])).evalf(5)
    #4) ESTETICA: semplificazioni
    for i in range(len(E)):
        for j in range(len(E[i])):
            E[i][j] = sym.nsimplify(E[i][j])
    for i in range(len(Z)):
        for j in range(len(Z[i])):
            Z[i][j] = sym.nsimplify(Z[i][j])
    return [E,Z]

def Stampa_BilancioNodi(BN,DAR,DR,S2):
    EZ  = BN[1]
    DN  = BN[0]
    DRE = elenca(DR)
    for N in DN:
        ReSym = Crea_ReSym(DN[N])
        ER = []
        for i in range(len(EZ[N][0])):
            ER.append(prodottoscalare(EZ[N][0][i],ReSym))
        cc = 0
        for i in range(len(EZ[N][1])):
            for j in range(len(ER)):
                if len(EZ[N][1]) >= j+1:#######################
                    if len(str(EZ[N][1][j])) > cc:
                        cc = len(str(EZ[N][1][j]))
    for N in DN:
        ReSym = Crea_ReSym(DN[N])
        Vn = Dati_V_MBM(DAR,DN[N])
        S  = Dati_S_MBM(S2,Vn)
        ER = []
        for i in range(len(EZ[N][0])):
            ER.append(prodottoscalare(EZ[N][0][i],ReSym))
        color.write('\nBilancio nodo '+N+'\n',colori['Rosso'])
        for i in range(len(EZ[N][1])):
            if i == 0:
                color.write('Sistema '+str(i)+': ',colori['Viola'])
                color.write('(sistema dei carichi esterni)\n')
            else:
                color.write('Sistema '+str(i)+': ',colori['Viola'])
                color.write('(relativo a '+str(DRE[i-1])+')\n')
            for j in range(len(ER)):
                print('{'+str(EZ[N][1][i][j])+' '*(cc-len(str(EZ[N][1][i][j])))+' =  '+str(ER[j]))
            color.write('Soluzione:\n',colori['Verde'])
            for j in range(len(ReSym)):
                print(ReSym[j],' '*(8-len(str(ReSym[j]))),'=  ',S[i][j])
            print()

def Mostra_ScomparsaNodo(DA,LF):
#R,Nx,Nr = ril,nodi pre-ril,nodi post-ril
    V = elenca(DA)
    R = []
    for i in LF:
        R.append(V[i])
    N2 = {}
    for i in V:
        s = spezza(i)
        for j in s:
            if j[0] not in N2:
                N2[j[0]] = 0
    for i in V:
        if i[-1] in ['Ⓝ','Ⓣ']:
            N2[i[0]] += 1
    for i in N2:
        N2[i] = int(N2[i]/2)
    Nx = []
    for i in N2:
        if N2[i] > 0:
            Nx.append(i)
    li,LFN = [],[]
    for i in R:
        if i[-1] in ['Ⓝ','Ⓣ']:
            LFN.append(i)
            if i[:-1] not in li:
                N2[i[0]] -= 1
                li.append(i[:-1])
    Nr = []
    for i in N2:
        if N2[i] > 0:
            Nr.append(i)
    NR = []
    for i in Nx:
        if i not in Nr:
            NR.append(i)
    if len(NR) > 0:
        w = ''
        for i in NR:
            w += i + ', '
        w = w[:-2]
        q = ''
        for i in LFN:
            q += i + ', '
        q = q[:-2]
        color.write('\nPresta attenzione:\n')
        l1,l2 = 'l','o'
        if len(LFN) > 0:
            l1,l2 = 'i','i'
        color.write('A seguito de'+l1+' rilassament'+l2+' effettuat'+l2+'',colori['Blu'])
        if len(LF) > 1:
            l1,l2 = 'a','e'
            if len(LFN) > 1:
                l1,l2 = 'e','i'
            color.write(' (nello specifico mi riferisco all'+l1+' condizion'+l2+' di vincolo '+q+')',colori['Blu'])
        l1,l2,l3,l4,l5 = 'l','o','e','l','è'
        if len(NR) > 1:
            l1,l2,l3,l4,l5 = '','i','i','i','sono'
        print(', si ha che i'+l1+' nod'+l2+' present'+l3+' ne'+l4+' punt'+l2+' '+w+' non '+l5+' più tal'+l3+'.')

def Mostra_ComparsaNodo(DA,DAR,DR):#DA VERIFICARE
    R,R2 = [],[]
    for i in DR:
        if i[-1] == '㊅':
            if len(i) == 5:
                if i[:-1] not in R:
                    R.append(i[:-1])
                    RA.append(i)
    I,I2 = [],[]
    for i in DAR:
        if i[:-1] in R:
            if i[-1] in ['Ⓝ','Ⓣ']:
                if i[-1] not in I:
                    I.append(i[-1])
                I2.append(i)
    if len(I) > 0:
        r = ''
        for i in R2:
            r += i + ', '
        r = w[:-2]
        t = ''
        for i in I2:
            t += i + ', '
        t = t[:-2]
        p = ' '
        for i in I2:
            p += i[0] + ', '
        p = p[:-2]
        p += ' '
        color.write('\nPresta attenzione:\n')
        l1,l2,l3,l4,l5,l6     = 'l','o','a','e','e degli'
        if len(I) > 0:
            l1,l2,l3,l4,l5,l6 = 'i','i','e',"i dell'"
        color.write('A seguito de'+l1+' rilassament'+l2+' dell'+l3+' condizion'+l4+' angolar'+l5+'incastr'+l2,colori['Blu'])
        if len(R2) > 1:
            l1,l2 = 'a','e'
            if len(DR) > 1:
                l1,l2 = 'e','i'
            color.write(' (nello specifico mi riferisco all'+l1+' condizion'+l2+' di vincolo '+r+')',colori['Blu'])
        l1,l2,l3,l4,l5     = 'l','o',  "l'",    '',' un'
        if len(I2) > 1:
            l1,l2,l3,l4,l5 = 'i','i','gli ',  'no',' '
        color.write(', si ha che ne'+l1+' punt'+l2+ p +l3+'quest'+l2+' diventa'+l4+l5+'nod'+l2,colori['Blu'])
        print('(mi riferisco cioè alle condizioni di vincolo'+t+')')
        
def SpiegaConvenzioneNodi(DA):
    D = elenca(DA)
    NODO = []
    for i in D:
        if len(i) == 2:
            if i[0] not in NODO:
                NODO.append(i[0])
    if len(NODO) > 0:
        color.write('\nConvenzione scelta (circa nodi sia interni che esterni):\n')
        frase = 'nei punti:'
        if len(NODO) == 1:
            frase = 'nel punto:'
        print("Il sistema presenta un vincolo sia assoluto che relativo (nodo)",frase,str(NODO)[1:-1])
        print('Per facilità di calcolo assegno la condizione di vincolo assoluta al corpo del minor numero identificativo fra quelli che condividono il nodo.')
        print('Il risultato risulta difatti equivalente rispetto ad uno studio del bilancio meccanico dei nodi e la scelta è arbitraria fra i corpi che lo condividono.')

#DIVIDO LE REAZIONI VINCOLARI PER OGNI CORPO (escluse quelle rilassate)
def Dividi_ReazioniVincolari(DAR,n):
    V = elenca(DAR)
    RE = []
    for i in range(n):
        RE.append([])
    for i in V:
        s = spezza(i[:-1])
        e = i[-1]
        if len(s) == 1:
            s = s[0]
            if len(s) == 2:
                RE[int(s[1])-1].append(s+e)
        elif len(s) == 2:
            s1,s2 = s[0],s[1]
            if s1[1] != '0':
                RE[int(s1[1])-1].append(s1+s2+e)
            if s2[1] != '0':
                RE[int(s2[1])-1].append(s1+s2+e)
    return RE

def EliminaNodi(DAR2):
    DAR = {}
    for i in DAR2:
        if len(i) == 3:
            if i[1] != '0':
                DAR[i] = DAR2[i]
        else:
            DAR[i] = DAR2[i]
    return DAR

def CalcolaBilancioCorpi(DAR2,DR,AC,AD,D,Pr):
    n,Pu,P,V = len(Pr),Pu_(Pr),P_(Pr),elenca(DAR2)
    #Elimino i vincoli esterni sui nodi
    DAR = EliminaNodi(DAR2)
    V = elenca(DAR)
    RE = Dividi_ReazioniVincolari(DAR,len(Pr))
    #1) CREO LA MATRICE VUOTA (di zeri) IN CUI ANDRO' AD INSERIRE (le proiezioni) DELLE REAZIONI VINCOLARI
    Equazioni = []
    for i in range(3*n):
        M = []
        for j in range(len(V)):
            M.append(0)
        Equazioni.append(M)
    #2) RIEMPIO EQUAZIONI senza azioni esterne o forze campionatrici
    for i in range(n):
        for j in RE[i]:
            m = V.index(j)#(Ricordati che RE è fatto a partire da V)
            s = spezza(j[:-1])
            segno = +1
            '''
            if len(s) == 2:
                if (s[0][1] == '0') and (s[1][1] == '0'):
                    segno == 0
                elif s[0][1] == '0':
                    s = [s[1]]
                    segno = -1
                elif s[1][1] == '0':
                    s = [s[0]]
            '''
            if len(s) == 2:
                if int(s[1][1])-1 == i:
                    segno = -1                    
            if len(s) == 1:
                k = s[0]
            else:
                for h in P[i]:
                    if s[0] == h:
                        k = h
                    if s[1] == h:
                        k = h
            if j[-1] in ['ⓝ','ⓣ','ⓔ','Ⓝ','Ⓣ','㊈','㊆']:
                Equazioni[3*i][m]   += segno*sym.cos(rad(DAR[j]))#.evalf(5)
                Equazioni[3*i+1][m] += segno*sym.sin(rad(DAR[j]))#.evalf(5)
                Equazioni[3*i+2][m] += sym.sympify(prodottovettoriale(D[k],[segno*sym.cos(rad(DAR[j])).evalf(5),segno*sym.sin(rad(DAR[j])).evalf(5),0])[2])
            elif j[-1] in ['ⓐ','㊅']:
                Equazioni[3*i+2][m] += segno
                    
    #3) CREO LA LISTA DEI VETTORI RISULTATO:
    Z = []
    for i in range(len(elenca(DR))+1):
        M = []
        for i in range(3*n):
            M.append(0)
        Z.append(M)
    #3-0) RIEMPIO LA LISTA N.0 (SISTEMA 0)
    #3-0:E) Azioni esterne:
    ###Considerare il caso il cui la forza ext tocca un nodo
    if len(AC) != 0:
        ACxy = [AC[0],AC[1]]
        ACm  =  AC[2]
        for h in range(2):
            for i in ACxy[h]:
                cc = -1
                for j in range(len(Pu)):
                    cc += 1
                    for k in Pu[j]:
                        if k == i:
                            Z[0][3*cc+h] -= ACxy[h][i]
                            Z[0][3*cc+2] -= sym.sympify(prodottovettoriale(D[k],[[ACxy[h][i],0,0],[0,ACxy[h][i],0]][h])[2])
        for i in ACm:
            cc = -1
            for j in range(len(Pu)):
                cc += 1
                for k in Pu[j]:
                    if k == i:
                        Z[0][3*cc+2] -= sym.sympify(ACm[i])
    #3-0:D) Azioni distribuite:
    ###Considerare il caso di aste inclinate
    if len(AD) != 0:
        ADx, ADy = AD[0], AD[1]
        for i in ADx:
            for j in range(len(Pu)):
                if (i[0] in Pu[j]) and (i[1] in Pu[j]):
                    c = j
            segno = +1
            if ADx[i][0] < 0:
                segno = -1
            Z[0][3*c]   -= segno*abs(sym.integrate(   ADx[i][0]+ξ*(ADx[i][1]-ADx[i][0])/(D[i[1]][1]-D[i[0]][1]), (ξ,abs(D[i[0]][1]),abs(D[i[1]][1]))))
            ###CORREGGERE SOTTO: (Caso asta inclinata:moltiplicare per la giusta funz.trig.)
            #Z[0][3*c+2] += sym.integrate(ξ*(ADx[i][0]+ξ*(ADx[i][1]-ADx[i][0])/(D[i[1]][1]-D[i[0]][1])),(ξ,abs(D[i[0]][1]),abs(D[i[1]][1])))#*sym.cos(rad(direzione(D[i[0]],D[i[1]])))
            if D[i[1]][1]-D[i[0]][1] < 0:
                segno *= -1
            Z[0][3*c+2] += abs(sym.integrate(ξ*(ADx[i][0]+ξ*(ADx[i][1]-ADx[i][0])/(D[i[1]][1]-D[i[0]][1])),(ξ,D[i[0]][1],D[i[1]][1])))*segno
        for i in ADy:
            for j in range(len(Pu)):
                if (i[0] in Pu[j]) and (i[1] in Pu[j]):
                    c = j
            segno = +1
            if ADy[i][0] < 0:
                segno = -1
            Z[0][3*c+1] -= segno*abs(sym.integrate(   ADy[i][0]+ξ*(ADy[i][1]-ADy[i][0])/(D[i[0]][0]-D[i[1]][0]), (ξ,abs(D[i[0]][0]),abs(D[i[1]][0]))))
            #Z[0][3*c+2] -= sym.integrate(ξ*(ADy[i][0]+ξ*(ADy[i][1]-ADy[i][0])/(D[i[0]][0]-D[i[1]][0])),(ξ,D[i[0]][0],D[i[1]][0]))#*sym.sin(rad(direzione(D[i[0]],D[i[1]])))
            if D[i[1]][0] - D[i[0]][0] < 0:
                segno *= -1                
            Z[0][3*c+2] -= abs(sym.integrate(ξ*(ADy[i][0]+ξ*(ADy[i][1]-ADy[i][0])/(D[i[1]][0]-D[i[0]][0])),(ξ,D[i[0]][0],D[i[1]][0])))*segno#*sym.cos(rad(direzione(D[i[0]],D[i[1]])))
            #Z[0][3*c+2] -= sym.integrate(ξ*(ADy[i][0]+ξ*(ADy[i][1]-ADy[i][0])/(D[i[1]][0]-D[i[0]][0])),(ξ,abs(D[i[0]][0]),abs(D[i[1]][0])))#*sym.cos(rad(direzione(D[i[0]],D[i[1]])))

    #3-J) RIEMPIO TUTTI GLI ALTRI SISTEMI
    cc = 0
    for i in DR:
        cc += 1
        s = spezza(i)
        segno = +1
        for f in range(len(s)):
            if segno == 0:
                segno = 1
            s1 = s[f]
            if f == 1:
                segno *= -1
            if s1[1] == '0':
                segno = 0
            if i[-1] in ['ⓝ','ⓣ','ⓔ','Ⓝ','Ⓣ','㊈','㊆']:
                Z[cc][3*(int(s1[1])-1)]   -= segno*sym.cos(rad(DR[i][0])).evalf(5)
                Z[cc][3*(int(s1[1])-1)+1] -= segno*sym.sin(rad(DR[i][0])).evalf(5)
                Z[cc][3*(int(s1[1])-1)+2] -= sym.sympify(prodottovettoriale(D[s1],[segno*sym.cos(rad(DR[i][0])).evalf(5),segno*sym.sin(rad(DR[i][0]).evalf(5)),0])[2])
            elif i[-1] in ['ⓐ','㊅']:
                Z[cc][3*(int(s1[1])-1)+2] -= segno*l
    #4) ESTETICA: semplificazioni
    for i in range(len(Equazioni)):
        for j in range(len(Equazioni[i])):
            Equazioni[i][j] = sym.nsimplify(Equazioni[i][j])
    for i in range(len(Z)):
        for j in range(len(Z[i])):
            Z[i][j] = sym.nsimplify(Z[i][j])
    return [Equazioni,Z,V]#V è stato aggiunto da poco!

def Soluzioni_BNR(BE,BN,EZ,DAR3):
    #UNIFORMO Bil.ext,nodi,Eq.vinc allo stesso format: [[equazioneS0,...,equazioneS1,...,soluzioneS0,vincoli],...]
    DAR = EliminaNodi(DAR3)
    V = elenca(DAR3)
    Ei = [[[BE[0],BE[1]],BE[2]]]
    for i in BN[0]:
        a = [BN[1][i],BN[0][i]]
        Ei.append(a)
    s = len(Ei[0][0][1])
    RE = Dividi_ReazioniVincolari(DAR,int(len(EZ[0])/3))
    for c in range(len(RE)):
        ei,sn = [],[]
        for h in range(s):
            sn.append([])
            for xym in range(3):
                sn[-1].append(EZ[1][-s+h][3*c+xym])
        for xym in range(3):
            ei.append(EZ[0][3*c+xym])
        Ei.append([[ei,sn],elenca(DAR)])
    E,Z = [],[]
    M2 = []
    cc = 0
    for i in Ei:
        M = []  
        for j in range(len(i[0][0])):
            M.append(i[0][0][j])
            cc += 1
        for h in range(s):
            M.append(i[0][1][h])
        M.append(i[1])
        M2.append(M)
    E.append(M2)    
    #CREO LE MATRICE DI ZERI (Eq e Sol)
    M = []
    for i in range(cc):
        M1 = []
        for j in range(len(DAR3)):
            M1.append(0)
        M.append(M1)
    S = []
    for h in range(s):
        S0 = []
        for i in range(cc):
            S0.append(0)
        S.append(S0)
    cc = -1
    for i in E:
        for j in i:
            Vi = j[-1]
            Eq = j[:-s-1]
            So = j[-s-1:-1]
            for k in Eq:
                cc += 1
                for h in range(s):
                    S[h][cc] = So[h][Eq.index(k)]
                gg = -1
                for t in k:
                    gg += 1
                    m2 = V.index(Vi[gg])
                    M[cc][m2] += t
    return [M,S]

def Idonea_Soluzioni_BNR(MS,DAR):
    M,S = MS[0],MS[1]
    L = TrovaRidondanze(M,DAR)[0]#troppa computazione inutile. Da modificare (pero funziona eh!)
    E = []
    for i in range(len(M)):
        if i not in L:
            E.append(M[i])
    Z = []
    for h in range(len(S)):
        Zm = []
        for i in range(len(M)):
            if i not in L:
                Zm.append(S[h][i])
        Z.append(Zm)
    return [E,Z]

def Soluzione_Reazioni(EZ,DR):
    E,Z = EZ[0],EZ[1]
    SM = []
    EM = Matrix(E)
    Einv = EM**-1
    for i in Z:
        SM.append(Einv*Matrix(i))
    #RENDO SM UNA LISTA DI SYM (e non di liste di sym):
    S = []
    for i in SM:
        S.append(i.tolist())
    #ss()
    for i in range(len(S)):
        for j in range(len(S[i])):
            S[i][j] = S[i][j][0]
            '''
            S[i][j] = sym.nsimplify(S[i][j][0])
            '''
    return S

def Stampa_Soluzione(S,DAR,DR):
    RS  = Crea_ReSym(DAR)
    DRE = elenca(DR)
    '''
    for h in range(len(S[0])):
        print(V[h],' '*(8-len(V[h])),S[0][h],' '*(10-len(str(S[0][h]))),S[1][h])
    '''
    print('Soluzioni per ogni sistema:\n')
    for h in range(len(S)):
        if h == 0:
            color.write('Sistema '+str(h)+': ',colori['Verde'])
            color.write('(sistema dei carichi esterni)\n')
        else:
            color.write('Sistema '+str(h)+': ',colori['Verde'])
            color.write('(relativo a '+str(DRE[h-1])+')\n')
        for j in range(len(RS)):
            color.write(str(RS[j]),colori['Blu'])
            print(' '*(8-len(str(RS[j]))),'=  ',S[h][j])
        print()        

#AGGIUNGE AI NODI int_rel IL NUMERO RELATIVO AL CORPO, in questo modo l'utente può sapere a quale corpo sia applicata la reazione vincolare (scelta arbitraria)
def Crea_ReSym(DAR):
    if type(DAR) == dict:
        V = elenca(DAR)
    else:
        V = DAR
    ReSym = []
    for i in range(len(V)):
        ReSym.append(sym.symbols('λ('+str(V[i])+')'))
    return ReSym#ReSym = [λ(A1Ⓝ), λ(F3Ⓝ), λ(C1Ⓝ), λ(C1C2Ⓝ), λ(C2C3Ⓝ), λ(E2E3Ⓝ), λ(C1Ⓣ), λ(C1C2Ⓣ), λ(C2C3Ⓣ)]

def sta(a):
    a = str(a)
    a = a.replace('**','^')
    a = a.replace('*','∙')
    #a = a.replace('sqrt(2)/2','2^(-1/2)')
    #a = a.replace('sqrt(2)','2^(1/2)')
    return a

def Spiega_ReSym(DAR,n):
    ReSym = Crea_ReSym(DAR)
    V = elenca(DAR)
    RE = Dividi_ReazioniVincolari(DAR,n)
    #Freccie = ['←','↑','→','↓','↖','↗','↘','↙','↺','↻']
    color.write('\nDirezioni scelte per le reazioni vincolari:\n')
    print("Ho scelto, per le versi dei vettori delle reazioni vincolari, le seguenti direzioni per ogni corpo (concordemente ai valori delle normali inseriti nell'input):")
    cc = 0
    relativi = []
    for i in RE:
        cc += 1
        color.write('Corpo '+str(cc)+':\n')
        for j in i:
            α = DAR[j]
            m = V.index(j)
            if j in relativi:
                α += 180
            else:
                relativi.append(j)
            if j[-1] in ['Ⓝ','Ⓣ','ⓝ','ⓣ','ⓔ','㊈','㊆']:
                if   α in [0,360]:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'→')
                elif α in [-270,90,450]:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'↑')
                elif α in [-180,180]:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'←')
                elif α in [-90,270]:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'↓')
                elif 0<α<90 or 360<α<450:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'↗')
                elif 90<α<180 or -270<α<-180:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'↖')
                elif 180<α<270 or -180<α<-90:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'↙')
                elif 270<α<360 or -90<α<0:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'↘')
            elif j[-1] in ['ⓐ','㊅']:
                if α == 0:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'↺')
                elif α == 180:
                    print(str(ReSym[m]),' '*(8-len(str(ReSym[m]))),'↻')

def Stampa_BilancioCorpi(EZ,S2,DAR,DR):
    E,Z = EZ[0],EZ[1]
    Vn = Dati_V_MBM(DAR,EliminaNodi(DAR))
    S  = Dati_S_MBM(S2,Vn)
    ReSym = Crea_ReSym(EliminaNodi(DAR))
    DRE = elenca(DR)
    ER = []
    for i in E:
        ER.append(prodottoscalare(i,ReSym))
    color.write('\nBilancio corpi:\n',colori['Rosso'])
    cc = 0
    for i in range(len(Z)):
        for j in range(len(ER)):
            if len(str(Z[i][j])) > cc:
                cc = len(str(Z[i][j]))
    for i in range(len(Z)):
        if i == 0:
            color.write('Sistema '+str(i)+': ',colori['Viola'])
            color.write('(sistema dei carichi esterni)\n')
        else:
            color.write('Sistema '+str(i)+': ',colori['Viola'])
            color.write('(relativo a '+str(DRE[i-1])+')\n')
        for j in range(len(ER)):
            print('{'+str(Z[i][j])+' '*(cc-len(str(Z[i][j])))+' =  '+str(ER[j]))
        color.write('Soluzione:\n',colori['Verde'])
        for j in range(len(ReSym)):
            print(ReSym[j],' '*(8-len(str(ReSym[j]))),'=  ',S[i][j])
        print()            
        
def Stampa_Legenda_Matrice():
    color.write('\nSoluzione di tutti i sistemi presenti in forma matriciale:\n')###
    print('Legenda per comprendere la rappresentazione sottostante:')
    print("E' un espressione compatta (difatti: numero di righe = costante = gradi di libertà) delle equazioni di bilancio meccanico e delle relative soluzioni per tutti i sistemi da analizzare.")
    print("Il primo termine è la matrice di bilancio meccanico")
    print("Il secondo termine è il vettore delle reazioni vincolari incognite")
    print("Il terzo termine è il vettore delle azioni esterne (con segno opposto) del sistema zero")
    print("I termini a seguire sono i vettori dei contributi alle equazioni di bilancio delle azioni campionatrici (con segno opposto) dei sistemi ausiliari")
    print("Dopo la freccia ci sono le soluzioni nell'ordine dei vettori mostrati prima (termini 3,4,..), ovvero nell'ordine: sistema 0,1,2,...")
    print()

def Stampa_MS(EZ,DAR,S,DN):
    E,Z = EZ[0],EZ[1]
    N = elenca(DN)
    Es = stampamatrice(E)
    m  =  0
    for i in Es[0]:
        m += len(str(i))+2
    t  =  0
    for h in S:
        for j in h:
            i = len(sta(j))
            if i > t:
                t = i
    q  =  0
    for h in Z:
        for j in h:
            i = len(sta(j))
            if i > q:
                q = i
    RS = Crea_ReSym(DAR)
    Zs  = []
    for i in Z[0]:
        Zs.append([])
    for i in range(len(Z)):
        for j in range(len(Z[i])):
            a = sta(Z[i][j])
            Zs[j].append('['+' '*(q-len(a))+a+']')
    Ss = []
    for i in S[0]:
        Ss.append([])
    for i in range(len(S)):
        for j in range(len(S[i])):
            a = sta(S[i][j])
            Ss[j].append('['+' '*(t-len(a))+a+']')
    RSs = []
    for i in RS:
        a = int((8-len(str(i)))/2)
        RSs.append('['+' '*a+str(i)+' '*a+']')
    n = 0
    for i in Es[0]:
        n += len(str(i)) + 2
    if len(E) > len(RS):
        lM = len(E)
        lm = len(RS)
    else:
        lM = len(RS)
        lm = len(E)
    #STAMPA:
    nc = 2*len(N)+3
    cc = -1
    kk = 0
    color.write('Bilancio esterno:',colori['Rosso'])
    for i in range(lm):
        cc += 1
        if 3 <= cc < 2*len(N)+3:
            if kk%2 == 0:
                d = 1
                w = N[int(kk/2)]
                color.write('Bilancio nodo '+w+':\n',colori['Rosso'])
            else:
                print()
            kk += 1
        elif cc >= 2*len(N)+3:
            if (cc-2*len(N))%3 == 0:
                corpo = str(int((cc-2*len(N))/3))
                color.write('Bilancio corpo '+corpo+':\n',colori['Rosso'])
            else:
                print()
        else:
            print()
        colorwrite(' '*(m-n))
        colorwrite(str(Es[i])+' ','Viola')#colori['Viola'])
        colorwrite(str(RSs[i]),'Arancione')#colori['Arancione'])
        colorwrite('  =  ','Blu')#colori['Blu'])
        colorwrite(str(Zs[i])[1:-1],'Rosso')#colori['Rosso'])
        if   i == int(lm/2) and lm%2 == 1:
            color.write('   =====>   ',colori['Nero'])
        else:
            color.write(' '*12)
        colorwrite(str(RSs[i]),'Arancione')#colori['Arancione'])
        colorwrite('  =  ','Blu')#colori['Nero'])
        colorwrite(str(Ss[i])[1:-1]+'\n','Verde')#colori['Verde'])
        if   i == int(lm/2)-1 and lm%2 == 0:
            colorwrite(' '*(m+16+(4+t)*len(S)))
            color.write('  =====>\n',colori['Nero'])
        #color.write('\n')
    vm1 = len(Es)-len(RS)
    vm2 = len(RS)-len(Es)
    if vm1 <= 0:
        vm1 = 0
    if vm2 <= 0:
        vm2 = 0
    for j in range(vm1):
        cc += 1
        if 3 <= cc < 2*len(N)+3:
            if kk%2 == 0:
                w = N[int(kk/2)]
                color.write('Bilancio nodo '+w+':\n',colori['Rosso'])
            kk += 1
        elif cc >= 2*len(N)+3:
            if (cc-2*len(N))%3 == 0:
                corpo = str(int((cc-2*len(N))/3))
                color.write('Bilancio corpo '+corpo+':\n',colori['Rosso'])
            else:
                print()
        else:
            print()
        i = lm+j
        #colorwrite(' '*(m-n))
        colorwrite(str(Es[i])+' ','Viola')#colori['Viola'])
        colorwrite(' '*(len(str(RSs[0]))+1),'Arancione')#colori['Arancione'])
        colorwrite('  =  ','Blu')#colori['Blu'])
        colorwrite(str(Zs[i])[1:-1],'Rosso')#colori['Rosso'])
        if   i == int(lm/2) and lm%2 == 1:
            color.write('   =====>   ')#,colori['Nero'])
        else:
            color.write(' '*12)
        if   i == int(lm/2)-1 and lm%2 == 0:
            colorwrite(' '*(16+(4+t)*len(S)))
            #colorwrite(' '*(len(str(Es[0]))+len(str(RSs[0]))+len(str(Zs[0])[1:-1])+7))
            colorwrite('  =====>')#,colori['Nero'])
        colorwrite('\n')

    for j in range(vm2):
        cc += 1
        if 3 <= cc < 2*len(N)+3:
            if kk%2 == 0:
                w = N[int(kk/2)]
                color.write('Bilancio nodo '+w+':\n',colori['Rosso'])
            kk += 1
        elif cc == 2*len(N)+3:
            color.write('Bilancio per ogni corpo:\n',colori['Rosso'])
        elif cc >= 2*len(N)+3:
            if (cc-2*len(N))%3 == 0:
                corpo = str(int((cc-2*len(N))/3))
                color.write('Bilancio corpo '+corpo+':\n',colori['Rosso'])
            else:
                print()
        else:
            print()
        i = lm+j
        colorwrite(' '*(m+1))
        colorwrite(str(RSs[i]),'Arancione')#colori['Arancione'])
        colorwrite('  =  ','Blu')#colori['Blu'])
        colorwrite(str(Zs[i])[1:-1]+' ','Rosso')#colori['Rosso'])
        if   i == int(lm/2) and lm%2 == 1:
            colorwrite('  =====>   ','Nero')#colori['Nero'])
        else:
            colorwrite(' '*11)
        colorwrite(str(RSs[i]),'Arancione')#,colori['Arancione'])
        colorwrite('  =  ','Blu')#,colori['Nero'])
        colorwrite(str(Ss[i])[1:-1]+'\n','Verde')#colori['Verde'])
        if   i == int(lm/2)-1 and lm%2 == 0:
            colorwrite(' '*(m+16+(4+t)*len(S)-1))
            #colorwrite(' '*(len(str(Es[0]))+len(str(RSs[0]))+len(str(Zs[0])[1:-1])))
            colorwrite('   =====>  ')#,colori['Nero'])
        colorwrite('\n')

def Stampa_MatriceBilancioMeccanico(MS,S2,DAR,VB):
    print('Considerando i vari sistemi singolarmente:')
    VBE,VBN,VRV = VB[0],VB[1],VB[2]
    V2,M,Z2 = elenca(DAR),MS[0],MS[1]
    #spazi per la stampa:
    gg = 3
    for i in VBN:
        gg += 2
    E0,V0 = M[gg:],[]
    for i in VRV:
        V0.append(V2.index(i))
    E1 = []
    for i in range(len(E0)):
        E1.append([])
        for j in range(len(E0[i])):
            if j in V0:
                E1[-1].append(E0[i][j])
    Es = stampamatrice(E1)
    n  =  0
    for i in Es[0]:
        n += len(str(i))+2#+2 se ci sono le virgolette
    t  =  0
    for h in S2:
        for j in h:
            i = len(sta(j))
            if i > t:
                t = i
    q  =  0
    for h in Z2:
        for j in h:
            i = len(sta(j))
            if i > q:
                q = i
    #Bilancio Esterno:
    color.write('\nBilancio Esterno:\n',colori['Rosso'])
    cc = 3
    E2 = M[:cc]
    none = 0
    for i in E2:
        for j in i:
            if j != 0:
                none = 1
    if none == 1:
        StampaSingola_MBM(E2,Z2,S2,V2,VBE,cc,0,n,q,t)
    else:
        print('∅')
    #Bilancio Nodi:
    N = elenca(VBN)
    for i in N:
        color.write('Bilancio Nodo '+i+':\n',colori['Rosso'])
        E2 = M[cc-1:cc+1]
        StampaSingola_MBM(E2,Z2,S2,V2,VBN[i],cc,1,n,q,t)
        cc += 2
    #Bilancio Corpi:
    color.write('Bilancio Corpi:\n',colori['Rosso'])
    E2 = M[cc:]
    #Z3 = Z2[cc:]
    StampaSingola_MBM(E2,Z2,S2,V2,VRV,cc,2,n,q,t)
    
#D2 = Dato_totale, D = dato specifico, Vn = posizione_V2_rispetto_V)
def Dati_V_MBM(DAR,V):
    if type(DAR) == list:
        V2 = DAR
    elif type(DAR) == dict:
        V2 = elenca(DAR)
    Vn = []
    for i in V:
        Vn.append(V2.index(i))
    return Vn
def Dati_E_MBM(E2,Vn):
    E = []
    for i in range(len(E2)):
        E.append([])
        for j in range(len(E2[i])):
            if j in Vn:
                E[-1].append(E2[i][j])
    return E

def Dati_Z_MBM(Z2,cc,le,U):
    Z = []
    for h in range(len(Z2)):
        Z.append([])
        for i in range(len(Z2[h])):
            if U == 0:
                if  i < 3:
                    Z[-1].append(Z2[h][i])
            elif U == 1:
                if cc-1 < i < cc+2:
                    Z[-1].append(Z2[h][i])
            elif U == 2:
                if i >= cc:
                    Z[-1].append(Z2[h][i])
    return Z
def Dati_S_MBM(S2,Vn):
    S = []
    for h in range(len(S2)):
        S.append([])
        for i in range(len(S2[h])):
            if i in Vn:
                S[-1].append(S2[h][i])
    return S
#Etot,Ztot,Stot,Vtot,Vspec -> Espec,Zspec,Sspec
def Dati_MBM(E2,Z2,S2,V2,V,cc,U):
    Vn = Dati_V_MBM(V2,V)
    E  = Dati_E_MBM(E2,Vn)
    Z  = Dati_Z_MBM(Z2,cc,len(E[0]),U)
    S  = Dati_S_MBM(S2,Vn)
    return [E,Z,S]

def StampaSingola_MBM(E2,Z2,S2,V2,V,cc,U,n,t,q):
    d = Dati_MBM(E2,Z2,S2,V2,V,cc,U)
    E,Z,S = d[0],d[1],d[2]
    Stampa_MBM([E,Z],S,V,n,t,q)

def Stampa_MBM(EZ,S,DAR,m,t,q):
    E,Z = EZ[0],EZ[1]
    RS = Crea_ReSym(DAR)
    Es = stampamatrice(E)
    Zs  = []
    for i in Z[0]:
        Zs.append([])
    for i in range(len(Z)):
        for j in range(len(Z[i])):
            a = sta(Z[i][j])
            Zs[j].append('['+' '*(t-len(a))+a+']')
    Ss = []
    for i in S[0]:
        Ss.append([])
    for i in range(len(S)):
        for j in range(len(S[i])):
            a = sta(S[i][j])
            Ss[j].append('['+' '*(q-len(a))+a+']')
    RSs = []
    for i in RS:
        a = int((8-len(str(i)))/2)
        RSs.append('['+' '*a+str(i)+' '*a+']')
    '''
    #n = lunghezza reale stringa riga matrice Es, se non serve cancella
    n = 0
    for i in Es:
        for j in i:
            n += len(str(j))
    n = int(n/len(E[0])+(len(E[0])-1)*4+2)
    n += len(str(RSs[0]))+len(str(Zs[0]))+9
    '''
    n = 0
    for i in Es[0]:
        n += len(str(i)) + 2#+2 se ci sono le virgolette
    if len(E) > len(RS):
        lM = len(E)
        lm = len(RS)
    else:
        lM = len(RS)
        lm = len(E)
    for i in range(lm):
        colorwrite(' '*(m-n))
        colorwrite(str(Es[i])+' ','Viola')#colori['Viola'])
        colorwrite(str(RSs[i]),'Arancione')#colori['Arancione'])
        colorwrite('  =  ','Blu')#colori['Blu'])
        colorwrite(str(Zs[i])[1:-1],'Rosso')#colori['Rosso'])
        if   i == int(lm/2) and lm%2 == 1:
            color.write('   =====>   ')#,colori['Nero'])
        else:
            color.write(' '*12)
        colorwrite(str(RSs[i]),'Arancione')#colori['Arancione'])
        colorwrite('  =  ','Blu')#colori['Nero'])
        colorwrite(str(Ss[i])[1:-1]+'\n','Verde')#colori['Verde'])
        if   i == int(lm/2)-1 and lm%2 == 0:
            colorwrite(' '*(m+16+(4+t)*len(S)))
            #colorwrite(' '*(len(str(Es[0]))+len(str(RSs[0]))+len(str(Zs[0])[1:-1])+7))
            colorwrite('  =====>')#,colori['Nero'])
        colorwrite('\n') 
    vm1 = len(Es)-len(RS)
    vm2 = len(RS)-len(Es)
    if vm1 < 0:
        vm1 = 0
    if vm2 < 0:
        vm2 = 0
    for j in range(vm1):
        i = lm+j
        colorwrite(' '*(m-n+1))
        colorwrite(str(Es[i])+' ','Viola')#colori['Viola'])
        colorwrite(' '*len(str(RSs[0])),'Arancione')#colori['Arancione'])
        colorwrite('  =  ','Blu')#colori['Blu'])
        colorwrite(str(Zs[i])[1:-1],'Rosso')#colori['Rosso'])
        if   i == int(lm/2) and lm%2 == 1:
            color.write('   =====>   ')#,colori['Nero'])
        else:
            color.write(' '*12)
        if   i == int(lm/2)-1 and lm%2 == 0:
            colorwrite(' '*(m+16+(4+t)*len(S)))
            #colorwrite(' '*(len(str(Es[0]))+len(str(RSs[0]))+len(str(Zs[0])[1:-1])+7))
            colorwrite('  =====>')#,colori['Nero'])
        colorwrite('\n\n')
    for j in range(vm2):
        i = lm+j
        colorwrite(' '*(m+1))
        colorwrite(str(RSs[i]),'Arancione')#colori['Arancione'])
        #colorwrite('  =  ','Blu')#colori['Blu'])
        colorwrite((len(str(Zs[0])))*' ','Rosso')#colori['Rosso'])
        if   i == int(lm/2) and lm%2 == 1:
            colorwrite('  =====>   ','Nero')#colori['Nero'])
        else:
            colorwrite(' '*11)
        colorwrite(str(RSs[i]),'Arancione')#,colori['Arancione'])
        colorwrite('  =  ','Blu')#,colori['Nero'])
        colorwrite(str(Ss[i])[1:-1]+'\n','Verde')#colori['Verde'])
        if   i == int(lm/2)-1 and lm%2 == 0:
            colorwrite(' '*(m+16+(4+t)*len(S)-1))
            #colorwrite(' '*(len(str(Es[0]))+len(str(RSs[0]))+len(str(Zs[0])[1:-1])))
            colorwrite('   =====>  ')#,colori['Nero'])
        #'''
        colorwrite('\n')
        
    
def Salva_Molle(DAR,S,DR,DRV):
    #DAR = {'E2Ⓝ': 180, 'A1E2Ⓝ': 0, 'C1C2Ⓝ': 90, 'F2Ⓝ': 90, 'C1C2Ⓐ': 0, 'A1ⓔ': 90}
    #S   = [[0, 0, 0, 1.0*l*p, 0.5*l**2*p, 1.0*l*p], [0, 0, -0.50000, -0.50000, 0.5*l, 0.50000]]
    s = len(S)
    RE  = elenca(DAR)
    Molle = {}
    for i in range(len(RE)):
        if RE[i][-1] == 'ⓔ':
            if RE[i][:-1] not in Molle:
                Molle[RE[i][:-1]] = []
                for j in range(s):
                    Molle[RE[i][:-1]].append(0)
            for j in range(s):
                Molle[RE[i][:-1]][j] += S[j][i]
    cc = -1
    for i in DR:
        cc += 1
        if i[-1] == 'ⓔ':
            s0 = spezza(i)
            for j in s0:
                for k in DRV:
                    if k[-1] != 'm':
                        #se quel punto è un nodo? #nuovo nodo ultimo nuovo pero eh!
                        if j == k[:-1]:
                            xy,a = k[-1],DR[i][0]
                            if j not in Molle:
                                Molle[i] = []
                                for h in range(s):
                                    Molle[i].append(0)#i! volutamente...
                                Molle[i].append(cc)
                            for h in range(s):
                                if xy == 'x':
                                    Molle[i][h] += DRV[k][h]*sym.cos(rad(a))
                                elif xy == 'y':
                                    Molle[i][h] += DRV[k][h]*sym.sin(rad(a))
    return Molle
       
def Associa_PuntiReazioni(S2,DAR2,DR,AC,AD,Pr):
    DAR = EliminaNodi(DAR2)
    li = []
    cc = -1
    for i in DAR2:
        cc += 1
        if i not in DAR:
            li.append(cc)
    S = []
    for h in range(len(DR)+1):
        S.append([])
        for i in range(len(S2[h])):
            if i not in li:
                S[-1].append(S2[h][i])
    V = elenca(DAR)
    P,Pu = P_(Pr),Pu_(Pr)
    RE  = Dividi_ReazioniVincolari(DAR,len(Pr))
    #CREO LE INCOGNITE PER OGNI PUNTO (con reazione): es: A1x,A1y,A1m,...
    PR1 = []
    for i in V:
        s = spezza(i)
        for j in s:
            if j not in PR1:
                PR1.append(j)
    for i in DR:
        s = spezza(i)
        for j in s:
            if j not in PR1:
                PR1.append(j)
    #PR1 = ['A1', 'F3', 'C1', 'C2', 'C3', 'E2', 'E3']
    PR = []
    for i in PR1:
        PR.append(i+'x')
        PR.append(i+'y')
        PR.append(i+'m')
    #PR=['A1x', 'A1y', 'A1m', 'F3x', 'F3y', 'F3m', 'C1x', 'C1y', 'C1m', 'C2x', 'C2y', 'C2m', 'C3x', 'C3y', 'C3m', 'E2x', 'E2y', 'E2m', 'E3x', 'E3y', 'E3m']
    DRV = {}
    for h in range(len(S)):
        for i in PR:
            if h == 0:
                DRV[i] = []
            DRV[i].append(0)
    #Aggiungo i valori dei punti non appartenenti alle forze esterne (che possono esser punti non vincolati!)
    if len(AC) != 0:
        for h in range(3):
            for i in AC[h]:
                cc = -1
                for j in range(len(Pu)):
                    cc += 1
                    for k in Pu[j]:
                        if k == i:
                            if k+str(j+1)+'x' not in DRV:
                                DRV[k+str(j+1)+'x'] = []
                                DRV[k+str(j+1)+'y'] = []
                                DRV[k+str(j+1)+'m'] = []
                                for f in range(len(S)):
                                    DRV[k+str(j+1)+'x'].append(0)
                                    DRV[k+str(j+1)+'y'].append(0)
                                    DRV[k+str(j+1)+'m'].append(0)
    #V,ReSym,S hanno lo stesso ordine! :) -> #['A1Ⓝ','F3Ⓝ','C1Ⓝ','C1C2Ⓝ','C2C3Ⓝ','E2E3Ⓝ','C1Ⓣ','C1C2Ⓣ','C2C3Ⓣ']
    #Valori reazioni vincolari
    for d in range(len(S)):
        cc = 0
        for h in RE:
            cc += 1
            for i in h:
                e = i[-1]
                s = spezza(i[:-1])
                for j in range(len(s)):
                    k = s[j]
                    m = V.index(i)
                    if cc == int(k[1]):
                        if j == 0:
                            if k[1] != '0':
                                if e in ['Ⓝ','Ⓣ','ⓝ','ⓣ','ⓔ','㊈','㊆']:
                                    DRV[k+'x'][d] += sym.cos(rad(DAR[i]))*S[d][m]
                                    DRV[k+'y'][d] += sym.sin(rad(DAR[i]))*S[d][m]
                                elif e in ['ⓐ','㊅']:
                                    DRV[k+'m'][d] += S[d][m]
                        else:
                            if k[1] != '0':
                                if e in ['Ⓝ','Ⓣ','ⓝ','ⓣ','ⓔ','㊈','㊆']:
                                    DRV[k+'x'][d] -= sym.cos(rad(DAR[i]))*S[d][m]
                                    DRV[k+'y'][d] -= sym.sin(rad(DAR[i]))*S[d][m]
                                elif e in ['ⓐ','㊅']:
                                    DRV[k+'m'][d] -= S[d][m]
    #Aggiungo i valori delle forze campionatrici:
    #DR = {'E2E3Ⓣ': [0, 0]}
    #DR = {'C1Ⓝ': [90, -δ], 'C1Ⓐ': [0, 0], 'C1Ⓣ': [0, 0]}
    for h in range(len(RE)):
        d = 0
        for i in DR:
            d += 1
            e = i[-1]
            s = spezza(i[:-1])
            segno = +1
            for j in range(len(s)):
                k = s[j]
                if h+1 == int(k[1]):
                    if j == 1:
                        segno *= -1
                    if k[1] != '0':
                        if e in ['Ⓝ','Ⓣ','ⓝ','ⓣ','ⓔ','㊈','㊆']:
                            DRV[k+'x'][d] += sym.cos(rad(DR[i][0]))*segno
                            DRV[k+'y'][d] += sym.sin(rad(DR[i][0]))*segno
                        elif e in ['ⓐ','㊅']:
                            DRV[k+'m'][d] += l*segno
    #Aggiungo i valori delle forze/momenti esterni del sistema 0:
    #[A1Ⓝ, F3Ⓝ, CⓃ, C1C2Ⓝ, C2C3Ⓝ, E2E3Ⓝ, CⓉ, C1C2Ⓣ, C2C3Ⓣ]#C2E3
    if len(AC) != 0:
        ACxy = [AC[0],AC[1]]#{'G': 2*F} #{'B': F}
        ACm = AC[2]#{'D': F*l}
        for h in range(2):
            for i in ACxy[h]:
                cc = -1
                for j in range(len(Pu)):
                    cc += 1
                    for k in Pu[j]:
                        if k == i:
                            if h == 0:
                                DRV[i+str(j+1)+'x'][0] += ACxy[h][i]
                            else:
                                DRV[i+str(j+1)+'y'][0] += ACxy[h][i]
        for i in ACm:
            cc = -1
            for j in range(len(Pu)):
                cc += 1
                for k in Pu[j]:
                    if k == i:
                        DRV[i+str(j+1)+'m'][0] += ACm[i]
    #elimino termini nulli
    DRVm = elenca(DRV)
    for i in DRVm:
        cc = 0
        for k in DRV[i]:
            if k == 0:
                cc +=1
        if cc == len(S):
            del DRV[i]
    #estetica
    for i in DRV:
        for j in range(len(DRV[i])):
            DRV[i][j] = sym.nsimplify(DRV[i][j])
    return DRV

def Stampa_Associa_PuntiReazioni(DRV,DAR,s,n):
    RE  = Dividi_ReazioniVincolari(DAR,n)
    color.write('Determino le reazioni vincolari associate agli n sistemi:\n')
    #stampo tutto (a parte i 'sotto'-termini nulli)
    print('Si ha quindi che ogni punto di ogni corpo di ogni sistema è sottoposto alle seguenti reazioni:')
    print('I segni sono scritti rispetto le direzioni e1,e2,e3 (e non rispetto le freccie mostrate in precedenza).')
    for h in range(s):
        color.write('SISTEMA '+str(h)+':\n',colori['RossoAcceso'])
        for i in range(len(RE)):
            color.write('Corpo '+str(i+1)+':\n')
            cc = 0
            for j in DRV:
                if i+1 == int(j[1]):
                    if DRV[j][h] != 0:
                        color.write(str(j)[0],colori['Nero'])
                        color.write(str(j)[2],colori['Viola'])
                        color.write(' => ',colori['Blu'])
                        color.write(str(DRV[j][h]),colori['Blu'])
                        print()
                        cc = 1
            if cc == 0:
                print('∅')
        print()
'''
S = [[[1.0*F], [-0.5*F], [-0.5*F], [-0.5*F], [-0.5*F], [0], [-1.0*F], [2.0*F], [0]], [[0], [0], [0], [0], [-1.0000], [1.0000], [0], [0], [-1.0000]]]
DAR = {'A1Ⓝ': 180, 'F3Ⓝ': 90, 'C1Ⓝ': 90, 'C1C2Ⓝ': 90, 'C2C3Ⓝ': 90, 'E2E3Ⓝ': 90, 'C1Ⓣ': 0, 'C1C2Ⓣ': 0, 'C2C3Ⓣ': 0}
DR = {'E2E3Ⓣ': [0, 0]}
AC  = [{'G': 2*F}, {'B': F}, {'D': F*l}]
AD  = [{}]
Pr  = ['ABC', 'CGE', 'CDEF']  
print(Associa_PuntiReazioni(S,DAR,DR,AC,AD,Pr))
'''
def idonea_AD(AD,ADP,D):
    #creo dizionario che unisce i dizionari di AD in un unico segnando come terzo elemento della lista associata il numero corrispondente alla direzione, invertendole
    A = {}
    for h in range(len(AD)):
        for i in AD[h]:
            A[i] = AD[h][i]
            if h == 0:
                A[i].append(1)
            else:
                A[i].append(0)
    #creo dizionario simil ADP che però considera le travi associate alle liste
    DT = {}
    for i in ADP:
        if len(i) == len(ADP[i]):
            DT[i] = [ADP[i]]
        else:
            DT[i] = []
            for j in range(len(ADP[i])-1):
                DT[i].append(ADP[i][j]+ADP[i][j+1])
    #creo DD (output) e lo riempio
    DD = {}
    for i in DT:
        for j in DT[i]:
            #DD[j] = [i[0],A[i][0]+ξ*(A[i][1]-A[i][0])/abs(D[i[0]][A[i][2]]/l-D[i[1]][A[i][2]]/l)*l]
            DD[j] = [i[0],A[i][0]+ξ*(A[i][1]-A[i][0])/abs(D[i[0]][A[i][2]]-D[i[1]][A[i][2]])]#/l * l è ancora necssario?##abs?
    return DD  

def Associa_TraviAzioni(DRV,L,AD,ADP,D):
    #numero sistemi:
    for i in DRV:
        s = len(DRV[i])
        break
    #lista di dizionari (uno a corpo) di liste (una a sistema) di liste (di 3 elementi:x,y,m) che associano (i dizionari) ad ogni trave le forze applicate nel primo punto descrivente la trave
    DRVT = []
    for i in range(len(L)):
        DRVT.append({})
    for i in range(len(L)):
        for j in L[i]:
            M1 = []
            for k in range(s):
                M2 = []
                for h in range(3):
                    M2.append(0)
                M1.append(M2)
            DRVT[i][j] = M1
    #Sommo tutto meno che i contributi
    V = elenca(DRV) #['A1y', 'C1y', 'C2y', 'C2m', 'F2y', 'F2m']
    for i in range(len(L)):
        for j in L[i]:
            for k in DRV:
                for h in range(s):
                    if k[0] == j[0]:
                        if k[1] == str(i+1):
                            if k[2] == 'x':
                                DRVT[i][j][h] = somma(DRVT[i][j][h],[DRV[k][h],0,0])
                            elif k[2] == 'y':
                                DRVT[i][j][h] = somma(DRVT[i][j][h],[0,DRV[k][h],0])
                            elif k[2] == 'm':
                                DRVT[i][j][h] = somma(DRVT[i][j][h],[0,0,DRV[k][h]])
    #Sto considerando anche il caso (capitato in un solo esame dal 2012 ad oggi) di azione distribuita non costante. Se cosi fosse credo il suo valore vada integrato per ξ (e non moltiplicato) ma devi verificarlo!! per ora procedo cosi. Se invece l'asta dovesse essere inclinata (mai capitato) credo che vada considerata una sola delle due proiezioni.. se cosi non fosse bisogna cambiare si qua sia nelle reazioni vincolari
    #mancano seni e coseni (caso mai capitato nei testi d'esame, però...)
    if len(AD) != 0:
        DD = idonea_AD(AD,ADP,D)
        ADE  = [elenca(AD[0]),elenca(AD[1])]
        ADE2 = [[],[]]
        for i in range(len(ADE)):
            for j in range(len(ADE[i])):
                if ADE[i][j] in ADP:
                    for k in range(len(ADP[ADE[i][j]])-1):
                        ADE2[i].append(ADP[ADE[i][j]][k]+ADP[ADE[i][j]][k+1])
        for h in range(len(AD)):
            for i in DD:
                if i in ADE2[h]:
                    for k in range(len(DRVT)):
                        if i in DRVT[k]:
                            if h == 0:
                                DRVT[k][i][0] = somma(DRVT[k][i][0],[  sym.integrate(DD[i][1],ξ),0,0])
                            else:
                                DRVT[k][i][0] = somma(DRVT[k][i][0],[0,sym.integrate(DD[i][1],ξ)  ,0])
    #estetica
    for i in range(len(DRVT)):
        for j in DRVT[i]:
            for h in range(s):
                for k in range(3):
                    DRVT[i][j][h][k] = sym.nsimplify(DRVT[i][j][h][k])
    DRVTs1 = copy.deepcopy(DRVT)#output di sola stampa    
    ###########################
    DRVTC = copy.deepcopy(DRVT)
    DRVT2 = copy.deepcopy(DRVT)#serve per stampare i contributi dei momenti correttamente ma mandare ai momenti il DRVT senza le codizioni al contorno affinchè non consideri due volte i momenti esterni
    ##N.B: Hai scelto di fare L NON cumulativo. Se cambi idea cancella riga e sostituisci sotto DRVTC con DRVT #Se L è comulativo DEVE essere ordinato (ora lo è già per corpi con soli due estremi liberi), se non lo è (come ora) non interessa che lo sia.
    for i in range(len(L)):
        for j in L[i]:
            for c in L[i][j]:
                for h in range(s):
                    b = [DRVTC[i][c][h][0],DRVTC[i][c][h][1]]
                    for g in range(len(b)):
                        e = []
                        for t in str(b[g]):
                            e.append(t)
                        if 'ξ' in e:
                            b[g] = b[g].subs(ξ,distanza(D[c[0]],D[c[1]]))
                    DRVT[i][j][h]  = somma([DRVT[i][j][h][0], DRVT[i][j][h][1], DRVT[i][j][h][2]],  [b[0],b[1],DRVTC[i][c][h][2]])
                    DRVT2[i][j][h] = somma([DRVT2[i][j][h][0],DRVT2[i][j][h][1],DRVT2[i][j][h][2]], [b[0],b[1],0])
                    #estetica
                    for w in range(len(DRVT[i][j][h])):
                        DRVT[i][j][h][w] = sym.nsimplify(DRVT[i][j][h][w])
                    for w in range(len(DRVT2[i][j][h])):
                        DRVT2[i][j][h][w] = sym.nsimplify(DRVT2[i][j][h][w])
    DRVTs2 = copy.deepcopy(DRVT)#output di sola stampa                    
    return [DRVT2,DRVTs1,DRVTs2]

def Stampa_Associa_TraviAzioni(DRVTs1,DRVTs2,s):
    c = 1
    if s == 1:
        c = 0
    color.write('Ogni tratto di trave è, singolarmente, sottoposto alle seguenti azioni concentrate:\n',colori[['Nero','Blu'][c]])# forze lungo e1 ed e2:')
    for h in range(s):
        if c == 1:
            color.write('SISTEMA '+str(h)+'\n',colori['RossoAcceso'])
        cc = 0
        for i in DRVTs1:
            cc += 1
            color.write('Corpo'+str(cc)+'\n',colori[['RossoAcceso','Nero'][c]])
            for j in i:
                color.write('Tratto ',colori['Blu'])
                color.write(str(j)+':  ')
                if len(stampavettore(i[j][h])) != 0:
                    print(sstampavettore(i[j][h]))
                else:
                    print('∅')
    color.write('\nConsiderando anche le forze trasmesse alle travi da quelle adiacenti:\n',colori[['Nero','Blu'][c]])
    for h in range(s):
        if c == 1:
            color.write('SISTEMA '+str(h)+'\n',colori['RossoAcceso'])
        cc = 0
        for i in DRVTs2:
            cc += 1
            color.write('Corpo '+str(cc)+'\n',colori[['RossoAcceso','Nero'][c]])
            for j in i:
                color.write('Tratto ',colori['Blu'])
                color.write(str(j)+':  ')
                if len(stampavettore(i[j][h])) != 0:
                    print(sstampavettore(i[j][h]))
                else:
                    print('∅')
    print()

def StampaConvenzioniSuiSegni():
    print('Convenzione sui segni di N, T, M nei diagrammi delle sollecitazioni:\n')
    color.write('      N',colori['Viola'])
    color.write('              T',colori['Verde'])
    color.write('              M\n',colori['RossoAcceso'])
    color.write('      _',colori['Viola'])
    color.write('              _',colori['Verde'])
    color.write('              _\n',colori['RossoAcceso'])
    color.write('   ← |+| →',colori['Viola'])
    color.write('        ↓ |+| ↑',colori['Verde'])
    color.write('        ↻ | | ↺\n',colori['RossoAcceso'])
    color.write('      ¯',colori['Viola'])
    color.write('              ¯',colori['Verde'])
    color.write('              ¯\n\n',colori['RossoAcceso'])
    print('N.B.: Se la convenzione sui segni di N e T è arbitraria, per M si sceglie di rappresentarare le sollcitazioni nel verso delle fibre tese.')

def Associa_Trave_NT(DRVT,D):
    #NON TESTATO CON ASTE INCLINATE (ma non dovrebbe far differenza)
    NT = []
    for i in DRVT:
        for j in i:
            s = len(i[j])
            break
        break
    for i in range(len(DRVT)):
        NT.append({})
    for i in range(len(DRVT)):
        for j in DRVT[i]:
            M1 = []
            for k in range(s):
                M2 = []
                for h in range(2):
                    M2.append(0)
                M1.append(M2)
            NT[i][j] = M1
    for i in range(len(DRVT)):
        for j in DRVT[i]:
            a = direzione(D[j[0]],D[j[1]])
            for h in range(s):
                NT[i][j][h][0] -= sym.cos(rad(a))*DRVT[i][j][h][0]
                NT[i][j][h][0] -= sym.sin(rad(a))*DRVT[i][j][h][1]
                #assicurarsi che sotto sia corretto
                NT[i][j][h][1] += sym.sin(rad(a))*DRVT[i][j][h][0]
                NT[i][j][h][1] -= sym.cos(rad(a))*DRVT[i][j][h][1]
    #estetica
    for i in range(len(NT)):
        for j in NT[i]:
            for h in range(s):
                NT[i][j][h][0] = sym.nsimplify(NT[i][j][h][0])
                NT[i][j][h][1] = sym.nsimplify(NT[i][j][h][1])
    return NT

def Separa_NT(NT):
    N = {}
    T = {}
    for i in NT:
        for j in i:
            N[j] = []
            T[j] = []
            for k in i[j]:
                N[j].append(k[0])
                T[j].append(k[1])
    return [N,T]

def Associa_Trave_M(NT,DRVT,L,D):
    nntt = Separa_NT(NT)
    N,T = nntt[0],nntt[1]
    for i in DRVT:
        for j in i:
            s = len(i[j])
            break
        break
    DM = {}
    for i in range(len(DRVT)):
        for j in DRVT[i]:
            M1 = []
            for k in range(s):
                M1.append(DRVT[i][j][k][2])#fleres mette -;rossi mette +. se cambi qui cambia anche giu
            DM[j] = M1
    #prima solo integrale di T e poi le azioni concentrate 
    M = {}
    for i in T:
        M1 = []
        for j in range(s):
            M1.append(0)
        M[i] = M1
    for h in range(s):
        for i in T:
            M[i][h] = sym.integrate(T[i][h],ξ)#fleres mette -;rossi mette +. se cambi qui cambia anche su
    for h in range(s):
        for i in M:
            M[i][h] += DM[i][h]
            '''
            M[i][h] += sym.nsimplify(DM[i][h])
            '''
    ############################################
    #il prossimo passaggio, reso commento, serve in caso di errori nel passaggio successivo a questo per rendere tali errori piu facilmente riconoscibili.
    '''
    color.write('\nMomenti senza condizioni al contorno:\n',colori['RossoAcceso'])
    for h in range(s):
        color.write('SISTEMA '+str(h)+':\n')
        cc = 0
        for i in NT:
            cc += 1
            color.write('Corpo '+str(cc)+':\n')
            for j in i:
                if M[j][h] != 0:
                    color.write('Ms'+str(h)+'(',colori['RossoAcceso'])
                    color.write(j+'(ξ)',colori['Nero'])
                    color.write(')',colori['RossoAcceso'])
                    color.write('= ',colori['Blu'])
                    print(M[j][h].evalf(5))
                else:
                    color.write('Ms'+str(h)+'(',colori['RossoAcceso'])
                    color.write(j+'(ξ)',colori['Nero'])
                    color.write(')',colori['RossoAcceso'])
                    color.write('= ',colori['Blu'])
                    print('∅')
    '''
    #c.c:
    #Il modo piu elegante per sostituire è il seguente. Per motivi sconosciti non funziona, quindi lo faccio sotto con replace() invece che con sub
    #dinanzi quindi, prima il caso, funzionante, con DRVT(C) e, subito dopo, l'equivalente con Mf
    Mf = copy.deepcopy(M)#DDDDDDDDDDDDDDDDDDDD
    for h in range(s):
        for c in L:
            for i in c:
                for k in c[i]:
                    w = Mf[k][h]
                    e = []
                    for t in str(w):
                        e.append(t)
                    if 'ξ' in e:
                        w = w.subs(ξ,distanza(D[k[0]],D[k[1]]))
                    M[i][h] += w
                    '''
                    M[i][h] += sym.nsimplify(w)
                    '''
    #M SEGNO OPPOSTO!!
    for i in M:
        for j in range(len(M[i])):
            M[i][j] = -M[i][j]
    return [N,T,M]

#Per far si che le funzioni Stampa funzionino sia per i diagrammi parziali che per quelli finali
def ControlloStampa(F):
    for i in F:
        if type(F[i]) == list:
            return [F,1]
        else:
            F[i] = [F[i]]
    return [F,0]

def StampaNoToM(NoToM,L,strNoToM):
    C = ControlloStampa(NoToM)
    X,c = C[0],C[1]
    if strNoToM == 'N':
        Le,Az,Co = 'N','\nAzioni normali:\n','Viola'
    elif strNoToM == 'T':
        Le,Az,Co = 'T','\nAzioni tangenti:\n','Verde'
    elif strNoToM == 'M':
        Le,Az,Co = 'M','\nMomenti:\n','Rosso'
    for i in NoToM:
        s = len(NoToM[i])
        break
    y = 0
    for h in range(s):
        for i in L:
            for j in i:
                if len(str(NoToM[j][h])) > y:
                    y = len(str(NoToM[j][h]))
    y += 1
    color.write(Az,colori[Co])
    for h in range(s):
        H = 's'+str(h)
        if c == 1:
            color.write('SISTEMA '+str(h)+':\n')
        else:
            H = 'f'
        cc = 0
        for i in L:
            cc += 1
            color.write('Corpo '+str(cc)+':\n')
            for j in i:
                if NoToM[j][h] != 0:
                    a = ' '
                    if str(NoToM[j][h])[0] == '-':
                        a = ''
                    b = ' '
                    if str(ss(NoToM[j][h]))[0] == '-':
                        b = ''
                    color.write(Le+H+'(',colori[Co])
                    color.write(j+'(ξ)',colori['Nero'])
                    color.write(')',colori[Co])
                    color.write(' = ',colori['Nero'])
                    color.write(a+str(NoToM[j][h]),colori['Blu'])
                    color.write(' '*(y-len(str(NoToM[j][h]))-len(a))+' = ',colori['Nero'])
                    print(b+str(ss(NoToM[j][h])))
                else:
                    color.write(Le+H+'(',colori[Co])
                    color.write(j+'(ξ)',colori['Nero'])
                    color.write(')',colori[Co])
                    color.write(' =  ',colori['Nero'])
                    print('∅')
    
def StampaNTM(N,T,M,L):
    StampaNoToM(N,L,'N'),StampaNoToM(T,L,'T'),StampaNoToM(M,L,'M')


#MANCANO CEDIMENTI DEI VINCOLI RELATIVI!!quando applicati 'allo stesso corpo' ho dubbi quindi ancora non li ho aggiunti
def LavoroEsterno(DRV,DA,DC):
    '''
    color.write('\nLavoro esterno:\n',colori['Rosso'])
    for i in DRV:
        print(i,DRV[i])
    print()
    ########################
    '''
    DCS = {}
    for i in DC:
        s = spezza(i)
        if len(s) == 1:
            if i[1] != 0:
                DCS[i] = s
        else:
            if s[0][1] != s[1][1]:
                DCS[i] = s
            else:
                DCS[i] = [s[0]]
                '''
                    ###COSI POSSO SBAGLIARMI COL SEGNO DEL LAVORO ESTERNO!!!
                    color.write('ATTENZIONE:',colori['Warning'])
                    print('\nPotrebbe esserci un errore nel segno del lavoro interno...')
                    print('Credo in realtà di aver risolto questo problema!!')
                    print('Anche se, se un pendolo interno ha due f* diverse (somma pendolo + altro) allora non so bene che vada fatto... ma questa cosa non lho mai vista in alcun esame..')
                    #cosi prendo i Le dei vincoli interni inerenti lo stesso corpo una sola volta...
                '''
    #print(DCS)
    ########################
    DRS = {}
    for i in DRV:
        DRS[i] = DRV[i][1:]
    for i in DRS:
        s = len(DRS[i])
        break
    Le = []
    for i in range(s):
        Le.append(0)
    '''
    print(DRV)
    print(DA)
    print(DC)
    print()
    print(DCS)
    print(DRS)
    print()
    '''
    #print(DCS)
    for h in range(s):
        for i in DRS:
            A = DRS[i][h]#azione
            P = i[:-1]#punto
            d = i[-1]#direzione
            for j in DC:
                if DC[j] != 0:
                    if len(j) > 2:###########
                        if P in DCS[j]:######
                            if j[-1] in ['ⓝ','ⓣ','ⓔ','㊈','㊆']:#'Ⓝ','Ⓣ'
                                if   d == 'x':
                                    Le[h] += sym.cos(rad(DA[j]))*A*DC[j]
                                elif d == 'y':
                                    Le[h] += sym.sin(rad(DA[j]))*A*DC[j]
                            elif j[-1] in ['ⓐ','㊅']:
                                if   d == 'm':
                                    Le[h] += A*DC[j]
                                #print(Le)
    return Le

def Deformazioni_Termiche(CT):
    Dεt = {}
    Dχt = {}
    for i in CT:
        Dεt[i] =   α*(CT[i][1]+CT[i][0])/2
        Dχt[i] =   α*(CT[i][1]-CT[i][0])/CT[i][2]#caso spessori diversi (tc[2])
    return [Dεt,Dχt]


def Stampa_Deformazioni_Termiche(CT):
    cc = 0
    for i in CT:
        if CT[i][0] != CT[i][1]:
            cc += 1
    if cc > 0:
        color.write('\nPremessa, alle equazioni di Müller-Breslau, riguardante le azioni termiche :\n')
        l1,l2,l3,l4 = 'è','e','','ha'
        if cc == 2:
            l1,l2,l3,l4 = 'sono','i','no','anno'
        print('Vi',l1,cc,'trav'+l2,'che separa'+l3,'due ambenti a temperature uniformi ma distinte')
        print('che',l4,"sezione 'h' << 'l', motivo per cui l'incremento termico è considerabile lineare luno 'h' secondo la legge di Fourier.")
        print('Detto α il coefficiente di dilatazione termica, si ha quindi che:')
        for i in CT:
            if CT[i][0] != CT[i][1]:
                print()
                color.write('{ ϑ(',colori['Marrone'])
                color.write(i)
                color.write(')',colori['Marrone'])
                color.write(' = ('+str(CT[i][1])+'+'+str(CT[i][0])+')/2',colori['Blu'])
                color.write('   '+'_'*6+'|\  ')
                color.write('εt(',colori['Marrone'])
                color.write(i)
                color.write(')',colori['Marrone'])
                print(' = α*ϑ      = ',α*(CT[i][1]+CT[i][0])/2)
                color.write('{Δθ(',colori['Marrone'])
                color.write(i)
                color.write(')',colori['Marrone'])
                color.write(' = ('+str(CT[i][1])+'-'+str(CT[i][0])+')/2',colori['Blu'])
                color.write('   '+'¯'*6+'|/  ')
                color.write('χt(',colori['Marrone'])
                color.write(i)
                color.write(')',colori['Marrone'])
                print(' = 2*α*Δθ/h =  ',(CT[i][1]-CT[i][0])/CT[i][2])

def Lavoro_Molle(Mol,Molle):
    #Mol   = {'A1':  k}
    #Molle = {'A1': [1.0*l*p, 0.5]}
    M = {}
    for i in Molle:
        M[i] = [Molle[i],Mol[i]]
    return M

def Separa_NTMo_NTMj(NTM):
    NTMo = [{},{},{}]
    NTMj = [{},{},{}]
    for i in range(len(NTM)):
        for j in NTM[i]:
            if j not in NTMj[i]:
                NTMj[i][j] = []
            cc = -1
            for k in NTM[i][j]:
                cc += 1
                if cc == 0:
                    NTMo[i][j] = k
                else:
                    NTMj[i][j].append(k)
    return [NTMo,NTMj]

def LavoriVirtuali(NTM,R,EC,CT,Le,D,Sub):
    '''
    print('Fi δ + |Mi θ + Ti v + Ni u|(l,0) = Σ(per ogni trave)')
    print('∫{(Ni(x)[(No(x) + Σ(j=1,s) Xj Nj(x))/A(x)  + εt(x)] +')
    print('+ (Ti(x)[(To(x) + Σ(j=1,s) Xj Tj(x))/C(x)] +')
    print('+ (Mi(x)[(Mo(x) + Σ(j=1,s) Xj Mj(x))/B(x)  + χt(x)]} dx, 0<x<l_trave +')
    print('+ (Fi   [(Fo    + Σ(j=1,s) Xj Fj)   /Ki]')
    #print('ove: εt = α<θ>              e  χt = 2αΔθ/h')
    #print('ove:       <θ> = (θ0+θ1)/2  e         Δθ = (θ1-θ0)/2\n')
    '''
    #separo il il sistema 0 dagli altri s sistemi
    ntm = Separa_NTMo_NTMj(NTM)
    NTMo, NTMj = ntm[0],ntm[1]
    #calcolo il numero (s) di sistemi ausiliari 
    for i in range(len(NTMj)):
        for j in NTMj[i]:
            s = len(NTMj[i][j])
            break
        break
    #creo  Xj (simbolo) e lista soluzioni:
    X,XS = [],[]
    for h in range(s):
        X.append(sym.sympify(sym.symbols('X'+str(h+1))))
        XS.append(0)
    #moltiplichiamo ogni NTMj[i] per X[i] e creiamo un nuovo NTMj (di 3 elementi) di 1 elemento
    NTMvero = [{},{},{}]
    for i in range(len(NTMj)):
        for j in NTMj[i]:
            if j not in NTMvero[i]:
                NTMvero[i][j] = 0
            cc = -1
            for k in NTMj[i][j]:
                cc += 1
                NTMvero[i][j] += k*X[cc]
    #sommo ad ogni NTMvero[i] il rispettivo NTMo
    NTM0X = [{},{},{}]
    for i in range(len(NTMo)):
        for j in NTMo[i]:
            NTM0X[i][j] = NTMo[i][j] + NTMvero[i][j]
    #divido per le relative rigidezze:
    NTMR = [{},{},{}]
    for i in range(len(NTM0X)):
        for j in NTM0X[i]:
            if R[j][i] != 0:
                NTMR[i][j] = NTM0X[i][j]/R[j][i]
            else:
                NTMR[i][j] = 0
    #aggiungo εt e χt risp a N e M
    CTN,CTM = CT[0],CT[1]
    for i in CTN:
        for j in NTMR[0]:
            if j == i:
                NTMR[0][j] += CTN[i]
    for i in CTM:
        for j in NTMR[2]:
            if j == i:
                NTMR[2][j] += CTM[i]
    #calcolo le molle, separatamente da NTM
    #caso in cui la molla è un vincolo rilassato:
    ECs,ECk = EC[0],EC[1]
    ECr = {}
    for i in ECs:
        if i[-1] == 'ⓔ':
            ECr[i[:-1]] = ECs[i]
    for i in ECr:
        if i+'ⓔ' in ECs:
            del ECs[i+'ⓔ']
    SM = {}
    for i in ECr:
        SM[i] = ECr[i][2]
        ECr[i] = ECr[i][:-1]
    #change
    ECO,ECN = {},{}
    for i in ECs:
        ECO[i] = ECs[i][0]
        ECN[i] = ECs[i][1:]
    #change
    for i in ECr:
        if i not in ECO:
            ECN[i] = []
            for j in range(s):
                ECN[i].append(0)
    for i in SM:
        ECO[i] = ECr[i][0]
        ECr[i] = ECr[i][1:]
    for i in SM:
        ECN[i][SM[i]] += ECr[i][SM[i]]
    #sum(Fo + Fi*Xi)

    FoX = {}
    e = elenca(ECN)
    for i in e:
        cc = -1
        FoX[i] = ECO[i]
        for j in ECN[i]:
            cc += 1
            FoX[i] += j*X[cc]
        FoX[i] = FoX[i]/ECk[i]
    #Fi*(Fo + Fi*Xi)
    FF = {}
    for h in range(s):
        for i in FoX:
            if i not in FF:
                FF[i] = [0]
            else:
                FF[i].append(0)
    for h in range(s):
        for i in FoX:
            FF[i][h] = ECN[i][h]*FoX[i]
    #calcolo, per ogni sistema l'"interno" finale di ogni integrale
    SNTM = [{},{},{}]
    for h in range(s):
        cc = -1
        for i in NTMR:
            cc += 1
            for j in i:
                if j not in SNTM[cc]:
                    SNTM[cc][j] = []
                SNTM[cc][j].append([])    
    dd = []
    for i in range(3):
        dd.append([])
        for h in range(s):
            dd[i].append(0)
    for h in range(s):#sistema 1,2,..n
        cc = -1
        for i in NTMR:#N,T,M
            cc += 1
            for j in i:#aste
                SNTM[cc][j][h] = NTMj[cc][j][h]*NTMR[cc][j]
                if SNTM[cc][j][h] != 0:
                    dd[cc][h] += 1
    #Risultati
    RSNTM = copy.deepcopy(SNTM)
    for h in range(s):
        cc = -1
        for i in RSNTM:
            cc += 1
            for j in i:
                if RSNTM[cc][j][h] != 0:
                    RSNTM[cc][j][h] = sym.integrate(RSNTM[cc][j][h],(ξ,0,distanza(D[j[0]],D[j[1]])))
                    '''
                    RSNTM[cc][j][h] = sym.nsimplify(sym.integrate(RSNTM[cc][j][h],(ξ,0,distanza(D[j[0]],D[j[1]]))))
                    '''
    #Somma Risultati (divisi per N,T,M,F)
    S = [[],[],[],[]]
    for h in range(s):
        for i in range(len(S)):
            S[i].append(0)
    for h in range(s):
        cc = -1
        for i in RSNTM:
            cc += 1
            for j in i:
                S[cc][h] += RSNTM[cc][j][h]
    for h in range(s):
        for i in FF:
            S[3][h] += FF[i][h]
    #Somma finale
    SF = []
    for h in range(s):
        SF.append(0)
    for h in range(s):
        for i in S:
            SF[h] += i[h]
    #estetica
    for h in range(s):
        for i in S:
            SF[h] = sym.nsimplify(SF[h])
    #Valore azione campionatrice:
    for h in range(s):
        if SF[h]-Le[h] != 0:
            XS[h] = sym.solve(SF[h]-Le[h],X[h])[0]
        else:
            XS[h] = 0
    '''
    print('\n\n\n\n\n')
    print(XS)
    print('\n\n\n\n\n')
    for i in XS:
        print(i)
        print()
    print('\n\n\n\n\n')
    '''
    #Dà problemi quando una soluzione è nulla (che poi non deve esserci sol. nulla...)
        
#    XS = [-164546548637357353441199*l*p/43200542691055847070735 - 14691690910360429588000*(5)**(1/2)*l*p/8640108538211169414147,0]#####

    #sistema fra i risultati ottenuti:
    XSc = copy.deepcopy(XS)#output di sola stampa. XS pre-sistema
    if len(XS) > 0:
        soluzione = sym.linsolve((nsottrazione(XS,X)), (X))
        ########Nsottrazione (prima era senza n)
        #nsottrazione funziona. linsolve() carica come in un loop :(
        cc = -1
        for i in soluzione:
            for j in i:
                cc += 1
                XS[cc] = j
    XSsub = copy.deepcopy(XS)#output di sola stampa. XS post-sistema, pre-sostituzioni. == XSc se vi è una sola X
    #Sostituisco, eventualmente, i termini noti:
    for i in Sub:
        for h in range(s):
            if str(i) in str(XS[h]):#b[g] = b[g].subs(ξ,distanza(D[c[0]],D[c[1]]))
                XS[h] = XS[h].subs(i,Sub[i])#sym.nsimplify(XS[h].replace(i,Sub[i]))#replace??
    return [XS,XSc,XSsub,RSNTM,SNTM,NTM,S,FF,SF,ECk,X,Le,D,Sub,dd,s]


                
def Stampa_LavoriVirtuali(u):
    XS,XSc,XSsub,RSNTM,SNTM,NTM,S,FF,SF,ECk,X,Le,D,Sub,dd,s = u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14],u[15]
    #spiego cosa sto facendo
    lettera1 = 'a'
    lettera2 = 'e'
    if s > 1:
        lettera1 = 'e'
        lettera2 = 'i'
    print("Sfrutto l'ipotesi dei lavori virtuali per ricavare il valore dell"+lettera1+' forz'+lettera1+' campionatric'+lettera2+':\n')
    #stampo le equazioni
    color.write('LAVORO ESTERNO:\n',colori['Nero'])
    for h in range(s):
        color.write('Sistema '+str(h+1)+':\n',colori['RossoAcceso'])
        color.write('Fi δ + |Mi θ + Ti v + Ni u|(l,0)',colori['Viola'])
        color.write(' = ')
        print(Le[h])
    color.write('\nLAVORO INTERNO:\n',colori['Nero'])
    for h in range(s):
        color.write('Sistema '+str(h+1)+':\n',colori['RossoAcceso'])
        cc = -1
        for i in SNTM:
            cc += 1
            if cc == 0 and dd[cc][h] != 0:
                color.write('∫(Ni(ξ)[(No(ξ) + Σ(j=1,s) Xj Nj(ξ))/A(ξ) + εt(ξ)] dξ:\n\n',colori['Viola'])
            if cc == 1 and dd[cc][h] != 0:
                color.write('∫(Ti(ξ)[(To(ξ) + Σ(j=1,s) Xj Tj(ξ))/C(ξ)] dξ:\n\n',colori['Viola'])
            if cc == 2 and dd[cc][h] != 0:
                color.write('∫{(Mi(ξ)*[(Mo(ξ) + Σ(j=1,s) Xj*Mj(ξ))/B(ξ) + χt(ξ)]}dξ:  \n\n',colori['Viola'])
            for j in i:
                if SNTM[cc][j][h] != 0:
                    color.write(' '+str(j)+'(ξ): ',colori['Nero'])
                    print('∫'+str(ss(SNTM[cc][j][h])),'dξ, 0<ξ<'+str(ss(distanza(D[j[0]],D[j[1]]))))
                    color.write('∫'+str(j)+'(ξ)dξ 0<ξ<'+str(ss(distanza(D[j[0]],D[j[1]])))+': ',colori['Nero'])
                    color.write(str(RSNTM[cc][j][h]),colori['Blu'])
                    color.write(' = ')
                    print(ss(RSNTM[cc][j][h]))
                    print()
                elif dd[cc][h] != 0:
                    color.write(' '+str(j)+'(ξ): ',colori['Nero'])
                    print('0')
                    color.write('∫'+str(j)+'(ξ)dξ 0<ξ<'+str(ss(distanza(D[j[0]],D[j[1]])))+': ',colori['Nero'])
                    print('0')
                    print()
            if dd[cc][h] != 0:
                if cc == 0:
                    color.write('Σ ∫(Ni(ξ)[(No(ξ) + Σ(j=1,s) Xj Nj(ξ))/A(ξ) + εt(ξ)] dξ:\n',colori['Viola'])
                if cc == 1:
                    color.write('Σ ∫(Ti(ξ)[(To(ξ) + Σ(j=1,s) Xj Tj(ξ))/C(ξ)] dξ:\n',colori['Viola'])
                if cc == 2:
                    color.write('Σ ∫{(Mi(ξ)*[(Mo(ξ) + Σ(j=1,s) Xj*Mj(ξ))/B(ξ) + χt(ξ)]}dξ:\n',colori['Viola'])
                color.write(str(S[cc][h]),colori['Blu'])
                color.write('\nSemplificandola:\n',colori[['Viola','Viola','Viola'][cc]])
                print(ss(S[cc][h]),'\n')
            if cc == 2 and len(ECk)>0:
                color.write('Fi*[(Fo + Σ(j=1,s) Xj*Fj)/Ki]:\n',colori['Nero'])
                for j in FF:
                    color.write(str(j)+': ',colori['Nero'])
                    color.write(str(FF[j][h])+'\n',colori['Blu'])
                    if FF[j][h] != 0:
                        color.write(' = ')
                        print(ss(FF[j][h]),'\n')
                color.write('Σ Fi*[(Fo + Σ(j=1,s) Xj*Fj)/Ki]: \n',colori['Nero'])
                color.write(str(S[3][h]),colori['Blu'])
                if S[3][h] != 0:
                    color.write('\nSemplificandola:\n')
                    print(ss(S[3][h]))
                print()
        color.write('EQUAZIONE FINALE:\n')
        color.write(str(Le[h]),colori['Blu'])
        color.write(' = ',colori['Blu'])
        print(SF[h])
        color.write('Semplificandola:\n')
        color.write(str(ss(Le[h])),colori['Blu'])
        color.write(' = ',colori['Blu'])
        print(ss(SF[h]),'\n')
        color.write('VALORE AZIONE CAMPIONATRICE:\n')
        color.write(str(X[h]),colori['Arancione'])
        color.write(' = ',colori['Nero'])
        color.write(str(XSc[h]),colori['Blu'])
        color.write(' = ')
        print(ss(XSc[h]),'\n')
    #stampo le soluzioni frutto della messa a sistema delle varie equazioni f(Xj)
    if len(XS) > 1:
        color.write('Mettendo a sistema i risultati ottenuti:\n')
        y = 0
        for i in range(len(XSc)):
            if len(str(XSc[i])) > y:
                y = len(str(XSc[i]))
        y += 1
        for i in range(len(XSc)):
            color.write('{')
            color.write(str(X[i]),colori['Arancione'])
            color.write(' = ')
            color.write(str(XSc[i]),colori['Blu'])
            color.write(' '*(y-len(str(XSc[i])))+' = ')
            print(ss(XSc[i]))
        color.write('\nValori forze campionatrici:\n')
        y = 0
        for i in range(len(XSsub)):
            if len(str(XSsub[i])) > y:
                y = len(str(XSsub[i]))
        y += 1
        for i in range(len(XSsub)):
            a = ' '
            if str(XSsub[i])[0] == '-':
                a = ''
            b = ' '
            if str(ss(XSsub[i]))[0] == '-':
                b = ''
            color.write(str(X[i]),colori['Arancione'])
            color.write(' = ')
            color.write(a+str(XSsub[i]),colori['Blu'])
            color.write(' '*(y-len(str(XSsub[i]))-len(a))+' = ')
            print(b+str(ss(XSsub[i])))
    #Stampo, eventualmente, le Xj sostituendoci i valori noti
    if XSsub != XS:
        color.write('Sostituendo i valori noti, ovvero:\n')
        for i in Sub:
            #color.write(str(i))
            color.write(str(i)+' '*(4-len(str(i))),colori['Verde'])
            print('= ',Sub[i])
        color.write('si ha:\n')
        y = 0
        for i in range(len(XS)):
            if len(str(XS[i])) > y:
                y = len(str(XS[i]))
        y += 1
        for i in range(len(XS)):
            a = ' '
            if str(XS[i])[0] == '-':
                a = ''
            b = ' '
            if str(ss(XS[i]))[0] == '-':
                b = ''
        for i in range(len(XS)):
            color.write(str(X[i]),colori['Arancione'])
            color.write(' = ')
            color.write(str(XS[i]),colori['Blu'])
            color.write(' '*(y-len(str(XS[i]))-len(a))+' = ')
            print(b+str(ss(XS[i])))

def DiagrammiFinali(XS,NTM,L):
    #separo il il sistema 0 dagli altri s sistemi 
    ntm = Separa_NTMo_NTMj(NTM)
    NTM,NTMj = ntm[0],ntm[1]
    #calcolo il numero (s) di sistemi ausiliari 
    for i in range(len(NTMj)):
        for j in NTMj[i]:
            s = len(NTMj[i][j])
            break
        break
    #calcolo NTM finale
    for h in range(s):
        for i in range(len(NTM)):
            for j in NTM[i]:
                NTM[i][j] += NTMj[i][j][h]*XS[h].evalf(5)
    #estetica
    for i in range(len(NTM)):
        for j in NTM[i]:
                NTM[i][j] = sym.nsimplify(NTM[i][j])
    #print('NTM =',NTM)
    #print()
    return NTM

def Stampa_DiagrammiFinali(NTM,L,s):
    N,T,M = NTM[0],NTM[1],NTM[2]
    StampaNTM(N,T,M,L)
    
def Stampe_Finali(DRV,XS,Pr):
    NX,TX,MX = '','',''
    for i in range(len(XS)):
        NX += '+ N'+str(i+1)+'*X'+str(i+1)
        TX += '+ T'+str(i+1)+'*X'+str(i+1)
        MX += '+ M'+str(i+1)+'*X'+str(i+1)
    print('Per la sovrapposizione degli effetti, i diagrammi finali delle azioni di contatto saranno dati da:')
    print('Nf = No',NX)
    print('Tf = To',TX)
    print('Mf = Mo',MX)
    print()
    DRV2 = {}
    for i in DRV:
        DRV2[i] = []
        for h in range(len(XS)+1):
            if h == 0:
                DRV2[i].append(DRV[i][h])
            else:
                DRV2[i].append(DRV[i][h]*XS[h-1])
    uno = []
    for i in range(len(XS)+1):
        uno.append(1)
    for i in DRV2:
        DRV2[i] = prodottoscalare(DRV2[i],uno)
    P = P_(Pr)
    color.write('Reazioni vincolari associate ad ogni punto:\n')
    for i in range(len(P)):
        color.write('Corpo n.'+str(i+1)+'\n',colori['RossoAcceso'])
        for j in P[i]:
            for k in DRV2:
                if k[:-1] == j:
                    print(k,'=>',DRV2[k])
    for i in DRV2:
        DRV2[i] = [DRV2[i]]
    print()
    return DRV2

def VerificaSoluzioneAzioniCampionatrici(SC,XS,AZC,DR,Stampa):
    if SC != -1:
        if AZC != '?':
            XSV,AZV = [],[]
            for i in XS:
                XSV.append(str(ss(i.evalf(4))))
            for i in range(len(AZC[SC-1])):
                a = str(ss(AZC[SC-1][i].evalf(4)))
                AZV.append(a)
            if XSV == AZV:
                if Stampa == True:
                    color.write('RISULTATO CORRETTO ✔\n',colori['Verde'])
                return [AZV,DR]
            else:
                if Stampa == True:
                    color.write('RISULTATO SBAGLIATO ✘\n',colori['RossoAcceso'])
                return [XSV,AZV,DR]
        else:
            return False
            
def StampaVerifica(x):
    if x != False:
        if len(x) > 1:
            d,l = len(x[0]),0
            for i in range(d):
                if len(x[0][i])>l:
                    l = len(x[0][i])
            if len(x) == 2:
                l += 2
                a,b = x[0],elenca(x[1])
                for j in range(d):
                    color.write('X'+str(j+1),colori['Nero'])
                    color.write(' = '+str(a[j]),colori['Blu'])
                    color.write(' '*(l-len(str(a[j])))+'=> ')
                    color.write(b[j],colori['Blu'])
                    color.write(' (angolo -> ')
                    color.write(str(x[1][b[j]][0]),colori['Blu'])
                    color.write(' '*(4-len(str(x[1][b[j]][0])))+'cedimento -> ')
                    color.write(str(x[1][b[j]][1]),colori['Blu'])
                    color.write(')\n')
            elif len(x) == 3:
                for i in range(d):
                    if len(x[1][i])>l:
                        l = len(x[1][i])
                l += 2
                a,b,c = x[0],x[1],elenca(x[2])
                color.write('Risultato corretto:\n',colori['Verde'])            
                for j in range(d):
                    color.write('X'+str(j+1),colori['Nero'])
                    color.write(' = '+str(b[j]),colori['Blu'])
                    color.write(' '*(l-len(str(b[j])))+'=> ')
                    color.write(c[j],colori['Blu'])
                    color.write(' (angolo -> ')
                    color.write(str(x[2][c[j]][0]),colori['Blu'])
                    color.write(' '*(4-len(str(x[2][c[j]][0])))+'cedimento -> ')
                    color.write(str(x[2][c[j]][1]),colori['Blu'])
                    color.write(')\n')
                color.write('Risultato ottenuto:\n',colori['RossoAcceso'])
                for j in range(d):
                    color.write('X'+str(j+1),colori['Nero'])
                    color.write(' = '+str(a[j]),colori['Blu'])
                    color.write(' '*(l-len(str(a[j])))+'=> ')
                    color.write(c[j],colori['Blu'])
                    color.write(' (angolo -> ')
                    color.write(str(x[2][c[j]][0]),colori['Blu'])
                    color.write(' '*(4-len(str(x[2][c[j]][0])))+'cedimento -> ')
                    color.write(str(x[2][c[j]][1]),colori['Blu'])
                    color.write(')\n')
        #print('\nLa verifica si basa sul confronto dei valori delle forze campionatrici fra quelle ottenute dal programma e quelle calcolate nel Vangelo secondo Fleres.\n\n')
        #print("\n(La verifica si basa sul confronto dei valori delle forze campionatrici rispetto i materiali open source gentilmente offerti da colleghi di studio del corso ing.mecc. dell'università La Sapienza disponibili sul Drive condiviso nei relativi gruppi social).")

def Stampa_DADC(DA,DC):
    l = 0
    for i in DA:
        if len(str(DA[i])) > l:
            l = len(str(DA[i]))
        if len(str(DC[i])) > l:
            l = len(str(DC[i]))
    color.write('DA   ')
    color.write('= {',colori['Blu'])
    dau,dcu = elenca(DA)[-1],elenca(DC)[-1]
    for i in DA:
        color.write(str(i)+': ',colori['Blu'])#['Blu','Viola'][1]])
        color.write(' '*(l-len(str(DA[i])))+str(DA[i]),colori['Blu'])
        if i != dau:
            color.write(', ',colori['Blu'])
        else:
            color.write('}\n',colori['Blu'])
    color.write('DC   ')
    color.write('= {',colori['Blu'])
    for i in DC:
        color.write(str(i)+': ',colori['Blu'])#['Blu','Viola'][1]])
        color.write(' '*(l-len(str(DC[i])))+str(DC[i]),colori['Blu'])
        if i != dcu:
            color.write(', ',colori['Blu'])
        else:
            color.write('}\n',colori['Blu'])

def Cinematica(A,DV,LD,DC,Pr):
    LagraDizio = copy.deepcopy(LD)
    v = len(DC)
    #punti di riferimenti (parametri lagrangiani)
    Lag = []
    for i in Pr:
        Lag.append(i[0])
    #[simboli q == parametri lagrangiani]
    q = []
    for i in range(len(A[0])):
        q.append(sym.sympify(sym.symbols('q'+str(i+1))))
    #vettore cedimenti
    C = []
    for i in DC:
        C.append(DC[i])
    #parte copia-incollata (con piccole modifiche) da: Cineamtica()
    if 1 == 1:
        q = Matrix(q)
        A = Matrix(A)
        C = Matrix(C)
        w = A**-1
        '''
        #rendo W stampabile in maniera esteticamente gradevole (matrice cinematica inversa) e lo stampo
        W = []
        for i in w:
            W.append([sym.sympify(i)])
        for i in range(len(W)):
            W[i] = [sym.sympify(str(W[i])[1:-1]).evalf(5)]
        K = []
        for i in range(v):
            V = []
            for j in range(v):
                V.append([])
            K.append(V)
        for i in range(v):
            for j in range(v):
                K[i][j] = W[j+v*i]
        for i in range(len(K)):
            for j in range(len(K[i])):
                K[i][j] = sym.sympify(str(K[i][j])[1:-1]).evalf(5)
        KKK = stampamatrice(K)
        for i in KKK:
            print(i)
        '''
        #rendo Q stampabile (vettore velocità) e lo stampo
        q = w*C
        Q = []
        for i in q:
            Q.append([sym.sympify(i)])
        #Q = pulisci(Q)
        for i in range(len(Q)):
            Q[i] = [sym.sympify(str(Q[i])[1:-1]).evalf(5)]
        color.write('\nVettore parametri lagrangiani:\n')
        cc = -1
        for i in range(len(Q)):
            cc += 1
            color.write('q'+str(cc+1),colori['Arancione'])
            print(' = '+str(Q[i])[1:-1])
        #stampo le velocità di ogni punti:
        color.write('\nInserendo i valori di q nelle equazioni delle velocità dei punti:\n')
        #Stringo Q e LagraDizio. Creo un vocabolario associato a Q. Replaccio i qi. RiSymizzo tutto che non si sanno mai le applicazioni future. Stampo.
        #print(LagraDizio)
        for i in LagraDizio:
            a = []
            for j in LagraDizio[i]:
                a.append(str(j))
            LagraDizio[i] = a
        for i in range(len(Q)):
            Q[i] = str(Q[i])[1:-1]
        VeloDizio = {}
        for i in range(len(Q)):
            VeloDizio['q'+str(i+1)] = Q[i]
        for i in LagraDizio:
            a = []
            for j in LagraDizio[i]:
                qq = j.count('q')
                for k in range(qq):
                    num = str(j[j.index('q')+1])
                    j = j.replace('q'+num,VeloDizio['q'+num])
                a.append(j)
            LagraDizio[i] = a
        for i in LagraDizio:
            a = []
            for j in LagraDizio[i]:
                a.append(sym.sympify(j))
            LagraDizio[i] = a
        a = []
        for i in Q:
            a.append([sym.sympify(i)])
        Q = a
        for i in LagraDizio:
            if i[0] == 'V':
                if i[1:] in Lag:
                    if i[1:] in punti:
                        color.write(str(i[0])+'(',colori['Rosso'])
                        color.write(i[1:])
                        color.write(')',colori['Rosso'])
                        print(' ='+' '*(3-len(str(i))),stampavettore(LagraDizio[i]))
                else:
                    color.write(str(i[0])+'(',colori['Rosso'])
                    color.write(i[1:])
                    color.write(')',colori['Rosso'])
                    color.write(' = '+' '*(3-len(str(i))))
                    if len(stampavettore(LagraDizio[i])) != 0:
                        print(stampavettore(LagraDizio[i]))
                    else:
                        print('0')
                    #print(str(i)+'='+' '*(3-len(str(i))),stampavettore(LagraDizio[i]))

def Stampa_IntroduzioneCinematica():
    print('Si avrà: A q = c, da cui possiamo ricavarci q = A^-1 c:')
    color.write("N.B.:")
    print("Stiamo considerando la velocità dei punti in funzione dei cedimenti esterni, senza considerare le velocità imposte dall'effetto della deformabilità delle travi e dalla presenza di azioni termiche. Le velocità finali totali dei punti saranno date dalla sovrapposizione dei vari contributi.")

def Stampa_ContributiVelocità(A,DV,LD,DC,Pr):
    Nc = 0
    for i in DC:
        if DC[i] != 0:
            Nc += 1
    if Nc > 1:
        print()
        print('Possiamo anche operare per sovrapposizione e vedere singolarmenti i contributi di ogni cedimento sulla velocità totale dei punti, che sarà data dalla somma delle velocità imposte da ogni cedimento preso singolarmente:')
        DC0 = {}
        for i in DC:
            DC0[i] = 0
        cont = 0
        for i in DC:
            if DC[i] != 0:
                DC0[i] = DC[i]
                print()
                color.write('Prendendo in esame il solo cedimento '+str(DC[i])+' relativo al vincolo '+str(i)+':',colori['Blu'])
                print()
                Cinematica(A,DV,LD,DC0,Pr)
                DC0[i] = 0
                
###################################################################################################
                    
#COSA MIGLIORARE:
#0) Colori :3
#1) Bilancio ai nodi -> programma un traliccio e adatta?
#2) Dall'analisi dei ranghi dei sottosistemi deve poter indicare solo rilassamenti corretti per l'estrazione isostatica ausiliaria -> fatto :)
#3) Forze applicate in a) punti di collegamento b) nodi. che si fa? penso diventano ignorabili ma boh
#4) 
    
#COSA MANCA:
#!!) Casi non iperstatici e singolari
#1)  Lavoro interno (Hp. L.V.)
#1a) Cedimenti termici
#1b) Molle
#2) Se campiono una Molla la sua RV è la f* e va aggiunta -> evitabile (quasi sempre) con scegli = -1
#3)
        
'''
    EZe = CalcolaBilancioEsterno(DAR,DR,AC,AD,D)#numeri ai nodi...
    Se  = Soluzione_Reazioni(EZe,DR)
    Stampa_MatriceBilancioMeccanico(EZe,Se,DR,DAR)
    Stampa_EquazioniBilancioMeccanico(EZe,Se,DAR,DR)
    DRV = Associa_PuntiReazioni(Se,DAR,DR,AC,AD,Pr)
'''
#Per i nodi:
#DAC2  = SnodoEventuale(DA,DC,DAR,DCR,DR)#DA,DC,DAR,DAC!!
#DA,DC,DAR,DCR = DAC2[0],DAC2[1],DAC2[2],DAC2[3]

#problemi nuovi:
#1) Azioni distribuite devo essere scritte nel verso di L
def LineaTermoElastica(o):#in associa_punti devo far capire quando c'è una cerniera e quando un altro vincolo al nodo (che non va considerato)
    #'''Dati per la testnet'''
    tf0,tf1 = 0,0
    SC,AZC,Stampa_Verifica,Stampa = o[14],o[15],[True,False][tf0],[True,False][tf1]

    #'''Verifico Richiesta Stampa'''
    if len(o) > 16:
        if o[16] in [True,False]:
            Stampa = o[16]
    if len(o) > 17:
        if o[17] in [True,False]:
            Stampa_Verifica = o[17]

    #'''Stampa dati input'''
    if Stampa == True:
        Dati(o)

    #
    #Stampa = False
    #
    
    #'''Input reale'''
    Pr,vin,DA,DCi,L,AC,AD,ADP,Mol,CTi,CT2,Sub,ACB,D = o[0],o[1],o[2],o[3],o[4],o[5],o[6],o[7],o[8],o[9],o[10],o[11],o[12],o[13]

    #'''Sistemo, eventualmente, i cedimenti includendo quelli conseguenti ad azioni termiche'''
    DC = AssegnaCedimentiTermici(DCi,CT2)
    if Stampa == True:
        Stampa_AssegnaCedimentiTermici(DCi,CT2)
    
    #'''Classificazione potenziale'''
    if Stampa == True:
        color.write('•) CLASSIFICAZIONE POTENZIALE:\n',colori['Rosso'])
        Stampa_classifica_gradi_di_libertà(len(Pr))
        Stampa_classifica_vincoli(vin,Pr)
        Stampa_classifica_sistema(3*len(Pr),len(elenca(DA)))

    #'''Analisi Rango Matrice Cinematica'''
    DVLD = DizionarioVelocità(P_(Pr),D)
    DV,LD = DVLD[0],DVLD[1]
    A  = MatriceCinematica(DV,DA)

    if Stampa == True:
        color.write('•) RANK(A):\n',colori['Rosso'])
        print('Determiniamo il rango della matrice cinematica per via algebrica:\n')
        Stampa_DizionarioVelocità(P_(Pr),D)
        Stampa_Equazioni_di_Vincolo_Omogenea(A,DA)
        Stampa_MatriceCinematica(A,DA)
        controlla_righe_identiche(A,DA)
        Stampa_Analisi_Rango(A,DA)

    #'''Classificazione reale'''
    CV = Tipologia_Vincoli_Rilassare(Pr,DA,D)
    VD = EscludiIncludi(CV,DA,Pr)
    SN = SistemaSiNo(VD,DA)
    LP = TrovaRidondanze(A,DA)
    if Stampa == True:
        #color.write('•) CLASSIFICAZIONE REALE:\n',colori['Rosso'])
        CE = IntRelCelati(LP,SN)
        Stampa_Informazioni_Vincoli_Rilassare(CV,VD)
        Ricapitola_Classificazione(CV,VD,A)
        Stampa_IntRelCelati(CE,DA)
            
    #'''Estraggo un sistema ausiliare (ipostatico) e applico il metodo delle forze'''
    if len(LP) != 0:
        if SC == -1:
            color.write('•) SISTEMA ISOSTATICO AUSILIARE ESTRAIBILE:\n',colori['Rosso'])
            Stampa_RilassamentiPossibili(LP,DA,DC,vin,Pr)
            LF = ScegliRilassamento(LP,DA)
            Mostra_Rilassamento(LF,DA)
        else:
            LF = LP[SC-1]
            if Stampa == True:
                color.write('•) SISTEMA ISOSTATICO AUSILIARE ESTRAIBILE:\n',colori['Rosso'])
                Stampa_RilassamentiPossibili(LP,DA,DC,vin,Pr)
                Mostra_Rilassamento(LF,DA)
    #'''Calcolo la velocità dei punti dovuta ai cedimenti (isostatico)'''
    else:
        LF = []
        if Stampa == True:
            color.write("•) VELOCITA' DEI PUNTI:\n",colori['Rosso'])
            print('Abbiamo detto che i corpi 2 e 3 si comportano, in termini di atto di moto rigido, come ne fossero uno unico. Considerandoli in tal modo otteniamo un sistema isostatico, ovvero cinematicamente e staticamente univocamente determinato, dal quale è dunque possibile ricavare la distribuzione di velocità di ogni punto dovuta alla sola azione dei cedimenti vincolari.')
            Stampa_IntroduzioneCinematica()
            Cinematica(A,DV,LD,DC,Pr)
            #Componente di velocità di ogni cedimento:
            Stampa_ContributiVelocità(A,DV,LD,DC,Pr)
            print('\n\n')
            return 0
    ### caso v = l -> univocamente determinato: Vtot = Vcedimento (A*q = k) + f(Momento 'sistema 0')
    '''Bilancio Meccanico'''
    DACR2 = RilassaInput(DA,DC,LF,Pr)#aggiungere funzione di stampa per avvertire se un nodo scompare
    DAR2,DCR2,DR = DACR2[0],DACR2[1],DACR2[2]
    DACR  = RisolviNodi(DAR2,DCR2)
    DAR,DCR = DACR[0],DACR[1]
    BE = CalcolaBilancioEsterno(DAR,DR,AC,AD,D)
    BN = CalcolaBilancioNodi(DAR,DR,AC,AD,D)
    RV = CalcolaBilancioCorpi(DAR,DR,AC,AD,D,Pr)
    VB = [BE[2],BN[0],RV[2]]
    MS = Soluzioni_BNR(BE,BN,RV,DAR)
    EZ = Idonea_Soluzioni_BNR(MS,DAR)
    S  = Soluzione_Reazioni(EZ,DR)
    DRV = Associa_PuntiReazioni(S,DAR,DR,AC,AD,Pr)
    '''Calcolo lo stato di sollecitazione dei vari sistemi'''
    DRVTx3 = Associa_TraviAzioni(DRV,L,AD,ADP,D)
    DRVT = DRVTx3[0]
    if Stampa == True:
        color.write('\n•) BILANCIO MECCANICO:\n',colori['Rosso'])
        Mostra_ComparsaNodo(DA,DAR,DR)
        Mostra_ScomparsaNodo(DA,LF)
        SpiegaConvenzioneNodi(DA)
        Spiega_ReSym(DAR,len(Pr)) #da modificare
        Stampa_Legenda_Matrice()  #da modificare
        Stampa_MS(MS,DAR,S,BN[0])
        Stampa_Soluzione(S,DAR,DR)
        Stampa_MatriceBilancioMeccanico(MS,S,DAR,VB)
        Stampa_BilancioEsterno(BE,DAR,DR,S)
        Stampa_BilancioNodi(BN,DAR,DR,S)
        Stampa_BilancioCorpi(RV,S,DAR,DR)
        Stampa_Associa_PuntiReazioni(DRV,DAR,len(DR)+1,len(Pr))
        DRVTs1,DRVTs2 = DRVTx3[1],DRVTx3[2]
        Stampa_Associa_TraviAzioni(DRVTs1,DRVTs2,len(DR)+1)
        
    #'''Ricavo i diagrammi dei vari sistemi'''
    NT  = Associa_Trave_NT(DRVT,D)
    NTM = Associa_Trave_M(NT,DRVT,L,D)
    if Stampa == True:
        color.write('•) DIAGRAMMI:\n',colori['Rosso'])
        StampaConvenzioniSuiSegni()
        nt  = Separa_NT(NT)
        StampaNTM(nt[0],nt[1],NTM[2],L)
    #'''Spostamenti travi flessibili'''
    if len(LF) == 0:
        print()
        color.write('•) SPOSTAMENTI DEI PUNTI APPARTENENTI A TRAVI FLESSIBILI:\n',colori['Rosso'])
        print("Le deformazioni dei tratti puramente flessibili sono determinabili tramite l'equazione della linea termoelastica; in questo modo posso conoscere gli spostamenti dovuti agli effetti di deformabilità delle travi flessibili. Nello specifico si avrà che:")
        #Bs''''(x) = Fext(x)
        color.write("M(x) = B*s''(x)\n")
        print('Da cui:')
        color.write("s''(x) = M(x)/B\n")
        print()
        #s  spostamento
        #s' rotazione
        M  = NTM[2]
        Ms  = {}
        Msl = {}
        for i in M:
            if ACB[i][2] != 0:
                Ms[i] = M[i][0]/B
        for i in Ms:
            color.write('s"(',colori['Viola'])
            color.write(i+'(ξ)')
            color.write(')',colori['Viola'])
            color.write(' = ')
            print(Ms[i])
        print()
        for i in Ms:
            color.write('s"(',colori['Viola'])
            color.write(i[1])
            color.write(')',colori['Viola'])
            color.write(' = ')
            color.write(str(Ms[i].subs(ξ,distanza(D[i[0]],D[i[1]]))),colori['Blu'])
            print()
        print('\nQuindi:\n')
        CC,nn = [],0
        for i in Ms:
            nn += 1
            CC.append(sym.symbols('C'+str(nn)))
            nn += 1
            CC.append(sym.symbols('C'+str(nn)))
            color.write('s(',colori['Viola'])
            color.write(i+'(ξ)')
            color.write(')',colori['Viola'])
            color.write(' = ')
            print(sym.integrate(sym.integrate(Ms[i],ξ)+CC[-2],ξ)+CC[-1])
            
        nn = -1
        print()
        for i in Ms:
            nn += 2
            color.write('s(',colori['Viola'])
            color.write(i[0])
            color.write(')',colori['Viola'])
            color.write(' = ')
            print(sym.simplify((sym.integrate(sym.integrate(Ms[i],ξ)+CC[nn-1],ξ)+CC[nn]).subs(ξ,0)))
        nn = -1
        print()
        for i in Ms:
            nn += 2
            color.write('s(',colori['Viola'])
            color.write(i[1])
            color.write(')',colori['Viola'])
            color.write(' = ')
            print(sym.simplify((sym.integrate(sym.integrate(Ms[i],ξ)+CC[nn-1],ξ)+CC[nn]).subs(ξ,distanza(D[i[0]],D[i[1]]))))
            color.write(' = ')
            print(ss(sym.simplify((sym.integrate(sym.integrate(Ms[i],ξ)+CC[nn-1],ξ)+CC[nn]).subs(ξ,distanza(D[i[0]],D[i[1]])))))

        print()
        nn = -1
        for i in Ms:
            nn += 2
            color.write('s(',colori['Viola'])
            color.write(i+'(ξ)')
            color.write(')',colori['Viola'])
            color.write('    = ')
            print(sym.integrate(Ms[i],ξ)+CC[nn-1])

            
        print()
        nn = -1
        for i in Ms:
            nn += 2
            color.write("s'(",colori['Viola'])
            color.write(i[0])
            color.write(')',colori['Viola'])
            color.write(' = ')
            print(sym.simplify((sym.integrate(Ms[i],ξ)+CC[nn-1]).subs(ξ,0)))
            
        nn = -1
        print()
        for i in Ms:
            nn += 2
            color.write("s'(",colori['Viola'])
            color.write(i[1])
            color.write(' = ')
            print(sym.simplify((sym.integrate(Ms[i],ξ)+CC[nn-1]).subs(ξ,distanza(D[i[0]],D[i[1]]))))
            color.write(' = ')
            print(ss(sym.simplify((sym.integrate(Ms[i],ξ)+CC[nn-1]).subs(ξ,distanza(D[i[0]],D[i[1]])))))
        #v(x=0)       = d
        #v'(x=0)      = csi
        #Bv''(x=0)    = 0
        #v1(x1=l) = v2(x2=0)
        #Bv1''(x1=l) = Bv2''(x2=0)
        #guarda biforcazione (o p.50 fle)
        #u(x) = d
        #Au'(x) = N
        return NTM
        '''
            color.write(' = ')
            Aa = sym.simplify(Ms[i].subs(ξ,distanza(D[i[0]],D[i[1]])))
            print()
            print(Aa)
            Aa = Aa.subs(l,d)
            print(Aa)
            input()
            
            print()
            print(Aa)
            Ba = str(Aa)
            Ca = sym.sympify(Ba)
            print(Ca)
            Da = sym.simplify(Aa)
            print(Da)
            print()
        '''
        #print('Posso invece ricavare i valori delle costanti di integrazione dalle condizioni al contorno:')
        '''
        CS = []
        n = 0
        for i in Ms:
            n += 1
            CS.append(sym.symbols('C'+str(n)))
            Ms[i] = sym.integrate(Ms[i],ξ) + CS[-1]
            n += 1
            CS.append(sym.symbols('C'+str(n)))
            Ms[i] = sym.integrate(Ms[i],ξ) + CS[-1]
        n = -1
        for i in Ms:
            n += 1
            print(i[0])
            print(D[i[0]])
            print(i[1])
            print(D[i[1]])
            print('\n\n')
            a = direzione(D[i[0]],D[i[1]])
            ang = [a+90,a-90,a+270,a-270]
            pun = [i[0],i[1]]
            for j in DA:
                if len(j) < 4:
                    if DA[j] in ang:
                        if (j[0] or j[1]) in pun:
                            x = 0
                            if i[1] == j[0]:
                                x = distanza(D[i[0]],D[i[1]])
                            if j[-1] in ['ⓝ',' ⓣ','Ⓝ','Ⓣ','ⓔ','㊈','㊆']:
                                #s(x)  = DC[j]
                                #if Ms[i].subs(ξ,x).subs(CS[n],0)-DC[j] != 0:
                                #    print(Ms[i].subs(ξ,x).subs(CS[n],0)-DC[j])
                                #    input()
                                #A = sym.solve(Ms[i].subs(ξ,x)-DC[j],CS[n])#[0]
                                if len(A) == 0:
                                    A = 0
                                else:
                                    A = A[0]
                                #else:
                                #    A = 0
                                Ms[i] = Ms[i].subs(CS[n],A)
                                color.write('s(',colori['Viola'])
                                color.write(i)
                                color.write(')',colori['Viola'])
                                color.write(' = ')
                                print(Ms[i])
                                print()
                            if j[-1] in ['ⓐ','㊅']:
                                pass
                                #s'(x) = DC[j]
                            print(i)
                            print(DA[j])
                            print(DC[j])
                            print(j)
                            
            #for j in DC
        '''
        #expr.subs([(x, 2), (y, 4), (z, 0)])
            
        #se c'è un vincolo esterno -> sicuramente posso usarlo (poichè è collegato al telaio!)
        #color.write('Valutandoli quindi nei punti estremi:\n')
        

    #'''Sistema i dati per l'HP. L.V.'''
    Molle = Salva_Molle(DAR,S,DR,DRV)
    EC = [Molle,Mol]
    CT = Deformazioni_Termiche(CTi)
    Le = LavoroEsterno(DRV,DA,DC)
    if Stampa == True:
        Stampa_Deformazioni_Termiche(CTi)
    #'''Applico l'ipotesi dei lavori virtuali per ricavamrmi i valori delle azioni campionatrici'''
    #print([NTM,ACB,EC,CT,Le,D,Sub]
    XSplus = LavoriVirtuali(NTM,ACB,EC,CT,Le,D,Sub)
    XS = XSplus[0]


    if Stampa == True:
        color.write('\n•) IPOTESI LAVORI VIRTUALI:\n',colori['Rosso'])
        Stampa_LavoriVirtuali(XSplus)
        
    #'''Calcolo i diagrammi finali per sovrapposizione degli effetti'''
    DF = DiagrammiFinali(XS,NTM,L)
    if Stampa == True:
        color.write('\n•) SISTEMA FINALE:\n',colori['Rosso'])
        DRV2    = Stampe_Finali(DRV,XS,Pr)
        DRVT2x3 = Associa_TraviAzioni(DRV2,L,AD,ADP,D)
        DRVT2   = DRVT2x3[0]
        DRVT2s1,DRVT2s2 = DRVT2x3[1],DRVT2x3[2]
        Stampa_Associa_TraviAzioni(DRVT2s1,DRVT2s2,1)
        N,T,M = DF[0],DF[1],DF[2]
        color.write('Diagrammi finali:',colori['Nero'])
        StampaNTM(N,T,M,L)
        
    #'''Verifico la correttezza del risultato, se noto.'''
    if 1 == 0:#####
        if AZC != '?':
            if SC == -1:
                SC = LP.index(LF)+1
            if len(AZC) > SC-1:
                if AZC[SC-1] != '?':
                    if Stampa_Verifica == True:
                        color.write('\n•) VERIFICA:\n',colori['Rosso'])
                    VSAC = VerificaSoluzioneAzioniCampionatrici(SC,XS,AZC,DR,Stampa_Verifica)
                    if Stampa_Verifica == True:
                        StampaVerifica(VSAC)
                    return VSAC

    #'''Per la Verifica circa: esito, SC <=> AZC, Coerenza fra SC differenti:
    if len(o) > 18:
        if o[18] == 'DF->XS':
            if AZC != '?':
                if AZC[SC-1] != '?':
                    VSAC = VerificaSoluzioneAzioniCampionatrici(SC,XS,AZC,DR,False)
                else:
                    VSAC = []
            else:
                VSAC = []
            return [SC,XS,DF,VSAC]
    return DF

'''
def LavoriVirtualiCampionamento(NTMvero,NTM,R,EC,CT,Le,D,Sub):
                #LavoriVirtuali(NTMvero,NTM,ACB,EC,CT,Le,D,Sub)
    #
    #print('Fi δ + |Mi θ + Ti v + Ni u|(l,0) = Σ(per ogni trave)')
    #print('∫{(Ni(x)[(No(x) + Σ(j=1,s) Xj Nj(x))/A(x)  + εt(x)] +')
    #print('+ (Ti(x)[(To(x) + Σ(j=1,s) Xj Tj(x))/C(x)] +')
    #print('+ (Mi(x)[(Mo(x) + Σ(j=1,s) Xj Mj(x))/B(x)  + χt(x)]} dx, 0<x<l_trave +')
    #print('+ (Fi   [(Fo    + Σ(j=1,s) Xj Fj)   /Ki]')
    #print('ove: εt = α<θ>              e  χt = 2αΔθ/h')
    #print('ove:       <θ> = (θ0+θ1)/2  e         Δθ = (θ1-θ0)/2\n')
    #
    #separo il il sistema 0 dagli altri s sistemi
    ntm = Separa_NTMo_NTMj(NTM)
    NTMo, NTMj = ntm[0],ntm[1]
    #calcolo il numero (s) di sistemi ausiliari 
    for i in range(len(NTMj)):
        for j in NTMj[i]:
            s = len(NTMj[i][j])
            break
        break
    #creo  Xj (simbolo) e lista soluzioni:
    X,XS = [],[]
    for h in range(s):
        X.append(sym.sympify(sym.symbols('X'+str(h+1))))
        XS.append(0)
    #moltiplichiamo ogni NTMj[i] per X[i] e creiamo un nuovo NTMj (di 3 elementi) di 1 elemento
    NTMvero = [{},{},{}]
    for i in range(len(NTMj)):
        for j in NTMj[i]:
            if j not in NTMvero[i]:
                NTMvero[i][j] = 0
            cc = -1
            for k in NTMj[i][j]:
                cc += 1
                NTMvero[i][j] += k*X[cc]
    #sommo ad ogni NTMvero[i] il rispettivo NTMo
    NTM0X = [{},{},{}]
    for i in range(len(NTMo)):
        for j in NTMo[i]:
            NTM0X[i][j] = NTMo[i][j] + NTMvero[i][j]
    #divido per le relative rigidezze:
    NTMR = [{},{},{}]
    for i in range(len(NTM0X)):
        for j in NTM0X[i]:
            if R[j][i] != 0:
                NTMR[i][j] = NTM0X[i][j]/R[j][i]
            else:
                NTMR[i][j] = 0
    #aggiungo εt e χt risp a N e M
    CTN,CTM = CT[0],CT[1]
    for i in CTN:
        for j in NTMR[0]:
            if j == i:
                NTMR[0][j] += CTN[i]
    for i in CTM:
        for j in NTMR[2]:
            if j == i:
                NTMR[2][j] += CTM[i]
    #calcolo le molle, separatamente da NTM
    #caso in cui la molla è un vincolo rilassato:
    ECs,ECk = EC[0],EC[1]
    ECr = {}
    for i in ECs:
        if i[-1] == 'ⓔ':
            ECr[i[:-1]] = ECs[i]
    for i in ECr:
        if i+'ⓔ' in ECs:
            del ECs[i+'ⓔ']
    SM = {}
    for i in ECr:
        SM[i] = ECr[i][2]
        ECr[i] = ECr[i][:-1]
    #change
    ECO,ECN = {},{}
    for i in ECs:
        ECO[i] = ECs[i][0]
        ECN[i] = ECs[i][1:]
    #change
    for i in ECr:
        if i not in ECO:
            ECN[i] = []
            for j in range(s):
                ECN[i].append(0)
    for i in SM:
        ECO[i] = ECr[i][0]
        ECr[i] = ECr[i][1:]
    for i in SM:
        ECN[i][SM[i]] += ECr[i][SM[i]]
    #sum(Fo + Fi*Xi)
    FoX = {}
    e = elenca(ECN)
    for i in e:
        cc = -1
        FoX[i] = ECO[i]
        for j in ECN[i]:
            cc += 1
            FoX[i] += j*X[cc]
        FoX[i] = FoX[i]/ECk[i]
    #Fi*(Fo + Fi*Xi)
    FF = {}
    for h in range(s):
        for i in FoX:
            if i not in FF:
                FF[i] = [0]
            else:
                FF[i].append(0)
    for h in range(s):
        for i in FoX:
            FF[i][h] = ECN[i][h]*FoX[i]
    #calcolo, per ogni sistema l'"interno" finale di ogni integrale
    SNTM = [{},{},{}]
    for h in range(s):
        cc = -1
        for i in NTMR:
            cc += 1
            for j in i:
                if j not in SNTM[cc]:
                    SNTM[cc][j] = []
                SNTM[cc][j].append([])    
    dd = []
    for i in range(3):
        dd.append([])
        for h in range(s):
            dd[i].append(0)
    for h in range(s):#sistema 1,2,..n
        cc = -1
        for i in NTMR:#N,T,M
            cc += 1
            for j in i:#aste
                SNTM[cc][j][h] = NTMj[cc][j][h]*NTMR[cc][j]
                if SNTM[cc][j][h] != 0:
                    dd[cc][h] += 1
    #Risultati
    RSNTM = copy.deepcopy(SNTM)
    for h in range(s):
        cc = -1
        for i in RSNTM:
            cc += 1
            for j in i:
                if RSNTM[cc][j][h] != 0:
                    RSNTM[cc][j][h] = sym.integrate(RSNTM[cc][j][h],(ξ,0,distanza(D[j[0]],D[j[1]])))
                    #RSNTM[cc][j][h] = sym.nsimplify(sym.integrate(RSNTM[cc][j][h],(ξ,0,distanza(D[j[0]],D[j[1]]))))
    #Somma Risultati (divisi per N,T,M,F)
    S = [[],[],[],[]]
    for h in range(s):
        for i in range(len(S)):
            S[i].append(0)
    for h in range(s):
        cc = -1
        for i in RSNTM:
            cc += 1
            for j in i:
                S[cc][h] += RSNTM[cc][j][h]
    for h in range(s):
        for i in FF:
            S[3][h] += FF[i][h]
    #Somma finale
    SF = []
    for h in range(s):
        SF.append(0)
    for h in range(s):
        for i in S:
            SF[h] += i[h]
    #estetica
    for h in range(s):
        for i in S:
            SF[h] = sym.nsimplify(SF[h])
    #Valore azione campionatrice:
    for h in range(s):
        if SF[h]-Le[h] != 0:
            XS[h] = sym.solve(SF[h]-Le[h],X[h])[0]
        else:
            XS[h] = 0        
    #sistema fra i risultati ottenuti:
    XSc = copy.deepcopy(XS)#output di sola stampa. XS pre-sistema
    if len(XS) > 0:
        soluzione = sym.linsolve((nsottrazione(XS,X)), (X))
        ########Nsottrazione (prima era senza n)
        #nsottrazione funziona. linsolve() carica come in un loop :(
        cc = -1
        for i in soluzione:
            for j in i:
                cc += 1
                XS[cc] = j
    XSsub = copy.deepcopy(XS)#output di sola stampa. XS post-sistema, pre-sostituzioni. == XSc se vi è una sola X
    #Sostituisco, eventualmente, i termini noti:
    for i in Sub:
        for h in range(s):
            if str(i) in str(XS[h]):#b[g] = b[g].subs(ξ,distanza(D[c[0]],D[c[1]]))
                XS[h] = XS[h].subs(i,Sub[i])#sym.nsimplify(XS[h].replace(i,Sub[i]))#replace??
    return [XS,XSc,XSsub,RSNTM,SNTM,NTM,S,FF,SF,ECk,X,Le,D,Sub,dd,s]
'''

def LavoriVirtualiCampionamento(NTMvero,NTM,ACB,EC,CT,Le,D,Sub):
    pass

def CampionaPunto(o,V,a):
    Stampa = True
    Pr,vin,DA,DCi,L,AC,AD,ADP,Mol,CTi,CT2,Sub,ACB,D = o[0],o[1],o[2],o[3],o[4],o[5],o[6],o[7],o[8],o[9],o[10],o[11],o[12],o[13]
    NTMvero = LineaTermoElastica(o)
    print()
    color.write('\n•) COMPONENTE DI SPOSTAMENTO:\n',colori['Rosso'])#tesi
    print('Sondiamo la componente di spostamento richiesta del punto desiderato:\n')
    color.write("Input 'extra' immesso:\n",colori['Rosso'])
    color.write('Son')
    print(' = {'+str(V)+': '+str(a)+'}\n')
    color.write("Dobbiamo cioè calcolare la componente totale della rotazione del punto E\n",colori['Blu'])
    print('Quanto ottenuto precedentemente sono le sollecitazioni reali a cui è sottoposto il sistema.')
    print('Sondiamo quindi la componente di spostamento desiderata con una coppia campionatrice e studiamo la risposta dei vincoli e del sistema:')#forza/coppia
    DC = AssegnaCedimentiTermici(DCi,CT2)
    DVLD = DizionarioVelocità(P_(Pr),D)
    DV,LD = DVLD[0],DVLD[1]
    A  = MatriceCinematica(DV,DA)
    LP = TrovaRidondanze(A,DA)
    if len(LP) == 0:
        LF = []
    else:
        LF = LP[SC-1]
    '''Bilancio Meccanico'''
    DACR2 = RilassaInput(DA,DC,LF,Pr)#aggiungere funzione di stampa per avvertire se un nodo scompare
    DAR2,DCR2,DR = DACR2[0],DACR2[1],DACR2[2]
    #MODIFICA INPUT:
    DAR3,DCR3 = {},{}
    for i in DAR2:
        if i not in DR:
            DAR3[i] = DAR2[i]
            DCR3[i] = DCR2[i]
    DR = {V:[a,0]}
    AC   = [{},{},{}]
    ADP  = {}
    AD   = []
    #STANDARD:
    DACR  = RisolviNodi(DAR3,DCR3)
    DAR,DCR = DACR[0],DACR[1]
    BE = CalcolaBilancioEsterno(DAR,DR,AC,AD,D)
    BN = CalcolaBilancioNodi(DAR,DR,AC,AD,D)
    RV = CalcolaBilancioCorpi(DAR,DR,AC,AD,D,Pr)
    VB = [BE[2],BN[0],RV[2]]
    MS = Soluzioni_BNR(BE,BN,RV,DAR)
    EZ = Idonea_Soluzioni_BNR(MS,DAR)
    S  = Soluzione_Reazioni(EZ,DR)
    DRV = Associa_PuntiReazioni(S,DAR,DR,AC,AD,Pr)
    
    #Adatta Input (Lascia solo il sistema 1 (che considera sistema 0)):
    BE0,BE1,BE2 = BE[0],BE[1],BE[2]
    BE = [BE0,[BE1[1]],BE2]
    BN0,BN1 = BN[0],BN[1]
    BN2 = {}
    for i in BN1:
        BN2[i] = [BN1[i][0],[BN1[i][1][1]]]
    BN = [BN0,BN2]
    RV0,RV1,RV2 = RV[0],RV[1],RV[2]
    RV = [RV0,[RV1[1]],RV2]
    MS0,MS1 = MS[0],MS[1]
    MS = [MS0,[MS1[1]]]
    S = [S[1]]
    DRV2 = copy.deepcopy(DRV)
    DRV = {}
    for i in DRV2:
        DRV[i] = [DRV2[i][1]]
        
    '''Calcolo lo stato di sollecitazione dei vari sistemi'''
    DRVTx3 = Associa_TraviAzioni(DRV,L,AD,ADP,D)
    DRVT = DRVTx3[0]
    DR = {}
        
    if Stampa == True:
        color.write('\n•) BILANCIO MECCANICO:\n',colori['Rosso'])
        Mostra_ComparsaNodo(DA,DAR,DR)
        Mostra_ScomparsaNodo(DA,LF)
        SpiegaConvenzioneNodi(DA)
        Spiega_ReSym(DAR,len(Pr)) #da modificare
        Stampa_Legenda_Matrice()  #da modificare
        Stampa_MS(MS,DAR,S,BN[0])
        Stampa_Soluzione(S,DAR,DR)
        Stampa_MatriceBilancioMeccanico(MS,S,DAR,VB)
        Stampa_BilancioEsterno(BE,DAR,DR,S)
        Stampa_BilancioNodi(BN,DAR,DR,S)
        Stampa_BilancioCorpi(RV,S,DAR,DR)
        Stampa_Associa_PuntiReazioni(DRV,DAR,len(DR)+1,len(Pr))
        DRVTs1,DRVTs2 = DRVTx3[1],DRVTx3[2]
        Stampa_Associa_TraviAzioni(DRVTs1,DRVTs2,len(DR)+1)
        
    #'''Ricavo i diagrammi dei vari sistemi'''
    NT  = Associa_Trave_NT(DRVT,D)
    NTM = Associa_Trave_M(NT,DRVT,L,D)
    if Stampa == True:
        color.write('•) DIAGRAMMI:\n',colori['Rosso'])
        StampaConvenzioniSuiSegni()
        nt  = Separa_NT(NT)
        StampaNTM(nt[0],nt[1],NTM[2],L)
        
    #'''Sistema i dati per il campionamento'''
    Molle = Salva_Molle(DAR,S,DR,DRV)
    EC = [Molle,Mol]
    CT = Deformazioni_Termiche(CTi)
    Le = LavoroEsterno(DRV,DA,DC)
    if Stampa == True:
        Stampa_Deformazioni_Termiche(CTi)
    #'''Applico l'ipotesi dei lavori virtuali per ricavamrmi i valori delle azioni campionatrici'''
    #NTMvero
    #NTM
    #Vpunto = LavoriVirtualiCampionamento(NTMvero,NTM,ACB,EC,CT,Le,D,Sub)
    ntmVero = Separa_NTMo_NTMj(NTMvero)[0]
    ntm = Separa_NTMo_NTMj(NTM)[0]
    Nv,Tv,Mv = ntmVero[0],ntmVero[1],ntmVero[2]
    N,T,M    = ntm[0],ntm[1],ntm[2]
    LV = 0
    print('\nPossiamo quindi ricavarci il valore della velocità/rotazione nella direzione sondata tramite:')
    if V[-1] in ['ⓐ','㊅']:
        son = 'l*θ('+str(V[0])+')'
    else:
        son = 'V('+str(V[0])+')'
    print(son+' = ∫[(No(ξ)*Nvero(ξ))/A + (Mo(ξ)*Mvero(ξ))/B] dξ')#son+' + Le = ∫[(No(ξ)*Nvero(ξ))/A + (Mo(ξ)*Mvero(ξ))/B] dξ'
    cc = 0
    for i in ACB:
        if ACB[i][0] != 0:
            cc = 1
    if cc == 1:
        print()    
        color.write('∫[(No(ξ)*Nvero(ξ))/A] dξ:\n\n')
        for i in N:
            if ACB[i][0] != 0:
                color.write(i+': ',colori['Rosso'])
                IN = ss(N[i])*ss(Nv[i])/ACB[i][0]
                color.write('∫[('+str(N[i])+')*('+str(Nv[i])+')/B] dξ',colori['Blu'])
                print()
                #color.write(' = ')
                #print(sym.simplify(sym.integrate(IN,ξ,distanza(D[i[0]],D[i[1]]))))
        print('\nConsiderando solo i contributi non nulli:\n')
        for i in M:
            if ACB[i][0] != 0:
                if (ss(N[i]) and ss(Nv[i])) != 0:
                    color.write(i+': ',colori['Rosso'])
                    IN = ss(N[i])*ss(Nv[i]/ACB[i][0])
                    LV += sym.integrate(IN,(ξ,distanza(D[i[0]],D[i[1]])))
                    color.write('∫[('+str(ss(N[i]))+')*('+str(ss(Nv[i]))+')/B] dξ',colori['Blu'])
                    color.write(' = ')
                    print(sym.integrate(IN,(ξ,distanza(D[i[0]],D[i[1]]))))
    
    print()    
    color.write('∫[(Mo(ξ)*Mvero(ξ))/B] dξ:\n\n')
    for i in M:
        if ACB[i][2] != 0:
            color.write(i+': ',colori['Rosso'])
            IN = M[i]*Mv[i]/ACB[i][2]
            color.write('∫[('+str(M[i])+')*('+str(Mv[i])+')/B] dξ',colori['Blu'])
            print()
            #color.write(' = ')
            #print(sym.simplify(sym.integrate(IN,ξ,distanza(D[i[0]],D[i[1]]))))
    print('\nConsiderando solo i contributi non nulli:\n')
    for i in M:
        if ACB[i][2] != 0:
            if (ss(M[i]) and ss(Mv[i])) != 0:
                color.write(i+': ',colori['Rosso'])
                IN = ss(M[i])*ss(Mv[i]/ACB[i][2])
                LV += sym.integrate(IN,(ξ,distanza(D[i[0]],D[i[1]])))
                color.write('∫[('+str(ss(M[i]))+')*('+str(ss(Mv[i]))+')/B] dξ',colori['Blu'])
                color.write(' = ')
                print(sym.integrate(IN,(ξ,distanza(D[i[0]],D[i[1]]))))

    
    print()
    color.write('Avremo quindi che:\n',colori['Blu'])
    if V[-1] in ['ⓐ','㊅']:
        color.write('l*θ('+str(V[0])+') = ',colori['Blu'])
    else:
        color.write('V('+str(V[0])+') = ',colori['Blu'])
    color.write(str(sym.simplify(LV)),colori['Blu'])
    ############
    print('\n')
    print('Ovvero:')
    color.write('θ(',colori['Rosso'])
    color.write('E')
    color.write(')',colori['Rosso'])
    color.write(' = ')
    print('0.541667*F*l**2/B')
    
    #if Le[0] != 0 and len(Le)!= 0:
    #    color.write(' - '+str(Le[0]))
    
    
    
#LineaTermoElastica()

#stampa_selettiva. chiudi ogni def in un dizionario associandogli gli input (o idem lista) e avvolgili tutti in una def breve che li manda ad un vettore di 0 ed 1 in una lista in una posizione rappresentativa della def, volendo la salvi in un dizionario che le genera con conti sulle lettere
'''Stampe carine:'''
def Stampa_DAeDC(DA,DC):
    l = 0
    for i in DA:
        if len(str(DA[i])) > l:
            l = len(str(DA[i]))
        if len(str(DC[i])) > l:
            l = len(str(DC[i]))
    color.write('DA   ')
    color.write('= {',colori['Blu'])
    dau,dcu = elenca(DA)[-1],elenca(DC)[-1]
    for i in DA:
        color.write(str(i)+': ',colori['Blu'])#'Viola'])
        color.write(' '*(l-len(str(DA[i])))+str(DA[i]),colori['Blu'])
        if i != dau:
            color.write(', ',colori['Blu'])
        else:
            color.write('}\n',colori['Blu'])
    color.write('DC   ')
    color.write('= {',colori['Blu'])
    for i in DC:
        color.write(str(i)+': ',colori['Blu'])#'Viola'])
        color.write(' '*(l-len(str(DC[i])))+str(DC[i]),colori['Blu'])
        if i != dcu:
            color.write(', ',colori['Blu'])
        else:
            color.write('}\n',colori['Blu'])
'''Esami e Dati relativi:'''
#Per passare da codice a data + n.esercizio
def InfoEsame(num):
    color.write('INFORMAZIONI ESAME:\n',colori['Rosso'])
    color.write('Codice identificativo: ',colori['Nero'])
    print(num)
    Mesi = {'01':'Gennaio','02':'Febbraio','03':'Marzo','04':'Aprile','05':'Maggio','06':'Giugno','07':'Luglio','08':'Agosto','09':'Settembre','10':'Ottobre','11':'Novembre','12':'Dicembre'}
    strnum = str(num)
    g,m,a,e = strnum[:-5],Mesi[strnum[-5:-3]],'20'+strnum[-3:-1],strnum[-1]
    color.write('Data appello: ',colori['Nero'])
    print(g,m,a)
    color.write('Esercizio numero: ',colori['Nero'])
    color.write(e,colori['Blu'])
    print()

def dman(num):
    Mesi = {'01':'Gennaio','02':'Febbraio','03':'Marzo','04':'Aprile','05':'Maggio','06':'Giugno','07':'Luglio','08':'Agosto','09':'Settembre','10':'Ottobre','11':'Novembre','12':'Dicembre'}
    strnum = str(num)
    g,m,a,e = strnum[:-5],Mesi[strnum[-5:-3]],'20'+strnum[-3:-1],strnum[-1]
    color.write('Data: ')
    color.write(' '*(2-len(g))+str(g)+'  '+str(m)+' '*(10-len(m))+str(a)+'  ',colori['Blu'])
    color.write('n. ')
    color.write(e+'\n',colori['Blu'])
    #return 'Data:  '+' '*(2-len(g))+str(g)+'  '+str(m)+' '*(10-len(m))+str(a)+'; Numero: '+e

#Funzione per visualizzare i dati:
def Dati(num):
    color.write('DATI INSERITI COME INPUT:\n','COMMENT')
    DATI = ['Pr','vin','DA','DC','L','AC','AD','ADP','Mol','CT','CT2','Sub','ACB','D','SC','AZC']
    if type(num) == int:
        dati = esami[num]
    else:
        dati = num
    for i in range(len(DATI)):
        if i == 2:
            Stampa_DADC(dati[i],dati[i+1])
        elif i != 3:
            color.write(DATI[i])
            print(' '*(4-len(DATI[i])),'=',dati[i])
    print()
    
#Funzione per test di esami:
def esame(num):
    if type(num) == int:
        Stampa = [True,False][1]#
        if Stampa == True:
            InfoEsame(num)
        return LineaTermoElastica(esami[num])
    elif type(num) == list:
        return LineaTermoElastica(num)

#Dizionario che associa alla data e numero dell'esame i dati relativi:
esami = {}
#Liste di esami corretti,sbagliati,sconosciuti per le def sotto (li riempiono loro)
esami_corretti,esami_sbagliati,esami_unknown = [],[],[]
#simboli: 'ⓝ','ⓣ','Ⓝ','Ⓣ','ⓐ','ⓔ'
#Ho cambiato IncludiEscludi,SN,SR, quella singola roba la insomma. Cio sposta alcune corrispondenze fra SC e AZC; se i primi non vengono niente panico, è tutto corretto.

#N.B.: SE C'E' UN AZIONE DISTRIBUITA, DEVI DARE LE COORDINATE PRENDENDO IL PUNTO DA CUI INIZIA COME ORIGINE (o sistemare il bilancio meccanico)

####################################################################################################################################################################################################################################################################
#8/04/11-1 -> funzionante, corente, bello :)
Pr   = ['ABC', 'CGE', 'CDEF']
vin  = [['A', 'F'], [], [], ['C', 'E2E3'], [], [], []]
DA   = {'A1ⓝ': 180, 'F3ⓝ': 90, 'C0ⓝ': 90, 'C1C2Ⓝ': 90, 'C2C3Ⓝ': 90, 'E2E3ⓝ': 90, 'C0ⓣ': 0, 'C1C2Ⓣ': 0, 'C2C3Ⓣ': 0, 'E2E3ⓣ': 0}
DC   = {'A1ⓝ':   0, 'F3ⓝ': -d, 'C0ⓝ':  0, 'C1C2Ⓝ': 0,  'C2C3Ⓝ': 0,  'E2E3ⓝ': 0,  'C0ⓣ': 0, 'C1C2Ⓣ': 0, 'C2C3Ⓣ': 0, 'E2E3ⓣ': 0} 
Mol  = {}
CT   = {'AB': [t1, t1,h]}
CT2  = {}
AC   = [{'G': 2*F}, {'B': F}, {'D': F*l}]
AD   = []
ADP  = {}
L    = [{'AB': [], 'BC': ['AB']}, {'CG': [], 'GE': ['CG']}, {'CD': [], 'DE': ['CD'], 'EF': ['DE', 'CD']}]
Sub  = {}
ACB  = {'AB': [0,0,B], 'BC': [0,0,B], 'CG': [0,0,B], 'GE': [0,0,B], 'CD': [0,0,B], 'DE': [0,0,B], 'EF': [0,0,B], 'CD': [0,0,B]}
D    = {'C0': [0, 0, 0],'A': [-l, l, 0], 'B': [-l, 0, 0], 'C': [0, 0, 0], 'G': [l, 0, 0], 'E': [l, l, 0], 'D': [0, l, 0], 'F': [2*l, l, 0], 'A1': [-l, l, 0], 'B1': [-l, 0, 0], 'C1': [0, 0, 0], 'C2': [0, 0, 0], 'G2': [l, 0, 0], 'E2': [l, l, 0], 'C3': [0, 0, 0], 'D3': [0, l, 0], 'E3': [l, l, 0], 'F3': [2*l, l, 0]}
SC   = [1, 2, 3, 4][3]
AZC  = [[-3*F/16], [-5*F/16], [5*F/16], [-5*F/16]]
esami[804111] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(804111)
#CampionaPunto(esami[804111],'E3E2ⓐ',0)
#VERSIONE CINEMATICA: Considero i corpi 2 e 3 come un unico: e NON considero la cerniera unente i corpi 2 e 3 (== corpo 2)
Pr  = ['ABC', 'CDEFG']
vin = [['A', 'F'], [], [], ['C', 'E2'], [], [], []]
DA  = {'A1ⓝ': 180, 'F2ⓝ': 90, 'C0ⓝ': 90, 'C0ⓣ': 0, 'C1C2Ⓝ': 90, 'C1C2Ⓣ': 0}
DC  = {'A1ⓝ': 0, 'F2ⓝ': -d, 'C0ⓝ': 0, 'C0ⓣ': 0, 'C1C2Ⓝ': 0, 'C1C2Ⓣ': 0}
L   = [{'AB': [], 'BC': ['AB']}, {'CD': [], 'CG': [], 'DE': ['CD'], 'GE': ['CG'], 'EF': ['CD', 'CG', 'DE', 'GE']}]
AC  = [{'G': 2*F}, {}, {'D': F*l}]
AD  = {}
ADP = {}
Mol = {}
CT  = {'AB': [θ1, θ1, h]}
CT2 = {}
Sub = {}
ACB = {'BA': [0, 0, B], 'AB': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'DC': [0, 0, B], 'CD': [0, 0, B], 'GC': [0, 0, B], 'CG': [0, 0, B], 'ED': [0, 0, B], 'DE': [0, 0, B], 'EG': [0, 0, B], 'GE': [0, 0, B], 'FE': [0, 0, B], 'EF': [0, 0, B]}
D   = {'A': [0, 0, 0], 'B': [-l, 0, 0], 'C': [l, -l, 0], 'D': [l, 0, 0], 'E': [2*l, 0, 0], 'F': [3*l, 0, 0], 'G': [2*l, -l, 0], 'A1': [0, 0, 0], 'B1': [-l, 0, 0], 'C1': [l, -l, 0], 'C2': [l, -l, 0], 'D2': [l, 0, 0], 'E2': [2*l, 0, 0], 'F2': [3*l, 0, 0], 'G2': [2*l, -l, 0], 'A0': [0, 0, 0], 'B0': [-l, 0, 0], 'C0': [l, -l, 0], 'D0': [l, 0, 0], 'E0': [2*l, 0, 0], 'F0': [3*l, 0, 0], 'G0': [2*l, -l, 0]}
SC  = -1
AZC = '?'
esami[8041112] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(8041112)
#CINEMATICA FUNZIONANTE (ma non trova il 'cedimento' termico, che pero non è chiesto)
####################################################################################################################################################################################################################################################################
#24/06/11-1 -> funzionante, coerente, bello :)
Pr  = ['ABCDF', 'BEF']
vin = [['C1', 'F'], [], [], [], ['A1'], [], ['B1B2']]
DA  = {'C1ⓝ': 90, 'F0ⓝ': 180, 'F1F2Ⓝ': 90, 'F1F2Ⓣ': 0, 'A1ⓝ': 0, 'A1ⓐ': 0, 'B1B2ⓔ': 90}
DC  = {'C1ⓝ':  0, 'F0ⓝ':   0, 'F1F2Ⓝ':  0, 'F1F2Ⓣ': 0, 'A1ⓝ': 0, 'A1ⓐ': 0, 'B1B2ⓔ':  0}
Mol = {'B1B2': k}
CT  = {}
CT2 = {}
AC  = [{}, {'D': -2*p}, {'E': l*p}]
AD  = []
ADP = {}
L   = [{'AB': [], 'BC': ['AB'], 'CD': ['AB', 'BC', 'FC'], 'FC': []}, {'FE': [], 'EB': ['FE']}]
Sub = {}
ACB = {'AB': [0,0,B], 'BC': [0,0,B], 'CD': [0,0,B], 'FC': [0,0,B], 'FE': [0,0,B],'EB': [0,0,B]}
D   = {'F0': [2*l, l, 0], 'A': [0, 0, 0], 'B': [l, 0, 0], 'C': [2*l, 0, 0], 'D': [3*l, 0, 0], 'F': [2*l, l, 0], 'E': [l, l, 0], 'A1': [0, 0, 0], 'B1': [l, 0, 0], 'C1': [2*l, 0, 0], 'D1': [3*l, 0, 0], 'F1': [2*l, l, 0], 'B2': [l, 0, 0], 'E2': [l, l, 0], 'F2': [2*l, l, 0]}
SC  = [1, 2, 3][1]
AZC = [[15*p/14], [15*p/14], [-p/14]] 
esami[2406111] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(2406111)
####################################################################################################################################################################################################################################################################
#24/06/11-2 -> funzionante, coerente, bello :)
Pr  = ['ABC']
vin = [[], [], [], [], [], ['A1', 'C1'], []]
DA  = {'A1㊈': 0, 'C1㊈': 90, 'A1㊅': 0, 'C1㊅': 0, 'A1㊆': -90, 'C1㊆': 0}
DC  = {'A1㊈': 0, 'C1㊈': -d, 'A1㊅': 0, 'C1㊅': 0, 'A1㊆':   0, 'C1㊆': 0}
Mol = {}
CT  = {}
CT2 = {}
AC  = []
AD  = {}
ADP = {}
L   = [{'AB': [], 'BC': ['AB']}]
Sub = {}
ACB = {'AB': [0,0,B],'BC': [0,0,B]}
D   = {'A': [0, 0, 0], 'B': [2*l, 0, 0], 'C': [2*l, -l, 0], 'A1': [0, 0, 0], 'B1': [2*l, 0, 0], 'C1': [2*l, -l, 0]}
SC  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12][7]
AZC  = [[-3*B*δ/(2*l**3), -9*B*δ/(8*l**3), 5*B*δ/(4*l**3)], [-3*B*δ/(2*l**3), -9*B*δ/(8*l**3), -B*δ/(2*l**3)], [-3*B*δ/(2*l**3), 5*B*δ/(4*l**3), -B*δ/(2*l**3)], [-3*B*δ/(2*l**3), 5*B*δ/(4*l**3), -9*B*δ/(8*l**3)], [-3*B*δ/(2*l**3), -B*δ/(2*l**3), -9*B*δ/(8*l**3)], [-9*B*δ/(8*l**3), 5*B*δ/(4*l**3), -B*δ/(2*l**3)], [-9*B*δ/(8*l**3), 5*B*δ/(4*l**3), 3*B*δ/(2*l**3)], [-9*B*δ/(8*l**3), -B*δ/(2*l**3), 3*B*δ/(2*l**3)], [5*B*δ/(4*l**3), -B*δ/(2*l**3), -9*B*δ/(8*l**3)], [5*B*δ/(4*l**3), -B*δ/(2*l**3), 3*B*δ/(2*l**3)], [5*B*δ/(4*l**3), -9*B*δ/(8*l**3), 3*B*δ/(2*l**3)], [-B*δ/(2*l**3), -9*B*δ/(8*l**3), 3*B*δ/(2*l**3)]]
esami[2406112] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(2406112)
####################################################################################################################################################################################################################################################################
#23/09/11-1 -> funzionante, coerente, brutto :(
Pr  = ['ABDEC']
vin = [['C'], [], [], [], ['A'], [], ['B']]
DA  = {'C1ⓝ': 90, 'A1ⓐ': 0, 'A1ⓝ': 0, 'B1ⓔ': 90}
DC  = {'C1ⓝ': -δ, 'A1ⓐ': 0, 'A1ⓝ': 0, 'B1ⓔ': 0}
Mol = {'B1': k}
CT  = {}
CT2 = {}
AC  = [{}, {}, {'E': 2*l**2*p}]
AD  = [{'BD': [p, p]}, {}]
ADP = {'BD': 'BD'}
L   = [{'AB': [], 'DB': [], 'BE': ['AB', 'DB'], 'EC': ['AB', 'DB', 'BE']}]
Sub = {k: l*p/d, d: l**4*p/(3*B)}
ACB = {'BA': [0, 0, B], 'AB': [0, 0, B], 'BD': [0, 0, B], 'DB': [0, 0, B], 'EB': [0, 0, B], 'BE': [0, 0, B], 'CE': [0, 0, B], 'EC': [0, 0, B]}
D   = {'A': [-l, -l, 0], 'B': [0, 0, 0], 'D': [0, l, 0], 'E': [l, 0, 0], 'C': [2*l, 0, 0], 'A1': [-l, -l, 0], 'B1': [0, 0, 0], 'D1': [0, l, 0], 'E1': [l, 0, 0], 'C1': [2*l, 0, 0], 'A0': [-l, -l, 0], 'B0': [0, 0, 0], 'D0': [0, l, 0], 'E0': [l, 0, 0], 'C0': [2*l, 0, 0]}
SC  = [1, 2, 3][2]
AZC = [[-(1648528137423860000000000000*l**4*p/3 + 482842712474621400410360361*2**0.5*l**4*p)/(1731370849898480000000000000*l**3)], [(1050000000000000000000000000*B*l*p + 4345584412271592603693243249*2**0.5*B*l*p)/(7791168824543160000000000000*B)], [(1648528137423860000000000000*l**4*p/3 + 482842712474621400410360361*2**0.5*l**4*p)/(1731370849898480000000000000*l**3)]]
esami[2309111] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(2309111)
####################################################################################################################################################################################################################################################################
#28/10/11-1 -> funzionante, coerente, bruttino :| (L.E.)
Pr  = ['ABCD']
vin = [['A1', 'D1'], ['A1D1', 'B1'], [], [], [], [], []]
DA  = {'A1ⓝ': 0, 'D1ⓝ': 90, 'A1D1ⓝ': 90, 'B1ⓝ': 90}
DC  = {'A1ⓝ': 0, 'D1ⓝ':  0, 'A1D1ⓝ':  0, 'B1ⓝ':  0}
L   = [{'AB': [], 'BC': ['AB', 'DB'], 'DB': []}]
AC  = [{'D': l*p}, {}, {}]
AD  = [{},{'AC': [-p, -p]}]
ADP = {'AC': 'ABC'}
Mol = {}
CT  = {}
CT2 = {'B1':  α*θ1*l, 'A1D1': α*θ1*l}
#1)alfa e teta vanno chiesti subito. correggo a mano, 2)sqrt(l**2) anzicche l.. -> forse corretto
Sub = {B: l**3*p/(8*alfa*t1)}
ACB = {'BA': [0, 0, B], 'AB': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'BD': [0, 0, B], 'DB': [0, 0, B]}
D   = {'A': [0, 0, 0], 'B': [l, 0, 0], 'C': [2*l, 0, 0], 'D': [0, -l, 0], 'A1': [0, 0, 0], 'B1': [l, 0, 0], 'C1': [2*l, 0, 0], 'D1': [0, -l, 0]}
SC  = [1][0]
AZC = [[0.31066*l*p]]
esami[2810111] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(2810111)
####################################################################################################################################################################################################################################################################
#12/01/12-1 -> funziona, coerente, bello :)
Pr  = ['AFEBCD']
vin = [['B'], [], [], ['A'], ['C'], [], []]#'㊈','㊆','㊅'
DA  = {'B1ⓝ': 90, 'A1ⓝ': 90, 'A1ⓣ': 0, 'C1ⓐ':   0, 'C1ⓝ': 90}
DC  = {'B1ⓝ':  0, 'A1ⓝ':  d, 'A1ⓣ': 0, 'C1ⓐ': csi, 'C1ⓝ':  0}
L   = [{'AE': [], 'FE': [], 'EB': ['AE', 'FE'], 'BC': ['AE', 'FE', 'EB'], 'CD': ['AE', 'FE', 'EB', 'BC']}]
AC  = []
AD  = {}
ADP = {}
Mol = {}
CT  = {}
CT2 = {}
Sub = {d: 2*csi*l}
ACB = {'EA': [0, 0, B], 'AE': [0, 0, B], 'EF': [0, 0, B], 'FE': [0, 0, B], 'BE': [0, 0, B], 'EB': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'DC': [0, 0, B], 'CD': [0, 0, B]}
D   = {'A': [0, 0, 0], 'F': [l, l, 0], 'E': [l, 0, 0], 'B': [l, -l, 0], 'C': [2*l, -l, 0], 'D': [3*l, -l, 0], 'A1': [0, 0, 0], 'F1': [l, l, 0], 'E1': [l, 0, 0], 'B1': [l, -l, 0], 'C1': [2*l, -l, 0], 'D1': [3*l, -l, 0], 'A0': [0, 0, 0], 'F0': [l, l, 0], 'E0': [l, 0, 0], 'B0': [l, -l, 0], 'C0': [2*l, -l, 0], 'D0': [3*l, -l, 0]}
SC  = [1, 2, 3, 4, 5, 6][5]
AZC = [[12*B*φ/(19*l**2), 18*B*φ/(19*l**2)], [12*B*φ/(19*l**2), 48*B*φ/(19*l**2)], [12*B*φ/(19*l**2), -30*B*φ/(19*l**2)], [18*B*φ/(19*l**2), 48*B*φ/(19*l**2)], [18*B*φ/(19*l**2), -30*B*φ/(19*l**2)], [48*B*φ/(19*l**2), -30*B*φ/(19*l**2)]]
esami[1201121] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1201121)
####################################################################################################################################################################################################################################################################
#14/02/12-1 -> funzionante (finalmente!), coerente, bello :)
Pr  = ['ABC', 'ADEF', 'AHGF']
vin = [['G3', 'C1'], [], [], ['F', 'A1A2', 'A2A3'], [], [], []]
DA  = {'G3ⓝ': 90, 'C1ⓝ': 90, 'F0ⓝ': 90, 'F2F3Ⓝ': 90, 'A1A2Ⓝ': 90, 'A2A3Ⓝ': 90, 'F0ⓣ': 0, 'F2F3Ⓣ': 0, 'A1A2Ⓣ': 0, 'A2A3Ⓣ':  0}
DC  = {'G3ⓝ':  0, 'C1ⓝ':  0, 'F0ⓝ':  δ, 'F2F3Ⓝ':  0, 'A1A2Ⓝ':  0, 'A2A3Ⓝ':  0, 'F0ⓣ': 0, 'F2F3Ⓣ': 0, 'A1A2Ⓣ': 0, 'A2A3Ⓣ':  0}
L   = [{'AB': [], 'BC': ['AB']}, {'AD': [], 'DE': ['AD'], 'EF': ['DE', 'AD']}, {'AH': [], 'HG': ['AH'], 'GF': ['HG', 'AH']}]
AC  = []
AD  = [{}, {'AD': [-p, -p], 'AB': [-p, -p]}]
ADP = {'AD': 'AD', 'AB': 'AB'}
Mol = {}
CT  = {}
CT2 = {}
Sub = {δ: l**3*p/(24*B)}
ACB = {'BA': [0, 0, B], 'AB': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'DA': [0, 0, B], 'AD': [0, 0, B], 'ED': [0, 0, B], 'DE': [0, 0, B], 'FE': [0, 0, B], 'EF': [0, 0, B], 'HA': [0, 0, B], 'AH': [0, 0, B], 'GF': [0, 0, B], 'FG': [0, 0, B], 'GH': [0, 0, B], 'HG': [0, 0, B]}
D   = {'A0': [0, 0, 0], 'F0': [-2*l, -l, 0],  'A': [0, 0, 0],  'B': [l, 0, 0],  'C': [2*l, 0, 0],'D': [-l, 0, 0], 'E': [-2*l, 0, 0], 'F': [-2*l, -l, 0], 'H': [0, -l, 0], 'G': [-l, -l, 0], 'A1': [0, 0, 0], 'B1': [l, 0, 0], 'C1': [2*l, 0, 0], 'A2': [0, 0, 0], 'D2': [-l, 0, 0], 'E2': [-2*l, 0, 0], 'F2': [-2*l, -l, 0], 'A3': [0, 0, 0], 'H3': [0, -l, 0], 'G3': [-l, -l, 0], 'F3': [-2*l, -l, 0]}
SC  = [1,2,3,4][3]
AZC = [[19*l*p/192], [317*l*p/192], [-29*l*p/96], [29*l*p/96]]
esami[1402121] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1402121)
####################################################################################################################################################################################################################################################################
#18/06/12-4 -> NUOVO NON FUNZIONANTE
'''
Pr  = ['ABCDE']
vin = [[], [], [], ['D'], [], [], ['B', 'C', 'D1']]
DA  = {'D1ⓝ': 90, 'D1ⓣ': 0, 'B1ⓔ': 90, 'C1ⓔ': 0, 'D1ⓔ': 180}
DC  = {'D1ⓝ': 0, 'D1ⓣ': 0, 'B1ⓔ': 0, 'C1ⓔ': 0, 'D1ⓔ': 0}
L   = [{'AB': [],''}]
AC  = [{}, {'A': -2*F}, {'E': -F*l}]
AD  = {}
ADP = {}
Mol = {'B1': k, 'C1': k, 'D1': 2*k}
CT  = {}
CT2 = {}
Sub = {B: k*l**3/2}
ACB = {'BA': [0, 0, B], 'AB': [0, 0, B], 'EB': [0, 0, B], 'BE': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'DC': [0, 0, B], 'CD': [0, 0, B], 'DE': [0, 0, B], 'ED': [0, 0, B]}
D   = {'A': [-l, 0, 0], 'B': [0, 0, 0], 'C': [l, 0, 0], 'D': [l, l, 0], 'E': [0, l, 0], 'A1': [-l, 0, 0], 'B1': [0, 0, 0], 'C1': [l, 0, 0], 'D1': [l, l, 0], 'E1': [0, l, 0], 'A0': [-l, 0, 0], 'B0': [0, 0, 0], 'C0': [l, 0, 0], 'D0': [l, l, 0], 'E0': [0, l, 0]}
SC  = -1
AZC = '?'

Pr   = ['ABCDEF']
D    = {'A': [-l, 0, 0], 'B': [0, 0, 0], 'C': [l, 0, 0], 'D': [0.999999*l, l, 0], 'E': [0, l, 0], 'F': [l, l, 0], 'A1': [-l, 0, 0], 'B1': [0, 0, 0], 'C1': [l, 0, 0], 'D1': [l, l, 0], 'E1': [0, l, 0], 'F1': [l, l, 0], 'A0': [-l, 0, 0], 'B0': [0, 0, 0], 'C0': [l, 0, 0], 'D0': [l, l, 0], 'E0': [0, l, 0], 'F0': [l, l, 0]}
Link = {'AB': [], 'BE': ['AB'], 'BC': ['AB'], 'CF': ['AB', 'BE'], 'ED': ['AB', 'BE'], 'DF': ['AB', 'BE']}
L    = [{'AB': [], 'BE': ['AB'], 'BC': ['AB'], 'CF': ['AB', 'BE'], 'ED': ['AB', 'BE'], 'DF': ['AB', 'BE']}]
vin  = [[], [], [], ['F'], [], [], ['B', 'C', 'DF']]
DA   = {'F1ⓝ': 90, 'F1ⓣ': 0, 'B1ⓔ': 90, 'C1ⓔ': 0, 'D1F1ⓔ': 180}
DC   = {'F1ⓝ': 0, 'F1ⓣ': 0, 'B1ⓔ': 0, 'C1ⓔ': 0, 'D1F1ⓔ': 0}
Mol  = {'B1': k, 'C1': k, 'D1F1': 2*k}
CT   = {}
CT2  = {}
Sub = {B: (k*l**3)/3}
AC   = [{}, {'A': -2*F}, {'E': -F*l}]
AD   = {}
ADP  = {}
ACB  = {'BA': [0, 0, B], 'AB': [0, 0, B], 'EB': [0, 0, B], 'BE': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'FC': [0, 0, B], 'CF': [0, 0, B], 'DE': [0, 0, B], 'ED': [0, 0, B], 'FD': [0, 0, B], 'DF': [0, 0, B]}
SC   = -1
AZC  = '?'
Pr  = ['ABCDEF']
vin = [[], [], [], ['D'], [], [], ['B', 'C', 'DF']]
DA  = {'D1ⓝ': 90, 'D1ⓣ': 0, 'B1ⓔ': 90, 'C1ⓔ': 0, 'D1F1ⓔ': 180}
DC  = {'D1ⓝ': 0, 'D1ⓣ': 0, 'B1ⓔ': 0, 'C1ⓔ': 0, 'D1F1ⓔ': 0}
L   = [{'AB': [], 'EB': ['DE'], 'CB': ['FC'], 'FC': [], 'DE': [], 'DF': []}]
AC  = [{}, {'A': -2*F}, {'E': -F*l}]
AD  = {}
ADP = {}
Mol = {'B1': k, 'C1': k, 'D1F1': 2*k}
CT  = {}
CT2 = {}
Sub = {B: k*l**3/2}
ACB = {'BA': [0, 0, B], 'AB': [0, 0, B], 'BE': [0, 0, B], 'EB': [0, 0, B], 'BC': [0, 0, B], 'CB': [0, 0, B], 'CF': [0, 0, B], 'FC': [0, 0, B], 'ED': [0, 0, B], 'DE': [0, 0, B], 'FD': [0, 0, B], 'DF': [0, 0, B]}
D   = {'A': [-l, 0, 0], 'B': [0, 0, 0], 'C': [l, 0, 0], 'D': [l, l, 0], 'E': [0, l, 0], 'F': [1.0001*l, l, 0], 'A1': [-l, 0, 0], 'B1': [0, 0, 0], 'C1': [l, 0, 0], 'D1': [l, l, 0], 'E1': [0, l, 0], 'F1': [1.0001*l, l, 0], 'A0': [-l, 0, 0], 'B0': [0, 0, 0], 'C0': [l, 0, 0], 'D0': [l, l, 0], 'E0': [0, l, 0], 'F0': [1.0001*l, l, 0]}
SC  = 3#-1
AZC = '?'

esami[1806124] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
esame(1806124)
'''
####################################################################################################################################################################################################################################################################
#12/07/12-4: funzionante, coerente, bello :)  {Modello Galatà}
Pr   = ['ABC', 'CDEF']
vin  = [['E'], ['A1E2'], [], [], ['C1C2', 'F'], [], ['A']]
DA   = {'E2ⓝ': 180, 'A1E2ⓝ': 0, 'C1C2ⓝ': 90, 'F2ⓝ': 90, 'C1C2ⓐ': 0, 'F2ⓐ': 0, 'A1ⓔ': 90}
DC   = {'E2ⓝ':  -d, 'A1E2ⓝ': 0, 'C1C2ⓝ':  0, 'F2ⓝ':  0, 'C1C2ⓐ': 0, 'F2ⓐ': 0, 'A1ⓔ':  0}
Mol  = {'A1': k}
CT   = {'AE': [t1, t1, h]}
CT2  = {}
AC   = []
AD   = [{},{'BC':[-p,-p],'CD':[-p,-p]}]
ADP  = {'BC': 'BC', 'CD': 'CD'}
L    = [{'AB': [], 'BC': ['AB']}, {'CD': [], 'DE': ['CD'], 'EF': ['CD','DE']}]
Sub  = {k: 3*B/l**3}
ACB  = {'AB': [0,0,B], 'BC': [0,0,B], 'CD': [0,0,B], 'DE': [0,0,B], 'EF': [0,0,B]}
D    = {'A': [-l, -l, 0], 'B': [-l, 0, 0], 'C': [0, 0, 0], 'D': [l, 0, 0], 'E': [l, -l, 0], 'F': [l, -2*l, 0], 'A1': [-l, -l, 0], 'B1': [-l, 0, 0], 'C1': [0, 0, 0], 'C2': [0, 0, 0], 'D2': [l, 0, 0], 'E2': [l, -l, 0], 'F2': [l, -2*l, 0]}
SC   = [1, 2, 3, 4, 5][3]
AZC  = [[l*p/11], [12*l*p/11], [9*l*p/22], [-2*l*p/11], [10*l*p/11]]
esami[1207124] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1207124)
####################################################################################################################################################################################################################################################################
#09/11/12-1 -> funzionante, coerente, brutto :(
Pr  = ['AED', 'AHDBC']
vin = [['A0', 'D0'], ['D0B2'], [], [], [], [], ['C2']]
DA  = {'A0ⓝ': -90, 'D0ⓝ': 90, 'D0B2ⓝ': 225, 'A1A2Ⓝ': 90, 'A1A2Ⓣ': 0, 'D1D2Ⓝ': 90, 'D1D2Ⓣ': 0, 'C2ⓔ': 135}
DC  = {'A0ⓝ':   0, 'D0ⓝ':  d, 'D0B2ⓝ':   0, 'A1A2Ⓝ':  0, 'A1A2Ⓣ': 0, 'D1D2Ⓝ':  0, 'D1D2Ⓣ': 0, 'C2ⓔ':   0}
L   = [{'AE': [], 'ED': ['AE']}, {'AH': [], 'DH': [], 'HB': ['AH', 'DH'], 'BC': ['AH', 'DH', 'HB']}]
AC  = [{}, {}, {'E': l**2*p}]
AD  = [{}, {'HC': [-p, -p]}]
ADP = {'HC': 'HBC'}
Mol = {'C2': k}
CT  = {}
CT2 = {}
Sub = {B: 4*k*l**3, d: l/1000}
ACB = {'EA': [0, 0, B], 'AE': [0, 0, B], 'DE': [0, 0, B], 'ED': [0, 0, B], 'HA': [0, 0, B], 'AH': [0, 0, B], 'HD': [0, 0, B], 'DH': [0, 0, B], 'BH': [0, 0, B], 'HB': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B]}
D   = {'A': [0, 0, 0], 'E': [0, -l, 0], 'D': [l, -l, 0], 'H': [l, 0, 0], 'B': [2*l, 0, 0], 'C': [3*l, 0, 0], 'A1': [0, 0, 0], 'E1': [0, -l, 0], 'D1': [l, -l, 0], 'A2': [0, 0, 0], 'H2': [l, 0, 0], 'D2': [l, -l, 0], 'B2': [2*l, 0, 0], 'C2': [3*l, 0, 0], 'A0': [0, 0, 0], 'E0': [0, -l, 0], 'D0': [l, -l, 0], 'H0': [l, 0, 0], 'B0': [2*l, 0, 0], 'C0': [3*l, 0, 0]}
SC  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10][1]
AZC = ['?',[2.3233*l*p,1.1607*l*p],'?','?','?','?','?','?','?','?']
#AZC  = [[5969398693750000*sqrt(2)*l*p/8213449879322499 + 10640784815935000*l*p/8213449879322499, -1253208931866875*sqrt(2)*l*p/5475633252881666 + 446120973730648*l*p/2737816626440833], [5969398693750000*sqrt(2)*l*p/8213449879322499 + 10640784815935000*l*p/8213449879322499, 1253208931866875*sqrt(2)*l*p/5475633252881666 + 2291695652710185*l*p/2737816626440833], [23*sqrt(2)*l*p/14, 9*l*p/56], [23*sqrt(2)*l*p/14, -65*l*p/56], [4*l*p*(-72019843129416328691777648244585113956539969087459672982693912014883734930267422325736574029596725493396441402101640934121007202720390044356219224174567422267288243342218571*k**2*l**6 + 50925719456801670033610609778702343117299251155769749608929593910285298130338801991763509352147051387240133118438283346117733223646705892812816643787303189098463282088099375*sqrt(2)*k**2*l**6)/(3*(-214218520701851081211117112966237052542793670994311254689633002019974939481024560980542348254273368461244311015290122347996520077183066660515412737493116817288607474395405713*k**2*l**6 + 151475368644029713494303950862003957564030766247555908271575830577015188304856609353785522635725777841763145239966736488593260144657023035729272738807330004016762483399770000*sqrt(2)*k**2*l**6)), 5*l*p*(-144724390318791056816394744865061346638279810958778523671275002953226277287749969347515316289975469427000335976357*k*l**3 + 102335597797505884731420994307640561516990472845254472517592320114790841236210684644117675053818403126807017340500*sqrt(2)*k*l**3)/(3*(-358009730330769412702496541140397353983797094836417143776556700068750644476835734925596392939502017002584317929071*k*l**3 + 253151108047654253573941756805771610888356836782202447069483061038259341203244008844410003411861736490547265810000*sqrt(2)*k*l**3))], [2*l*p/5, -4*l*p/15], [2*l*p/5, -11*l*p/15], [5*l*p*(-25374765737731877381*k**2*l**6 + 16687577578764091500*sqrt(2)*k**2*l**6)/(3*(-63237475026180632143*k**2*l**6 + 40950391214224095000*sqrt(2)*k**2*l**6)), -4*l*p*(-1312554375*sqrt(2)*k*l**3 + 2299974107*k*l**3)/(-10288305000*sqrt(2)*k*l**3 + 22537266963*k*l**3)], [5*l*p*(-25374765737731877381*k**2*l**6 + 16687577578764091500*sqrt(2)*k**2*l**6)/(3*(-63237475026180632143*k**2*l**6 + 40950391214224095000*sqrt(2)*k**2*l**6)), -5*l*p*(-1007617500*sqrt(2)*k*l**3 + 2667474107*k*l**3)/(-10288305000*sqrt(2)*k*l**3 + 22537266963*k*l**3)], [-l*p*(-27254651485982227500*sqrt(2)*k**2*l**6 + 37862680611689663981*k**2*l**6)/(-114775770492312480000*sqrt(2)*k**2*l**6 + 166300641688498447700*k**2*l**6), -3*l*p*(-2327537500*sqrt(2)*k*l**3 + 4207594029*k*l**3)/(-11266460000*sqrt(2)*k*l**3 + 19916442900*k*l**3)]]
esami[911121] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(911121)
####################################################################################################################################################################################################################################################################
#'''
#10/01/13-1 -> singolare
Pr   = ['LKJ', 'LHJ']
D    = {'L': [0, 0, 0], 'K': [2*l, 0, 0], 'J': [2*l, -l, 0], 'H': [0, -l, 0], 'L1': [0, 0, 0], 'K1': [2*l, 0, 0], 'J1': [2*l, -l, 0], 'L2': [0, 0, 0], 'H2': [0, -l, 0], 'J2': [2*l, -l, 0], 'L0': [0, 0, 0], 'K0': [2*l, 0, 0], 'J0': [2*l, -l, 0], 'H0': [0, -l, 0]}
vin  = [[], ['LJ'], [], ['L1L2', 'J1J2'], [], [], []]
DA   = {'L0J0ⓝ': float(-180*sym.atan(1/2)/pi + 180), 'L1L2Ⓝ': 90, 'L1L2Ⓣ': 0, 'J1J2Ⓝ': 90, 'J1J2Ⓣ': 0}#float() scritto a mano. non ricordo come avessi inserito l'input, forse gia con 180+
DC   = {'L0J0ⓝ': 0,                                  'L1L2Ⓝ':  0, 'L1L2Ⓣ': 0, 'J1J2Ⓝ':  0, 'J1J2Ⓣ': 0}
L    = [{'LK': [], 'KJ': ['LK']}, {'LH': [], 'HJ': ['LH']}]
AC   = []
AD   = {}
ADP  = {}
Mol  = {}
CT   = {'LK': [θ1, θ1, h]}
CT2  = {}
#Sub  = {d: 2*5**0.5*alfa*t1*l}
Sub  = {alfa*t1: d/(2*5**0.5*l)}
ACB  = {'KL': [0, 0, B], 'LK': [0, 0, B], 'JK': [0, 0, B], 'KJ': [0, 0, B], 'HL': [0, 0, B], 'LH': [0, 0, B], 'JH': [0, 0, B], 'HJ': [0, 0, B]} 
SC   = [1,2,3,4][3]
AZC  = '?'
esami[1001131] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1001131)
#'''
####################################################################################################################################################################################################################################################################
#SUBS() NON FUNZIONA (devi aggiornalo per le relazioni con le azioni termiche)
#12/02/13-4 -> Funziona ma NON so come trattare la sostituzione finale (i diagrammi semi-finali però coincidono con quelli di Fleres)
#Sub ha d = f(delta_teta...); errori in chiedimi_CT per via del t1t2 (shallona ma risolvi)
Pr  = ['BA', 'ADI']
vin = [[], [], [], ['I'], ['A'], ['B'], []]
DA  = {'I2ⓝ': 90, 'I2ⓣ': 0, 'A1A2ⓐ': 0, 'A1A2ⓝ': 0, 'B1㊈': 90, 'B1㊆': 0, 'B1㊅': 0}
DC  = {'I2ⓝ':  0, 'I2ⓣ': d, 'A1A2ⓐ': 0, 'A1A2ⓝ': 0, 'B1㊈':  0, 'B1㊆': 0, 'B1㊅': 0}
L   = [{'BA': []}, {'AD': [], 'DI': ['AD']}]
AC  = [{}, {}, {'D': M}]
AD  = {}
ADP = {}
Mol = {}
CT  = {'BA': [t1, t2, h]}
CT2 = {}
Sub = {d: M*l**2/(8*B), h: l/10}##-t2/2+t1/2: d/(3*alfa*l)#t2: M*l/(12*alfa*B)+t1#Fleres aggiunge h = l/10. forse lo si puo fare sempre
ACB = {'AB': [0, 0, B], 'BA': [0, 0, B], 'DA': [0, 0, B], 'AD': [0, 0, B], 'ID': [0, 0, B], 'DI': [0, 0, B]}
D   = {'B': [-l, -l, 0], 'A': [0, 0, 0], 'D': [l, 0, 0], 'I': [l, -l, 0], 'B1': [-l, -l, 0], 'A1': [0, 0, 0], 'A2': [0, 0, 0], 'D2': [l, 0, 0], 'I2': [l, -l, 0], 'B0': [-l, -l, 0], 'A0': [0, 0, 0], 'D0': [l, 0, 0], 'I0': [l, -l, 0]}
SC  = 1
AZC = '?'
#esami[1202134] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1202134)#########################################################
####################################################################################################################################################################################################################################################################
#12/04/13-4 -> funzionante, coerente, bello :) {X2 viene pl/2 invece che pl/4.. ma i diagrammi finali coincidono quindi è corretto}
Pr  = ['BED', 'EVFAD']
vin = [[], [], [], ['D', 'E1E2'], ['E1'], [], []]
DA  = {'D0ⓝ': 90, 'D0ⓣ': 0, 'D1D2Ⓝ': 90, 'D1D2Ⓣ': 0, 'E1E2ⓝ': 90, 'E1E2ⓣ': 0, 'E1ⓝ': 90,  'E1ⓐ': 0}
DC  = {'D0ⓝ':  0, 'D0ⓣ': δ, 'D1D2Ⓝ':  0, 'D1D2Ⓣ': 0, 'E1E2ⓝ':  0, 'E1E2ⓣ': 0, 'E1ⓝ':  0,  'E1ⓐ': 0}
L   = [{'BE': [], 'ED': ['BE']}, {'EV': [], 'VF': ['EV'], 'FA': ['EV', 'VF'], 'AD': ['EV', 'VF', 'FA']}]
#Link modificato ma va ancora aggiustato ancora (è facile ma mo non me pija)
AC  = []
AD  = [{}, {'BE': [-p, -p], 'VF': [-p, -p]}]
ADP = {'BE': 'BE', 'VF': 'VF'}
Mol = {}
CT  = {'BE': [θ1, θ1, h], 'ED': [θ1, θ1, h]}
CT2 = {}
Sub = {d: 3*alfa*l*t1, t1: l**3*p/(24*B*alfa)}
ACB = {'EB': [0, 0, B], 'BE': [0, 0, B], 'DE': [0, 0, B], 'ED': [0, 0, B], 'VE': [0, 0, B], 'EV': [0, 0, B], 'DA': [0, 0, B], 'AD': [0, 0, B], 'FV': [0, 0, B], 'VF': [0, 0, B], 'AF': [0, 0, B], 'FA': [0, 0, B]}
D   = {'B': [-l, 0, 0], 'E': [0, 0, 0], 'D': [2*l, 0, 0], 'V': [0, l, 0], 'F': [l, l, 0], 'A': [2*l, l, 0], 'B1': [-l, 0, 0], 'E1': [0, 0, 0], 'D1': [2*l, 0, 0], 'E2': [0, 0, 0], 'V2': [0, l, 0], 'F2': [l, l, 0], 'A2': [2*l, l, 0], 'D2': [2*l, 0, 0], 'B0': [-l, 0, 0], 'E0': [0, 0, 0], 'D0': [2*l, 0, 0], 'V0': [0, l, 0], 'F0': [l, l, 0], 'A0': [2*l, l, 0]}
SC  = [1,2,3,4,5,6][5]
AZC = [[l*p/4, 3*l*p/32], [l*p/4, -3*l*p/32], [3*l*p/32, 7*l*p/4], [3*l*p/32, -l*p/2], [-3*l*p/32, 7*l*p/4], [-3*l*p/32, -l*p/2]]
esami[1204134] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1204134)
####################################################################################################################################################################################################################################################################
#19/06/13-2 -> NON TROVA IL LAVORO ESTERNO (se lo calcolasse bene: Le = [2*d,0] funzionerebbe!!)
#Aggiustare L
Pr  = ['GFAED', 'ABECD']
vin = [[], ['F', 'C'], [], ['D'], [], [], ['A1A2', 'E1E2']]
DA  = {'F1ⓝ':  270, 'C2ⓝ': 0, 'D0ⓝ': 90, 'D0ⓣ': 0, 'D1D2Ⓝ': 90, 'D1D2Ⓣ': 0, 'A1A2ⓔ': 180, 'E1E2ⓔ': 90}
DC  = {'F1ⓝ': -2*d, 'C2ⓝ': d, 'D0ⓝ':  0, 'D0ⓣ': 0, 'D1D2Ⓝ':  0, 'D1D2Ⓣ': 0, 'A1A2ⓔ':   0, 'E1E2ⓔ':  0}
L   = [{'GF': [], 'AF': [], 'FE': ['GF', 'AF'], 'ED': ['GF', 'AF', 'FE']},{'AB': [], 'EB': [], 'BC': ['AB', 'EB'], 'CD': ['AB', 'EB', 'BC']}]
AC  = []
AD  = {}
ADP = {}
Mol = {'A1A2': k, 'E1E2': k}
CT  = {}
CT2 = {}
Sub = {k: 2*B/l**3}
ACB = {'FG': [0, 0, B], 'GF': [0, 0, B], 'FA': [0, 0, B], 'AF': [0, 0, B], 'EF': [0, 0, B], 'FE': [0, 0, B], 'DE': [0, 0, B], 'ED': [0, 0, B], 'BA': [0, 0, B], 'AB': [0, 0, B], 'BE': [0, 0, B], 'EB': [0, 0, B], 'DC': [0, 0, B], 'CD': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B]}
D   = {'G': [0, 0, 0], 'F': [l, 0, 0], 'A': [l, l, 0], 'E': [2*l, 0, 0], 'D': [3*l, 0, 0], 'B': [2*l, l, 0], 'C': [3*l, l, 0], 'G1': [0, 0, 0], 'F1': [l, 0, 0], 'A1': [l, l, 0], 'E1': [2*l, 0, 0], 'D1': [3*l, 0, 0], 'A2': [l, l, 0], 'B2': [2*l, l, 0], 'E2': [2*l, 0, 0], 'C2': [3*l, l, 0], 'D2': [3*l, 0, 0], 'G0': [0, 0, 0], 'F0': [l, 0, 0], 'A0': [l, l, 0], 'E0': [2*l, 0, 0], 'D0': [3*l, 0, 0], 'B0': [2*l, l, 0], 'C0': [3*l, l, 0]}
SC  = 7
AZC = '?'
#esami[1906132] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1906132)#########################################################
####################################################################################################################################################################################################################################################################
#8/07/13-1 Fleres lo fa ma un po incasinato. E' pieno di roba termica.
####################################################################################################################################################################################################################################################################
#21/09/13-4
####################################################################################################################################################################################################################################################################
#8/11/13-4 SINGOLARE
####################################################################################################################################################################################################################################################################
#FINE RACCOLTA 1 DI ESERCIZI.
#Fatteli venire tutti il prima possibile e passa alla seconda raccolta.
####################################################################################################################################################################################################################################################################
#24/10/20-1 -> isostatico 
Pr  = ['QR', 'HJK']
vin = [[], ['RJ', 'RK'], [], ['H'], ['Q'], [], []]
DA  = {'R1J2ⓝ': 90, 'R1K2ⓝ': -180*sym.atan(1/2)/pi + 180, 'H2ⓝ': 90, 'H2ⓣ': 0, 'Q1ⓐ': 0, 'Q1ⓝ': 0}##26.57 = ARCTG(1/2)#-180*sym.atan(1/2)/pi
DC  = {'R1J2ⓝ': 0, 'R1K2ⓝ': 0, 'H2ⓝ': 0, 'H2ⓣ': 0, 'Q1ⓐ': (p*l**3)/(3*B), 'Q1ⓝ': 0}
L   = [{'QR': []}, {'HJ': [], 'JK': ['HJ']}]
AC  = []
AD  = [{}, {'HK': [0, p]}]
ADP = {'HK': 'HJK'}
Mol = {}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'RQ': [0, 0, 0], 'QR': [0, 0, 0], 'JH': [0, 0, B], 'HJ': [0, 0, B], 'KJ': [0, 0, B], 'JK': [0, 0, B]}
D   = {'Q': [-l, l, 0], 'R': [l, l, 0], 'H': [0, 0, 0], 'J': [l, 0, 0], 'K': [3*l, 0, 0], 'Q1': [-l, l, 0], 'R1': [l, l, 0], 'H2': [0, 0, 0], 'J2': [l, 0, 0], 'K2': [3*l, 0, 0], 'Q0': [-l, l, 0], 'R0': [l, l, 0], 'H0': [0, 0, 0], 'J0': [l, 0, 0], 'K0': [3*l, 0, 0]}
SC  = -1
AZC = '?'
esami[2410201] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(2410201)
#CampionaPunto(esami[2410201],'R1ⓝ',90)#sbaglia di 0.1 su 1.76
#CampionaPunto(esami[2410201],'J2ⓝ',90)#stesso risultato (credo debba essere cosi a ragione)

#CampionaPunto(esami[2410201],'K2ⓝ',90)#stesso risultato (...)


#17/09/20-1
#N.B.: SE avessi scritto KO anzicchè OK in L mi avrebbe dato errore!! (la parte sulle azioni distribuite và sistemata)
#Devi centrare l'origine in base alla forza distribuita
Pr  = ['PQR', 'HJK', 'OK']
vin = [['P', 'R'], ['QH', 'QJ'], [], [], ['K2K3'], ['O'], []]
DA  = {'P1ⓝ': 90, 'R1ⓝ': 180, 'Q1H2ⓝ': 180, 'Q1J2ⓝ': 135, 'K2K3ⓐ': 0, 'K2K3ⓝ': 180, 'O3㊈': 90, 'O3㊆': 0, 'O3㊅': 0}
DC  = {'P1ⓝ': 0, 'R1ⓝ': 0, 'Q1H2ⓝ': l*α*θ, 'Q1J2ⓝ': 0, 'K2K3ⓐ': 0, 'K2K3ⓝ': 0, 'O3㊈': 0, 'O3㊆': 0, 'O3㊅': 0}
L   = [{'PQ': [], 'QR': ['PQ']}, {'HJ': [], 'JK': ['HJ']}, {'OK': []}]
AC  = []
AD  = [{'OK': [0, p]}, {}]
ADP = {'OK': 'OK'}
Mol = {}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'QP': [0, 0, 0], 'PQ': [0, 0, 0], 'RQ': [0, 0, 0], 'QR': [0, 0, 0], 'JH': [0, 0, 0], 'HJ': [0, 0, 0], 'KJ': [0, 0, 0], 'JK': [0, 0, 0], 'OK': [0, 0, B], 'KO': [0, 0, B]}
D   = {'P': [-3*l, 0, 0], 'Q': [-2*l, 0, 0], 'R': [-2*l, -l, 0], 'H': [-l, 0, 0], 'J': [-l, -l, 0], 'K': [0, -l, 0], 'O': [0, 0, 0], 'P1': [-3*l, 0, 0], 'Q1': [-2*l, 0, 0], 'R1': [-2*l, -l, 0], 'H2': [-l, 0, 0], 'J2': [-l, -l, 0], 'K2': [0, -l, 0], 'O3': [0, 0, 0], 'K3': [0, -l, 0], 'P0': [-3*l, 0, 0], 'Q0': [-2*l, 0, 0], 'R0': [-2*l, -l, 0], 'H0': [-l, 0, 0], 'J0': [-l, -l, 0], 'K0': [0, -l, 0], 'O0': [0, 0, 0]}
SC  = -1
AZC = '?'
esami[1709201] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1709201)

'''
#08/11/13 -> singolare: va messa una cerniera interna in S: riscrivo dopo:
Pr  = ['HRSJ', 'HJQ']
vin = [[], [], [], ['H1H2', 'J1J2'], [], [], ['H', 'J', 'Q']]
DA  = {'H1H2Ⓝ': 90, 'H1H2Ⓣ': 0, 'J1J2Ⓝ': 90, 'J1J2Ⓣ': 0, 'Hⓔ': 90, 'Jⓔ': 90, 'Q2ⓔ': 90}
DC  = {'H1H2Ⓝ': 0, 'H1H2Ⓣ': 0, 'J1J2Ⓝ': 0, 'J1J2Ⓣ': 0, 'Hⓔ': 0, 'Jⓔ': 0, 'Q2ⓔ': 0}
L   = [{'HR': [], 'HJ': [], 'RS': ['HR'], 'SJ': ['HR', 'RS']}, {'HJ': [], 'JQ': ['HJ']}]
AC  = []
AD  = [{}, {'RS': [p, p], 'JQ': [p, p]}]
ADP = {'RS': 'RS', 'JQ': 'JQ'}
Mol = {'H': 2*k, 'J': k, 'Q2': k}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'RH': [0, 0, B], 'HR': [0, 0, B], 'JH': [0, 0, B], 'HJ': [0, 0, B], 'SR': [0, 0, B], 'RS': [0, 0, B], 'JS': [0, 0, B], 'SJ': [0, 0, B], 'QJ': [0, 0, B], 'JQ': [0, 0, B]}
D   = {'H': [-l, 0, 0], 'R': [-l, l, 0], 'S': [0, l, 0], 'J': [0, 0, 0], 'Q': [l, 0, 0], 'H1': [-l, 0, 0], 'R1': [-l, l, 0], 'S1': [0, l, 0], 'J1': [0, 0, 0], 'H2': [-l, 0, 0], 'J2': [0, 0, 0], 'Q2': [l, 0, 0], 'H0': [-l, 0, 0], 'R0': [-l, l, 0], 'S0': [0, l, 0], 'J0': [0, 0, 0], 'Q0': [l, 0, 0]}
SC  = -1
AZC = '?'
esami[81113] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
##################con l'aggiunta di una cerniera in S: (quando a rilassa ottiene una f.campionatrice == momento...)
Pr  = ['HRSJ', 'HJQ']
vin = [[], [], [], ['H1H2', 'J1J2', 'S1'], [], [], ['H', 'J', 'Q']]
DA  = {'H1H2Ⓝ': 90, 'H1H2Ⓣ': 0, 'J1J2Ⓝ': 90, 'J1J2Ⓣ': 0, 'S1ⓝ': 90, 'S1ⓣ': 0, 'Hⓔ': 90, 'Jⓔ': 90, 'Q2ⓔ': 90}
DC  = {'H1H2Ⓝ': 0, 'H1H2Ⓣ': 0, 'J1J2Ⓝ': 0, 'J1J2Ⓣ': 0, 'S1ⓝ': 0, 'S1ⓣ': 0, 'Hⓔ': 0, 'Jⓔ': 0, 'Q2ⓔ': 0}
L   = [{'HR': [], 'HJ': [], 'RS': ['HR'], 'SJ': ['HR', 'RS']}, {'HJ': [], 'JQ': ['HJ']}]
AC  = []
AD  = [{}, {'RS': [p, p], 'SQ': [p, p]}]
ADP = {'RS': 'RS', 'SQ': 'SQ'}
Mol = {'H': 2*k, 'J': k, 'Q2': k}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'RH': [0, 0, B], 'HR': [0, 0, B], 'JH': [0, 0, B], 'HJ': [0, 0, B], 'SR': [0, 0, B], 'RS': [0, 0, B], 'JS': [0, 0, B], 'SJ': [0, 0, B], 'QJ': [0, 0, B], 'JQ': [0, 0, B]}
D   = {'H': [-l, 0, 0], 'R': [-l, l, 0], 'S': [0, l, 0], 'J': [0, 0, 0], 'Q': [l, 0, 0], 'H1': [-l, 0, 0], 'R1': [-l, l, 0], 'S1': [0, l, 0], 'J1': [0, 0, 0], 'H2': [-l, 0, 0], 'J2': [0, 0, 0], 'Q2': [l, 0, 0], 'H0': [-l, 0, 0], 'R0': [-l, l, 0], 'S0': [0, l, 0], 'J0': [0, 0, 0], 'Q0': [l, 0, 0]}
SC  = -1
AZC = '?'
esami[81113] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(81113)
##################con l'aggiunta di un pantografo in S: (quando a rilassa ottiene una f.campionatrice == momento...)
Pr  = ['HRSJ', 'HJQ']
vin = [[], [], ['S'], ['H1H2', 'J1J2'], [], [], ['H', 'J', 'Q']]
DA  = {'S1ⓐ': 0, 'H1H2Ⓝ': 90, 'H1H2Ⓣ': 0, 'J1J2Ⓝ': 90, 'J1J2Ⓣ': 0, 'Hⓔ': 90, 'Jⓔ': 90, 'Q2ⓔ': 90}
DC  = {'S1ⓐ': 0, 'H1H2Ⓝ': 0, 'H1H2Ⓣ': 0, 'J1J2Ⓝ': 0, 'J1J2Ⓣ': 0, 'Hⓔ': 0, 'Jⓔ': 0, 'Q2ⓔ': 0}
L   = [{'HR': [], 'HJ': [], 'RS': ['HR'], 'SJ': ['HR', 'RS']}, {'HJ': [], 'JQ': ['HJ']}]
AC  = []
AD  = [{}, {'RS': [p, p], 'SQ': [p, p]}]
ADP = {'RS': 'RS', 'SQ': 'SQ'}
Mol = {'H': 2*k, 'J': k, 'Q2': k}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'RH': [0, 0, B], 'HR': [0, 0, B], 'JH': [0, 0, B], 'HJ': [0, 0, B], 'SR': [0, 0, B], 'RS': [0, 0, B], 'JS': [0, 0, B], 'SJ': [0, 0, B], 'QJ': [0, 0, B], 'JQ': [0, 0, B]}
D   = {'H': [-l, 0, 0], 'R': [-l, l, 0], 'S': [0, l, 0], 'J': [0, 0, 0], 'Q': [l, 0, 0], 'H1': [-l, 0, 0], 'R1': [-l, l, 0], 'S1': [0, l, 0], 'J1': [0, 0, 0], 'H2': [-l, 0, 0], 'J2': [0, 0, 0], 'Q2': [l, 0, 0], 'H0': [-l, 0, 0], 'R0': [-l, l, 0], 'S0': [0, l, 0], 'J0': [0, 0, 0], 'Q0': [l, 0, 0]}
SC  = -1
AZC = '?'
esami[81113] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(81113)
'''

#esercizio Rossi: problema statico -> NON SCRITTO 
Pr  = ['ABCD']
vin = [['A', 'B', 'C'], [], [], [], [], [], ['D']]
DA  = {'A1ⓝ': 90, 'B1ⓝ': 0, 'C1ⓝ': 0, 'D1ⓔ': 0}
DC  = {'A1ⓝ': 2*d, 'B1ⓝ': -d, 'C1ⓝ': d, 'D1ⓔ': 0}
L   = [{'AC': [], 'BC': [], 'CD': []}]#dubbi
AC  = [{'A': 2*F}, {'B': -F}, {'D': 2*F*l}]
AD  = {}
ADP = {}
Mol = {'D1': 2*k}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'CA': [0, 0, B], 'AC': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'DC': [0, 0, B], 'CD': [0, 0, B]}
D   = {'A': [-l, 0, 0], 'B': [0, l, 0], 'C': [0, 0, 0], 'D': [0, -l, 0], 'A1': [-l, 0, 0], 'B1': [0, l, 0], 'C1': [0, 0, 0], 'D1': [0, -l, 0], 'A0': [-l, 0, 0], 'B0': [0, l, 0], 'C0': [0, 0, 0], 'D0': [0, -l, 0]}
SC  = -1
AZC = '?'
#esami[1111111111] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1111111111)

#Prova: Campionamento sistemi isostatici: aggiungo un vincolo che impedisce la componente di spostamento che voglio sondare in un sistema isostatico e copio fino ai diagrammi dei momenti dei sistemi 0 e 1:
#FUNZIONATE!!! Cafonata, ma funzionante!!!
#ottieni i valori delle azioni di contatto del sistema 0 (sistema reale) e del sistema 1 (sistema con punto campionato)
#a questo punto prendi i valori dei momenti e sui la formula:
# 1*v(P) = integrale (M* M/B + T* T/C + N* N/A) da cui v(P).... :)
#in realtà andrebbero aggiunti eventuali reazioni vincolari*spostamenti (== Lavoro esterno) se altri punti si spostano a seguito della forza fittizia
#questi li puoi prendere dal Lext ottenuto (verifica meglio)
#N.B.: Componente di spostamento testata non presentava alcun vincolo nella direzione da campionare
Pr  = ['ABC', 'EDH']
vin = [['H'], ['B1E2', 'C1E2'], [], ['D'], ['A'], [], []]
DA  = {'H2ⓝ': 90, 'B1E2ⓝ': 90, 'C1E2ⓝ': 45, 'D2ⓝ': 90, 'D2ⓣ': 0, 'A1ⓐ': 0, 'A1ⓝ': 45}
DC  = {'H2ⓝ': 0, 'B1E2ⓝ': 0, 'C1E2ⓝ': 0, 'D2ⓝ': 0, 'D2ⓣ': 0, 'A1ⓐ': 0, 'A1ⓝ': 0}
L   = [{'AB': [], 'BC': ['AB']}, {'ED': [], 'DH': ['ED']}]
AC  = []
AD  = [{}, {'AB': [p, p]}]
ADP = {'AB': 'AB'}
Mol = {}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'BA': [0, 0, B], 'AB': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'DE': [0, 0, B], 'ED': [0, 0, B], 'HD': [0, 0, B], 'DH': [0, 0, B]}
D   = {'A': [-2*l, l, 0], 'B': [0, l, 0], 'C': [l, l, 0], 'E': [0, 0, 0], 'D': [l, 0, 0], 'H': [2*l, 0, 0], 'A1': [-2*l, l, 0], 'B1': [0, l, 0], 'C1': [l, l, 0], 'E2': [0, 0, 0], 'D2': [l, 0, 0], 'H2': [2*l, 0, 0], 'A0': [-2*l, l, 0], 'B0': [0, l, 0], 'C0': [l, l, 0], 'E0': [0, 0, 0], 'D0': [l, 0, 0], 'H0': [2*l, 0, 0]}
SC  = -1
AZC = '?'
#esami[1201122] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1201122)

#Prova: Tralicci come se non fossero tali: con cerniere...
#dubbi su link...
Pr  = ['ABCDEFGH']
vin = [['A', 'B', 'C'], [], [], ['A1', 'B1', 'C1', 'F1', 'G1', 'E1', 'H1', 'D1'], [], [], []]
DA  = {'A1ⓝ': 90, 'B1ⓝ': 90, 'C1ⓝ': 90, 'A1ⓣ': 0, 'B1ⓣ': 0, 'C1ⓣ': 0, 'F1ⓝ': 90, 'F1ⓣ': 0, 'G1ⓝ': 90, 'G1ⓣ': 0, 'E1ⓝ': 90, 'E1ⓣ': 0, 'H1ⓝ': 90, 'H1ⓣ': 0, 'D1ⓝ': 90, 'D1ⓣ': 0}
DC  = {'A1ⓝ': 0, 'B1ⓝ': 0, 'C1ⓝ': 0, 'A1ⓣ': 0, 'B1ⓣ': 0, 'C1ⓣ': 0, 'F1ⓝ': 0, 'F1ⓣ': 0, 'G1ⓝ': 0, 'G1ⓣ': 0, 'E1ⓝ': 0, 'E1ⓣ': 0, 'H1ⓝ': 0, 'H1ⓣ': 0, 'D1ⓝ': 0, 'D1ⓣ': 0}
L   = [{'AF': [], 'AG': [], 'AB': [], 'BG': [], 'BC': ['AB'], 'CD': [],'EH': [], 'HD': ['EH'], 'EG': [], 'EF': [], 'FG': [], 'GH': []}]
AC  = []
AD  = [{}, {'ED': [p, p]}]
ADP = {'ED': 'EHD'}
Mol = {}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'FA': [0, 0, B], 'AF': [0, 0, B], 'GA': [0, 0, B], 'AG': [0, 0, B], 'BA': [0, 0, B], 'AB': [0, 0, B], 'GB': [0, 0, B], 'BG': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'DC': [0, 0, B], 'CD': [0, 0, B], 'HD': [0, 0, B], 'DH': [0, 0, B], 'HE': [0, 0, B], 'EH': [0, 0, B], 'GE': [0, 0, B], 'EG': [0, 0, B], 'FE': [0, 0, B], 'EF': [0, 0, B], 'GF': [0, 0, B], 'FG': [0, 0, B], 'HG': [0, 0, B], 'GH': [0, 0, B]}
D   = {'A': [-l, -l, 0], 'B': [0, -l, 0], 'C': [l, -l, 0], 'D': [l, l, 0], 'E': [-l, l, 0], 'F': [-l, 0, 0], 'G': [0, 0, 0], 'H': [0, l, 0], 'A1': [-l, -l, 0], 'B1': [0, -l, 0], 'C1': [l, -l, 0], 'D1': [l, l, 0], 'E1': [-l, l, 0], 'F1': [-l, 0, 0], 'G1': [0, 0, 0], 'H1': [0, l, 0], 'A0': [-l, -l, 0], 'B0': [0, -l, 0], 'C0': [l, -l, 0], 'D0': [l, l, 0], 'E0': [-l, l, 0], 'F0': [-l, 0, 0], 'G0': [0, 0, 0], 'H0': [0, l, 0]}
SC  = 1#>322 proposte...
AZC = '?'
###con pendoli! solo 3 liste proposte!! :D
Pr  = ['ABCDEFGH']
vin = [['A', 'B', 'C'], ['AB', 'AF', 'AG', 'BG', 'BC', 'CD', 'FG', 'EF', 'EG', 'EH', 'HD', 'HG'], [], [], [], [], []]
DA  = {'A1ⓝ': 90, 'B1ⓝ': 90, 'C1ⓝ': 90, 'A1B1ⓝ': 180, 'A1F1ⓝ': 270, 'A1G1ⓝ': 225, 'B1G1ⓝ': 270, 'B1C1ⓝ': 180, 'C1D1ⓝ': 270, 'F1G1ⓝ': 180, 'E1F1ⓝ': 90, 'E1G1ⓝ': 135, 'E1H1ⓝ': 180, 'H1D1ⓝ': 180, 'H1G1ⓝ': 90}
DC  = {'A1ⓝ': 0, 'B1ⓝ': 0, 'C1ⓝ': 0, 'A1B1ⓝ': 0, 'A1F1ⓝ': 0, 'A1G1ⓝ': 0, 'B1G1ⓝ': 0, 'B1C1ⓝ': 0, 'C1D1ⓝ': 0, 'F1G1ⓝ': 0, 'E1F1ⓝ': 0, 'E1G1ⓝ': 0, 'E1H1ⓝ': 0, 'H1D1ⓝ': 0, 'H1G1ⓝ': 0}
L   = [{'AF': [], 'AG': [], 'AB': [], 'BG': [], 'BC': ['AB'], 'DC': [], 'HD': ['EH'], 'EH': [], 'EG': [], 'EF': [], 'FG': [], 'GH': []}]
AC  = []
AD  = [{}, {'ED': [p, p]}]
ADP = {'ED': 'EHD'}
Mol = {}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'FA': [0, 0, B], 'AF': [0, 0, B], 'GA': [0, 0, B], 'AG': [0, 0, B], 'BA': [0, 0, B], 'AB': [0, 0, B], 'GB': [0, 0, B], 'BG': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'DC': [0, 0, B], 'CD': [0, 0, B], 'DH': [0, 0, B], 'HD': [0, 0, B], 'HE': [0, 0, B], 'EH': [0, 0, B], 'GE': [0, 0, B], 'EG': [0, 0, B], 'FE': [0, 0, B], 'EF': [0, 0, B], 'GF': [0, 0, B], 'FG': [0, 0, B], 'HG': [0, 0, B], 'GH': [0, 0, B]}
D   = {'A': [-l, -l, 0], 'B': [0, -l, 0], 'C': [l, -l, 0], 'D': [l, l, 0], 'E': [-l, l, 0], 'F': [-l, 0, 0], 'G': [0, 0, 0], 'H': [0, l, 0], 'A1': [-l, -l, 0], 'B1': [0, -l, 0], 'C1': [l, -l, 0], 'D1': [l, l, 0], 'E1': [-l, l, 0], 'F1': [-l, 0, 0], 'G1': [0, 0, 0], 'H1': [0, l, 0], 'A0': [-l, -l, 0], 'B0': [0, -l, 0], 'C0': [l, -l, 0], 'D0': [l, l, 0], 'E0': [-l, l, 0], 'F0': [-l, 0, 0], 'G0': [0, 0, 0], 'H0': [0, l, 0]}
SC  = -1#3 proposte :)
AZC = '?'
#considerando due corpi rigidi senza considerare i pendoli interni (a parte uno che li unisce)
#DA MODIFICARE PERCHè FUNZIONI
Pr  = ['EABGC', 'EHDC']
vin = [['A', 'B', 'C'], ['G1H2'], [], ['E1E2', 'C1C2', 'D1'], [], [], []]
DA  = {'A1ⓝ': 90, 'B1ⓝ': 90, 'C0ⓝ': 90, 'G1H2ⓝ': 270, 'E1E2Ⓝ': 90, 'E1E2Ⓣ': 0, 'C1C2Ⓝ': 90, 'C1C2Ⓣ': 0, 'D2ⓝ': 90, 'D2ⓣ': 0}
DC  = {'A1ⓝ': 0, 'B1ⓝ': 0, 'C0ⓝ': 0, 'G1H2ⓝ': 0, 'E1E2Ⓝ': 0, 'E1E2Ⓣ': 0, 'C1C2Ⓝ': 0, 'C1C2Ⓣ': 0, 'D2ⓝ': 0, 'D2ⓣ': 0}
L   = [{'EA': [], 'AB': [], 'BG': [], 'BC': ['AB']}, {'EH': [], 'HH': ['EH'], 'HD': ['HH', 'EH'], 'DC': ['HD', 'HH', 'EH']}]
AC  = []
AD  = [{}, {'ED': [p, p]}]
ADP = {'ED': 'EHD'}
Mol = {}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'AE': [0, 0, B], 'EA': [0, 0, B], 'BA': [0, 0, B], 'AB': [0, 0, B], 'GB': [0, 0, B], 'BG': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'HE': [0, 0, B], 'EH': [0, 0, B], 'HH': [0, 0, B], 'DH': [0, 0, B], 'HD': [0, 0, B], 'CD': [0, 0, B], 'DC': [0, 0, B]}
D   = {'E': [-l, l, 0], 'A': [-l, -l, 0], 'B': [0, -l, 0], 'G': [0, 0, 0], 'C': [l, -l, 0], 'H': [0, l, 0], 'D': [l, l, 0], 'E1': [-l, l, 0], 'A1': [-l, -l, 0], 'B1': [0, -l, 0], 'G1': [0, 0, 0], 'C1': [l, -l, 0], 'E2': [-l, l, 0], 'H2': [0, l, 0], 'D2': [l, l, 0], 'C2': [l, -l, 0], 'E0': [-l, l, 0], 'A0': [-l, -l, 0], 'B0': [0, -l, 0], 'G0': [0, 0, 0], 'C0': [l, -l, 0], 'H0': [0, l, 0], 'D0': [l, l, 0]}
SC  = -1
AZC = '?'
#esami[1709202] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1709202)

#TRALICCIO 18/06/12-1 #poichè si considerano pendoli, Ntot è nulla perchè le azioni da un lato sono uaguali e opposte dall'altro. Bisogna considerare cerniere e vedere i bilancio ai nodi...
Pr  = ['LJHG']
vin = [['L', 'H', 'G'], ['LJ', 'LG', 'JG', 'GH', 'JH'], [], [], [], [], []]
DA  = {'L1ⓝ': 90, 'H1ⓝ': 180, 'G1ⓝ': 90, 'L1J1ⓝ': 225, 'L1G1ⓝ': 180, 'J1G1ⓝ': 135, 'G1H1ⓝ': 225, 'J1H1ⓝ': 180}
DC  = {'L1ⓝ': 0, 'H1ⓝ': 0, 'G1ⓝ': 0, 'L1J1ⓝ': 0, 'L1G1ⓝ': 0, 'J1G1ⓝ': 0, 'G1H1ⓝ': 0, 'J1H1ⓝ': 0}
L   = [{'LJ': [], 'LG': [], 'JG': [], 'JH': [], 'GH': []}]
AC  = [{'G': p, 'L': p}, {'J': -p}, {}]
AD  = {}
ADP = {}
Mol = {}
CT  = {}
CT2 = {'GH': 2**(1/2)*l}
Sub = {}
#ACB = {'JL': [A, 0, B], 'LJ': [A, 0, B], 'GL': [A, 0, B], 'LG': [A, 0, B], 'GJ': [A, 0, B], 'JG': [A, 0, B], 'HJ': [A, 0, B], 'JH': [A, 0, B], 'HG': [A, 0, B], 'GH': [A, 0, B]}
ACB = {'JL': [A, 0, 0], 'LJ': [A, 0, 0], 'GL': [A, 0, 0], 'LG': [A, 0, 0], 'GJ': [A, 0, 0], 'JG': [A, 0, 0], 'HJ': [A, 0, 0], 'JH': [A, 0, 0], 'HG': [A, 0, 0], 'GH': [A, 0, 0]}
D   = {'L': [0, 0, 0], 'J': [l, l, 0], 'H': [3*l, l, 0], 'G': [2*l, 0, 0], 'L1': [0, 0, 0], 'J1': [l, l, 0], 'H1': [3*l, l, 0], 'G1': [2*l, 0, 0], 'L0': [0, 0, 0], 'J0': [l, l, 0], 'H0': [3*l, l, 0], 'G0': [2*l, 0, 0]}
SC  = -1
AZC = '?'
#esami[1806121] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(1806121)

#traliccio singolare senza sollecitazione esterne e solo cedimenti
'''
Pr  = ['AB', 'BC', 'CD', 'DA']
vin = [[], ['AC', 'BD'], [], ['A1A4', 'B1B2', 'C2C3', 'D3D4'], [], [], []]
DA  = {'A0C0ⓝ': 135, 'B0D0ⓝ': 45, 'A1A4Ⓝ': 90, 'A1A4Ⓣ': 0, 'B1B2Ⓝ': 90, 'B1B2Ⓣ': 0, 'C2C3Ⓝ': 90, 'C2C3Ⓣ': 0, 'D3D4Ⓝ': 90, 'D3D4Ⓣ': 0}
DC  = {'A0C0ⓝ': 2*d, 'B0D0ⓝ': d, 'A1A4Ⓝ': 0, 'A1A4Ⓣ': 0, 'B1B2Ⓝ': 0, 'B1B2Ⓣ': 0, 'C2C3Ⓝ': 0, 'C2C3Ⓣ': 0, 'D3D4Ⓝ': 0, 'D3D4Ⓣ': 0}
L   = [{'AB': []}, {'BC': []}, {'CD': []}, {'AD': []}]
AC  = []
AD  = {}
ADP = {}
Mol = {}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'BA': [A, 0, B], 'AB': [A, 0, B], 'CB': [A, 0, B], 'BC': [A, 0, B], 'DC': [A, 0, B], 'CD': [A, 0, B], 'DA': [A, 0, B], 'AD': [A, 0, B]}
D   = {'A': [0, 0, 0], 'B': [l, 0, 0], 'C': [l, -l, 0], 'D': [0, -l, 0], 'A1': [0, 0, 0], 'B1': [l, 0, 0], 'B2': [l, 0, 0], 'C2': [l, -l, 0], 'C3': [l, -l, 0], 'D3': [0, -l, 0], 'D4': [0, -l, 0], 'A4': [0, 0, 0], 'A0': [0, 0, 0], 'B0': [l, 0, 0], 'C0': [l, -l, 0], 'D0': [0, -l, 0]}
SC  = -1
AZC = '?'
esami[234] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
esame(234)
'''
Pr  = ['ABC', 'CDEFG', 'GA']
vin = [[], [], [], ['A1A3', 'G2G3'], ['C1C2'], [], ['GD']]
DA  = {'A1A3Ⓝ': 90, 'A1A3Ⓣ': 0, 'G2G3Ⓝ': 90, 'G2G3Ⓣ': 0, 'C1C2ⓐ': 0, 'C1C2ⓝ': 0, 'G0D2ⓔ': 270}
DC  = {'A1A3Ⓝ':  0, 'A1A3Ⓣ': 0, 'G2G3Ⓝ':  0, 'G2G3Ⓣ': 0, 'C1C2ⓐ': 0, 'C1C2ⓝ': 0, 'G0D2ⓔ':   0}
L   = [{'AB': [], 'BC': ['AB']}, {'CD': [], 'DE': ['CD'], 'EF': ['DE', 'CD'], 'FG': ['EF', 'DE', 'CD']}, {'AG': []}]
AC  = [{}, {'E': -F, 'G0': F}, {'B': F*l}]
AD  = {}
ADP = {}
Mol = {'G0D2': k}
CT  = {}
CT2 = {}
Sub = {B: 3*k*l**3}
ACB = {'BA': [0, 0, B], 'AB': [0, 0, B], 'CB': [0, 0, B], 'BC': [0, 0, B], 'DC': [0, 0, B], 'CD': [0, 0, B], 'ED': [0, 0, B], 'DE': [0, 0, B], 'FE': [0, 0, B], 'EF': [0, 0, B], 'GF': [0, 0, B], 'FG': [0, 0, B], 'GA': [0, 0, B], 'AG': [0, 0, B]}
D   = {'A': [0, 0, 0], 'B': [0, l, 0], 'C': [l, l, 0], 'D': [2*l, l, 0], 'E': [3*l, l, 0], 'F': [3*l, 0, 0], 'G': [2*l, 0, 0], 'A1': [0, 0, 0], 'B1': [0, l, 0], 'C1': [l, l, 0], 'C2': [l, l, 0], 'D2': [2*l, l, 0], 'E2': [3*l, l, 0], 'F2': [3*l, 0, 0], 'G2': [2*l, 0, 0], 'G3': [2*l, 0, 0], 'A3': [0, 0, 0], 'A0': [0, 0, 0], 'B0': [0, l, 0], 'C0': [l, l, 0], 'D0': [2*l, l, 0], 'E0': [3*l, l, 0], 'F0': [3*l, 0, 0], 'G0': [2*l, 0, 0]}
SC  = -1
AZC = '?'
esami[911201] = [Pr,vin,DA,DC,L,AC,AD,ADP,Mol,CT,CT2,Sub,ACB,D,SC,AZC]
#esame(911201)

#len == 2 -> corretto, 3 -> sbagliato
def AggiornaEsami_Corretti_Sbagliati_Unknown():
    #
    #TF,s,sv = [True,False],1,1
    #Stampa,Stampa_Verifica = TF[s],TF[sv]
    #
    for i in esami:
        j = esami[i]
        if j[15] == '?':
            esami_unknown.append(i)
        else:
            #
            #j.append(Stampa)
            #j.append(Stampa_Verifica)
            #
            if len(esame(j)) == 2:
                esami_corretti.append(i)
            elif len(esame(j)) == 3:
                esami_sbagliati.append(i)
            else:
                color.write('ATTENZIONE!')
                print('\nEsame:',i)
                print('Nè corretto,nè sbagliato,nè conosciuto...')
    return [esami_corretti,esami_sbagliati,esami_unknown]
    
def MostraEsami_Corretti_Sbagliati_Unknown(*o):
    AggiornaEsami_Corretti_Sbagliati_Unknown()
    StampaInLinea,StampaListe = False,True
    if len(o) != 0:
        StampaInLinea,StampaListe =  True,False
    if StampaInLinea == True:
        color.write('Esami corretti:\n',colori['Verde'])
        for i in esami_corretti:
            color.write(str(i),colori['Blu'])
            color.write(' '*(7-len(str(i)))+' => ',colori['Arancione'])
            dman(i)
            #print(i,' '*(7-len(str(i))),'-> ',dman(i))
        if len(esami_corretti) == 0:
            print('Nessuno :(')
        color.write('\nEsami sbagliati:\n',colori['Rosso'])
        for i in esami_sbagliati:
            color.write(str(i),colori['Blu'])
            color.write(' '*(7-len(str(i)))+' => ',colori['Arancione'])
            dman(i)
            #print(i,' '*(7-len(str(i))),'-> ',dman(i))
        if len(esami_sbagliati) == 0:
            print('Nessuno :)')
        color.write('\nEsami sconosciuti:\n',colori['Viola'])
        for i in esami_unknown:
            color.write(str(i),colori['Blu'])
            color.write(' '*(7-len(str(i)))+' => ',colori['Arancione'])
            dman(i)
            #print(i,' '*(7-len(str(i))),'-> ',dman(i))
        if len(esami_unknown) == 0:
            print('Nessuno :|')
        print()
    if StampaListe == True:
        print('esami_corretti  =',esami_corretti,'\n')
        print('esami_sbagliati =',esami_sbagliati,'\n')
        print('esami_unknown   =',esami_unknown,'\n')
        
def MostraEsami(*o):
    MostraEsami_Corretti_Sbagliati_Unknown(*o)
    
#MostraEsami()
    
def TestaEsami(ris):
    for h in copy.deepcopy(ris):
        if type(ris[h][0]) == dict:
            print('Non ho informazioni su',h)
            del ris[h]
    l = 0
    for h in ris:
        x = ris[h]

        if len(x) > 1:
            d = len(x[0])
            for i in range(d):
                if len(x[0][i])>l:
                    l = len(x[0][i])
    l += 2
    for h in ris:
        x = ris[h]
        if len(x) > 1:
            if len(x) == 2:
                color.write('Esame: ',colori['Verde'])
                color.write(str(h)+'\n')
                a,b = x[0],elenca(x[1])
                for j in range(d):
                    color.write('X'+str(j+1),colori['Nero'])
                    color.write(' = '+str(a[j]),colori['Blu'])
                    color.write(' '*(l-len(str(a[j])))+'=> ')
                    color.write(b[j],colori['Blu'])
                    color.write(' '*(6-len(b[j]))+'(angolo -> ')
                    color.write(str(x[1][b[j]][0]),colori['Blu'])
                    color.write(' '*(4-len(str(x[1][b[j]][0])))+'cedimento -> ')
                    color.write(str(x[1][b[j]][1]),colori['Blu'])
                    color.write(')\n')
            elif len(x) == 3:
                color.write('Esame:',colori['Rosso'])
                color.write(' '+str(h)+'\n')
                for i in range(d):
                    if len(x[1][i])>l:
                        l = len(x[1][i])
                a,b,c = x[0],x[1],elenca(x[2])
                color.write('Risultato corretto:\n',colori['Viola'])            
                for j in range(d):
                    color.write('X'+str(j+1),colori['Nero'])
                    color.write(' = '+str(a[j]),colori['Blu'])
                    color.write(' '*(l-len(str(a[j])))+'=> ')
                    color.write(c[j],colori['Blu'])
                    color.write(' '*(6-len(c[j]))+'(angolo -> ')
                    color.write(str(x[2][c[j]][0]),colori['Blu'])
                    color.write(' '*(4-len(str(x[2][c[j]][0])))+'cedimento -> ')
                    color.write(str(x[2][c[j]][1]),colori['Blu'])
                    color.write(')\n')
                color.write('Risultato ottenuto:\n',colori['Viola'])
                for j in range(d):
                    color.write('X'+str(j+1),colori['Nero'])
                    color.write(' = '+str(b[j]),colori['Blu'])
                    color.write(' '*(l-len(str(b[j])))+'=> ')
                    color.write(c[j],colori['Blu'])
                    color.write(' '*(6-len(c[j]))+'(angolo -> ')
                    color.write(str(x[2][c[j]][0]),colori['Blu'])
                    color.write(' '*(4-len(str(x[2][c[j]][0])))+'cedimento -> ')
                    color.write(str(x[2][c[j]][1]),colori['Blu'])
                    color.write(')\n')
        else:
            print("Non ho informazioni circa l'esame:",h)

def Controllo_Input_TuttiDef_Testnet(o,name):
    if len(o) == 0:
        return esami
    else:
        o = o[0]
    if type(o) != int:
        print('Sono '+name+'(*o)')
        print('O non mi assegni un input o mi assegni un numero compreso fra 0 e 2.')
        print('Input == 0 -> Tutti gli esami')
        print('Input == 1 -> Testo solo gli esami corretti')
        print('Input == 2 -> Testo solo gli esami sbagliati')
        print('Input == 3 -> Testo solo gli esami sconosciuti')
        print('N.B.: Se len(input) == 0 => input = 1')
    else:
        return AggiornaEsami_Corretti_Sbagliati_Unknown()[o-1]
        
def TestaTuttiGliEsami(*o):
    Esami = Controllo_Input_TuttiDef_Testnet(o,'TestaTuttiGliEsami')
    ris = {}
    Stampa_InfoEsame = [False,True][0]
    for i in Esami:
        if Stampa_InfoEsame == True:
            InfoEsame(i)
        ris[i] = esame(i)
        if Stampa_InfoEsame == True:
            print('')
    color.write('\nSOLUZIONI ESAMI:\n',colori['Rosso'])
    TestaEsami(ris)
    
#TestaTuttiGliEsami()
    
def Testa(TF):
    ris = {}
    for i in esami:
        color.write(str(i)+' '*(10-len(str(i))))
        ris[i] = esame(i)

#vuole return DT
def TestaTuttiRilassamentiEsame(num):
    InfoEsame(num)
    o = esami[num]
    o[14] = 0
    ril = {}
    for i in range(len(o[15])):
        o[14] += 1
        ril[o[14]] = LineaTermoElastica(o)
    RN,RT,RM = {},{},{}
    n,t,m = {},{},{}
    cc = 0
    for i in ril:
        cc += 1
        NTM = ril[i]
        N,T,M = NTM[0],NTM[1],NTM[2]
        n[cc],t[cc],m[cc] = N,T,M
        if tuple(N) not in RN:
            RN[tuple(N)] = [cc]
        else:
            RN[tuple(N)].append(cc)
        if tuple(T) not in RT:
            RT[tuple(T)] = [cc]
        else:
            RT[tuple(T)].append(cc)
        if tuple(M) not in RM:
            RM[tuple(M)] = [cc]
        else:
            RM[tuple(M)].append(cc)
    TestaTuttiRilassamentiRIL([RM,RT,RM])
def TestaTuttiRilassamentiRIL(RNTM):
    RN,RT,RM = RNTM[0],RNTM[1],RNTM[2]
    if len(RN)+len(RT)+len(RM) != 3:
        color.write('NON COERENTE ',colori['Rosso'])
        print('Ecco le soluzioni errate per ognuno dei rilassamenti possibili:\n')
    else:
        color.write('COERENTE ',colori['Verde'])
        print('(con ognuno dei rilassamenti possibili)\n')
    if len(RN) > 1:
        for i in n:
            color.write('N'+str(i)+': ')
            print(n[i])
        print()
    if len(RT) > 1:
        for i in t:
            color.write('T'+str(i)+': ')
            print(t[i])
        print()
    if len(RM) > 1:
        for i in m:
            color.write('M'+str(i)+': ')
            print(m[i])
        
def TestaTuttiRilassamentiTuttiGliEsami(*o):
    Esami = Controllo_Input_TuttiDef_Testnet(o,'TestaTuttiRilassamentiEsame')
    for num in Esami:
        TestaTuttiRilassamentiEsame(num)

#Per le prossime due def, cambiare return di LineaTermoElastica(o) da DT a [SC,XS,DT]
def ValutaEsame(num):
    o = esami[num]
    t = o[14]
    o[14] = 0
    o.append(False)
    o.append(False)
    o.append('DF->XS')
    ril,ver = {},{}
    SC,AZC = [],[]
    for i in range(len(o[15])):
        o[14] += 1
        ril[o[14]] = LineaTermoElastica(o)
        SC.append(ril[o[14]][0])
        AZC.append(ril[o[14]][1])
        if o[14] == t:
            ver[num] = ril[o[14]][3]
        ril[o[14]] = ril[o[14]][2]
    RN,RT,RM = {},{},{}
    dn,dt,dm = {},{},{}
    cc = 0
    for i in ril:
        cc += 1
        NTM = ril[i]
        N,T,M = NTM[0],NTM[1],NTM[2]
        dn[cc],dt[cc],dm[cc] = N,T,M
    DN,DT,DM = {},{},{}
    DD = [DN,DT,DM]
    dd = [dn,dt,dm]
    for h in range(3):
        D = DD[h]
        d = dd[h]
        for i in d:
            if tuple(d[i]) not in D:
                D[tuple(d[i])] = [i]
            else:
                D[tuple(d[i])].append(i)
    InfoEsame(num)
    color.write('VALUTAZIONE:\n',colori['Rosso'])
    color.write('Correttezza: ',colori['Nero'])
    if num in ver:
        if len(ver[num]) == 2:
            color.write('✔\n',colori['Verde'])
        elif len(ver[num]) == 3:
            color.write('✘\n',colori['Rosso'])
    else:
        color.write('❓\n',colori['Viola'])
    color.write('Coerenza: ',colori['Nero'])
    cc = []
    for h in range(3):
        if len(DD[h]) != 1:
            cc.append(h)
    if len(cc) == 0:
        color.write('✔\n',colori['Verde'])
    else:
        color.write('✘\n',colori['Rosso'])
    color.write('VALORI:\n',colori['Rosso'])
    color.write('SC:  ',colori['Nero'])
    print(SC)
    color.write('AZC: ',colori['Nero'])#AZC -> 'sqrt(2)'
    print(AZC)
    Dntm = {0:'Normali:\n',1:'Tangenti:\n',2:'Momenti:\n'}
    if len(cc) != 0:
        color.write('INCOERENZE: \n',colori['Rosso'])
        for i in cc:
            color.write(Dntm[i],['Viola','Verde','RossoAcceso'][i])
            d = DD[i]
            for i in d:
                print(i,'->',d[i])

def ValutaTuttiGliEsami():
    for num in esami:
        ValutaEsame(num)
        print('\n')
        
#ValutaTuttiGliEsami()


#1) BILANCIO VINCOLI-FORZE ESTERNE (sia vincoli che forze)
##) Aggiungi un equazione a sistema dove fai il bilancio delle forze esterne, bilanciate dai vincoli interni.
##s) Ora hai meno incognite e il sistema è risolvibile sempre, nonostante i nodi
#considera i valori ottenuti come forze esterne

#2) BILANCIO INTERNO NODO PER NODO
#s) se il nodo è colpito, riflette la forza in verso opposto (az.-reaz.)
#s) nell cc rifletti l'inverso dell'inverso ai nodi adiacenti (attento alle direzioni)
#s) parti da un nodo esterno, calcole le forze, trasmettile agli adiacenti, trova l'adiacente risolvibile e itera
#s)    






























