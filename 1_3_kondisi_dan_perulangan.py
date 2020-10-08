import time

#APLIKASI PENILAIAN
def main():
    nilai = int(input('masukkan nilai:  '))
    #time.sleep(1)

    if nilai <= 100 and nilai>=90 :
        print("nilai anda A")
    elif nilai >=80 and nilai <=89:
        print('nilai anda B')
    elif nilai >=70 and nilai <=79:
        print('nilai anda C')
    else:
        print('Anda belum lulus')
    time.sleep(2)

    back = input('apakah anda ingin mencari nilai lagi? y/n  = ').lower()
    if back == 'y':
        main()
    else:
        exit()
main()