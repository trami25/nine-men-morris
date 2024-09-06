from email.errors import MultipartConversionError
from minimax import Igra
from hm import ChainedHashMap
from copy import deepcopy

pozicija=ChainedHashMap(24)
for i in range(1,25):
    pozicija[i]='x'
igra=Igra()
heur_mice=[[pozicija[1],pozicija[2],pozicija[3]],
            [pozicija[1],pozicija[10],pozicija[22]],
            [pozicija[2],pozicija[5],pozicija[8]],
            [pozicija[3],pozicija[15],pozicija[24]],
            [pozicija[4],pozicija[5],pozicija[6]],
            [pozicija[4],pozicija[11],pozicija[19]],
            [pozicija[6],pozicija[14],pozicija[21]],
            [pozicija[7],pozicija[8],pozicija[9]],
            [pozicija[7],pozicija[12],pozicija[16]],
            [pozicija[9],pozicija[13],pozicija[18]],
            [pozicija[10],pozicija[11],pozicija[12]],
            [pozicija[13],pozicija[14],pozicija[15]],
            [pozicija[16],pozicija[17],pozicija[18]],
            [pozicija[19],pozicija[20],pozicija[21]],
            [pozicija[22],pozicija[23],pozicija[24]],
            [pozicija[17],pozicija[20],pozicija[23]]]

heur2_mice=[[pozicija[1],pozicija[2],pozicija[3],pozicija[10],pozicija[22]],
            [pozicija[1],pozicija[2],pozicija[3],pozicija[15],pozicija[24]],            
            [pozicija[1],pozicija[22],pozicija[23],pozicija[10],pozicija[24]],
            [pozicija[22],pozicija[23],pozicija[3],pozicija[15],pozicija[24]],
            [pozicija[4],pozicija[5],pozicija[6],pozicija[11],pozicija[19]],
            [pozicija[4],pozicija[5],pozicija[6],pozicija[14],pozicija[21]],
            [pozicija[4],pozicija[11],pozicija[19],pozicija[20],pozicija[21]],
            [pozicija[6],pozicija[14],pozicija[21],pozicija[19],pozicija[20]],
            [pozicija[7],pozicija[8],pozicija[9],pozicija[13],pozicija[18]],
            [pozicija[7],pozicija[8],pozicija[9],pozicija[12],pozicija[16]],
            [pozicija[7],pozicija[12],pozicija[16],pozicija[17],pozicija[18]],
            [pozicija[9],pozicija[13],pozicija[18],pozicija[16],pozicija[17]],
]
dozvoljena_mesta={
    1:[2,7],
    2:[1,3,5],
    3:[2,15],
    4:[5,11],
    5:[2,4,6,8],
    6:[5,14],
    7:[8,12],
    8:[5,7,9],
    9:[8,13],
    10:[1,11,22],
    11:[4,10,12,19],
    12:[7,11,16],
    13:[9,14,18],
    14:[6,13,15,21],
    15:[3,14,24],
    16:[12,17],
    17:[16,18,20],
    18:[13,17],
    19:[11,20],
    20:[17,19,21,23],
    21:[14,20],
    22:[10,23],
    23:[20,22,24],
    24:[15,23]
}
x_1=['A','B','C','D','E','F','G']
y_1=['1','2','3','4','5','6','7']
koords=['A1','A4','A7','B2','B4','B6','C3','C4','C5','D1','D2','D3','D5','D6','D7','E3','E4','E5','F2','F4','F6','G1','G4','G7']
koordinate={
    'A1':1,
    'D1':2,
    'G1':3,
    'B2':4,
    'D2':5,
    'F2':6,
    'C3':7,
    'D3':8,
    'E3':9,
    'A4':10,
    'B4':11,
    'C4':12,
    'E4':13,
    'F4':14,
    'G4':15,
    'C5':16,
    'D5':17,
    'E5':18,
    'B6':19,
    'D6':20,
    'F6':21,
    'A7':22,
    'D7':23,
    'G7':24
}


    

