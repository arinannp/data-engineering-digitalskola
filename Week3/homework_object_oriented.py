class Karyawan():
    perusahaan = "E-commerce"
    pendapatan = 5000000
    lembur = 250000
    
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
     
    def deskripsi(self):
        print(self.nama, "bekerja di Perusahaan", self.perusahaan, "dengan usia", self.usia, "tahun")
        
    @staticmethod
    def gaji_bersih():
        print("Karyawan Perusahaan", Karyawan.perusahaan)
        print("Memiliki gaji bersih tanpa lembur:", Karyawan.pendapatan)
    
    @classmethod
    def gaji_lembur(cls):
        print("Karyawan Perusahaan", cls.perusahaan)
        print("Memiliki gaji dengan lembur:", cls.pendapatan + cls.lembur)
    
    def summary(self, tambahan_proyek=0):
        print(self.nama, "usia", self.usia, "tahun bekerja di Perusahaan", self.perusahaan)
        print("Memiliki total gaji", self.pendapatan + self.lembur + tambahan_proyek)
       
class dataEngineer(Karyawan):
    pendapatan = 7000000
    lembur = 500000
    
    def __init__(self, nama, usia=27, pendapatan_tambahan=0):
        super().__init__(nama, usia)
        self.pendapatan_tambahan = pendapatan_tambahan
    
    def summary(self, tambahan_proyek=0):
        print(self.nama, "bekerja di Perusahaan", self.perusahaan, "sebagai Data Engineer")
        print("Memiliki total gaji", self.pendapatan + self.lembur + self.pendapatan_tambahan + tambahan_proyek)
    
class dataScientist(Karyawan):
    pendapatan = 7500000
    lembur = 500000
    
    def __init__(self, nama, usia=28, pendapatan_tambahan=0):
        super().__init__(nama, usia)
        self.pendapatan_tambahan = pendapatan_tambahan
    
    def summary(self, tambahan_proyek=0):
        print(self.nama, "bekerja di Perusahaan", self.perusahaan, "sebagai Data Scientist")
        print("Memiliki total gaji", self.pendapatan + self.lembur + self.pendapatan_tambahan + tambahan_proyek)
       

rudi = Karyawan("Rudi", 25)
brando = dataScientist("Brando")
nando = dataEngineer("Nando")                               #Overloading
randi = dataEngineer("Randi", usia=25)                      #Overloading
sandi = dataEngineer("Sandi", pendapatan_tambahan= 1000000) #Overloading

rudi.deskripsi()    #Inheritance
nando.deskripsi()   #Inheritance

rudi.summary()  #Overriding
randi.summary() #Overriding
brando.summary()#Overriding

print(Karyawan.pendapatan)      #ClassAttribute
print(dataEngineer.pendapatan)  #ClassAttribute
print(dataScientist.pendapatan) #ClassAttribute

print(rudi.usia)    #InstanceAttribute
print(randi.usia)   #InstanceAttribute
print(brando.usia)  #InstanceAttribute
