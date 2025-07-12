guests = {}

def read_guestlist(file_name):
    with open(file_name) as f:
        entries = f.read().splitlines()
    
    while entries:
        line_data = entries.pop().split(',')
        print(line_data)
        name, age = line_data[0], int(line_data[1])
        guests[name] = age
        entry = yield name
        if entry != None:
            entries.append(entry)
    

guest_list = read_guestlist('guest_list.txt')
next(guest_list)
