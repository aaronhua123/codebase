square_num = 1
long = 2019
wide = 324
while long != wide:
    if long > wide:
        long = wide
    else:
        wide -= long
    square_num += 1
print(square_num)  # 因为最后会剩两个正方形,所以+1