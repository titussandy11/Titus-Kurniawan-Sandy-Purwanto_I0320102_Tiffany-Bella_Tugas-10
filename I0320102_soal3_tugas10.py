print('SELAMAT DATANG DI PROGRAM INPUT BIODATA')
print('===============================')

#input dari user
nama = input('Nama : ')
kota_asal = input('asal : ')
usia = input('usia : ')

#format teks
teks = 'Nama: {}\nasal: {}\nusia: {}'.format(nama, kota_asal, usia)

#buka file
file_bio = open('bio.txt', 'a')

#tulis file
file_bio.write(teks)

#tutup file
file_bio.close()
