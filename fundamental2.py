#array

anak= ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)
print(f'Hai {anak[1]}!')

for a in anak:
    print(f'Hai {a}')

print('\n')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')