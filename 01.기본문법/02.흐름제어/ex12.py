#남탕: 남자 or 여자, 나이 4세 미만
#여탕: 여자 or 남자, 나이 4세 미만

while True:
    type = input('1.남탕|2.여탕|0.종료> ')
    
    if type == '0':
        print('프로그램을 종료합니다.')
        break

    elif type == '1' or type == '2':
        gen = input('1.남자|2.여자> ')

        if gen != '1' and gen!= '2':
            print('성별은 1~2를 입력하세요.')
            continue

        if type == '1':
            if gen == '1':
                print('남자이므로 입장이 가능합니다.')

            else:
                age = int(input('나이> '))

                if age < 4:
                    print('여자지만 4세미만이므로 남탕에 입장이 가능합니다.')

                else:
                    print('여자이고 4세이상이므로 남탕에 입장이 불가능합니다.')

        else:
            if gen == '2':
                print('여자이므로 입장이 가능합니다.')

            else:
                age = int(input('나이> '))

                if age < 4:
                    print('남자이지만 4세미만이므로 여탕에 입장이 가능합니다.')

                else:
                    print('남자이고 4세이상이므로 여탕에 입장이 불가능합니다.')

    else:
        print('0~2 숫자를 입력하세요.')