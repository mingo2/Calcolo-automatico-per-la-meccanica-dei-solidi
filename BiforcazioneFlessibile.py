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
from mpmath import *
from sympy import solve
mpmath.mp.dps = 5; mpmath.mp.pretty = True
pi=sym.pi
import numpy
from sympy import sqrt
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
    d = ''
    for i in a:
        if i != "'":
            d += i
    color.write(d,colori[b])
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
b        =  sym.symbols('b',positive=True)
#costante elastica
k        =  sym.symbols('k',  positive=True)
Ke       =  sym.symbols('Ke', positive=True)
Ke1      =  sym.symbols('Ke1',positive=True)
Ke2      =  sym.symbols('Ke2',positive=True)
Ke3      =  sym.symbols('Ke3',positive=True)
Ke4      =  sym.symbols('Ke4',positive=True)
Kr       =  sym.symbols('Kr', positive=True)
Kr1      =  sym.symbols('Kr1',positive=True)
Kr2      =  sym.symbols('Kr2',positive=True)
Kr3      =  sym.symbols('Kr3',positive=True)
Kr4      =  sym.symbols('Kr4',positive=True)


#azioni distribuite:
p        =  sym.symbols('p',positive=True)
#azioni esterne:
F        =  sym.symbols('F',positive=True)
N        =  sym.symbols('N',positive=True)
T        =  sym.symbols('T',positive=True)
M        =  sym.symbols('M',positive=True)
#
P        =  sym.symbols('P',positive=True)
##############################################
'''Liste e Dizionari utili'''
numeri     = ['0','1','2','3','4','5','6','7','8','9']
lettere    = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

esponenti  = ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']#ⁿ ⁽ ⁾ ⁺ ⁻
pedici     = ['₀','₁','₂','₃','₄','₅','₆','₇','₈','₉','₁₀','₁₁','₁₂','₁₃','₁₄','₁₅','₁₆']
derivate   = ['','⁽¹⁾','⁽²⁾','⁽³⁾','⁽⁴⁾']
#cerchiati  = ['ⓝ','ⓣ','ⓐ','ⓔ','Ⓝ','Ⓣ','Ⓐ','Ⓔ']
#simboli    = [l,R,δ,delta,d,φ,csi,c,teta,θ,ξ]#...

Cm  = {'Ⓝ': 'ⓝ', 'Ⓣ': 'ⓣ', 'Ⓐ': 'ⓐ', 'Ⓔ': 'ⓔ', 'Ⓕ': 'ⓕ','㊈': 'ⓝ', '㊆': 'ⓣ', '㊅': 'ⓐ','ⓝ': 'ⓝ', 'ⓣ': 'ⓣ', 'ⓐ': 'ⓐ', 'ⓔ': 'ⓔ', 'ⓕ': 'ⓕ'}
cC  = {'ⓝ': 'Ⓝ', 'ⓣ': 'Ⓣ', 'ⓐ': 'Ⓐ', 'ⓔ': 'Ⓔ', 'ⓕ': 'Ⓕ'}#'ⓝ': '㊈', 'ⓣ': '㊆', 'ⓐ': '㊅'}
Cc  = {'Ⓝ': 'ⓝ', 'Ⓣ': 'ⓣ', 'Ⓐ': 'ⓐ', 'Ⓔ': 'ⓔ', 'Ⓕ': 'ⓕ'}
Cx  = ['ⓝ','ⓣ','ⓐ','ⓔ','ⓕ']
CX  = ['Ⓝ','Ⓣ','Ⓐ','Ⓔ','Ⓕ']
CI  = ['㊈','㊆','㊅']
CC  = ['Ⓝ','Ⓣ']

Ctra = ['ⓝ','ⓔ']
Cang = ['ⓐ','ⓕ']

#Ccc = {'Ⓝ': 'ⓝ', 'Ⓣ': 'ⓣ', 'Ⓐ': 'ⓐ', 'Ⓔ': 'ⓔ', 'ⓝ': 'ⓝ', 'ⓣ': 'ⓣ', 'ⓐ': 'ⓐ', 'ⓔ': 'ⓔ'}
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
    a = str(d)
    if len(a) > 4:
        if a[-5:] == '**1.0':
            a = a[:-5]
    if '.0*' in a:
        a = a.replace('.0*','*')
    if '1.4142135623731' in a:
        a = a.replace('1.4142135623731','2**(1/2)')
    a = sym.nsimplify(a)
    return a
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
            α = pi
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
            α = pi/2
        else:
            α = 3*pi/2
    else:
        if Δy/Δx > 0:
            if Δx > 0:
                α = sym.atan(Δy/Δx)
            else:
                α = pi + sym.atan(Δy/Δx)
        else:
            α = gradi(sym.atan(Δy/Δx))  
            if Δx > 0:
                α = 2*pi + sym.atan(Δy/Δx)
            else:
                α = pi + sym.atan(Δy/Δx)
    α = gradi(α)
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
    sv = []
    c  = 0
    for i in a:
        c+=1
        if i != 0:
            sv.append('('+str(i)+')e'+str(c))
    sta = ''
    c   = len(sv)-1
    for i in sv:
        if sv[c] == i:
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
            color.write(sta(i),colori['Blu'])
            color.write(')e'+str(c),colori['Viola'])
            if c == 1:
                if ss(a[1]) != '0' or ss(a[2]) != '0':
                    color.write(' + ',colori['Blu'])
            elif c == 2:
                if ss(a[2]) != '0':
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
'''VIN()'''
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

def unisci(*DL):
    if type(DL[0]) == dict:
        D = {}
        for i in DL:
            for j in i:
                D[j] = i[j]
        return D
    if type(DL[0]) == list:
        L = []
        for i in DL:
            for j in i:
               L.append(j)
        return L

##############################################
#FUNZIONI SYM INVERSE: Ritornato Liste (o Liste di liste) di stringhe, così che siano pronte per la stampa
#ELIMINATI TUTTI I PEZZI IN CUI VENGONO USATE (e sostituite con le funzioni sym apposite scoperte tardi)
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
'Funzioni di estetica sulla stampa valori sym'#⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ 
def sta(a):
    if type(a) not in [str,list,dict,tuple]:
        a = sym.nsimplify(a)#sym.sympify(a))
    '''
        if type(a) not in [int]:
            if 'sin' or 'cos' in str(a):
                a = a.evalf(4)
    '''
    a = str(a)
    '''
    if 'e-' in a:
        a = a.replace('e-','*0*')
        a = sym.nsimplify(a)
        a = str(a)
    '''
    if a[-3:] == '**2':
        a = a[:-3] + '²'
    if a[-3:] == '**3':
        a = a[:-3] + '³'
    if a[-3:] == '**3':
        a = a[:-3] + '⁴'
    a = a.replace('**2)','²)')
    a = a.replace('**2*','²∙')
    a = a.replace('**2/','²/')
    a = a.replace('**2 ','² ')
    a = a.replace('**3)','³)')
    a = a.replace('**3*','³∙')
    a = a.replace('**3/','³/')
    a = a.replace('**3 ',' ')
    a = a.replace('**4*','⁴∙')
    a = a.replace('**4/','⁴/')
    a = a.replace('**4 ',' ')
    a = a.replace('**','^')
    a = a.replace('*','∙')
    a = a.replace('sqrt','√')
    a = a.replace('.0∙','∙')
    a = a.replace('√(2)','√2')
    if a[-4:] == '∙l/2':
        a = a[:-4]+'/2'
    return a

