from minimax import Igra

def main():
    b=9
    w=9
    print('DOBRODOSLI U IGRU MICE! UZIVAJTE U IGRI!')
    print()
    igra=Igra()
    igra.igraj_prva_faza(b,w)
    pobednik=igra.igraj_druga_faza()
    print('IGRA JE GOTOVA')
    if pobednik=='B':
        print('PORAZ!')
    else:
        print('POBEDA!')
    exit(0)
        

if __name__=='__main__':
    main()