#NAVIER
import sympy as sym
import mpmath
from sympy import solve
#mpmath.mp.dps = 5
mpmath.mp.pretty = True #sym sà fare lo stesso? Volendo esiste: .evalf(n)
pi=mpmath.pi
a  =  sym.symbols('a',positive=True)  #lunghezza
s  =  sym.symbols('s',positive=True)  #spessore
S  =  sym.symbols('S',positive=True)  #Spessore (non trascurabile != a)
x  =  sym.symbols('x')  #x
y  =  sym.symbols('y')  #y
z  =  sym.symbols('z')  #z
r  =  sym.symbols('r',positive=True)  #raggio
R  =  sym.symbols('R',positive=True)  #Raggio
K  =  sym.symbols('K')  #T/I (Jourawski)
ξ  =  sym.symbols('ξ')  #ascissa curvilinea
η  =  sym.symbols('η')  #Eta
θ  =  sym.symbols('θ')  #angolo generico
τ  =  sym.symbols('θ')  #tau
σ  =  sym.symbols('θ')  #sigma
Ω  =  sym.symbols('θ')  #Area vuota (Bredt)
F   = sym.symbols('F')  #F
N   = sym.symbols('N')  #N
Ty  = sym.symbols('Ty') #Ty
Tz  = sym.symbols('Tz') #Tz
Mx  = sym.symbols('Mx') #Mx
My  = sym.symbols('My') #My
Mz  = sym.symbols('Mz') #Mz

import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
colori = {'Viola':'BUILTIN','Marrone':'console','Rosso':'COMMENT','Nero':'TODO','RossoAcceso':'stderr','Blu':'stdout','Verde':'STRING','Arancione':'KEYWORD','Errore':'ERROR','Warning': 'ERROR'}


'''
Nx  = sym.symbols('Nx') #N
Ta  = sym.symbols('Ta') #Ty o Tz
Mxa = sym.symbols('Mxa')#Mx applicato
Ma  = sym.symbols('Ma') #My o Mz applicato
Mxf = sym.symbols('Mxf')#Mx non applicato
Mf  = sym.symbols('Mf') #My o Mz non applicato
'''
SIMBOLI = [a,s,S,x,y,z,r,R,ξ,K,θ,τ,σ,Ω,N,Ty,Tz,Mx,My,Mz]#[Nx,Ta,Mxa,Ma,Mxf,Mf]
'''per controllare rapidamente se un termine è già stato usato come simbolo'''
def simbolo(x):
    if x in SIMBOLI:
        print(x,'è simbolo')
    else:
        print(x,'non è un simbolo')
'''per vedere rapidamente gli elementi di una lista'''
def mostra(L):
    for i in range(len(L)):
        print(i)
'''per vedere le chiavi di un dizionario'''
def chiavi(D):
    for i in D:
        print(i)
'''radianti -> gradi'''
def gradi(x):
    x=180*x/pi
    return x
'''gradi -> radianti'''
def rad(x):
    x=x*pi/180
    return x

'''cos e sin per evitare e-'''
def cos(a):
    if a in [90,-90,270,-270]:
        return 0
    else:
        return sym.cos(rad(a))##rad
def sin(a):
    if a in [0,180,-180]:
        return 0
    else:
        return sym.sin(rad(a))##rad

'''lista di stringhe -> stampa somma strighe'''
def somma(Ls):
    if str(Ls[0]) != '0':
        S = str(Ls[0])
    else:
        S = ''
    for i in range(1,len(Ls)):
        if str(Ls[i]) != '0':
            S = S + ' + ' + str(Ls[i])
    if len(S) == 0:
        S = '0'
    return S
'''elimina gli s**n (n>1). Se non vanno semplificati chiama s -> S (maiuscolo), oppure a,r o R
#sym o lista di sym contenente ((+ o -) e s**) una sola volta -> sym o lista di sym semplificata'''
def semplifica(I):
    cc = 0
    if type(I) != list:
        I = [I,0,0]
        cc = 1
    kk = 0
    ll = 0
    J  = []
    for i in range(len(I)):
        J.append(str(I[i]))
    for i in range(len(J)):
        for j in range(len(J[i])):
            if ll == 0:
                if J[i][j] == '+' or J[i][j] == '-':
                    kk=j
                if J[i][j] == 's':
                    if len(J[i])-1 != j:
                        if J[i][j+1] == '*' and J[i][j+2] == '*':
                            if kk==0:
                                I[i]=sym.sympify(J[i][kk:])
                                ll=1
                            else:
                                I[i]=sym.sympify(J[i][:kk])
                                ll=1
        kk=0
        ll=0
    if cc == 1:
        I = I[0]
    return I