def ss(a):
    '''
    if 'sin' or 'cos' in str(a):
        if type(a) not in [int]:
            a = a.evalf(4)
        if 'e-' in str(a):
            a = str(a).replace('e-','*0*')
            a = sym.sympify(a)
            if a == 0:
                return 0
    '''
    b = str(a)
    if 'e-' in b:
        if b.count(' ') == 0:
            return 0
    a = sta(a)
    if ' ' not in a:
        if '.' in a:
            while a[-1] == '0':
                a = a[:-1]
    if a[-1] == '.':
        a = a[:-1]
    '''
    b = copy.deepcopy(a)
    while b[-1] == '0':
        b = b[:-1]
        if b[:-1] == '.':
            b = b[:-1]
            return b
        if len(b) == 0:
            break
    '''
    return a
def ssqrt(a):
    s = str(a)
    while 'sqrt(' in s:
        cc = s.index('sqrt(')
        while s[cc] != ')':
            cc += 1
        s = s[:cc+1]+'**(0.5)'+s[cc+1:]
        s = s.replace('sqrt','',1)
    return s

def uturn(a):
    a = ssqrt(a)
    a = a.replace('∙','*')
    a = a.replace('√(5)','5**0.5')
    a = a.replace('²','**2')
    a = a.replace('³','**3')
    if ('sin' or 'cos') not in str(a):
        return a
    a = a.replace('sin','sym.ssin')
    a = a.replace('cos','sym.ccos')
    while 'sym.ssin(' in a:
        gg = a.index('sym.ssin(')
        a  = a.replace('sym.ssin(','sym.sin(',1)
        a  = a[:gg+8]+'sym.sympify('+a[gg+8:]
        while a[gg] != ')':
            gg += 1
        a = a[:gg]+').evalf(4)'+a[gg:]
    while 'sym.ccos(' in a:
        gg = a.index('sym.ccos(')
        a  = a.replace('sym.ccos(','sym.cos(',1)
        a  = a[:gg+8]+'sym.sympify('+a[gg+8:]
        while a[gg] != ')':
            gg += 1
        a = a[:gg]+').evalf(4)'+a[gg:]
    return a

def sin(a):
    if sym.sin(a).evalf(7) == 1/5**0.5:
        return 1/5**0.5
    a = sym.sin(a)
    return a
def cos(a):
    if sym.cos(a).evalf(7) == -2/5**0.5:
        return -2/5**0.5
    a = sym.cos(a)
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
        if i[-1] in lettere:
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
    '''
    #Controllo se vi siano pendoli legati a punti esterni ai corpi (di cui mi interessa conoscere la lunghezza)
    P = []
    for i in vin[1]:
        for j in i:
            P.append(j)
    E = []
    for i in P:
        if i not in PUNTI:
            E.append(i)
    if len(E) == 0:
        return V
    else:
        V1b = V[1]
        V1,V2  = [],[]
        for i in V1b:
            if len(i) == 2:
                V1.append(i)
    '''
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
    #nuovo
    print('Ci sono punti, non appartenenti ai corpi, di cui mi interessa conoscere la posizione?')
    m = si_o_no()
    if m == True:
        print('Digitali i punti in questione, senza spazi.')
        M = input().upper()
        for i in M:
            punti.append(i)
    else:
        M = []
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
    #nuovo, continuo parte sopra
    for i in M:
        for c in range(1,len(Pr)+1):
            D[i+str(c)] = D[i]
    return D

def chiedimi_i_collegamenti(Pr):
    punti = punti_(Pr)
    print('Per ognuno dei punti che ti indicherò, scrivimi con quali altri punti è collegato tramite travi (e non pendoli, presta attenzione a non confonderli) (senza spazi ne numeri).')
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
    ln = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    eln = elenca(ln)
    N,F = [],[]
    for i in DA:
        if i[-1] in ['Ⓝ','Ⓣ']:
            if i[:-1] not in N:
                N.append(i[:-1])
    if len(N) > 0:
        print('Ho considerato le cerniere interne come nodi, ovvero i seguenti vincoli:')
        for i in range(len(N)):
            print(eln[i]+')',N[i])
        print('Se effettivamente lo sono tutti, digita invio.')
        print('Alternativamente scrivi, senza spazi, le lettere relative le cerniera che non costituiscono un nodo.')
        m = input().lower()
        if len(m) > 0:
            et = {'Ⓝ':'ⓝ','Ⓣ':'ⓣ'}
            for i in m:
                F.append(N[ln[i]]+'Ⓝ')
                F.append(N[ln[i]]+'Ⓣ')
            DA2 = copy.deepcopy(DA)
            DA  = {}
            for i in DA2:
                if i in F:
                    DA[i[:-1]+et[i[-1]]] = DA2[i]
                else:
                    DA[i] = DA2[i]
    DC = {}
    for i in DA:
        DC[i] = 0
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
            print('Vi sono',n,"pendoli esterni:",epa+". Te li mostrerò uno alla volta; per ciascuno di questi:")
        print("digita invio se non vi sono azioni di natura termica su di esso, altrimenti rispondi con la lunghezza del pendolo.")
        for i in PenAss:
            lung = input('Lunghezza '+str(i)+': ')
            if len(lung) > 0:
                if lung == '1':
                    lung = sym.sympify(l)
                else:
                    lung = sym.sympify(lung)
                T2[i] = lung
                #NON messo il caso in cui un PENDOLO ABBIA DUE T DISTINTE. NON CONSIDERO QUESTA IPOTESI
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

def chiedimi_le_rigidezze(L):
    ACB = {}
    for i in L:
        ACB[i[1]+i[0]], ACB[i] = [0,0,B], [0,0,B]
    print("Mi serve conoscere le rigidezze a flessione (B), scorrimento angolare (C), allungamento (A).")
    print("In genere l'unico termine non trascurabile nell'ipotesi dei lavori virtuali è B.")
    print("Se in questo caso, come di solito avviente, ti interessa conoscere solo B (che è uniforme), digita invio; altrimenti digita qualsiasi altra cosa.")
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
    Pr = chiedimi_i_punti(n)
    print('    Pr  =',Pr,'\n')
    Di = chiedimi_le_coordinate(Pr)
    D = AggiornaDizionario(Di,Pr)
    print('    Pr  =',Pr)
    print('    D   =',D,'\n')
    Relazioni = chiedimi_i_collegamenti(Pr)
    Collegamenti = sistema_relazioni(Relazioni,Pr)
    Link = sistema_collegamenti(Collegamenti)
    L = Sistema_Link(Link,Pr)
    print('    Pr   =',Pr)
    print('    D    =',D)
    print('    Link =',Link)
    print('    L    =',L,'\n')
    vin = chiedimi_i_vincoli()#numero?
    vin = numeravincoli(vin,Pr)
    print('    Pr   =',Pr)
    print('    D    =',D)
    print('    Link =',Link)
    print('    L    =',L)
    print('    vin  =',vin)
    DAC = chiedimi_angoli_e_cedimenti(vin,Pr,D)
    DA,DC,Mol = DAC[0],DAC[1],DAC[2]
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



