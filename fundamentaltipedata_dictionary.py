"""
tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""
kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\nData ini dikirimkan oleh server gojek untuk memberikan info di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-12-07',
    'driver_list': [
        {'nama': 'eko', 'jarak': 10},
        {'nama': 'dwi', 'jarak': 30},
        {'nama': 'tri', 'jarak': 100},
        {'nama': 'catur', 'jarak': 1000}]
}
print(data_dari_server_gojek)
print(f"\nDriver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #2 {data_dari_server_gojek['driver_list'][1]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
