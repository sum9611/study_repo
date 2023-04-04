def low(new_id):
    id = ''
    for i in new_id:
        id += i.lower()
    return id

def rm(new_id):
    id = ''
    for i in new_id:
        if (ord(i)>= 48 and ord(i)<= 57) or (ord(i)>= 97 and ord(i)<= 122) or i == '-' or i == '_' or i == '.':
            id += i
    return id

def change(new_id):
    id = ''
    start = 0
    for i in new_id:
        if i == '.':
            start += 1
        elif i != '.' and start > 0:
            id += '.'
            id += i
            start = 0
        else:
            id += i
    return id

def rm2(new_id):
    if len(new_id) != 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    else:
        return new_id
    return new_id

def ap(new_id):
    if len(new_id) == 0:
        return 'a'
    else:
        return new_id
def len_check(new_id):
    if len(new_id) >= 16:
        return new_id[:15]
    else:
        return new_id
    
def len_check2(new_id):
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
        return new_id
    else:
        return new_id
            

def solution(new_id):
    
    new_id = low(new_id)
    new_id = rm(new_id)
    new_id = change(new_id)
    new_id = rm2(new_id)
    new_id = ap(new_id)
    new_id = len_check(new_id)
    new_id = len_check2(new_id)
    new_id = rm2(new_id)

    return new_id