a = 0#...cosi funziona solo per travi 'unidirezionali', anche sotto...
def AdattaInput(Pr,L,DA,DC,Mol,D,a):
    T = elenca(L)#Pr
    V = elenca(DA)
    #'''
    #sistemo gli angoli delle cerniere
    W1,W2 = [],[]
    for i in V:
        if i[-1] in ['ⓝ','ⓣ']:
            if i[:-1] not in W2:
                W2.append(i[:-1])
            else:
                W1.append(i[:-1])
    if len(W1) > 0:
        DA2 = copy.deepcopy(DA)
        DA  = {}
        for i in DA2:
            if i[-1] in ['ⓝ','ⓣ']:
                if i[:-1] in W1:
                    if   i[-1] in ['ⓝ']:
                        k = a+90
                    elif i[-1] in ['ⓣ']:
                        k = a
                    DA[i] = k
                else:
                    DA[i] = DA2[i]
            else:
                DA[i] = DA2[i]
    #sistemo gli angoli degli incastri e le etichette (e i nodi):
    C = unisci(CC,CI)
    cc = 0
    for i in DA:
        if i[-1] in C:
            cc = 1
    if cc == 1:
        DA2,DC2 = copy.deepcopy(DA),copy.deepcopy(DC)
        DA,DC = {},{}
        for i in DA2:
            if i[-1] in C:
                j = i[:-1]+Cm[i[-1]]
                if   i[-1] in ['㊈','Ⓝ']:
                    k = a+90
                elif i[-1] in ['㊆','Ⓣ']:
                    k = a
                elif i[-1] in ['㊅']:
                    k = DA2[i]#cambiato da DA a DA2 NUOVO (4/11/20)
                DA[j],DC[j] = k,DC2[i]
            else:
                DA[i],DC[i] = DA2[i],DC2[i]
    #'''
    #Rendo Relativi i vincoli non 'estremi'
    #1r) Creo Dizionario: VR[p (relativo)] -> p+n1+p+n2
    Tn = punti_numerati(T)
    R1,R2 = [],[]
    for i in Tn:
        if i[0] not in R2:
            R2.append(i[0])
        else:
            R1.append(i[0])
    R = []
    for i in Tn:
        if i[0] in R1:
            R.append(i)
    R.sort()
    VR = {}
    for i in R1:
        VR[i] = ''
    for i in R:
        if i[0] in VR:
            VR[i[0]] += i
    #1a) Aggiungo a VR i vincoli assoluti
    for i in Tn:
        if i[0] not in VR:
            VR[i[0]] = i
    #2) DA,DC
    DA2,DC2 = copy.deepcopy(DA),copy.deepcopy(DC)
    DA,DC   = {},{}
    for i in DA2:
        v = VR[i[0]]+i[-1]
        DA[v],DC[v] = DA2[i],DC2[i]
    #3) Mol
    Mol2 = copy.deepcopy(Mol)
    Mol  = {}
    for i in Mol2:
        p = VR[i[0]]
        Mol[p] = Mol2[i]
    #4) D
    D2 = copy.deepcopy(D)
    D,D1  = {},{}
    for i in D2:
        if len(i) == 1:
            D1[i] = D2[i]
    D1 = AggiornaDizionario(D1,T)
    for i in D1:
        if i[-1] != '0':
            D[i] = D1[i]
    return [T,DA,DC,Mol,D]

def rank(A):
    return len(Matrix(A).rref()[1])

def TrovaRidondanze(Mc,Vc):
    L1 = []
    v = 8
    r = 6
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
   

'''
if 1 == 0:
    print('T   =',T)
    print('DA  =',DA)
    print('DC  =',DC)
    print('Mol =',Mol)
    print('D   =',D)

T   = ['HJ', 'JK']
DA  = {'H1ⓐ': 0, 'K2ⓝ': 90, 'K2ⓣ': 0, 'J1J2ⓔ': 90}
DC  = {'H1ⓐ': 0, 'K2ⓝ':  0, 'K2ⓣ': 0, 'J1J2ⓔ':  0}
Mol = {'J1J2': k}
D   = {'H': [0, 0, 0], 'J': [l, 0, 0], 'K': [2*l, 0, 0], 'H1': [0, 0, 0], 'J1': [l, 0, 0], 'J2': [l, 0, 0], 'K2': [2*l, 0, 0]}
a   = 0#anche sopra

ACB = {'HJ': [0, 0, B], 'JK': [0, 0, 2*B]}
'''


def LavoraDati(T,DA,DC,Mol,D,a):
    #Ddist[pn] = valore ascissa curvilinea
    TN = []
    for h in range(1,len(T)+1):
        tn = ''
        for i in T[h-1]:
            tn += i+str(h)
        TN.append(tn)
    Ddist = {}
    for i in TN:
        tr1,tr2 = i[:2],i[2:]
        Ddist[tr1] = 0
        Ddist[tr2] = distanza(D[tr2],D[tr1])
    #DA,DC
    A  = []
    b = a-90
    while b > -360:
        b -= 180
    A.append(b)
    while b < +360:
        b += 180
        A.append(b)
    TA = {}
    for i in DA:
        TA[i[:-1]] = []
    for i in DA:
        v = i[:-1]
        e = i[-1]
        d = DC[i]
        if   e in ['ⓐ']:
            TA[v].append(e)
            TA[v].append(d)
        elif e in ['ⓕ']:
            TA[v].append(e)
            d = Mol[v]
            TA[v].append(d)
        elif e in ['ⓔ']:
            d = Mol[v]
            TA[v].append(e)
            TA[v].append(d)
        elif e in ['ⓝ','ⓣ']:
            if DA[i] in A:
                TA[v].append('ⓝ')
                TA[v].append(d)
    #ipotizzando non ci siano due condizioni uguali...
    for i in TA:
        if len(TA[i]) == 2:
            e = TA[i][0]
            if e in Ctra:
                TA[i].append('Ⓐ')
                TA[i].append(0)
            if e in Cang:
                TA[i].append('Ⓣ')
                TA[i].append(0)
        elif len(TA[i]) == 0:
            TA[i].append('Ⓐ')
            TA[i].append(0)
            TA[i].append('Ⓣ')
            TA[i].append(0)
    #Nei punti di congiunzione devo assegnare l'assenza di vincoli come condizione comune
    #mentre eventuali vincoli li assegni alla trave 2 (poichè lì X = 0 e i conti sono più semplici)
    #lascio TA cosi com'è e ci penso poi
    #es: J1J2: ['ⓔ','Ⓐ'] => Ⓐ è comune, ⓔ appartiene solo a J2
    cc = 0
    for i in TA:
        if len(i) == 4:
            cc += 1
    if cc != len(TA)-1:
        #PUNTI COMUNI:
        P = []
        for i in PUNTI_(T):
            if len(i) == 2:
                if i[-1] != '0':
                    P.append(i)
        #segnalo eventuali errori
        if len(P)%2 != 0:
            color.write('TA sbagliata! Scriverla a mano',colori['Errore'])
            print('\n\n\n\n\n')
        #Li ordino, cosi a coppie saranno consecutivi
        P.sort()
        R = []
        for i in range(0,len(P),2):
            p1 = P[i]
            p2 = P[i+1]
            R.append(p1+p2)
        for i in R:
            if i not in TA:
                TA[i] = ['Ⓣ', 0, 'Ⓐ', 0]
    return [Ddist,TA]

