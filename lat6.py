class Kalkulator :
    def __init__ (self,a,b):
        self.a=a
        self.b=b
    def tambah (self):
        return self.a+self.b
    def kurang (self):
        return self.a-self.b
    def kali(self):
        return self.a*self.b
    def bagi (self):
        return self.a/self.b
a = int (input("masukkan bilangan pertama : "))
b = int (input("masukkan bilangan kedua : "))
obj = Kalkulator(a,b)
choice = 1
while choice != 0:
    print ("0. Keluar")
    print ("1. Tambah")
    print ("2. Kurang")
    print ("3. Kali")
    print ("4. Bagi")
    choice = int(input ("Masukkan pilihan (1/2/3/4) : "))
    if choice == 1 :
        print ("Hasil:",obj.tambah())
    elif choice == 2 :
        print ("Hasil:",obj.kurang())
    elif choice == 3 :
        print ("Hasil:",obj.kali())
    elif choice == 4 :
        print ("Hasil:",round(obj.bagi(),2))
    elif choice == 0 :
        print("Anda Sudah Keluar")
    else :
        print("Input Salah" )

print()