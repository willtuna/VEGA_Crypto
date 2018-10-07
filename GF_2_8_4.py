import numpy as np

row = np.asarray([2,3,1,1])
hex_e = lambda a: format(a,'08b')
row_lst = []
for r_e in row:
    string = hex_e(r_e)
    row_lst.append( np.asarray([int(i) for i in string]) )

test_row = row_lst[0]
test_vec = np.asarray([1,1,1,1,1,1,1,1])

print("a:", test_row)
print("b:", test_vec)

test_row = test_row[::-1]
test_vec = test_vec[::-1]

irr      = np.asarray([1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0])

acc      = np.zeros(16)

for i in range(8):
    for j in range(8):
        idx = i + j
        acc[idx] = acc[idx] + test_row[i]*test_vec[j]

for idx in range(15,7,-1):
    if acc[idx] == 1:
        acc = acc + np.roll(irr,idx-8)





print(acc%2)