def EquazioniGenerali(n):
    #CARICO: P
    P = sym.symbols('P')
#VELOCITA'
    Ve,Ve1,Ve2,Ve3 = [],[],[],[]
    Vetot = [Ve,Ve1,Ve2,Ve3]
    for k in range(1,n+1):
        i = pedici[k]
        for h in range(len(Vetot)):
            Vetot[h].append(sym.symbols('V'+str(i)+derivate[h]))
#Creo le incognite; per ogni corpo:
    #4 costanti (c.c.) 
    C = []
    for k in range(1,4*n+1):
        i = pedici[k]
        C.append(sym.symbols('C'+str(i)))
    #2 termini argomenti sin,cos:
    A = []
    for k in range(1,n+1):
        i = pedici[k]
        A.append(sym.symbols('α'+str(i)))
    B = []
    for k in range(1,n+1):
        i = pedici[k]
        B.append(sym.symbols('B'+str(i)))
    #αi = (Pi/Bi)^0.5
    Alfa = []
    for i in range(n):
        Alfa.append((P/B[i])**0.5)
    #2 termini argomenti sin,cos:
    X = []
    for k in range(1,n+1):
        i = pedici[k]
        X.append(sym.symbols('X'+str(i)))
#Riempio S delle eq. velocità:
    S = []
    cc = 0
    for i in range(n):
        S.append(C[4*cc]*cos(A[cc]*X[cc])+C[4*cc+1]*sin(A[cc]*X[cc])+C[4*cc+2]*X[cc]+C[4*cc+3])
        cc += 1
#TRASVERSALE (non elastico)
    TX = []
    for i in range(n):
        TX.append(B[i]*Ve3[i]+P*Ve1[i])
#MOMENTO (non elastico)
    MX = []
    for i in range(n):
        MX.append(B[i]*Ve2[i])
#Ke
    Ke = []
    for k in range(1,n+1):
        i = pedici[k]
        Ke.append(sym.symbols('Ke'+str(i)))
#Kr
    Kr = []
    for k in range(1,n+1):
        i = pedici[k]
        Kr.append(sym.symbols('Kr'+str(i)))
#C1234:
    Ctot = []
    for i in range(n):
        Ctot.append([])
        for h in range(4):
            Ctot[-1].append(C[4*i+h])
#DIZIONARIZZAZIONE: D[numero] = equazione e Dizionari di liste di simboli
#Velocità e Derivate in una lista di dizionari:
    V,V1,V2,V3 = {},{},{},{}
    LV = [V,V1,V2,V3]
    for i in range(n):
        V[i+1],a = S[i],S[i]
        for j in range(1,4):
            a = sym.diff(a,X[i])
            LV[j][i+1] = a
#Tangenti:
    DT = {}
    for i in range(n):
        DT[i+1] = TX[i]
#Momenti:
    DM = {}
    for i in range(n):
        DM[i+1] = MX[i]
#ALFA:
    Dα = {}
    for i in range(n):
        Dα[i+1] = Alfa[i]
#Vtot:
    Vtot = []
    for i in range(n):
        Vtot.append([])
        for j in Vetot:
            Vtot[-1].append(j[i])
#return
    DG = [V,V1,V2,V3,DT,DM,Dα]
    LS = [Vtot,Ctot,A,B,X,Ke,Kr]
    return [DG,LS]