'''Centro d'area
#Lista -> Lista con origine nel centro d'area'''
def CentroDArea(L,S): 
    sumY = []
    sumZ = []
    sumA = []
    M = []
    for i in range(len(L)):
        K = []
        for j in range(len(L[i])):
            K.append(L[i][j])
        M.append(K)    
    YA = 0
    ZA = 0
    A  = 0
    if S == 'NO':
        for i in range(len(L)):
            if type(L[i][2]) == int:
                Yg  = L[i][0]
                Zg  = L[i][1]
                l   = L[i][3]
                s   = L[i][4]
                YA += Yg * l*s           
                ZA += Zg * l*s
                A  += l*s
                sumY.append(Yg*l*s)
                sumZ.append(Zg*l*s)
                sumA.append(l*s)
            elif L[i][2] == 'C':
                Yc   =  L[i][0]
                Zc   =  L[i][1]
                R    =  L[i][3]
                s    =  L[i][4]
                ain  =  L[i][5]
                afin =  L[i][6]
                YAA = R*s*sym.integrate(Zc+R*sym.cos(x),(x,rad(ain),rad(afin)))
                ZAA = R*s*sym.integrate(Yc+R*sym.sin(x),(x,rad(ain),rad(afin)))
                if abs(YAA) < R**2*s/10000:
                    YAA = 0
                if abs(ZAA) < R**2*s/10000:
                    ZAA = 0
                YA += YAA
                ZA += ZAA
                A  += abs(R*s*rad(afin-ain))
                sumY.append(YAA)
                sumZ.append(ZAA)
                sumA.append(abs(R*s*rad(afin-ain)))
        Yg = YA/A
        Zg = ZA/A
        for i in range(len(L)):
            M[i][0] -= Yg
            M[i][1] -= Zg
    elif S == 'Y':
        for i in range(len(L)):
            if type(L[i][2]) == int:
                Yg  = L[i][0]
                l   = L[i][3]
                s   = L[i][4]
                YA += Yg*l*s
                A  +=    l*s
                sumY.append(Yg*l*s)
                sumA.append(l*s)
            elif L[i][2] == 'C':
                print('ca(L) circonferenze\nnon mi hai ancora scritto')#
        Yg = YA/A
        Zg = 0
        A = 2*A
        for i in range(len(L)):
            M[i][0] -= Yg
    elif S == 'Z':
        for i in range(len(L)):
            if type(L[i][2]) == int:
                Zg  = L[i][1]
                l   = L[i][3]
                s   = L[i][4]        
                ZA += Zg*l*s
                A  +=    l*s
                sumZ.append(Zg*l*s)
                sumA.append(l*s)
            elif L[i][2] == 'C':
                print('ca(L) circonferenze\nnon mi hai ancora scritto')#
        Yg = 0
        Zg = ZA/A
        A = 2*A
        for i in range(len(L)):
            M[i][1] -= Zg
    Sum = [sumY,sumZ,sumA]
    return [M,Yg,Zg,A,Sum]

