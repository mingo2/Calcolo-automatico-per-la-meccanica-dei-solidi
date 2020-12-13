#Centro di Taglio
'''
Per la teoria su questa parte, consultare il sito:
http://www.scienzadellecostruzioni.co.uk/Teoria%20di%20Jourawski.pdf
'''
import sympy as sym
import mpmath
from sympy import solve
mpmath.mp.dps = 25; mpmath.mp.pretty = True
pi=mpmath.pi

import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
colori = {'Viola':'BUILTIN','Marrone':'console','Rosso':'COMMENT','Nero':'TODO','RossoAcceso':'stderr','Blu':'stdout','Verde':'STRING','Arancione':'KEYWORD','Errore':'ERROR','Warning': 'ERROR'}

a  =  sym.symbols('a')
s  =  sym.symbols('s')
S  =  sym.symbols('S')
x  =  sym.symbols('x')
y  =  sym.symbols('y')
z  =  sym.symbols('z')
P  =  sym.symbols('P')
r  =  sym.symbols('r')
R  =  sym.symbols('R')
F  =  sym.symbols('F')
N  =  sym.symbols('N')
T  =  sym.symbols('T')
Ty =  sym.symbols('Ty')
Tz =  sym.symbols('Tz')
M  =  sym.symbols('M')
Mx =  sym.symbols('Mx')
My =  sym.symbols('My')
Mz =  sym.symbols('Mz')
c  =  sym.symbols('c')#
ξ  =  sym.symbols('ξ')##
K  =  sym.symbols('K')
θ  =  sym.symbols('θ')##

def stampa(x):
    for i in x:
        print(i)
    return S
def gradi(x):
    x=180*x/pi
    return x
def rad(x):
    x=x*pi/180
    return x
#cos e sin per evitare e-
def cos(a):
    if a in [90,-90,270,-270]:
        return 0
    else:
        return sym.cos(rad(a))
def sin(a):
    if a in [0,180,-180]:
        return 0
    else:
        return sym.sin(rad(a))
    
#stampa la somma dei termini contenuti in una lista di stringhe
def somma(I):
    if str(I[0]) != '0':
        S = str(I[0])
    else:
        S = ''
    for i in range(1,len(I)):
        if str(I[i]) != '0':
            S = S + ' + ' + str(I[i])
    if len(S) == 0:
        S = '0'
    return S
#elimina gli s**n (n>1). Se non vanno semplificati chiama s -> S
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
            Iy  += s*sym.integrate(ξ**2*sin(a)**2,(ξ,-l/2,l/2))
            Isy.append(str(s*sym.integrate(ξ**2*sin(a)**2,(ξ,-l/2,l/2))))
            #termini solitamente trascurabili
            Iy  += l*sym.integrate(ξ**2*cos(a)**2,(ξ,-s/2,s/2))
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
            Iy  += s*R**3*sym.integrate((sym.sin(x)**2),(x, rad(ain),rad(afin)))
            Isy.append(str(s*R**3*sym.integrate((sym.sin(x)**2),(x, rad(ain),rad(afin)))))
            #trasporto
            Iy  += R*s*Zg**2
            Isy.append(str(R*s*Zg**2))
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
            Iz  += s*sym.integrate(ξ**2*cos(a)**2,(ξ,-l/2,l/2))
            Isz.append(str(s*sym.integrate(ξ**2*cos(a)**2,(ξ,-l/2,l/2))))
            #termini solitamente trascurabili
            Iz  += l*sym.integrate(ξ**2*sin(a)**2,(ξ,-s/2,s/2))
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
            Iz  += s*R**3*sym.integrate((sym.cos(x)**2),(x, rad(ain),rad(afin)))
            Isz.append(str(s*R**3*sym.integrate((sym.cos(x)**2),(x, rad(ain),rad(afin)))))
            #trasporto
            Iz  += R*s*Yg**2
            Isz.append(R*s*Yg**2)
    return [Iz,Isz]

#NON USATO
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

def ItcA(L):
    It   =  0
    Ist  =  []
    for i in range(len(L)):
        if type(L[i][2]) == int:
            l  = L[i][3]
            s  = L[i][4]

            It += l*s**3/3
            Ist.append(str(l*s**3/3))
    print('It = 2*(',somma(Ist),')')
    print('It =',2*It)
    return 2*It
    

