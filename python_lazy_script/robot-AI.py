import re
import os,sys,time,getpass
import respon_panjang as long

def pesan_kemungkinan(pesan_user, kata_dikenal, respon_sendiri=False, kata_penting=[]):
    pesan_pasti = 0
    has_kata_penting = True

    # Counts how many katas are present in each predefined pesan
    for kata in pesan_user:
        if kata in kata_dikenal:
            pesan_pasti += 1

    # Calculates the percent of recognised katas in a user pesan
    persentase = float(pesan_pasti) / float(len(kata_dikenal))

    # Checks that the required katas are in the string
    for kata in kata_penting:
        if kata not in pesan_user:
            has_kata_penting = False
            break

    # Must either have the required katas, or be a single respon
    if has_kata_penting or respon_sendiri:
        return int(persentase * 100)
    else:
        return 0


def cek_semua_pesan(pesan):
    daftar_list = {}

    # Simplifies respon creation / adds it to the dict
    def respon(bot_respon, list_of_katas, respon_sendiri=False, kata_penting=[]):
        nonlocal daftar_list
        daftar_list[bot_respon] = pesan_kemungkinan(pesan, list_of_katas, respon_sendiri, kata_penting)

    # respons -------------------------------------------------------------------------------------------------------
    respon('Halo jugaa!', ['hello', 'hi', 'hey', 'sup', 'heyo','halo' ,'hallo'], respon_sendiri=True)
    respon('dadah, Sampai bertemu lagi!', ['bye', 'goodbye', 'dadah'], respon_sendiri=True)
    respon('kabar saya baik baik saja kawan!', ['kabar', 'apa',], kata_penting=['apa','kabar'])
    respon('hmm, sepertinya kabar saya baik baik saja!', ['kabar', 'bagaimana',], kata_penting=['bagaimana','kabar'])
    respon('Terima kasih Kembali!', ['terimakasih', 'makasih'], respon_sendiri=True)
    respon('ohh iya, Terima Kasih Kembali!', ['terima', 'kasih',], kata_penting=['terima','kasih'])
    respon('Thank you!', ['i', 'love', 'code', 'palace'], kata_penting=['code', 'palace'])

    # Longer respons
    respon(long.R_ADVICE, ['give', 'advice'], kata_penting=['advice'])
    respon(long.R_EATING, ['what', 'you', 'eat'], kata_penting=['you', 'eat'])
    respon(long.R_MALAM, ['selamat', 'malam'], kata_penting=['malam', 'selamat'])

    kata_paling_cocok = max(daftar_list, key=daftar_list.get)
    # print(daftar_list)
    # print(f'Best match = {kata_paling_cocok} | Score: {daftar_list[kata_paling_cocok]}')

    return long.tidak_dikenal() if daftar_list[kata_paling_cocok] < 1 else kata_paling_cocok


# kode script untuk mengambil data respon
def dapatkan_respon(input_pengguna):
    bagi_pesan = re.split(r'\s+|[,;?!.-]\s*', input_pengguna.lower())
    respon = cek_semua_pesan(bagi_pesan)
    return respon

# Testing respon robot
while True:
    print('Robot: ' + dapatkan_respon(input('Kamu: ')))