def Stampa_CentroDArea(CA,S):
    M,Yg,Zg,A,Sum  = CA[0],CA[1],CA[2],CA[3],CA[4]
    sumY,sumZ,sumA = Sum[0],Sum[1],Sum[2]
    S = S.upper()
    if Yg == 0 and Zg == 0:
        print("Il centro d'area G coincide con il centro del sistema di riferimento scelto, difatti si ha:")     
    if S == 'NO':
        YA,ZA = Yg*A, Zg*A
        print('YA = Σ Yg*(l*s) =',somma(sumY),'=',YA)
        print('ZA = Σ Zg*(l*s) =',somma(sumZ),'=',ZA)
        print('A  = Σ l*s      =',somma(sumA),'=', A)
        print('YA/A = Yg =',Yg)
        print('ZA/A = Zg =',Zg)
    elif S == 'Y':
        A = A/2
        YA,ZA = Yg*A, Zg*A
        print('YA = Σ Yg*(l*s) =',somma(sumY),'=',YA)
        print('A  = Σ l*s      =',somma(sumA),'=', A)
        print('YA/A = Yg =',Yg)
        A = 2*A
        print('Atot = 2*A =',A)
    elif S == 'Z':
        A = A/2
        YA,ZA = Yg*A, Zg*A        
        print('ZA = Σ Zg*(l*s) =',somma(sumZ),'=',ZA)
        print('A  = Σ l*s      =',somma(sumA),'=', A)
        print('ZA/A = Zg =',Zg)
        A = 2*A
        print('Atot = 2*A =',A)
    if S in ['Y','Z']:
        print()
        print("In questo modo non solo ho determinato il centro d'area G, ma anche un sistema di coordinate centrali e principali di inerzia.")
        print("Infatti l'asse",S,"è principale in quanto di simmetria e ogni asse ortogonale ad un'asse principale è principale.")
        print("Per cui, traslando l'asse",S,"in G = (",Yg,Zg,") ottengo il sistema di coordinate desiderato")
    else:
        print()
        print('In questo modo ho determinato una terna centrale ma non principale.')
        print('Per ottenere la terna centrale devo diagonalizzare la matrice di ineria associata a questo sistema.')
        
#Momenti di inerzia
def miy(L):
    Iy   =  0
    Isy  =  []
    for i in range(len(L)):
        #travi rettilinee
        if type(L[i][2]) == int:
            Yg = L[i][0]
            Zg = L[i][1]
            a  = L[i][2]
            l  = L[i][3]
            s  = L[i][4]
            #termini mai trascurabili
            Iy  +=         s*sym.integrate(ξ**2*sin(a)**2,(ξ,-l/2,l/2))
            Isy.append(str(s*sym.integrate(ξ**2*sin(a)**2,(ξ,-l/2,l/2))))
            #termini solitamente trascurabili
            Iy  +=         l*sym.integrate(ξ**2*cos(a)**2,(ξ,-s/2,s/2))
            Isy.append(str(l*sym.integrate(ξ**2*cos(a)**2,(ξ,-s/2,s/2))))
            #trasporto
            Iy  += l*s*Zg**2
            Isy.append(str(l*s*Zg**2))
        #travi a curvatura costante
        elif L[i][2] == 'C': 
            Yc   =  L[i][0]
            Zc   =  L[i][1]
            R    =  L[i][3]
            s    =  L[i][4]
            ain  =  L[i][5]
            afin =  L[i][6]
            #termini mai trascurabili
            IY = s*R*sym.integrate((Zc+R*sym.sin(x))**2,(x, rad(ain),rad(afin)))
            if abs(IY) < s*R**3/10000:#quadratico ma non si sa mai (abs)
                IY = 0
            Iy  += IY
            Isy.append(str(IY))
    return [Iy,Isy]

def miz(L):
    Iz   =  0
    Isz  =  []
    for i in range(len(L)):
        #travi rettilinee
        if type(L[i][2]) == int:
            Yg = L[i][0]
            Zg = L[i][1]
            a  = L[i][2]
            l  = L[i][3]
            s  = L[i][4]
            #termini mai trascurabili
            Iz  +=         s*sym.integrate(ξ**2*cos(a)**2,(ξ,-l/2,l/2))
            Isz.append(str(s*sym.integrate(ξ**2*cos(a)**2,(ξ,-l/2,l/2))))
            #termini solitamente trascurabili
            Iz  +=         l*sym.integrate(ξ**2*sin(a)**2,(ξ,-s/2,s/2))
            Isz.append(str(l*sym.integrate(ξ**2*sin(a)**2,(ξ,-s/2,s/2))))
            #trasporto
            Iz  += l*s*Yg**2
            Isz.append(str(l*s*Yg**2))
        #travi a curvatura costante
        elif L[i][2] == 'C':
            Yc   =  L[i][0]
            Zc   =  L[i][1]
            R    =  L[i][3]
            s    =  L[i][4]
            ain  =  L[i][5]
            afin =  L[i][6]
            #termini mai trascurabili
            IZ = s*R*sym.integrate((Yc+R*sym.cos(x))**2,(x, rad(ain),rad(afin)))
            if abs(IZ) < s*R**3/10000:#quadratico ma non si sa mai (abs)
                IZ = 0
            Iz  += IZ
            Isz.append(str(IZ))
    return [Iz,Isz]

