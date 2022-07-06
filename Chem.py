import random

acak = random.randint(1, 10)
peluang = 8
while peluang > 0:
    data = int(input("masukkan angka tebakan: "))
    if data > acak: 
        peluang -= 1
        print("angka tebakan nilainya lebih kecil")
        print(f"tersisa {peluang} kesempatan lagi")
    
    if data < acak:
        peluang -= 1
        print("angka tebakan nilainya lebih besar")
        print(f"tersisa {peluang} kesempatan lagi")

    if data == acak:
        peluang -= 1
        print("selamat tebakan kamu benar")
        break

    if peluang == 0:
        print("kesempatanmu telah habis, kamu kalah")
        print(f"angka tebakan adalah {peluang} ")

