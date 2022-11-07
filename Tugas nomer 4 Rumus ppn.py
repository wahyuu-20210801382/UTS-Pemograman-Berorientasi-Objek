# Kode awal
total_harga = 10000
potongan_harga = 2500
pajak = 0.10 # pajak dalam persen ~ 10%
harga_bayar = 1 - 0.5 # baris pertama
harga_bayar *= total_harga # baris kedua
pajak_bayar = pajak * harga_bayar # baris ketiga
harga_bayar += pajak_bayar # baris ke-4
print("Kode awal - harga_bayar=", harga_bayar)
# Penyederhanaan baris kode dengan menerapkan prioritas operator
total_harga = 10000
potongan_harga = 0.3
harga = int(input("masukkan harga: "))
potongan_harga = 10/100
h_harga = harga + (harga * potongan_harga)
print(f"harga input : {harga}")
print(f"harga : {h_harga}")