def myz(L):
    Iyz   =  0
    Isyz  =  []
    for i in range(len(L)):
        if type(L[i][2]) == int:
            Yg = L[i][0]
            Zg = L[i][1]
            a  = L[i][2]
            l  = L[i][3]
            s  = L[i][4]
            Iyz  += l*s*Yg*Zg
            Isyz.append(str(l*s*Yg*Zg))
        elif L[i][2] == 'C':
            Yc   =  L[i][0]
            Zc   =  L[i][1]
            R    =  L[i][3]
            s    =  L[i][4]
            ain  =  L[i][5]
            afin =  L[i][6]            
            IYZ = s*R*sym.integrate((Yc+R*sym.cos(x))*(Zc+R*sym.sin(x)),(x, rad(ain),rad(afin)))
            if abs(IYZ) < s*R**3/10000:
                IYZ = 0
            Iyz  += IYZ
            Isyz.append(str(IYZ))
    return [Iyz,Isyz]

def MatriceDiInerzia(L):
    a,b,c = miy(L),miz(L),myz(L)
    Iy,Iz,Iyz    = a[0],b[0],c[0]
    Isy,Isz,Isyz = a[1],b[1],c[1]
    I  = [Iy,Iz,Iyz]
    Is = [Isy,Isz,Isyz]
    return [I,Is]

def Stampa_Inerzie(Is):
    Isy,Isz,Isyz = Is[0],Is[1],Is[2]
    print('Iy  =',somma(Isy))
    #print()
    print('Iz  =',somma(Isz))
    #print()
    print('Iyz =',somma(Isyz))

def Stampa_SommaInerzie(I):
    Iy,Iz,Iyz = I[0],I[1],I[2]
    print('Iy  =',Iy)
    print('Iz  =',Iz)
    print('Iyz =',Iyz)    

def SemplificaInerzie(I):
    Iy,Iz,Iyz = I[0],I[1],I[2]
    Jy,Jz,Jyz = semplifica(Iy),semplifica(Iz),semplifica(Iyz)
    return [Jy,Jz,Jyz]

def Stampa_SemplificaInerzie(I):        
    cc = 0
    for k in I:    
        for i in range(len(str(k))-3):
            if str(k)[i:i+3] == 's**':
                cc = 1    
    if cc == 1:
        print('Essendo s << a possiamo trascurare i termini che presentano s di grado > 1º:')
        J = SemplificaInerzie(I)
        Jy,Jz,Jyz = J[0],J[1],J[2]
        print('Iy  =',Jy)
        print('Iz  =',Jz)
        print('Iyz =',Jyz)

def Stampa_MatriceDiInerzia(I):
    Iy,Iz,Iyz = I[0],I[1],I[2]
    l = len(str(Iy))
    if len(str(Iz))  > l:
        l = len(str(Iz))
    if len(str(Iyz)) > l:
        l = len(str(Iyz))
    print('(Iy   -Iyz) _ (',  Iy,' '*(l-len(str(Iy))), -Iyz,')')
    print('(-Iyz  Iz ) ¯ (',-Iyz,' '*(l-len(str(Iyz))),  Iz,')')

'''angolo di rotazione
   [Iy,Iz,Iyz] -> α'''
def AngoloDiRotazione(I):
    Iη  = I[0]
    Iξ  = I[1]
    Iηξ = I[2]
    if Iηξ == 0:
        return 0
    else:
        if Iη != Iξ:
            A = 2*Iηξ/(Iξ-Iη)
            A = str(A)
            A = sym.sympify(A)
            A = sym.simplify(A)
            
            α = mpmath.atan(A)/2
        else:
            α = pi/4 # piu o meno??
        return α

def Stampa_AngoloDiRotazione(α):
    if α == 0:
        print('La matrice di inerzia è diagonale, quindi α = 0')
    else:
        print('α = (1/2)*arctg(2*Iηξ/(Iξ-Iη)) =',str(α),'rad =',str(gradi(α))+'º')
    
'''diagonalizzazione matrici di inerzia
   [Iy,Iz,Iyz] -> [Iy_diag,Iz_diag]'''

def MatriceDiRotazione(α):
    R = [[mpmath.cos(α),mpmath.sin(α)],[-mpmath.sin(α),mpmath.cos(α)]]
    return R

def Stampa_MatriceDiRotazione(R):
    print('( +cos(α)  +sin(α) )  _  (',R[0][0],'  ',R[0][1],')')
    print('( -sin(α)  +cos(α) )  ¯  (',R[1][0],'  ',R[1][1],')')

