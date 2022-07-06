from cmath import log, log10


print("Haiiii makasih udah berkunjung di program kami")
print("jadi kami bikin program tentang asam basa, kan yang lagi viral lagu itu wkwkkkw")
print("okeyyy kalian mau apa dulu nih aku kasih option yaaa")
print("1. Hitung konsentrasi asam")
print("2. Hitung konsentrasi basa")
print("3. Hitung PH")
print("4. konsentrasi dari Titrasi asam basa")
n = input("silahkan dipilih,kalkulator kami siap membantu cmiwiwi :3 : ")

while n == "1" :
    H = input("Masukkan larutan asam: (Asam lemah/Asam kuat) ")
    if H == "Asam Kuat" :
            Va = int (input("masukkan valensi asam: "))
            Cm = int (input("masukkan konsentrasi molar asam kuat: "))
            print("[H+]= Valensi asam x Cm  (Cm : konsentrasi molar asam)")
            hasil= Va * Cm 
            print("hasilnya adalah: ", Va, "x", Cm, "=", hasil )
    else :
            Ka = int (input("masukkan nilai Ka: "))
            Cm = int (input("masukkan nilai konsentrasi molar: "))
            print("[H+]= √ka.cm ")
            hasil= (Ka * Cm)**0.5
            print("hasilnya adalah: ", "√", Ka, "x", Cm, "=", hasil )
# ini adalah commant  
while n == "2" :
    A = input("Basa kuat/Basa lemah: ")
    if A == "Basa kuat" :
        Vb = int (input("masukkan valensi basa: "))
        Cm = int (input("masukkan konsentrasi molar basa kuat: "))
        print("[H+]= Valensi basa x Cm  (Cm : konsentrasi molar basa)")
        hasil= Vb * Cm 
        print("hasilnya adalah: ", Vb, "x", Cm, "=", hasil )
    else :
        Kb = int (input("masukkan nilai Kb: "))
        Cm = int (input("masukkan nilai konsentrasi molar: "))
        print("[OH-]= √kb.cm ")
        hasil= (Ka * Cm)**0.5
        print("hasilnya adalah: ", "√", Kb, "x", Cm, "=", hasil )
# commant multiplane
while n == "3" :
    S = input("hitung pH dari [H+] / [OH-] : ([H+] / [OH-]):  ")
    u = input("masukkan larutan: ")
    if S == "[H+]" :
        pH = int (input("masukkan konsentrasi larutan: "))
        print("pH = -log[H+]")
        hasil= -log10(pH)
        print("maka hasil pH dari larutan", u,  "adalah", hasil )
    else :
        POH = int(input("Masukkan konsentrasi [OH-]: "))
        print("PH = PW - POH")
        hasil= -log10(POH)
        print("PH=Pw-POH (dengan pw=14")
        hasil1= 14 - hasil 
        print("maka hasil dari PH larutan basa adalah", hasil1)
# ini dikosongin ajaa heheh
while n == "4" :
    El = input(" Mau mencari konsentrasi apa?: (asam/basa")
    if El == "asam" :
        N = int (input("masukkan volume asam: "))
        M = int (input("masukkan konsentasi basa: "))
        D = int (input("Masukkan volume basa: "))
        print("M1.V1 = M2.V2")
        hasil = (M * D) / N
        print("maka hasil konsentrasi asam adalah", hasil )
    else : 
        Q = int (input("masukkan konsentrasi asam: "))
        T = int (input("masukkan volume asam: "))
        Y = int (input("masukkan volume basa: "))
 
    break
