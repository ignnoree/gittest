items = [1, 1, 2, 2, 2, 3]
freq_dict = {}

for i in items:
    if i not in freq_dict:
        freq_dict[i] = 1
    else:
        freq_dict[i] += 1
wh=[23]
print(freq_dict) 
