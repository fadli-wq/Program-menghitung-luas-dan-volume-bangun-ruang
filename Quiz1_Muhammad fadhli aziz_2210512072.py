from cmath import pi


print('Muhammad fadhli aziz'); print('2210512072')
print('Program menghitung luas dan volume bangun ruang')
print ('1. Kubus\n2. Balok\n3. Bola\n4. Tabung\n5. Kerucut\n6. Limas segitiga\n7. Prisma')
p=int (input('Silahkan pilih bangun ruang yang akan dihitung : '))
if p==1 :
    print('1. luas\n2. volume')
    lv=int (input('Silahkan pilih yang ingin dihitung : '))
    if lv==1 :
        b='Kubus'
        print('\nMenghitung luas',b)
        print('\nRumus mengitung luas',b,'= 6 x sisi^2' )
        s=int (input('\nMasukkan nilai sisi : '))
        l=6*s**2
        print('luas',b,'=',l)
    if lv==2 :
        b='Kubus'
        print ('\nMenghitung volume',b)
        print ('\nRumus menghitung volume',b,'= sisi x sisi x sisi')
        s=int (input('\nMasukkan nilai sisi : '))
        v=s*s*s
        print('volume',b,'=',v)
        
elif p==2 :
    print('1. luas\n2. volume')
    lv=int (input('Silahkan pilih yang ingin dihitung : '))
    if lv==1 :
        b='Balok'
        print('\nMenghitung luas',b)
        print('\nRumus mengitung luas',b,'= 2 x ((p x l) + (l x t) + (p x t))' )
        p=int (input('\nMasukkan nilai panjang : '))
        l=int (input('\nMasukkan nilai lebar : '))
        t=int (input('\nMasukkan nilai tinggi : '))
        L=2*((p*l)+(l*t)+(p*t))
        print('luas',b,'=',L)
    if lv==2 :
        b='Balok'
        print ('\nMenghitung Volume',b)
        print ('\nRumus Menghitung Volume',b,'= panjang x lebar x tinggi')
        p=int (input('\nMasukkan nilai panjang : '))
        l=int (input('\nMasukkan nilai lebar : '))
        t=int (input('\nMasukkan nilai tinggi : '))
        v=p*l*t
        print('volume',b,'=',v)
elif p==3 :
    print('1. luas\n2. volume')
    lv=int (input('Silahkan pilih yang ingin dihitung : '))
    if lv==1 :
        b='Bola'
        print('\nMenghitung luas',b)
        print('\nRumus mengitung luas',b,'= 4 x pi x r^2' )
        r=int (input('\nMasukkan nilai r(jari-jari) : '))
        L=4*pi*r**2
        print('luas',b,'=',L)
    if lv==2 :
        b='Bola'
        print ('\nMenghitung Volume',b)
        print ('\nRumus Menghitung Volume',b,'= 4/3 x pi x r^3')
        r=int (input('\nMasukkan nilai r(jari-jari) : '))
        v=4/3*pi*r**3
        print('volume',b,'=',v)
elif p==4 :
    print('1. luas\n2. volume')
    lv=int (input('Silahkan pilih yang ingin dihitung : '))
    if lv==1 :
        b='Tabung'
        print('\nMenghitung luas',b)
        print('\nRumus mengitung luas',b,'= 2 x pi x r x (r + t)' )
        r=int (input('\nMasukkan nilai r(jari-jari) : '))
        t=int (input('\nMasukkan nilai tinggi : '))
        L=2*pi*r*(r+t)
        print('luas',b,'=',L)
    if lv==2 :
        b='Tabung'
        print ('\nMenghitung Volume',b)
        print ('\nRumus Menghitung Volume',b,'= pi x r^2 x t')
        r=int (input('\nMasukkan nilai r(jari-jari) : '))
        t=int (input('\nMasukkan nilai tinggi : '))
        v=pi*r**2*t
        print('volume',b,'=',v)
elif p==5 :
    print('1. luas\n2. volume')
    lv=int (input('Silahkan pilih yang ingin dihitung : '))
    if lv==1 :
        b='Kerucut'
        print('\nMenghitung luas',b)
        print('\nRumus mengitung luas',b,'= ((pi x r x s) + (pi x r^2))' )
        r=int (input('\nMasukkan nilai r(jari-jari) : '))
        s=int (input('\nMasukkan nilai s(garis pelukis kerucut) : '))
        L=(pi*r*s)+(pi*r**2)
        print('luas',b,'=',L)
    if lv==2 :
        b='Kerucut'
        print ('\nMenghitung Volume',b)
        print ('\nRumus Menghitung Volume',b,'= 1/3 x pi x r^2 x t')
        r=int (input('\nMasukkan nilai r(jari-jari) : '))
        t=int (input('\nMasukkan nilai tinggi : '))
        v=1/3*pi*r**2*t
        print('volume',b,'=',v)
elif p==6 :
    print('1. luas\n2. volume')
    lv=int (input('Silahkan pilih yang ingin dihitung : '))
    if lv==1 :
        b='Limas segitiga'
        print('\nMenghitung luas permukaan',b)
        print('\nRumus mengitung luas permukaan',b,'= luas alas + jumlah luas sisi tegak' )
        la=int (input('\nMasukkan nilai luas alas : '))
        st=int (input('\nMasukkan nilai luas sisi tegak : '))
        L=la+st
        print('luas permukaan',b,'=',L)
    if lv==2 :
        b='Limas segitiga'
        print ('\nMenghitung Volume',b)
        print ('\nRumus Menghitung Volume',b,'= 1/3 x luas alas x tinggi')
        la=int (input('\nMasukkan nilai luas alas : '))
        t=int (input('\nMasukkan nilai tinggi : '))
        v=1/3*la*t
        print('volume',b,'=',v)
elif p==7 :
    print('1. luas\n2. volume')
    lv=int (input('Silahkan pilih yang ingin dihitung : '))
    if lv==1 :
        b='Prisma'
        print('\nMenghitung luas permukaan',b)
        print('\nRumus mengitung luas permukaan',b,'= ((2 x luas alas) + (keliling alas x tinggi))' )
        la=int (input('\nMasukkan nilai luas alas : '))
        ka=int (input('\nMasukkan nilai keliling alas : '))
        t=int (input('\nMasukkan nilai tinggi : '))
        L=2*la+ka*t
        print('luas permukaan',b,'=',L)
    if lv==2 :
        b='Prisma segitiga'
        print ('\nMenghitung Volume',b)
        print ('\nRumus Menghitung Volume',b,'= luas alas x tinggi')
        la=int (input('\nMasukkan nilai luas alas : '))
        t=int (input('\nMasukkan nilai tinggi : '))
        v=la*t
        print('volume',b,'=',v)
else :
    print('Pilihan anda salah!!!')