class Stanje(object):
    def __init__(self):
            self._tabla=[]
    
    def x_check(self,x):
        for i in x_1:
            if i==x:
                return True
        return False

    def y_check(self,y):
        for i in y_1:
            if i==y:
                return True
        return False

    def validno(self,koordinata):
        if koordinata in koords: 
            broj=koordinate[koordinata]
            if pozicija[broj]=='x':
                return True
            
        return False        
    
    def broj_fig(self):
        skup=[]
        for i in range(1,25):
            if pozicija[i]!='x':
                skup.append(pozicija[i])
        return skup

    def broj_figurica(self,pozicija, vrednost):
        c=0
        ukupno=[]
        for i in pozicija:
            if pozicija[i]==vrednost:
               c+=1
               ukupno.append(i)
        return ukupno,c


    def oduzmi(self,igrac):
        while True:
            print('Koju figuru biste sklonili?: ')
            x=input('X koordinata: ').upper()
            y=input('Y koordinata: ')
            while not self.x_check or not self.y_check:
                print('Niste uneli dobre podatke! Probajte ponovo!')
                x=input('X koordinata: ').upper()
                y=input('Y koordinata: ')
            koordinata=x+y
            broj=koordinate[koordinata]
            if igrac=='B':
                if pozicija[broj] =='W'  and not self.napravljena_mica(koordinata) or\
                (self.napravljena_mica(koordinata) and self.broj_figurica(pozicija, 'W') == 3):
                        pozicija[broj] = 'x'
                        break
                else:
                    print('Ne mozete ukloniti ovog pijuna!')
            
            elif igrac=='W':
                
                if pozicija[broj] =='B'  and not self.napravljena_mica(koordinata) or\
                (self.napravljena_mica(koordinata) and self.broj_figurica(pozicija, 'B') == 3):
                        pozicija[broj] = 'x'
                        break
                else:
                    print('Ne mozete ukloniti ovog pijuna!')
            else:
                print('Greska u sistemu!')

    def postavi_vrednost(self,koordinata,vrednost):
        broj=koordinate[koordinata]
        pozicija[broj]=vrednost

    def provera_mica(self,p, pozicija,p1,p2):
        if (pozicija[p1] == p and pozicija[p2] == p):
            return True
        else:
            return False

    def napravljena_mica(self,koordinata):
            broj=koordinate[koordinata]
            p = pozicija[broj]
    
            if p != 'x':
                return self.provera(broj, pozicija, p)
            else:
                return False
            
    def provera(self,broj, pozicija,p):
        mice = [
        (self.provera_mica(p, pozicija,2,3) or self.provera_mica(p, pozicija,10,22)),
        (self.provera_mica(p, pozicija,1,3) or self.provera_mica(p, pozicija,5,8)),
        (self.provera_mica(p, pozicija,1,2) or self.provera_mica(p, pozicija,15,24)),
        (self.provera_mica(p, pozicija,5,6) or self.provera_mica(p, pozicija,11,19)),
        (self.provera_mica(p, pozicija,4,6) or self.provera_mica(p, pozicija,2,8)),
        (self.provera_mica(p, pozicija,4,5) or self.provera_mica(p, pozicija,14,21)),
        (self.provera_mica(p, pozicija,8,9) or self.provera_mica(p, pozicija,12,16)),
        (self.provera_mica(p, pozicija,7,9) or self.provera_mica(p, pozicija,2,5)),
        (self.provera_mica(p, pozicija,7,8) or self.provera_mica(p, pozicija,13,18)),
        (self.provera_mica(p, pozicija,1,22) or self.provera_mica(p, pozicija,11,12)),
        (self.provera_mica(p, pozicija,10,12) or self.provera_mica(p, pozicija,4,19)),
        (self.provera_mica(p, pozicija,10,11) or self.provera_mica(p, pozicija,7,16)),
        (self.provera_mica(p, pozicija,14,15) or self.provera_mica(p, pozicija,9,18)),
        (self.provera_mica(p, pozicija,13,15) or self.provera_mica(p, pozicija,6,21)),
        (self.provera_mica(p, pozicija,13,14) or self.provera_mica(p, pozicija,3,24)),
        (self.provera_mica(p, pozicija,17,18) or self.provera_mica(p, pozicija,12,4)),
        (self.provera_mica(p, pozicija,16,18) or self.provera_mica(p, pozicija,20,23)),
        (self.provera_mica(p, pozicija,16,17) or self.provera_mica(p, pozicija,9,13)),
        (self.provera_mica(p, pozicija,20,21) or self.provera_mica(p, pozicija,4,11)),
        (self.provera_mica(p, pozicija,19,21) or self.provera_mica(p, pozicija,17,23)),
        (self.provera_mica(p, pozicija,19,20) or self.provera_mica(p, pozicija,6,14)),
        (self.provera_mica(p, pozicija,23,24) or self.provera_mica(p, pozicija,1,10)),
        (self.provera_mica(p, pozicija,22,24) or self.provera_mica(p, pozicija,17,20)),
        (self.provera_mica(p, pozicija,22,23) or self.provera_mica(p, pozicija,3,15))
    ]

        return mice[broj-1]

    def validno_mesto1(self,x,y,igrac):
        koordinata=x+y
        for k in koords:
            if k==koordinata:
                broj=koordinate[koordinata]
                if pozicija[broj]==igrac:
                    return True
        return False

    def validno_mesto2(self,koord1,x,y):
        koordinata=x+y
        for k in koords:
            if k==koordinata:
                broj1=koordinate[koord1]
                broj2=koordinate[koordinata]
                for i in dozvoljena_mesta[broj1]:
                    if i==broj2 and pozicija[broj2]=='x':
                        return True
        return False

    def pomeranje(self,k1,k2):
        broj1=koordinate[k1]
        broj2=koordinate[k2]
        pozicija[broj2]=pozicija[broj1]
        pozicija[broj1]='x'

    def blokirano(self,igrac):
        indexi=[]
        for i in range(1,25):
            if igrac==pozicija[i]:
                indexi.append(i)
        
        neblokirani=[]
        for i in indexi:
            for a in dozvoljena_mesta[i]:
                if pozicija[a]=='x':
                        neblokirani.append(a)
    
        if len(neblokirani)==0:
            return True
        else:
            return False

                        
    def zavrseno(self,igrac):
        if self.broj_figurica(pozicija,igrac)<3 or self.blokirano(igrac):
            return True
        return False



    def ralika_broja_figurica(self):
        bp=0
        wp=0
        for i in pozicija:
            if pozicija[i]=='B':
                bp+=1
            elif pozicija[i]=='W':
                wp+=0
        return bp-wp

    def razlika_mica(self,igrac):
        bp=0
        wp=0
        if self.napravljena_mica(igrac):
            if igrac=='B':
                bp+=1
            else:
                wp+=1
        return bp-wp
    
    def razlika_broja_mica(self):
        bp=0
        wp=0
        for red in heur_mice:
            if red[0]==red[1] and red[0]==red[2] and red[0]!='x':
                if red[0]=='B':
                    bp+=1
                else:
                    wp+=1
        return bp-wp

    def razlika_blokiranih(self):
        bp=0
        wp=0
        k=0
        for i in range(1,25):
            if pozicija[i]=='B':
                for a in dozvoljena_mesta[i]:
                    if pozicija[a]!='W':
                        k+=1
                if k==0:
                    wp+=1
            elif pozicija[i]=='W':
                for a in dozvoljena_mesta[i]:
                    if pozicija[a]!='B':
                        k+=1
                if k==0:
                    bp+=1
        return wp-bp

    def razlika_2_konf(self):
        for red in heur_mice:
            wp=0
            bp=0
            if red[0]==red[1] or red[0]==red[2] or red[2]==red[1]:
                if red[0]=='B'or red[1]=='B' or red[2]=='B':
                    bp+=1
                elif red[0]=='W'or red[1]=='W' or red[2]=='W':
                    wp+=1
            return bp-wp

    def razlika_3_konf(self):
        bp=0
        wp=0
        for i in range(1,25):
            if pozicija[i]=='B':
                if len (dozvoljena_mesta[i])==2:
                   if pozicija(dozvoljena_mesta[i][0])=='B' and pozicija(dozvoljena_mesta[i][1])=='B':
                        bp+=1
            elif pozicija[i]=='W':
                if len (dozvoljena_mesta[i])==2:
                   if pozicija(dozvoljena_mesta[i][0])=='W' and pozicija(dozvoljena_mesta[i][1])=='W':
                        wp+=1
        return bp-wp

    def razlika_broja_duplih_mica(self):
        bp=0
        wp=0
        for red in heur2_mice:
            if red[0]==red[1] and red[0]==red[2] and red[0]==red[3] and red[0]==red[4] and red[0]!='x':
                if red[0]=='B':
                    bp+=1
                else:
                    wp+=1
        return bp-wp

    def pobednicki(self,igrac):
        bp=0
        wp=0
        if self.zavrseno() and igrac=='W':
            bp+=1
        else:
            wp+=1
        return bp-wp
            

    def heuristicka_funkcija1(self,igrac):
        heurist1= 18 * self.razlika_mica(igrac) +\
            26 * self.razlika_broja_mica() +\
            1 * self.razlika_blokiranih() +\
            9 * self.razlika_broja_mica() +\
            10 * self.razlika_2_konf() +\
            7 * self.razlika_3_konf()
        return heurist1



    def heuristicka_funkcija2(self,igrac):
        heurist2= 14 *self.razlika_mica(igrac)+\
                  43 *self.razlika_broja_mica()+\
                  10 *self.razlika_blokiranih()+\
                  11 *self.razlika_broja_mica() +\
                  8 *self.razlika_broja_duplih_mica()+\
                  1086 *self.pobednicki(igrac)
        return heurist2

    def minimax1(self,tabla,dubina,max_igrac,alfa,beta):
        if dubina==0:
            self.heuristicka_funkcija1(igra._na_redu)
        if max_igrac:
            maxE=float('-inf')
            najbolji_potez=None
            for potez in self.daj_sve_poteze(tabla,'W'):
                eval=self.minimax1(potez,dubina-1,False)[0]
                maxE=max(maxE,eval)
                if maxE==eval:
                    najbolji_potez=potez
                if maxE >= beta:
                    return maxE,najbolji_potez

                if maxE > alfa:
                    alfa = maxE
            return maxE,najbolji_potez
        else:
            minE=float('inf')
            najbolji_potez=None
            for potez in self.daj_sve_poteze(tabla,'W'):
                eval=self.minimax1(potez,dubina-1,True)[0]
                minE=min(minE,eval)
                if minE==eval:
                    najbolji_potez=potez
                if minE<=alfa:
                    return minE,najbolji_potez
                if minE<beta:
                    beta=minE

            return minE,najbolji_potez


    def daj_sve_poteze(self,tabla,igrac):
        potezi=[]
        for poz in self.broj_fig():
            dozv_mesta=dozvoljena_mesta[pozicija]
            trenutna_tabla=deepcopy(tabla)
            nova_tabla=self.simuliraj(tabla,trenutna_tabla,poz)
            potezi.append(nova_tabla)
        return potezi


    def simuliraj(self,pozicija,trenutna_tabela,poz):
        self.pomeranje()

    def daj_tablu(self):
        return self.ispis_table()

    def ispis_table(self):
        print(pozicija[1]+"-------------------"+pozicija[2]+"-------------------"+pozicija[3]+"     1")
        print("|                   |                   |")
        print("|       "+pozicija[4]+"-----------"+pozicija[5]+"-----------"+pozicija[6]+"       |     2")
        print("|       |           |           |       |")
        print("|       |      "+pozicija[7]+ "----" +pozicija[8] + "----" +pozicija[9]+"      |       |     3")
        print("|       |      |         |      |       |")
        print(pozicija[10]+"-------"+pozicija[11]+"------"+pozicija[12]+"         "+pozicija[13]+"------"+pozicija[14]+"-------"+pozicija[15]+"     4")
        print("|       |      |         |      |       |")
        print("|       |      "+pozicija[16]+ "----" +pozicija[17] + "----" +pozicija[18]+"      |       |     5")
        print("|       |           |           |       |")
        print("|       "+pozicija[19]+"-----------"+pozicija[20]+"-----------"+pozicija[21]+"       |     6")
        print("|                   |                   |")
        print(pozicija[22]+"-------------------"+pozicija[23]+"-------------------"+pozicija[24]+"     7")
        print("\n")
        print("A       B      C    D     E     F       G")
 


    def __repr__(self):
        y='Mozes ti to!'        
        print(pozicija[1]+"-------------------"+pozicija[2]+"-------------------"+pozicija[3]+"     1")
        print("|                   |                   |")
        print("|       "+pozicija[4]+"-----------"+pozicija[5]+"-----------"+pozicija[6]+"       |     2")
        print("|       |           |           |       |")
        print("|       |      "+pozicija[7]+ "----" +pozicija[8] + "----" +pozicija[9]+"      |       |     3")
        print("|       |      |         |      |       |")
        print(pozicija[10]+"-------"+pozicija[11]+"------"+pozicija[12]+"         "+pozicija[13]+"------"+pozicija[14]+"-------"+pozicija[15]+"     4")
        print("|       |      |         |      |       |")
        print("|       |      "+pozicija[16]+ "----" +pozicija[17] + "----" +pozicija[18]+"      |       |     5")
        print("|       |           |           |       |")
        print("|       "+pozicija[19]+"-----------"+pozicija[20]+"-----------"+pozicija[21]+"       |     6")
        print("|                   |                   |")
        print(pozicija[22]+"-------------------"+pozicija[23]+"-------------------"+pozicija[24]+"     7")
        print("\n")
        print("A       B      C    D     E     F       G")
        return y 