#jourawski (?)
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

def ct(A):
    n = 5
    LTrave = {}
    L      = A[0]
    Isim   = A[1]
    q      = A[2]
    C      = 0 
    for i in range(len(L)):
        LTrave[i] = L[i]
    for i in range(len(L)):
        if type(L[i][2]) == int:
            Yg = L[i][0]
            Zg = L[i][1]
            a  = L[i][2]
            l  = L[i][3]
           #s  = L[i][4]
            C += 2*Yg*sym.integrate(q[i],(ξ,0,l))*sin(a)
            C -= 2*Zg*sym.integrate(q[i],(ξ,0,l))*cos(a)
            print('2*ξ'+str(i+1)+':',LTrave[i])
            print('"e1":',+2*Yg*sym.integrate(q[i], (ξ,0,l))*sin(a))
            print('"e2":',-2*Zg*sym.integrate(q[i], (ξ,0,l))*cos(a),'\n')
        elif L[i][2] == 'C':
           #Yc   =  L[i][0]
           #Zc   =  L[i][1]
            R    =  L[i][3]
            s    =  L[i][4]
            ain  =  L[i][5]
            afin =  L[i][6]
            C += 2*(R**2)*sym.integrate(q[i],(θ,rad(ain),rad(afin)))
            print('2*ξ'+str(i+1)+':',LTrave[i])
            print('"e1+e2":',2*(R**2)*sym.integrate(q[i],(θ,rad(ain),rad(afin))),'\n')
    print('∫ OP X q(ξ) versor(ξ) dξ =',C)
    print('Centro di Taglio:\nQCt =',C/K,'/I\nQCt =',(C/K)/Isim)
    return (C/K)/Isim


