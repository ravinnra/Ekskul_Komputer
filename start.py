# VARIABEL
nama = "Ravindra" # string
umur = 15 # integer
lakilaki = True # boolean (True/False)
tinggi = 170.5 # float

daftarNama = ["Ravindra","Rabbani","Pradiptha"]

kalimat = "Nama saya " + nama + ". Umur saya " + str(umur) + " tahun. "
if not lakilaki:
    print("saya perempuan")
else:
    print("saya laki-laki")
    

print(daftarNama)

panjang = len(daftarNama)
 
daftarNama.append("Tambahan")

print(daftarNama[3])

#if else
n = 9
if n < 10:
    print("n adalah satuan")
else:
    print("n bukan satuan")

#if else if
b = -10
if b < 0:
    print("b bukan negatif, b adalah " + str(b))
elif b < 10:
    print("b adalah satuan")
else: 
    print("b lebih dari atau sama dengan 10")

# PERULANGAN
# for loop
i = 0
for nama in daftarNama:
    i += 1
    print(str(i)+ "==" + nama)