def Diagonalizzazione(I):
    α = AngoloDiRotazione(I)
    Iη  = I[0]
    Iξ  = I[1]
    Iηξ = I[2]
    if α != 0:
        Iy = Iη*mpmath.cos(α)**2 + Iξ*mpmath.sin(α)**2 - 2*Iηξ*mpmath.cos(α)*mpmath.sin(α)
        Iz = Iξ*mpmath.sin(α)**2 + Iξ*mpmath.cos(α)**2 + 2*Iηξ*mpmath.cos(α)*mpmath.sin(α)
        J = [Iy,Iz]
        return J
    else:
        return I

def Stampa_Diagonalizzazione(I):
    Iy,Iz  = I[0],I[1]
    print('Iy = Iη*cos(α)**2 + Iξ*sin(α)**2 - 2*Iηξ*cos(α)*sin(α)')
    print('Iz = Iη*sin(α)**2 + Iξ*cos(α)**2 + 2*Iηξ*cos(α)*sin(α)')
    print()
    print('Dunque gli elementi della traccia della matrice di inerzia diagonalizzata sono:')
    print('Iy = ',Iy,'\n'+'Iz = ',Iz)

def jo(A):
    L      = A[0]
    Isim   = A[1]
    Asim   = A[2]
    Cont   = A[3]
    q      = {} #q(c)
    Q      = {} #q(c = l tot)
    LTrave = {}
    for i in range(len(L)):
        LTrave[i] = L[i]
    
    if Asim == 'Y': 
        print('q(ξ) = -(Tz/Iy)(Zg*)(A*)')
        print('chiamiamo ora K = Tz/Iy per semplicità, cosicchè:\nq(ξ) = -K(Yg*)(A*)\n')
        for i in range(len(L)):
            if type(L[i][2]) == int:
                Yg = L[i][0]
                Zg = L[i][1]
                a  = L[i][2]
                l  = L[i][3]
                s  = L[i][4]
                q[i] = -K*s*ξ*(Zg-sin(a)*l/2 + sin(a)*ξ/2)
                Q[i] = -K*s*l*(Zg-sin(a)*l/2 + sin(a)*l/2)
            elif L[i][2] == 'C':
               #Yc   = L[i][0]
               #Zc   = L[i][1]
                R    = L[i][3]
                s    = L[i][4]
                ain  = L[i][5]
                afin = L[i][6]
                q[i] = -K*s*R**2*sym.integrate((sym.sin(x)),(x, rad(ain),θ))        
                Q[i] = -K*s*R**2*sym.integrate((sym.sin(x)),(x, rad(ain),rad(afin)))
    if Asim == 'Z':
        print('q(ξ) = -(Ty/Iz)(Yg*)(A*)')
        print('chiamiamo ora K = Tz/Iy per semplicità, cosicchè\nq(ξ) = -K(Yg*)(A*)\n')
        for i in range(len(L)):
            if type(L[i][2]) == int:
                Yg = L[i][0]
                Zg = L[i][1]
                a  = L[i][2]
                l  = L[i][3]
                s  = L[i][4]
                q[i] = -K*s*ξ*(Yg-cos(a)*l/2 + cos(a)*ξ/2)
                Q[i] = -K*s*l*(Yg-cos(a)*l/2 + cos(a)*l/2)
            elif L[i][2] == 'C': 
               #Yc   = L[i][0]
               #Zc   = L[i][1]
                R    = L[i][3]
                s    = L[i][4]
                ain  = L[i][5]
                afin = L[i][6]
                q[i] = -K*s*R**2*sym.integrate((sym.cos(x)),(x, rad(ain),θ))             
                Q[i] = -K*s*R**2*sym.integrate((sym.cos(x)),(x, rad(ain),rad(afin)))
    for i in range(len(L)):
        if type(L[i][2]) == int:
            f = str(L[i][3])
            print('trave nº',i+1,':',LTrave[i])
            print('q(ξ'+str(i+1)+') =',q[i])
            print('q(ξ'+str(i+1)+'='+f+') =',Q[i],'\n')
        elif L[i][2] == 'C':
            f = str(L[i][6])+'º'
            print('trave nº',i+1,':',LTrave[i])
            print('q(θ'+str(i+1)+') =',q[i])
            print('q(θ'+str(i+1)+'='+f+') =',Q[i],'\n')
            
    for i in range(len(L)):
        flusso = str(Cont[i])
        if flusso == '0':
            pass
        else:
            for j in range(int((len(flusso)+1)/2)):
                q[i] += Q[int(flusso[2*j])-1]
                Q[i] += Q[int(flusso[2*j])-1]
    print('Sommando le condizioni al contorno:\n')
    for i in range(len(L)):
        if type(L[i][2]) == int:
            f = str(L[i][3])
            print('trave nº',i+1,':',LTrave[i])
            print('q(ξ'+str(i+1)+')+C =',q[i])
            print('q(ξ'+str(i+1)+'='+f+')+C =',Q[i],'\n')
        elif L[i][2] == 'C':
            f = str(L[i][6])+'º'
            print('trave nº',i+1,':',LTrave[i])
            print('q(θ'+str(i+1)+')+C =',q[i])
            print('q(θ'+str(i+1)+'='+f+')+C =',Q[i],'\n')
    return [L,Isim,q]

    

