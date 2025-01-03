locks = []
keys = []

is_beginning = True
is_ending = False
with open('input.txt') as file:
    for line in file:
        if is_beginning:
            if line[0] == '.':
                new_key = [0 for _ in range(5)]
                i = 5
                is_beginning = False
                is_key, is_lock = True, False
            else: 
                new_lock = [0 for _ in range(5)]
                i = 1
                is_beginning = False
                is_key, is_lock = False, True
        elif is_key:
            if i == 0:
                keys.append(new_key)
                is_ending = True
                is_key = False
            else:
                for j in range(5):
                    if line[j] == '#' and new_key[j] == 0:
                        new_key[j] = i
                i -= 1
        elif is_lock:
            if i == 6:
                locks.append(new_lock)
                is_ending = True
                is_lock = False
            else:  
                for j in range(5):
                    if line[j] == '#':
                        new_lock[j] = i
                i += 1
        elif is_ending:
            is_beginning = True
            is_ending = False
            
count = 0
for lock in locks:
    for key in keys:
        is_valid = True
        for i in range(5):
            if lock[i] + key[i] > 5:
                is_valid = False
        count+= is_valid

print(count)