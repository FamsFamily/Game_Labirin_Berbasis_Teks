import time

room = {
    'Mulai': {'rooms': ['1'], 'items':[]},
    '1': {'rooms': ['Mulai','2'], 'items':[]},
    '2': {'rooms': ['1','3','4'], 'items':[]},
    '3': {'rooms': ['2'], 'items':['dead']},
    '4': {'rooms': ['5','6'], 'items': []},
    '5': {'rooms': ['4'], 'items':['key']},
    '6': {'rooms': ['4','7'], 'items':[]},
    '7': {'rooms': ['6','8','10'], 'items':[]},
    '8': {'rooms': ['7','9'], 'items':['key']},
    '9': {'rooms': ['8'], 'items': []},
    '10': {'rooms': ['7','11'], 'items':[]},
    '11': {'rooms': ['10','12'], 'items':[]},
    '12': {'rooms': ['11','Keluar'], 'items':[]},
    'Keluar': {'rooms':['12'], 'items':[]}
}

print('GAME LABIRIN BERBASIS TEKS')
print('Hati-hati, ada jebakan! Jangan lupa, temukan 2 kunci!')
ruangan = 'Mulai'
kunci = 0
while True:
    print('============================')
    print('Anda ada di sebuah ruangan', ruangan)
    print('Berikut adalah neighbouring rooms yang bisa Anda pilih:', room[ruangan]['rooms'])
    new_room = input('Ruangan apa yang Anda pilih?')
    if new_room in room[ruangan]['rooms']:
        if new_room == '3':
            ruangan = 'Mulai'
            print('Anda mati dan mengulang dari awal!')
        else:
            ruangan = new_room
        if room[ruangan]['items'] == ['key']:
            kunci = kunci + 1
            sementara = room[ruangan]['rooms']
            room[ruangan] = {'rooms':sementara,'items':[]}
            print('Selamat! Anda menemukan kunci!!!')
        if ruangan == 'Keluar' and kunci == 2:
            break
    else:
        print("Ruangan yang Anda pilih tidak ada di dalam pilihan!")
print("Selamat! Anda berhasil keluar!!!")
