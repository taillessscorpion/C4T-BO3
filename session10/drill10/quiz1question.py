China = {
    'population': 1409773089,
    'acreage': 9596961,
    'capital': 'Beijing',
    'location': 'East Asia',
}
popquest = [1300773089, China['population'], 1390773089, 1459773090]
print('Dân số Trung Quốc hiện tại là:')
for i, j in enumerate(popquest,1):
    print('{}. {} người.'.format(i, j))
while True:
    popans = input('Chọn đáp án của bạn: ')
    if popans.isdigit() and 1 <= int(popans) <= 4:
        if int(popans) == 2:
            print('Đáp án 2 là một đáp án hoàn toàn chính xác.')
            break
        else:
            print('Đáp án {} là một đáp án không chính xác.'.format(popans))
            break
    else:
        print('{} là một đáp án không tồn tại. Mời trả lời lại.'.format(popans))