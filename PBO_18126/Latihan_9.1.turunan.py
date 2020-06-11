#INHERITANCE(TURUNAN)
class Mahasiswa:
    nama=""
    __kelas=""
    jurusan=""

    def __init__(self,nama,kelas,jurusan):
        self.nama=nama
        self.__kelas=kelas
        self.jurusan=jurusan

    def tampil(self):
        print("nama      : ",self.nama)
        print("kelas     : ",self.__kelas)
        print("jurusan   : ",self.jurusan)
        print("========================================================")
#tambahan class baru (turunan dari class mahasiswa)
class Krs(Mahasiswa):
    
  def __init__(self,nama,kelas,jurusan,semester):
    super().__init__(nama,kelas,jurusan)
    self.semester=semester

  def matakuliah(self):
    matakuliah=[]
    tanya=input("apakah anda ingin menginput mata kuliah ya|tidak? ")
    if tanya=="ya":
        a=input("silahkan masukan mata kuliah : ")
        matakuliah.append(a)
        print("matakuliah berhasil di tambahkan ")
        print("matakuliah yang diambil = ",matakuliah)
    else:
        print("anda tidak menginput mata kuliah")

#objek
siswa1=Mahasiswa("ira","3","sistem informasi")
siswa2=Krs("humaira","3","jaringan","semester 4")

#fungsi tampil
print("tampil data siswa I",)
siswa1.tampil()
print("tampil data siswa II",)
siswa2.tampil()

#atribut baru pada class krs : semester
print("semester:",siswa2.semester)
siswa2.matakuliah()