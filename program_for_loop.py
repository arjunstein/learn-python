# menggunakan for loop, list, range

data = int(input("Masukkan data yang ingin dihitung: "))

nama = []
umur = []

for i in range(0, data):
    print(f"Data ke- {i}")
    input_nama = input("Nama: ") 
    input_umur = int(input("Umur: "))
    
    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur} tahun.")