D = {}
#########################################################################
#esercizi con s<<a:

#24-10-14 n.2 CORRETTO (tutto)
#N.B.:Fleres considera un sistema ruotato di pi rispetto al mio quindi alcuni punti hanno tutti i segni invertiti
L = [[a/2,a,0,a,s],[a,a/2,-90,a,s],[0,0,180,2*a,s],[-a,-a/2,-90,a,s],[-a/2,-a,0,a,s]]
P = {}
Ty = []
Tz = []
Cont = []
M = [1,0]
D[2410142] = [L,P,Ty,Tz,Cont,M]

#23-09-11 n.3
#Fleres considera metà sezione, da cui un Iy diverso
#credo sia Fleres a sbagliare
L = [[-a/2,2*a,0,3*a,s],[0,0,-90,4*a,s],[a/2,-2*a,180,3*a,s]]
P = {}
Ty = {}
Tz = {}
Cont = []
M = [1,0]
D[2309113] = [L,P,Ty,Tz,Cont,M]

#12-01-12 n.3 CORRETTO (tutto)
#Iz (diagonalizzata) di poco diversa
L = [[0,a,-90,2*a,s],[a,0,0,4*a,s]]
P = {}
Ty = []
Tz = []
Cont = []
M = [1,0]
D[1201123] = [L,P,Ty,Tz,Cont,M]

#24-06-11 n.3
#tutto come Fleres fino a Iy,Iz diagonalizzati.
#Lui inverte i valori di Iy e Iz e considera il suo Iy come il mio Iz/2.
#credo sia Fleres a sbagliare
L = [[0,a,-90,2*a,s],[a/2,0,0,a,s]]
P = {(0,0): -F}
Ty = []
Tz = []
Cont = []
M = [0,0]
D[2406113] = [L,P,Ty,Tz,Cont,M]

#18-07-16 n.2 CORRETTO (tutto)
#Iz (diagonalizzata) di poco diversa
L = [[-a/2,-a,180,a,s],[-a,0,90,2*a,s],[0,0,0,2*a,s],[a,0,90,2*a,s],[a/2,a,180,a,s]]
P = {}
Ty = []
Tz = []
Cont = []
M = [1,0]
D[1807162] = [L,P,Ty,Tz,Cont,M]

#29-10-16 n.2 CORRETTO (tutto)
#Iz (diagonalizzata) di pochissimo diversa (circa 0.08 su 21,2)
L = [[-a,0,0,2*a,2*s],[0,a/2,90,a,s]]
P = {(0,0): F}
Ty = []
Tz = []
Cont = []
M = [0,0]
D[2910162] = [L,P,Ty,Tz,Cont,M]


#30-10-15 N.2 CORROTTO (tutto)
##Iz (diagonalizzata) di poco diversa
L = [[-3*a/2,-a,180,a,s],[-2*a,-a/2,90,a,s],[0,0,0,4*a,s],[2*a,a/2,90,a,s],[3*a/2,a,180,a,s]]
P = {}
Ty = []
Tz = []
Cont = []
M = [0,1]
D[3010152] = [L,P,Ty,Tz,Cont,M]
#########################################################################
#esercizi senza s<<a:

