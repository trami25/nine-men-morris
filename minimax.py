from stanje2 import *
class Igra(object):
    def __init__(self):
        __slots__ = ['_trenutno_stanje', '_na_redu']
        
        self._trenutno_stanje=None
        self._na_redu='B'
        self.zapocni_igru()

    def zapocni_igru(self):
        self._trenutno_stanje= Stanje()
        self._na_redu='B'
    
    def igraj_druga_faza(self):
        while True:
            while not self._trenutno_stanje.zavrseno(self._na_redu):
                print(self._trenutno_stanje)
                if self._na_redu=='B':
                    print('Na potezu je ',self._na_redu)
                    print('Upisite koordinatu onog mesta sa kojeg biste pomerili pijuna!')
                    x=input('Unesite koordinatu po x osi: ')
                    y=input('Unesite koordinatu po y osi: ')
                    while not self._trenutno_stanje.x_check(x) or not self._trenutno_stanje.y_check(y) or not self._trenutno_stanje.validno_mesto1(x,y,self._na_redu):
                            print('Niste uneli dobre podatke! Probajte ponovo!')
                            x=input('Unesite koordinatu po x osi: ')
                            y=input('Unesite koordinatu po y osi: ')
                    
                    koord1=x+y
                    print('Upisite koordinatu onog mesta na koje biste pomerili pijuna!')
                    x=input('Unesite koordinatu po x osi: ').upper()
                    y=input('Unesite koordinatu po y osi: ')
                    while not self._trenutno_stanje.x_check(x) or not self._trenutno_stanje.y_check(y) or not self._trenutno_stanje.validno_mesto2(koord1,x,y):
                            print('Niste uneli dobre podatke! Probajte ponovo!')
                            x=input('Unesite koordinatu po x osi: ')
                            y=input('Unesite koordinatu po y osi: ')
                    
                    koord2=x+y
                    self._trenutno_stanje.pomeranje(koord1,koord2)
                    print('Pijun je pomeren sa mesta',koord1,'na mesto',koord2)
                    if self._trenutno_stanje.napravljena_mica(koord2):
                            self._trenutno_stanje.oduzmi(self._na_redu)
                    self._na_redu='W'
                    
                    

                else:
                    vrednost,nova_tabla=self._trenutno_stanje.minimax1(self._trenutno_stanje.daj_tablu(),3,self._na_redu,-2000,2000)
                    self._trenutno_stanje.daj_tablu(nova_tabla)
                    self._na_redu='B'
            return self._na_redu
    
    def igraj_prva_faza(self,b=9,w=9):
        while True:
            while b>0 and w>0:
                print(self._trenutno_stanje)
                if self._na_redu=='B':
                    print('Na potezu je ',self._na_redu)
                    x=input('Unesite koordinatu po x osi: ').upper()
                    y=input('Unesite koordinatu po y osi: ')
                    while not self._trenutno_stanje.x_check(x) or not self._trenutno_stanje.y_check(y):
                        print('Niste uneli dobre podatke! Probajte ponovo!')
                        x=input('Unesite koordinatu po x osi: ').upper()
                        y=input('Unesite koordinatu po y osi: ')
                    koordinata=x+y

                    if self._trenutno_stanje.validno(koordinata):
                        self._trenutno_stanje.postavi_vrednost(koordinata, self._na_redu)
                        b-=1
                        if self._trenutno_stanje.napravljena_mica(koordinata):
                                self._trenutno_stanje.oduzmi(self._na_redu)
                        print('Preostalo figurica: ',b)
                        self._na_redu = 'W'
                        
                        
                    else:
                        print('Na ovom polju postoji pijun ili to mesto na tabeli ne postoji! Probajte ponovo!')
                else:
                    vrednost,nova_tabla=self._trenutno_stanje.minimax1(self._trenutno_stanje.daj_tablu(),3,self._na_redu,-2000,2000)
                    self._trenutno_stanje.daj_tablu(nova_tabla)
                    self._na_redu='B'
                    
            return 
            
           
    

 