def CreaMatrice(T,DD,TA,EG):
    DG,LS = EG[0],EG[1]
    V,V1,V2,V3,DT,DM,Da   = DG[0],DG[1],DG[2],DG[3],DG[4],DG[5],DG[6]
    Vtot,Ctot,A,B,X,Ke,Kr = LS[0],LS[1],LS[2],LS[3],LS[4],LS[5],LS[6]
    #input(V)
    #'''
    ##########################################
    color.write('Tratti di trave\n')
    color.write('T:\n',colori['Rosso'])
    print(T,'\n')
    color.write('DD:\n',colori['Rosso'])
    color.write('Estremi tratti:\n')
    for i in DD:
        print(i+':',DD[i])
    color.write('\nTA:\n',colori['Rosso'])
    color.write('Vincoli associati ai punti:\n')
    for i in TA:
        print(i,' '*(5-len(i)),'-> ',TA[i])
    color.write('\nDG:\n',colori['Rosso'])
    '''
    color.write('Equazioni:\n')
    for i in DG:
        for j in i:
            print(i[j])
        print()
    color.write('Simboli\n')
    color.write('LS:\n',colori['Rosso'])
    for i in LS:
        print(i)
    '''
    #DIZIONARI:
    #V[n] = V n-esimo tratto
    #VN[n] = come sopra con derivata N-esima, N = 1,2,3
    #DT[n] = Relazione Meccanica n-esimo tratto TAGLIO
    #DM[n] = Relazione Meccanica n-esimo tratto MOMENTO
    #Da[n] = Argomento trigonometrico n-esimo tratto

    #LISTE DI LISTE:
    #Vtot[n] = simboli velocità e derivate n+esima lista
    #Ctto[n] = idem con costanti
        
    #LISTE:
    #A  = [α₁, α₂]
    #B  = [B₁, B₂]
    #X  = [X₁, X₂]
    #Ke = [Ke₁, Ke₂]
    #Kr = [Kr₁, Kr₂]
    ##########################################
    #print('\n\n\n')
    #'''
    print()
    #INIZIO REALE:
    color.write('Determino, attraverso il metodo energetico, il valore del moltiplicatore critico per il carico P:\n')
    print('Consideriamo le velocità di ogni tratto di trave:')
    cc = 0
    for i in V:
        color.write(str(Vtot[cc][0])+'('+str(X[cc])+')')
        print(' = '+str(V[i]))
        cc += 1
    ####################
    print()
    print('E le loro derivate:')
    cc = 0
    for i in V1:
        color.write(str(Vtot[cc][1])+'('+str(X[cc])+')')
        print(' = '+str(V1[i]))
        cc += 1
    print()
    cc = 0
    for i in V2:
        color.write(str(Vtot[cc][2])+'('+str(X[cc])+')')
        print(' = '+str(V2[i]))
        cc += 1
    print()
    cc = 0
    for i in V3:
        color.write(str(Vtot[cc][3])+'('+str(X[cc])+')')
        print(' = '+str(V3[i]))
        cc += 1
    print()
    print('Ove:')
    for i in Da:
        color.write(str(A[i-1]))
        print(' = '+str(Da[i]))
    print()
    ####################
    L = []
    C = []
    cc = 0
    print("Per la determinazione delle costanti 'Ci' considero le condizioni al contorno, ovvero le seguenti equazioni determinate dalla presenza o assenza di gradi di vincolo sulle componenti trasversali e rotazionali dei punti estremanti di ogni tratto di ascissa curvilinea:")
    for k in TA:
        #print()
        v1,v2,c1,c2 = TA[k][0],TA[k][2],TA[k][1],TA[k][3]
        Vi,Ci = [v1,v2],[c1,c2]
        if len(k) == 2:
            n = int(k[-1])-1
            color.write('In '+str(X[n])+' = '+str(DD[k])+':\n',colori['Rosso'])
            for i in range(2):
                cc += 1
                if   Vi[i] in ['ⓝ','ⓣ','ⓔ']:#t?
                    color.write(str(cc)+') Componente trasversale di spostamento:\n')
                    if   Vi[i] in ['ⓝ','ⓣ']:#t
                        print(str(Vtot[n][0])+'('+str(X[n])+' = '+str(DD[k])+')'+' = '+str(Ci[i]))
                        L.append(V[n+1].subs(X[n],DD[k]))
                        C.append(Ci[i])
                        print(L[-1],'=',C[-1])
                        ###################################################################
                            
                    elif Vi[i] in ['ⓔ']:#MOLLA FORZA
                        if DD[k] == 0:
                            color.write(str(DT[n+1])[:8],colori['Blu'])
                            color.write('('+str(X[n])+' = '+str(DD[k])+')',colori['Blu'])
                        
                            color.write(str(DT[n+1])[8:],colori['Blu'])
                            color.write('('+str(X[n])+' = '+str(DD[k])+') + ',colori['Blu'])

                            color.write(str(Ci[i])+'*',colori['Blu'])
                            color.write(str(Vtot[n][0])+'('+str(X[n])+' = '+str(DD[k])+')',colori['Blu'])
                            
                            print(' = 0')
                            
                            L.append(B[n]*V3[n+1].subs(X[n],DD[k])+P*V1[n+1].subs(X[n],DD[k])+ Ci[i]*V[n+1].subs(X[n],DD[k]))
                            C.append(0)
                            print(L[-1],'=',C[-1])
                        else:
                            color.write('-['+str(DT[n+1])[:8],colori['Blu'])
                            color.write('('+str(X[n])+' = '+str(DD[k])+')',colori['Blu'])
                        
                            color.write(str(DT[n+1])[8:],colori['Blu'])
                            color.write('('+str(X[n])+' = '+str(DD[k])+')] + ',colori['Blu'])

                            color.write(str(Ci[i])+'*',colori['Blu'])
                            color.write(str(Vtot[n][0])+'('+str(X[n])+' = '+str(DD[k])+')',colori['Blu'])

                            L.append(-B[n]*V3[n+1].subs(X[n],DD[k])-P*V1[n+1].subs(X[n],DD[k])+ Ci[i]*V[n+1].subs(X[n],DD[k]))
                            C.append(0)
                            
                            print(' = 0')
                            
                            L.append(-B[n]*V3[n+1].subs(X[n],DD[k])-P*V1[n+1].subs(X[n],DD[k])+ Ci[i]*V[n+1].subs(X[n],DD[k]))
                            C.append(0)
                            print(L[-1],'=',C[-1])
                        ####################################################################
                elif Vi[i] in ['ⓐ','ⓕ']:
                    color.write(str(cc)+') Componente rotazionale di spostamento:\n')
                    if   Vi[i] in ['ⓐ']:
                        print(str(Vtot[n][1])+'('+str(X[n])+' = '+str(DD[k])+')'+' = '+str(Ci[i]))
                        L.append(V1[n+1].subs(X[n],DD[k]))
                        C.append(Ci[i])
                        print(L[-1],'=',C[-1])
                    elif Vi[i] in ['ⓕ']:
                        if DD[k] == 0:
                            color.write('-'+str(DM[n+1])+'('+str(X[n])+' = '+str(DD[k])+') + ',colori['Blu'])
                            color.write(str(Ci[i])+'*',colori['Blu'])
                            color.write(str(Vtot[n][1])+'('+str(X[n])+' = '+str(DD[k])+')',colori['Blu'])
                            print(' = 0')
                            L.append(-B[n]*V2[n+1].subs(X[n],DD[k])+Ci[i]*V1[n+1].subs(X[n],DD[k]))
                            C.append(0)
                            print(L[-1],'=',C[-1])
                        else:
                            color.write(str(DM[n+1])+'('+str(X[n])+' = '+str(DD[k])+') + ',colori['Blu'])
                            color.write(str(Ci[i])+'*',colori['Blu'])
                            color.write(str(Vtot[n][1])+'('+str(X[n])+' = '+str(DD[k])+')',colori['Blu'])
                            print(' = 0')
                            L.append(B[n]*V2[n+1].subs(X[n],DD[k])+Ci[i]*V1[n+1].subs(X[n],DD[k]))
                            C.append(0)
                            print(L[-1],'=',C[-1])
                            
                elif Vi[i] in ['Ⓣ']:
                    color.write(str(cc)+') Assenza della componente trasversale di spostamento:\n')
                    
                    color.write(str(DT[n+1])[:8],colori['Blu'])
                    color.write('('+str(X[n])+' = '+str(DD[k])+')',colori['Blu'])
                    
                    color.write(str(DT[n+1])[8:],colori['Blu'])
                    color.write('('+str(X[n])+' = '+str(DD[k])+')',colori['Blu'])
                            
                    print(' = 0')#+str(Ci[i]))
                    L.append(B[n]*V3[n+1].subs(X[n],DD[k])+P*V1[n+1].subs(X[n],DD[k]))
                    C.append(0)
                    print(L[-1],'=',C[-1])
                    
                elif Vi[i] in ['Ⓐ']:
                    color.write(str(cc)+') Assenza della componente rotazionale di spostamento:\n')
                    print(str(DM[n+1])+'('+str(X[n])+' = '+str(DD[k])+')'+' = 0')#+str(Ci[i]))

                    L.append(B[n]*V2[n+1].subs(X[n],DD[k]))
                    C.append(0)
                    print(L[-1],'=',C[-1])
                    
        elif len(k) == 4:
            n1 = int(k[+1])-1
            n2 = int(k[-1])-1
            #PRESENZA DI VINCOLI -> Lo si assegna al corpo 2 (per semplicità di conti: lì infatti X2 = 0):
            #aggiorna cc += 1 solo se verificato!

            #CONTROLLARE SE CI SONO VINCOLI E IN CASO SCRIVERE: In X2 = 0:
            u = 0
            for y in TA[k]:
                if y in ['ⓝ','ⓣ','ⓔ','ⓐ','ⓕ']:
                    u = 1
            if u == 1:
                color.write('In '+str(X[n2])+' = '+str(DD[k[2:]])+':\n',colori['Rosso'])
            for i in range(2):
                if Vi[i] in ['ⓝ','ⓣ','ⓔ']:
                    cc += 1
                    color.write(str(cc)+') Componente trasversale di spostamento:\n')
                    if   Vi[i] in ['ⓝ','ⓣ']:
                        print(str(Vtot[n2][0])+'('+str(X[n2])+' = '+str(DD[k[2:]])+')'+' = '+str(Ci[i]))
                    elif Vi[i] in ['ⓔ']:#MOLLA (FORZA)
                        ####################################################################
                        #COME COND.MECCANICA TAGLIO MA CON IL TERMINE ELASTICO IN PIU:
                        color.write(str(DT[n2+1])[:8],colori['Blu'])
                        color.write('('+str(X[n2])+' = '+str(DD[k[2:]])+')',colori['Blu'])
                    
                        color.write(str(DT[n2+1])[8:],colori['Blu'])
                        color.write('('+str(X[n2])+' = '+str(DD[k[2:]])+') + ',colori['Blu'])

                        color.write(str(Ci[i])+'*',colori['Blu'])
                        color.write(str(Vtot[n2][0])+'('+str(X[n2])+' = '+str(DD[k[2:]])+')',colori['Blu'])
                        
                        print(' = 0')

                        L.append(B[n2]*V3[n2+1].subs(X[n2],DD[k[2:]])+P*V1[n2+1].subs(X[n2],DD[k[2:]])+ Ci[i]*V[n2+1].subs(X[n2],DD[k[2:]]))
                        C.append(0)
                        print(L[-1],'=',C[-1])
                        ####################################################################

                        
                elif Vi[i] in ['ⓐ','ⓕ']:
                    cc += 1
                    color.write(str(cc)+') Componente rotazionale di spostamento:\n')
                    if   Vi[i] in ['ⓐ']:
                        print(str(Vtot[n2][1])+'('+str(X[n2])+' = '+str(DD[k[2:]])+')'+' = '+str(Ci[i]))

                        L.append(V1[n2+1].subs(X[n2],DD[2:]))
                        C.append(Ci[i])
                                 
                        print(L[-1],'=',C[-1])
                        
                    elif Vi[i] in ['ⓕ']:#MOLLA (COPPIA)
                        color.write('-'+str(DM[n2+1])+'('+str(X[n2])+' = '+str(DD[k[2:]])+') + ',colori['Blu'])
                        color.write(str(Ci[i])+'*',colori['Blu'])
                        color.write(str(Vtot[n2][1])+'('+str(X[n2])+' = '+str(DD[k[2:]])+')',colori['Blu'])
                        print(' = 0')

                        L.append(-B[n2]*V2[n2+1].subs(X[n2],DD[k[2:]])+Ci[i]*V1[n2+1].subs(X[n2],DD[k[2:]]))
                        C.append(0)
                        print(L[-1],'=',C[-1])
                    
                
            #ASSENZA DI VINCOLI:
            #Ⓣ,Ⓐ

            u = 0
            for y in TA[k]:
                if y in ['Ⓣ','Ⓐ']:
                    u = 1
            if u == 1:
                color.write('In '+str(X[n1])+' = '+str(DD[k[:2]])+' ≡ '+str(X[n2])+' = '+str(DD[k[2:]])+':\n',colori['Rosso'])
            for i in range(2):
                if   Vi[i] in ['Ⓣ']:
                    cc += 1
                    color.write(str(cc)+') Assenza della componente trasversale di spostamento:\n')
                    
                    color.write('['+str(DT[n1+1])[:8],colori['Blu'])
                    color.write('('+str(X[n1])+' = '+str(DD[k[:2]])+')',colori['Blu'])
                        
                    color.write(str(DT[n1+1])[8:],colori['Blu'])
                    color.write('('+str(X[n1])+' = '+str(DD[k[:2]])+')]',colori['Blu'])

                    color.write(' - ')

                    color.write('['+str(DT[n2+1])[:8],colori['Blu'])
                    color.write('('+str(X[n2])+' = '+str(DD[k[2:]])+')',colori['Blu'])
                        
                    color.write(str(DT[n2+1])[8:],colori['Blu'])
                    color.write('('+str(X[n2])+' = '+str(DD[k[2:]])+')]',colori['Blu'])

                    print(' = 0')
                    
                    L.append(B[n1]*V3[n1+1].subs(X[n1],DD[k[:2]])+P*V1[n1+1].subs(X[n1],DD[k[:2]]) - B[n2]*V3[n2+1].subs(X[n2],DD[k[2:]])-P*V1[n2+1].subs(X[n2],DD[k[2:]]))
                    C.append(0)
                    print(L[-1],'=',C[-1])
            
                elif Vi[i] in ['Ⓐ']:
                    cc += 1
                    color.write(str(cc)+') Assenza della componente rotazionale di spostamento:\n')
                    print(str(DM[n1+1])+'('+str(X[n1])+' = '+str(DD[k[:2]])+') - '+str(DM[n2+1])+'('+str(X[n2])+' = '+str(DD[k[2:]])+')'+' = 0')#+str(Ci[i]))
                    L.append(B[n1]*V2[n1+1].subs(X[n1],DD[k[:2]]) - B[n2]*V2[n2+1].subs(X[n2],DD[k[2:]]))
                    C.append(0)
                    print(L[-1],'=',C[-1])
            #COMPATIBILITA' CINEMATICA:
            #V (X1 = l) - V (X2 = 0) = 0
            #V'(X1 = l) - V'(X2 = 0) = 0
            cc += 1
            color.write(str(cc)+') Compatibilità cinematica (trasversale):\n')
            print(str(Vtot[n1][0])+'('+str(X[n1])+' = '+str(DD[k[:2]])+') - '+str(Vtot[n2][0])+'('+str(X[n2])+' = '+str(DD[k[2:]])+')'+' = '+str(Ci[i]))
            L.append(V[n1+1].subs(X[n1],DD[k[:2]])-V[n2+1].subs(X[n2],DD[k[2:]]))
            C.append(Ci[i])
            print(L[-1],'=',C[-1])
            
            cc += 1
            color.write(str(cc)+') Compatibilità cinematica (rotazionale):\n')
            print(str(Vtot[n1][1])+'('+str(X[n1])+' = '+str(DD[k[:2]])+') - '+str(Vtot[n2][1])+'('+str(X[n2])+' = '+str(DD[k[2:]])+')'+' = '+str(Ci[i]))
            L.append(V1[n1+1].subs(X[n1],DD[k[:2]])-V1[n2+1].subs(X[n2],DD[k[2:]]))
            C.append(Ci[i])
            print(L[-1],'=',C[-1])
    Cfin = []
    for i in Ctot:
        for j in i:
            Cfin.append(j)    
    a = sym.linear_eq_to_matrix(L,Cfin)
    Mc = a[0]
    Vc = Matrix(Cfin)
    print()
    for i in a:
        print(i)
    print()
    DET = a[0].det()
    print('DET(A) =',DET,'\n=\n',sym.simplify(DET))
    for i in range(len(A)):
        DET = DET.subs(A[i],(B[i]*P)**0.5)
    DET = sym.simplify(DET)
    print('=')
    print(DET)
    print('=')

    
    ##########################################################################################
    DET = DET.subs(B[0],b)#####F sarebbe la B specifica che però ho gia usato per la lista
    DET = DET.subs(B[1],b)#####
    ##########################################################################################


    DET = sym.simplify(DET)
    print(DET)
    
    #A  = [α₁, α₂]
    #B  = [B₁, B₂]
    #SOLVE = sym.solve(DET,P)
    print()
    color.write('Pcr = P| det(A) = 0 \n',colori['Blu'])
    #SOLVE = sym.solve(DET,P)
    #print(SOLVE)
    #
    #'''
    # A = Matrice dei coefficienti
    print()
    print("Per determinare le costanti spaziali occorre mettere a sistema le condizioni al contorno (cinematiche, meccaniche e di compatibilità).")
    print('Si crea  così un sistema di N equazioni in N incognite:')
    print('A_ij C_i = ced')
    print('Il sistema ammette sempre la soluzione banale nulla C_i = 0, che è di poco interesse.')
    print('Nuovi percorsi elastici nascono invece quando il rango della matrice A non è massimo.')
    print("Pertanto esisteranno particolari valori dell'incremento di carico P per i quali si annullerà il determinante della matrice A e si definisce moltiplicatore di carico critico il più piccolo valore positivo di questi:")
    print('P_critico = P | det(A(P)) = 0')
    #'''
    return [L,C]

