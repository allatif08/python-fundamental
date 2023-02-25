"""
semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial  : langkah berurutan
2. percabangan : langkah melompat jika kondisi terpenuhi
3. perulangan  : mengulang langakah yang sama berkali - kali selama/sampai kondisi terpenuhi
"""
print('ibu berkata, "pergi ke toko"')
print('Budi menjawab,"baik, apa yang harus saya lakukan di toko ?"')
print('ibu menjawab,"beli satu botol susu, dan jika ada telor beli 6"')
print('maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"jumlah botol susu {jumlah_botol_susu} btl")
print(f"jumlah telur {jumlah_telur} btr")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup ")
    if jumlah_telur == 0:
    print("Budi membeli 1 botol susu")
    else:
    print("Budi membeli 6 botol susu")
else:
    print("budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")

