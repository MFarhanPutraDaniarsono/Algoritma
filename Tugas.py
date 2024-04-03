print('Penerimaan PKH')
nama= str(input('masukan nama:'))
nik= int(input('masukan nik:'))
kategori_keluarga= str(input('kategori keluarga(miskin/tidak): '))
bantuan_sosial= str(input('bantuan sosial(tidakmenerima/menerima): '))
status_anak= str(input('status anak(sekolah/tidak): '))
penerima_bnpt=str(input("penerimaan bnpt/tidak: "))
if kategori_keluarga=='miskin' and bantuan_sosial=='tidakmenerima' and status_anak=='sekolah' and penerima_bnpt=='tidak':
    print('selamat anda terpilih')
else:
    print('maaf tidak terpilih')