def Bif(Pr,L,DA,DC,Mol,D):
    a = 0
    I = AdattaInput(Pr,L,DA,DC,Mol,D,a)
    T,DA,DC,Mol,D = I[0],I[1],I[2],I[3],I[4]
    LD = LavoraDati(T,DA,DC,Mol,D,a)
    DD,TA = LD[0],LD[1]
    EG = EquazioniGenerali(len(T))
    VC = CreaMatrice(T,DD,TA,EG)
    V,C = VC[0],VC[1]
    if 1 == 1:
        print()
        print('ricapitolando')
        for i in V:
            print(i)


###Testo esami: #'㊈','㊆','㊅'
def esami(n):
    n = esame[n]
    Pr,L,DA,DC,Mol,D,a = n[0],n[1],n[2],n[3],n[4],n[5],n[6]
    Bif(Pr,L,DA,DC,Mol,D)
    

esame = {}
#19/06/13-1 (p.126)FUNZIONANTE -> Dopo lo rifà in maniera diversa!! (diversi anche i risultati rispetto quanto viene sotto)
Pr  = ['HJK']
vin = [[], [], ['H'], ['K'], [], [], ['J']]
DA  = {'H1ⓐ': 0, 'K1ⓝ': 135, 'K1ⓣ': 225, 'J1ⓔ': 90}
DC  = {'H1ⓐ': 0, 'K1ⓝ':   0, 'K1ⓣ':   0, 'J1ⓔ':  0}
L   = [{'HJ': [], 'JK': ['HJ']}]
AC  = [{'H': p}, {}, {}]
AD  = {}
ADP = {}
Mol = {'J1': Ke}
CT  = {}
CT2 = {}
Sub = {k: B/(4*l**3)}
#ACB = {'JH': [0, 0, B], 'HJ': [0, 0, B], 'KJ': [0, 0, B], 'JK': [0, 0, B]}
ACB = {'HJ': [0, 0, B],'JK': [0, 0, 2*B]}
D   = {'H': [0, 0, 0], 'J': [l, 0, 0], 'K': [2*l, 0, 0], 'H1': [0, 0, 0], 'J1': [l, 0, 0], 'K1': [2*l, 0, 0], 'H0': [0, 0, 0], 'J0': [l, 0, 0], 'K0': [2*l, 0, 0]}
#SC  = -1
#AZC = '?'
E = [Pr,L,DA,DC,Mol,D,a]
esame[1906131] = E
#esami(1906131)
#28/10/11-4 FUNZIONANTE
Pr  = ['ORS']
vin = [['S1'], [], [], [], [], ['O'], []]
DA  = {'S1ⓝ': 90, 'O㊈': 90, 'O㊆': 0, 'O㊅': 0}
DC  = {'S1ⓝ':  0, 'O㊈':  0, 'O㊆': 0, 'O㊅': 0}
#DA  = {'S1ⓝ': 90, 'Oⓝ': 90, 'Oⓣ': 0, 'Oⓐ': 0}
#DC  = {'S1ⓝ':  0, 'Oⓝ':  0, 'Oⓣ': 0, 'Oⓐ': 0}
L   = [{'OR': [], 'RS': ['OR']}]
AC  = [{'S': -p}, {}, {}]
AD  = {}
ADP = {}
Mol = {}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'RO': [0, 0, 2*B], 'OR': [0, 0, 2*B], 'SR': [0, 0, B], 'RS': [0, 0, B]}
D   = {'O': [0, 0, 0], 'R': [l, 0, 0], 'S': [2*l, 0, 0], 'O1': [0, 0, 0], 'R1': [l, 0, 0], 'S1': [2*l, 0, 0], 'O0': [0, 0, 0], 'R0': [l, 0, 0], 'S0': [2*l, 0, 0]}
#SC  = -1
#AZC = '?'
E = [Pr,L,DA,DC,Mol,D,a]
esame[2810114] = E
#esami(2810114)
#14/02/12-4 (p 139 2a) FUNZIONANTE
Pr   = ['QRK']
D    = {'Q': [0, 0, 0], 'R': [l, 0, 0], 'K': [2*l, 0, 0], 'Q1': [0, 0, 0], 'R1': [l, 0, 0], 'K1': [2*l, 0, 0], 'Q0': [0, 0, 0], 'R0': [l, 0, 0], 'K0': [2*l, 0, 0]}
Link = {'QR': [], 'RK': ['QR']}
L    = [{'QR': [], 'RK': ['QR']}]
vin  = [['R1'], [], ['K1'], [], ['Q1'], [], ['Q1']]
DA   = {'R1ⓝ': 90, 'K1ⓐ': 0, 'Q1ⓐ': 0, 'Q1ⓝ': 0, 'Q1ⓔ': 90}
DC   = {'R1ⓝ': -d, 'K1ⓐ': 0, 'Q1ⓐ': 0, 'Q1ⓝ': 0, 'Q1ⓔ': 0}
Mol  = {'Q1': Ke}
CT   = {}
CT2  = {}
AC   = [{'K': -p}, {}, {}]
AD   = {}
ADP  = {}
ACB  = {'RQ': [0, 0, B], 'QR': [0, 0, B], 'KR': [0, 0, B], 'RK': [0, 0, B]}
E = [Pr,L,DA,DC,Mol,D,a]
esame[1402124] = E