#CENTRO DI TAGLIO
#CDT(Arg) -> Arg = [L,LAsse]
def CDT(Arg):
    #DATI
    L    = Arg[0]
    Ltot = Arg[1]
    Asim = Arg[2]
    Cont = Arg[3]
    #TEORIA
    print("Il centro di taglio è il punto di una sezione trasversale di una trave per cui deve passare la retta d'azione dello sforzo tagliante affinché non si produca momento torcente sulla sezione.")
    color.write("La sezione presenta "+Asim+" come asse di simmetria, ",colori['Blu'])
    Ξ = ''
    for i in range(len(L)):
        if i != len(L)-1:
            Ξ += 'ξ'+str(i+1)+', '
        else:
            Ξ += 'ξ'+str(i+1)+'.'
    if   Asim == 'Y':
        I  = 'Iy'
        T  = 'Tz'
        Cg = 'Zg'
    elif Asim == 'Z':
        I  = 'Iz'
        T  = 'Ty'
        Cg = 'Yg'
    print("quindi per determinare il Ct occorre testarla con una forza di taglio di prova ⟂ all'asse",str(Asim)+':',T)
    print('In questo modo si genera una distribuzione di tenzione tangenziale il cui flusso è determinabile tramite la formula di Jourawski:')
    print("q(ξ) = -(Tz/Iy)Zg*A* -(Ty/Iz)Yg*A\nche non nostro caso, essendo presente solo",T+", diventa:")
    print("q(ξ) = -("+T+"/"+I+")"+Cg+"*A*")
    print("da applicare per i",len(L),"tratti di ascisse curvilinee:",Ξ)
    print("Infatti, data la simmetria, posso studiare solo metà sezione.")
    print("Per il calcolo del momento d'inerzia",I,"applico la definizione:")
    if   Asim == 'Y':
        print(I,'=','∫ z^2 dA')
    elif Asim == 'Z':
        print(I,'=','∫ y^2 dA')
    cc = 0
    for i in range(len(L)):
        if type(L[i][2]) == int and cc == 0:
            if L[i][2] not in [0,180,-180] and L[i][2] not in [90,-90,270,-270]:
                color.write("Per il calcolo del momento d'inerzia delle travi non parallele ad uno degli",colori['Blu'])
                color.write("assi del sistema di riferimento y-z, ne introduciamo uno ausiliare η-ξ",colori['Blu'])
                print("per ognuna di queste travi, centrato nel centro d'area delle stesse.")
                print("Ci calcoliamo quindi i momenti di inerzia rispetto ad η e a ξ")
                print("per poi riportare il risultato nel sistema y-z.")
                print("Avendo poi fatto il calcolo con un sistema centrato nel centro d'area bisogna")
                print("aggiungere il contributo legato alla distanza rispetto l'asse di rotazione,")
                print("che calcoliamo tramite il teorema di Huygens-Steiner: I = Ica + A*d^2")
                print("Avremo quindi che:")
                print("Iη = s*l**3/12, Iξ = l*s**3/12")
                if   Asim == 'Y':
                    print("Iy = Iη*sin(90-a)^2 + Iξ*cos(90-a)^2 + Area*Zg^2\n")
                elif Asim == 'Z':
                    print("Iz = Iη*cos(90-a)^2 + Iξ*sin(90-a)^2 + Area*Yg^2\n")
                cc = 1
    #MOMENTO DI INERZIA
    if   Asim == 'Y':
        MIY = miy(Ltot)
        Isim  = MIY[0]
        Issim = MIY[1]
    elif Asim == 'Z':
        MIZ = miz(Ltot)
        Isim  = MIZ[0]
        Issim = MIZ[1]
    print()
    print('I'+Asim.lower()+' =',somma(Issim))
    print()
    print('Sommando i termini:')
    print('I'+Asim.lower()+' =',Isim)
    print()
    cc = 0
    for i in range(len(str(Isim))-3):
        if str(Isim)[i:i+3] == 's**':
            cc = 1
    if cc == 1:
        print('Essendo s << a possiamo trascurare i termini che presentano s di grado > 1º:')
        print('I'+Asim.lower()+' =',semplifica(Isim),'\n')
        Isim = semplifica(Isim)
    #TEORIA
    color.write('I flussi delle τ sono nulli agli estremi della sezione aperta ',colori['Blu'])
    print('e massimi nei punti in cui la corda baricentrica interseca la sezione.')
    color.write("Mi aspetto inoltre che i flussi abbiano un'andamento lineare sui tratti ",colori['Blu'])
    print("⟂ all'asse",Asim,"e parabolico in quelli // ad",Asim+'.')
    print("Anche per il calcolo dei momenti d'area di primo ordine applico la definizione:")
    print(Cg+'*A* =','∫',T[1],'dA','\n')
    #JOURAWSKI
    JO = jo([L,Isim,Asim,Cont]) # -> [L,Isim,q,Sign]
    #TEORIA
    color.write('Per trovare il centro di taglio calcolo il momento torcente ',colori['Blu'])
    print("generato dai flussi rispetto ad un polo arbitrario Q posto sull'asse di simmetria")
    print('Formula di Timoshenko:\nQCt x',T,'= ∫[QP x (q(ξ) versor(ξ))] dξ \n')
    #CENTRO DI TAGLIO
    CT = ct(JO)
    
    

'''
N.B.:
L_Segmento      = [Yg, Zg,  a, l, s]
L_Circonferenza = [Yc, Zc,'C',Ra,Sp,a.in,a.fin]
Scrivere l'angolo tenendo a mente la direzione dell'ascissa curvilinea
Scrivere le travi tenendo a mente i contribuiti che daranno alle adiacenti
Se nessuna trave passa per l'asse di simmetria, nello scrivere Ltot basterà considerare identici per due volte gli elementi di L
Scegliere adeguatamente l'origine
'''

#09-01-14 n.2 funziona :)
L    = [[-3*a/2,a/2,-90,a,s],[-a,0,0,a,s],[-a/2,a/2,90,a,s],[-a/4,a,0,a/2,s]]
Ltot = [[-3*a/2,a/2,-90,a,s],[-a,0,0,a,s],[-a/2,a/2,90,a,s],[0,a,0,a,s],[a/2,a/2,-90,a,s],[a,0,0,a,s],[3*a/2,a/2,90,a,s]]
Asim = 'Z'
Cont = [0,1,2,3]
#CDT([L,Ltot,Asim,Cont])

#24-06-11 n.2 funziona :)
L    = [[R,R/2,-90,R,s], [0,0,'C',R,s,0,180]]
Ltot = [[R,0,-90,2*R,s], [0,0,'C',R,s,0,360]]
Asim = 'Y'
Cont = [0,1]
#CDT([L,Ltot,Asim,Cont])

