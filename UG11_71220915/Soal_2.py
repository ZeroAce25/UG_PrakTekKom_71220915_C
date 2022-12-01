print("Pemeriksa Kelipatan 9")
bil = int(input("Masukkan Kelipatan 9 yang ingin diperiksa: "))
def kelipatan_9(bil):
    jawab = (bil%9)
    return jawab
if kelipatan_9(bil)== 0:
    print("Benar")
else:
    print("Salah")