#9/11/12-3 (p.95) RIDONTANTE!!

#22/03/17-4 (p.103 2a)
Pr  = ['QRK']
vin = [[], [], [], [], ['Q1'], [], ['R1', 'K1']]
DA  = {'Q1ⓐ': 0, 'Q1ⓝ': 0, 'R1ⓔ': 90, 'K1ⓔ': 90}
DC  = {'Q1ⓐ': 0, 'Q1ⓝ': 0, 'R1ⓔ': 0, 'K1ⓔ': 0}
L   = [{'QR': [], 'RK': ['QR']}]
AC  = [{'K': -p}, {}, {}]
AD  = {}
ADP = {}
Mol = {'R1': Ke, 'K1': 2*Ke}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'RQ': [0, 0, B], 'QR': [0, 0, B], 'KR': [0, 0, B], 'RK': [0, 0, B]}
D   = {'Q': [0, 0, 0], 'R': [l, 0, 0], 'K': [2*l, 0, 0], 'Q1': [0, 0, 0], 'R1': [l, 0, 0], 'K1': [2*l, 0, 0], 'Q0': [0, 0, 0], 'R0': [l, 0, 0], 'K0': [2*l, 0, 0]}
E = [Pr,L,DA,DC,Mol,D,a]
esame[2203174] = E
#esami(2203174)


