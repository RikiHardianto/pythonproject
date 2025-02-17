tinggi = int(input('Masukan nilai A (tinggi): '))
alas = int(input('Masukan nilai b (alas): '))
c = int(input('Masukan nilai c: '))

def menu():
    print('1. keliling')
    print('2. luas')
    print('3. keluar')

menu()
option = int(input('Masukan Daftar Yang Ingin Di tuju: '))

while option != 3:
    if option == 1:
        keliling = tinggi + alas + c
        print('Dengan rumus a+b+c. Keliling segitiga siku-siku ini adalah', keliling)
        menu()
        option = int(input('Masukan menu yang dituju: '))

    elif option == 2:
        luas = 0.5 * alas * tinggi
        print('Dengan rumus  ½ x a x t Luas dari Segitiga siku-siku ini adalah', luas)
        menu()
        option = int(input('Masukan menu yang dituju: '))
