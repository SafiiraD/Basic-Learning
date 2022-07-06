Nama = input("Haiii kamu makasih udah mau jadi volunteer. btw tak kenal maka tak sayang. jadi namanya siapa klo boleh tau:")
poin = 0
chance = 3

print("Halo " +Nama, ", siap main game yaa... harus siap dong :v")
print("1...2...3..")
input("(ENTER)")

while chance > 0:
    if poin < 75:
        print("semangattt main nya ntar kalo bener aku kasih permen deh 1 aja wkwkkw")
        print("okey kesempatan mu", chance, "kali kesempatan")
        mulai =input("pertama pahami dulu soalnya (ya/tidak): ")

        if mulai == "ya" :
            poin -= poin
            chance -= 1
            print("Aku ada di siang hari. aku sangat panas. jam berapakah aku? ")
            print("Sin π/2")
            ans1 = input("jawaban: ")
            if ans1 == "1":
                poin += 25
                print("widiiihhh bener dong pinter banget kamu,okeyy poin anda", poin )
                input("(enter)")
            else:
                print("dasar pabo_-. poin mu sisa segini nih", poin)
                input("(enter)")
            print("soal selanjutnya nih, haduhhh buka puasa lama banget yaa guys")
            print("3!")
            ans2 = input("jawaban: ")
            if ans2 == "6":
                poin += 25
                print("semangat sayang :v", poin )
            else:
                print("parah gitu aja salah ihh :(", poin)        
    break
print("udah kelar 2 soal aja, next time jangan join lagi. pusing juga bikin program huft :v")
print("makasih yaa.. semangat kuliahnya. jangan capek2 ya. jaga mata,jaga hati dan jaga pikiran. klo kmu sakit ntar aku sedih soalnya")