#28-10-11 n.3 CORRETTO (tutto)
L = [[-a,a,-90,2*a,a],[0,a/2,0,a,a],[a,a,90,2*a,a]]
P = {(3*a/2,2*a): F}
Ty = []
Tz = []
M = [0,0]
D[2810113] = [L,P,Ty,Tz,Cont,M]

#09-11-12 N-4 CORRETTO (tutto, probabilmente)
#Fleres sbaglia Iy e Iz (diagonalizzate) (lo scrive) 
L = [[2*a,a/2,0,4*a,a],[3*a/2,3*a,90,4*a,a]]
P = {}
Ty = []
Tx = []
Cont = []
M = [1,0]
D[911124] = [L,P,Ty,Tz,Cont,M]

#22-03-17 n.2 CORRETTO (tutto)(L come 2810113)
L = [[-a,a,-90,2*a,a],[0,a/2,0,a,a],[a,a,90,2*a,a]]
P = {(-3*a/2,0): F,(-a/2,2*a): F,(3*a/2,a): -F}
Ty = []
Tz = []
Cont = []
M = [0,0]
D[2203172] = [L,P,Ty,Tz,Cont,M]

######################################################
#22-11-16 n.2 
L  = [[0,0,0,a,s],[-a/4,a*3**(1/2)/4,60,a,s],[a/4,a*3**(1/2)/4,120,a,s]]
P = {}#credo, l'ho modificato per sbaglio e non ricordo quanto fosse (credo non ci fosse)
Ty = []
Tz = [-a/2,0]
Cont = [0,1]
M = [0,0]
D[2211162] = [L,P,Ty,Tz,Cont,M]
'''
#9-9-18 n.2
L = [ ]
P  = {}
Ty = [-a,a]
Tz = []
Cont = []
M = [0,0]
D[2211162] = [L,P,Ty,Tz,Cont,M]
'''
#######################################################
#17-01-19 n.2
L    = [[-3*a/2,-a/2,45,2**(0.5)*a,s],[0,0,'C',a,s,180,360],[3*a/2,-a/2,135,2**(0.5)*a,s]]
P  = {(-a,0): -2*F, (2*a,-a): +F}
Ty   = []
Tz   = []
Cont = []
M    = [0,0]
D[1701192] = [L,P,Ty,Tz,Cont,M]
########################################################
#esame 9/11/20:
L    = []#[[-3*a/2,-a/2,45,2**(0.5)*a,s],[0,0,'C',a,s,180,360],[3*a/2,-a/2,135,2**(0.5)*a,s]]
P    = {}#{(-a,0): -2*F, (2*a,-a): +F}
Ty   = []
Tz   = []
Cont = []
M    = [0,0]
D[91129] = [L,P,Ty,Tz,Cont,M]