#14-02-12 n.3 funziona :) (segno Ct)
L    = [[-3*a/2,0,180,a,s],[-2*a,-a,-90,2*a,s],[-2*a,-5*a/2,90,a,s],[-a,-a,45,2**(3/2)*a,s]]
Ltot = [[-3*a/2,0,0,a,s],[-2*a,-a,90,2*a,s],[-2*a,-5*a/2,90,a,s],[-a,-a,45,2**(3/2)*a,s],[-3*a/2,0,0,a,s],[-2*a,-a,90,2*a,s],[-2*a,-5*a/2,90,a,s],[-a,-a,45,2**(3/2)*a,s]]#scritto male ma non dovrebbe creare problemi
Asim = 'Z'
Cont = [0,1,0,'2 3']
#CDT([L,Ltot,Asim,Cont])

#18-06-12 n.2 funziona :)
L    = [[5*a/(2**(5/2)),-3*a/(2**(5/2)),-135,a/2,s],[a/(2**(3/2)),-a/(2**(3/2)),135,a,s]]
Ltot = [[5*a/(2**(5/2)),-3*a/(2**(5/2)),-135,a/2,s],[a/(2**(3/2)),-a/(2**(3/2)),135,a,s],[5*a/(2**(5/2)),3*a/(2**(5/2)),-135,a/2,s],[a/(2**(3/2)),a/(2**(3/2)),135,a,s]]#idem
Asim = 'Y'
Cont = [0,1]
#CDT([L,Ltot,Asim,Cont])

#############################################
#Altro oltre CT

#28-10-17 n.2
L    = [[-a,-a,180,a,s],[-3*a/2,-a/2,90,a,s],[-a,0,0,a,s],[-a,a,0,a,s],[-a/2,a/2,-90,a,s],[-a/4,0,0,a/2,s]]
Ltot = [[-a,-a,180,a,s],[-3*a/2,-a/2,90,a,s],[0,0,0,3*a,s],[-a,a,0,a,s],[-a/2,a/2,-90,a,s],[a,-a,0,a,s],[3*a/2,-a/2,90,a,s],[a/2,a/2,90,a,s],[a,a,180,a,s]]
Asim = 'Z'
Cont = [0,1,2,0,4,'3 5']
#CDT([L,Ltot,Asim,Cont])

#12-02-19 n.1: simmetrica rispetto a Z ma con Tz quindi flesha: SISTEMARE
#12-04-23 n.1 idem (p.116)
L    = [[-3*a/2,0,0,a,s],[-a,a/2,-90,a,s],[-a/2,0,180,a,s],[-a,-a/2,-90,a,s],[-a,-a,0,a,s]]
Ltot = [[0,0,0,4*a,s],[-a,0,-90,2*a,s],[a,0,-90,2*a,s],[0,-a,0,2*a,s]]
Asim = 'Z'
Cont = [0,0,0,'1 2 3',4]
#CDT([L,Ltot,Asim,Cont])

#19-06-13 n.3
#doppiamente simmetrica quindi problematica (per via delle ascisse curvilinee)
#p.138
#08-07-13 n-2 idem (p.144)

#08-04-11 n.3
L    = [[a,-3*a/4,-90,a/2,s],[a/2,-a,180,a,s],[0,-a/2,90,a,s]]
Ltot = [[a,-3*a/4,-90,a/2,s],[a/2,-a,180,a,s],[0,0,90,2*a,s],[a/2,a,0,a,s],[a,3*a/4,90,a/2,s]]
Asim = 'Y'
Cont = [0,1,2]
#CDT([L,Ltot,Asim,Cont])

