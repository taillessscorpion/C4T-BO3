print('CHÚ Ý')
print('Báo thức hoạt động theo hệ 24 giờ, đề nghị bạn sử dụng theo tiêu chuẩn 24 giờ để phần mềm hoạt động chính xác.')
import datetime
from random import randint
from playsound import playsound
a = datetime.datetime.now()
hr = int(a.hour)
mr = int(a.minute)
whileh = 0
while whileh < 1:
    alh = input('Nhập giờ cần báo thức: ')
    if alh.isdigit():
        ah = int(alh)
        if 0 <= ah <= 23:
            print('Đã nhận giờ báo thức.')
            whileh = 1
        elif ah > 23:
            print('Giờ báo thức phải là một số thuộc từ 0 đến 23. Mời nhập lại.')
            rh = randint(0,23)        
            print('Ví dụ:', rh, 'giờ.')
        else:
            print(alh, 'giờ', alm, "phút không tồn tại. Mời nhập lại.")
            rm = randint(0,59)
            print('Ví dụ:', alh, 'giờ', rm, 'phút.')
    else:
        print(alh, 'giờ không tồn tại. Mời nhập lại.')
        rh = randint(0,23)        
        print('Ví dụ:', rh, 'giờ.')
whilem = 0
while whilem < 1:
    print('Bạn cần đặt chính xác là', ah, 'giờ bao nhiêu phút: ')
    alm = input('')
    if alm.isdigit():
        am = int(alm)
        if 0<= am <= 59:
            print('Giờ báo thức đã được đặt thành công.', ah, 'giờ', am, 'phút.')
            whilem = 1
        elif am > 59:
            print('Phút báo thức phải là một số thuộc từ 0 đến 59. Mời nhập lại.')
            rm = randint(0,59)
            print('Ví dụ:', ah, 'giờ', rm, 'phút.')
        else:
            print(alh, 'giờ', alm, "phút không tồn tại. Mời nhập lại.")
            rm = randint(0,59)
            print('Ví dụ:', alh, 'giờ', rm, 'phút.')
    else:
        print(alh, 'giờ', alm, "phút không tồn tại. Mời nhập lại.")
        rm = randint(0,59)
        print('Ví dụ:', alh, 'giờ', rm, 'phút.')
while True:
    if hr == ah and mr == am:
        for alarm in range (5):
            print('BÁO THỨC.')
            print('BÁO THỨC..')
            print('BÁO THỨC...')
        print('Bây giờ là', hr, 'giờ', mr, 'phút.')
        playsound('D:\python\c4t bo4\session6\Lost3.mp3')
        break