def Navier():
    LP = D[2410142]
    ##################
    L    = LP[0]
    P    = LP[1]
    Ty   = LP[2]
    Tz   = LP[3]
    Cont = LP[4]
    M    = LP[5]
    '''
    print('Lista di input:')
    print(L)
    print('Lista azioni normali:')
    print(P)
    print('[My,Mz]:')
    print(M)
    print('\n')
    '''
    ##################
    print("Calcoliamoci il centro d'area:")
    CA = CentroDArea(L,'NO')
    Stampa_CentroDArea(CA,'NO')
    LCA = CA[0]
    Yg,Zg,A = CA[1],CA[2],CA[3]
    print()
    print("Calcoliamoci i momenti di inerzia del sistema Y-Z con origine traslata nel centro d'area:")
    MI = MatriceDiInerzia(LCA)
    I,Is  = MI[0],MI[1]
    Stampa_Inerzie(Is)
    print()
    print('Sommando i termini:')
    Stampa_SommaInerzie(I)
    print()
    Stampa_SemplificaInerzie(I)
    J = SemplificaInerzie(I)
    print()
    print('Dunque la matrice di inerzia vale:')
    Stampa_MatriceDiInerzia(J)
    print()
    print("Calcoliamoci l'angolo di rotazione:")
    α = AngoloDiRotazione(J)
    Stampa_AngoloDiRotazione(α)
    print()
    print("Tramite l'angolo di rotazione calcolo il sistema di coordinate centrale-principale.")
    print()
    print('La matrice di rotazione vale dunque:')
    R = MatriceDiRotazione(α)
    Stampa_MatriceDiRotazione(R)
    print()
    print('Per i calcolo degli elementi della traccia della matrice di inerzia diagonalizzata uso:')
    I = Diagonalizzazione(J)
    Iy,Iz = I[0],I[1]
    Stampa_Diagonalizzazione(I)
    print()
    print("Ovvero, in forma tensoriale:")
    Stampa_MatriceDiInerzia([I[0],I[1],0])
    print()
    #print('Osserviamo come il momento misto, calcolato come momento deviatore delle sottofigure sommato al prodotto con segno dei termini di spostamento (raggi vettori), si annulla quando calcolato con una terna principale centrale')
    #print()
    N  = 0
    Ns = []
    Mfy,Mfz = 0,0
    Msy,Msz = [],[]
    if len(P) != 0:
        cc = 0
        for i in P:
            if i != [Yg,Zg]:
                cc = 1
        if cc == 1:
            print("Poichè N non è applicata al centro d'area produrrà dei momenti flettenti.")
            print("Occorre ora ridurre le forze al centro d'area.")
            print("Conviene, per comodità, calcolarsi queste sulla terna (X,Y,Z) e poi applicare la matrice di rotazione.")
            print()
        for i in P:
            N += P[i]
            Ns.append(P[i])
            Mfy += (i[1]-Zg)*P[i]
            Msy.append(str((i[1]-Zg)*P[i]))
            Mfz -= (i[0]-Yg)*P[i]
            Msz.append(str(-(i[0]-Yg)*P[i]))
        print('N  =',somma(Ns), '=',N)
        print('My =',somma(Msy),'=',Mfy)
        print('Mz =',somma(Msz),'=',Mfz)
        print()
    if M != [0,0]:
        Mfy += M[0]*My
        Mfz += M[1]*Mz
    if len(P) != 0 or Mfy != 0 or Mfz != 0:
        print('Calcoliamo le forze ridotte al centro della nuova terna principale centrale:')
        print('( My )  _  (',R[0][0],'  ',R[0][1],') (',Mfy,')')
        print('( Mz )  ¯  (',R[1][0],'  ',R[1][1],') (',Mfz,')')
        print()
        MY = R[0][0]*Mfy + R[0][1]*Mfz
        MZ = R[1][0]*Mfy + R[1][1]*Mfz
        print('My =',MY)
        print('Mz =',MZ)
        print()
        print("formula trinomia di Navier:")
        print('σₓ(y,z) = N/A + (My/Iy)z - (Mz/Iz)y')
        print()
        SIGMAx = N/A + (MY/Iy)*z - (MZ/Iz)*y
        print('σ =', SIGMAx)
        print()
        print('Equazione asse neutro [(y,z)|σ = 0]:')
        print('z =',solve(SIGMAx,z))
    #LCA = [[-a/4, -0.288675134594813*a, 0, a/2, s], [-a/4, 0.144337567297406*a, 60, a, s]]#, [a/4, 0.144337567297406*a, 120, a, s]]
    #jo() VUOLE META' LISTA!
    if 1 == 0:###################################
        if Tz or Ty != []:
            color.write('SCRIVERE a mano META" LISTA prima di questo "if"!! poi cancellami\n',colori['Attenzione'])
    if Ty != []:
        Asim = 'Z'#NON è necessariamente Y l'asse di simmetria
        jo([LCA,Iz,Asim,Cont])
        color.write('I flussi delle τ sono nulli agli estremi della sezione aperta ',colori['Blu'])
        print('e massimi nei punti in cui la corda baricentrica interseca la sezione.')
        color.write("Mi aspetto inoltre che i flussi abbiano un'andamento lineare sui tratti ",colori['Blu'])
        print("⟂ all'asse Y e parabolico in quelli // a Z.")
        print("Saranno inoltre nulli all'intersezione fra la trave e l'asse Y (di simmetria).")
    if Tz != []:
        Asim = 'Y'#NON è necessariamente Y l'asse di simmetria
        jo([LCA,Iz,Asim,Cont])##L,Isim,Asim,Cont
        color.write('I flussi delle τ sono nulli agli estremi della sezione aperta ',colori['Blu'])
        print('e massimi nei punti in cui la corda baricentrica interseca la sezione.')
        color.write("Mi aspetto inoltre che i flussi abbiano un'andamento lineare sui tratti ",colori['Blu'])
        print("⟂ all'asse Z e parabolico in quelli // ad Z.")
        print("Saranno inoltre nulli all'intersezione fra la trave e l'asse Z (di simmetria).")
        



Navier()