#26/06/17-2 (p.107 2a)FUNZIONANTE# Devi mettere ⓕ a mano
Pr  = ['QR']
vin = [[], ['Q1'], [], [], [], [], ['Q1', 'R1']]
DA  = {'Q1ⓝ': 180, 'Q1ⓕ': 0, 'R1ⓔ': csi}
DC  = {'Q1ⓝ':   0, 'Q1ⓕ': 0, 'R1ⓔ':  0}
L   = [{'QR': []}]
AC  = [{'R': -p}, {}, {}]
AD  = {}
ADP = {}
Mol = {'Q1': Kr, 'R1': Ke}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'RQ': [0, 0, B], 'QR': [0, 0, B]}
D   = {'Q': [0, 0, 0], 'R': [l, 0, 0], 'Q1': [0, 0, 0], 'R1': [l, 0, 0], 'Q0': [0, 0, 0], 'R0': [l, 0, 0]}
E = [Pr,L,DA,DC,Mol,D,a]
esame[2606172] = E
#esami(2606172)

Pr  = ['QPR']
vin = [[], [], [], ['P1P2'], ['Q1'], [], ['Q1', 'R1']]
DA  = {'P1P2Ⓝ': 90, 'P1P2Ⓣ': 0, 'Q1ⓐ': 0, 'Q1ⓝ': 0, 'Q1ⓔ': 90, 'R1ⓔ': 90}
DC  = {'P1P2Ⓝ': 0, 'P1P2Ⓣ': 0, 'Q1ⓐ': 0, 'Q1ⓝ': 0, 'Q1ⓔ': 0, 'R1ⓔ': 0}
L   = [{'QP': [], 'PR': ['QP']}]
AC  = [{'P': -P}, {}, {}]
AD  = {}
ADP = {}
Mol = {'Q1': Ke, 'R1': 2*Ke}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'PQ': [0, 0, B], 'QP': [0, 0, B], 'RP': [0, 0, B], 'PR': [0, 0, B]}
D   = {'Q': [0, 0, 0], 'P': [l, 0, 0], 'R': [3*l, 0, 0], 'Q1': [0, 0, 0], 'P1': [l, 0, 0], 'R1': [3*l, 0, 0], 'Q0': [0, 0, 0], 'P0': [l, 0, 0], 'R0': [3*l, 0, 0]}
SC  = -1
AZC = '?'
E = [Pr,L,DA,DC,Mol,D,a]
esame[911203] = E
#esami(911203)


''' SBAGLIATO (Parametrico. Fallo con la Lagrangiana!!)
#24/06/20
Pr  = ['QSU']
vin = [[], [], [], ['Q1'], [], [], ['S1', 'S1S2']]
DA  = {'Q1ⓝ': 90, 'Q1ⓣ': 0, 'S1ⓔ': csi, 'S1S2ⓕ': 0}
DC  = {'Q1ⓝ':  0, 'Q1ⓣ': 0, 'S1ⓔ':   0, 'S1S2ⓕ': 0}
L   = [{'QS': [], 'SU': ['QS']}]
AC  = [{'U': -p}, {}, {}]
AD  = {}
ADP = {}
Mol = {'S1': Ke, 'S1S2': Kr}
CT  = {}
CT2 = {}
Sub = {}
ACB = {'SQ': [0, 0, B], 'QS': [0, 0, B], 'US': [0, 0, B], 'SU': [0, 0, B]}
D   = {'Q': [0, 0, 0], 'S': [l, 0, 0], 'U': [3*l, 0, 0], 'Q1': [0, 0, 0], 'S1': [l, 0, 0], 'U1': [3*l, 0, 0], 'Q0': [0, 0, 0], 'S0': [l, 0, 0], 'U0': [3*l, 0, 0]}
E = [Pr,L,DA,DC,Mol,D,a]
esame[240620] = E
esami(240620)
'''


'''
for i in esame:
    print(i)
    esami(i)
    break
'''

'''
#DV = SmaltisciVincoli(DA,L,D)
def EquazioniCinematiche(Pr,DV,S):
    #2 termini argomenti sin,cos:
    X = []
    for i in range(1,2*n+1):
        X.append(sym.symbols('X'+str(i)))
    EC = []
#VC = lista di liste (tante quante le travi) contenente i vincoli che la riguardano
    VC = []
    for i in range(len(Pr)):
        VC.append([])
    for i in DV:
        c = int(i[1])-1
        VC[c].append(i)
#DEC = dizionario equazioni cinematiche (solo V e non le derivate)
    DEC = {}
    for i in range(len(VC)):
        for j in VC[i]:
            DEC[j] = S[i].subs(X[i],DV[j])
    return DEC
'''

'''
#EquazioniCinematiche(Pr,DV,S)
def EquazioniMeccaniche(Pr,DV,S):
    EM = []
'''
