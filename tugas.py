# ===========tugas gret nilai=============
print("==================================")
print("--SELAMAT DATANG DI GREADE NILAI--")
print("==================================")
nama=input("Masukkan nama anda : ")
nim=input("Masukkan NIM anda : ")
absen=int(input("Masukkan nilai absen anda : "))
uts=int(input("Masukkan nilai uts anda : "))
uas=int(input("Masukkan nilai uas anda : "))
jumlah=absen+uts+uas
rata=jumlah/3
nilai=60
print("----------------------------------------------")
print("|    NAMA                     : ",nama)
print("|    NIM                      : ",nim)
print("|    Nilai absen anda         : ",absen)
print("|    Nilai UTS anda           : ",uts)
print("|    Nilai UAS anda           : ",uas)
print("|    Jumlah nilai keseluruhan : ",jumlah)
print("|    Nilai Rata-rata anda     : ",rata)
print("KETERANGAN : ")
if rata >= 90 and rata <= 100:
    print("NILAI ANDA DI GREADE A")
elif rata >= 80 and rata <=89:
    print("NILAI ANDA DI GREADE B")
elif rata >= 70 and rata <=79:
    print("NILAI ANDA DI GREADE C")
elif rata >= 50 and rata <=69:
    print("NILAI ANDA DI GREADE D")
elif rata <= 49 and rata >=0:
    print("NILAI ANDA DI GREADE E")
else:
    print("NILAI ANDA TIDAK TERDAFTAR DI DALAM GREADE NILAI")
print("----------------------------------------------")


