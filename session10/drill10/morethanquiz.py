import random
from random import randint
quesnumber = 0
pointcount = 0
data = [{
    'name': 'Trung Quốc',
    'capital': 'Bắc Kinh',
}, {
    'name': 'Ấn Độ',
    'capital': 'New Dehli',
}, {
    'name': 'Hoa Kì',
    'capital': 'Washington, D.C',
}, {
    'name': 'In-đô-nê-xi-a',
    'capital': 'Jakarta',
}, {
    'name': 'Việt Nam',
    'capital': 'Hà Nội',
}]
while quesnumber < 4:
    quesnumber += 1
    rcountry = random.choice(data)
    data.remove(rcountry)
    print(data)
    rlocation = randint(0,3)
    groupcaps = []
    capitals = ['Tokyo', 'Paris', 'London', 'Bangkok', 'Moscow', 'Mexico City', 'Marid', 'Hồng Kông', 'Berlin', 'New York', 'Pnom pênh', 'Bình Nhưỡng', 'Macau', 'Havana', 'Bạc Liêu']
    for i in range(4):
        rcapitlas = random.choice(capitals)
        groupcaps.append(rcapitlas)
        capitals.remove(rcapitlas)
    groupcaps[rlocation] = rcountry['capital']
    print('Câu số {}. Thủ đô của {} là một trong bốn thành phố nào sau đây:'.format(quesnumber,rcountry['name']))
    for i, j in enumerate(groupcaps,1):
        print('{}. {}.'.format(i, j))
    while True:
        answer = input('Hãy chọn một trong bốn phương án trên: ')
        if answer.isdigit() and 1 <= int(answer) <= 4:
            if int(answer) == rlocation+1:
                pointcount += 1
                if pointcount == 1:
                    print('Xin chúc mừng, đây là câu trả lời đúng đầu tiên của bạn.')
                else:
                    print('Xin chúc mừng, bạn đã trả lời đúng {} câu.'.format(pointcount))
                print('Đáp án {} là một đáp án hoàn toàn chính xác.'.format(answer))
                print('Đúng như vậy. Thành phố {} chính là thủ đô của {}.'.format(rcountry['capital'],rcountry['name']))
            else:
                print('Đáp án {} là một đáp án không chính xác.'.format(answer))
                print('Không phải {} mà {} mới chính là thủ đô của {}.'.format(groupcaps[int(answer)-1],rcountry['capital'],rcountry['name']))
                if pointcount == 0:
                    print('Rất đáng tiếc, bạn vẫn chưa đưa ra được đáp án chính xác')
                else:
                    print('Rất đang tiếc, số câu trả lời đúng của bạn vẫn dừng ở mốc {} câu.'.format(pointcount))
            break
        else:
            print('Đán án {} là một đáp án không hợp lệ. Mời chọn lại đáp án từ 1 đến 4'.format(answer))
rightpertage = (pointcount / 4) * 100
print('Bạn đã trả lời đúng {}%, trên tổng số câu hỏi'.format(rightpertage))