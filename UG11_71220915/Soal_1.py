print("=======================")
print("Operasi Matematika")
print(" 1. Jumlah [+]")
print(" 2. Kurang [-]")
print(" 3. Kali [*]")
print(" 4. Bagi [/]")
print("=======================")
operasi = input("Pilih operasi (1/2/3/4): ")
print("=======================")
bil_1 = int(input("Masukkan bilangan pertama: "))
bil_2 = int(input("Masukkan bilangan kedua: "))
def jumlah():
    jumlah = bil_1+bil_2
    return jumlah

def kurang():
    kurang = bil_1-bil_2
    return kurang

def kali():
    kali = bil_1*bil_2
    return kali

def bagi():
    bagi = bil_1/bil_2
    return bagi
if operasi == '1' :
    print("Hasil operasi dari ",bil_1,"+",bil_2,"=",jumlah())
elif operasi == '2' :
    print("Hasil operasi dari ",bil_1,"-",bil_2,"=",kurang())
elif operasi == '3' :
    print("Hasil operasi dari ",bil_1,"*",bil_2,"=",kali())
elif operasi == '4' :
    print("Hasil operasi dari ",bil_1,"/",bil_2,"=",bagi())
