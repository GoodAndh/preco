class Hewan:
    def __init__(self,spesies:str,nama:str,umur:int,kelamin) -> None:
        self.spesies=spesies
        self.nama=nama
        self.umur=umur
        self.__kelamin=kelamin
    def getKelamin(self):
        print(self.__kelamin)
    def setKelaminBaru(self,kelamin):
        self.__kelamin=kelamin
    def suara(self):
        print("hewan bersuara")

class Ayam(Hewan):
    def __init__(self,nama:str,umur:int):
        super().__init__("ayam",nama,umur,"laki-laki")
    def suara(self):
        print(f"ayam bersuara kukuruyuk")
class Kucing(Hewan):
    def __init__(self,nama:str,umur:int):
        super().__init__("kucing",nama,umur,"laki-laki")
    def suara(self):
        print(f"kucing bersuara meow meow")
class Anjing(Hewan):
    def __init__(self,nama:str,umur:int):
        super().__init__("anjing",nama,umur,"laki-laki")
    def suara(self):
        print(f"anjing bersuara guk guk guk ")


def cekSuara(hewan:Hewan):
    hewan.suara()

ayam=Ayam("ayam pertama",1)
kucing=Kucing("kucing nedy",2)
anjing=Anjing("penjaga",1)
# print(kucing.kelamin)
kucing.getKelamin()
# cekSuara(ayam)
# cekSuara(kucing)
# cekSuara(anjing)

# ganggaputra@refactory.id