def digits(number):
    digit = ['soon', 'neung', 'song', 'sam',
             'si', 'ha', 'hok', 'chet', 'paet', 'kao']
    return digit[number]


def tens(number):
    digit = ['', 'et', 'song', 'sam',
             'si', 'ha', 'hok', 'chet', 'paet', 'kao']
    ten = ['', '', 'yi ', 'sam ',
           'si ', 'ha ', 'hok ', 'chet ', 'paet ', 'kao ']
    return ten[int(number[0])] + "sib " + digit[int(number[1])]


def hundreds(number):
    digit = ['', 'et', 'song', 'sam',
             'si', 'ha', 'hok', 'chet', 'paet', 'kao']
    ten = ['', '', 'yi ', 'sam ',
           'si ', 'ha ', 'hok ', 'chet ', 'paet ', 'kao ']
    hundred = ['', 'neung ', 'song ', 'sam ',
               'si ', 'ha ', 'hok ', 'chet ', 'paet ', 'kao ']
    if int(str(number)[1]) != 0:
        return hundred[int(number[0])] + "roi " + ten[int(number[1])] + "sib " + digit[int(number[2])]
    return hundred[int(number[0])] + "roi " + ten[int(number[1])] + digit[int(number[2])]


def thousands(number):
    digit = ['', 'et', 'song', 'sam',
             'si', 'ha', 'hok', 'chet', 'paet', 'kao']
    ten = ['', '', 'yi ', 'sam ',
           'si ', 'ha ', 'hok ', 'chet ', 'paet ', 'kao ']
    hundred = ['', 'neung ', 'song ', 'sam ',
               'si ', 'ha ', 'hok ', 'chet ', 'paet ', 'kao ']
    thousand = ['', 'neung ', 'song ', 'sam ',
                'si ', 'ha ', 'hok ', 'chet ', 'paet ', 'kao ']
    ans = thousand[int(number[0])] + "pun " + hundred[int(number[1])]
    if int(number[1]) != 0:
        ans += "roi "
    ans += ten[int(number[2])]
    if int(number[2]) != 0:
        ans += "sib "
    ans += digit[int(number[3])]
    return ans


def transalate(number):
    if number <= 9:
        print(digits(number))
    elif number <= 99:
        print(tens(str(number)))
    elif number <= 999:
        print(hundreds(str(number)))
    else:
        print(thousands(str(number)))


number = int(input("Enter Num: "))
transalate(number)