#22-11-16 n. 2
L    = [[-a/4, -0.288675134594813*a, 0, a/2, s], [-a/4, 0.144337567297406*a, 60, a, s]]
Ltot = [[0, -0.288675134594813*a, 0, a, s], [-a/4, 0.144337567297406*a, 60, a, s], [a/4, 0.144337567297406*a, 120, a, s]]
Asim = 'Z'
Cont = [0,1]
#CDT([L,Ltot,Asim,Cont])
#L    = [[-2*a,a/2,-90,a,s],[-3*a/2,0,0,a,s],[-3*a/2,-a,0,a,s],[-a,-a/2,90,a,s],[-a,a/2,90,a,s],[-a/2,a,0,a,s],[-a/2,0,0,a,s]]
L    = [[-2*a,a/2,-90,a,s],[-3*a/2,0,0,a,s],[-a/2,0,180,a,s],[-3*a/2,-a,0,a,s],[-a,-a/2,90,a,s],[-a,a/2,90,a,s],[-a/2,a,0,a,s]]
Ltot = [[-2*a,a/2,-90,a,s],[2*a,a/2,-90,a,s],[-a,0,0,2*a,s],[a,0,0,2*a,s],[-a,0,90,2*a,s],[a,0,90,2*a,s],[0,a,0,2*a,s],[-3*a/2,-a,0,a,s],[3*a/2,-a,0,a,s]]
Asim = 'Z'
Cont = [0,1,0,0,4,'2 3 5',6]
#CDT([L,Ltot,Asim,Cont])



'''
L    = []
Ltot = 
Asim = 'Z'
Cont = []
'''

'''
D={}
D[2406113] = [[0,a,90,2*a,s],[a/2,0,0,a,s]]
D[2406112] = [[R,R/2,90,R,s],[0,0,'C',R,s,0,180]]
D[911124]  = [[2*a,a/2,0,4*a,a],[3*a/2,3*a,90,4*a,a]]
D[1201123] = [[0,a,90,2*a,s],[a,0,0,4*a,s]]
D[2410142] = [[3*a/2,2*a,0,a,s],[2*a,3*a/2,90,a,s],[a,a,0,2*a,s],[0,a/2,90,a,s],[a/2,0,0,a,s]]
D[3010152] = [[7*a/2,2*a,0,a,s],[4*a,3*a/2,90,a,s],[2*a,a,0,4*a,s],[0,a/2,90,a,s],[a/2,0,0,a,s]]
D[2910162] = [[a,0,0,2*a,2*s],[2*a,a/2,90,a,s]]
D[1806142] = [[-a,a,0,2*a,s],[0,0,'C',a,s,90,270],[-a,-a,0,2*a,s]]
D[901142]  = [[-3*a/2,a/2,90,a,s],[-a,0,0,a,s],[-a/2,a/2,90,a,s],[-a/4,a,0,a/2,s]]
D[1401162] = [[2*a,a/2,90,a,s],[3*a/2,0,0,a,s],[a/2,0,0,a,s],[0,0,'C',a,2*s,0,90]]
D[1601162] = [[2*a,a/2,90,a,s],[3*a/2,0,0,a,s],[a/2,0,0,a,s],[0,0,'C',a,2*s,0,90]]
D[1207122] = [[-a/2,0,0,a,s],[0,0,'C',a,s,180,270]]
D[202112]  = [[3*R/(2**(3/2)),R/(2**(3/2)),135,R,s ],[0,0,'C',R,s,45,180]] #https://elearning.uniroma1.it/pluginfile.php/258860/mod_resource/content/2/02.02.2011%20es.%202.pdf
D[1402123] = [[-3*a/2,0,0,a,s],[-2*a,-a,90,2*a,s],[-2*a,-5*a/2,90,a,s],[-a,-a,45,2**(3/2)*a,s]] #FUNZIONA (credo, anche se non sembra). Mias diverso di poco, CT uguale se correggi fleres (credo)
D[1806122] = [[5*a/(2**(5/2)),3*a/(2**(5/2)),-45,a/2,s],[a/(2**(3/2)),a/(2**(3/2)),45,a,s]] #NON FUNZIONA  ##18-06-12 (mias(L) dà un valore molto diverso da quello di fleres, che però lo calcola due volte con due valori diversi...)                                                                                        #L = [[a/4,a,0,a/2,s],[0,a/2,90,a,s],[a/2,0,0,a,s],[a,a/4,90,a/2,s]]  ##18-06-12 ###non funzionante (integrare con aste curve). METTERE SOLO META LISTA
D[509193]  = [[5*a/(6*3**(1/2)),a/6,60,2*a/(3**(3/2)),s],[a/3**(3/2),a/3,-60,4*a/(3**(3/2)),s]]
'''

#18-06-14 n.2
#L = [[-a,a,0,2*a,s],[0,0,'C',a,s,90,270],[-a,-a,0,2*a,s]]





