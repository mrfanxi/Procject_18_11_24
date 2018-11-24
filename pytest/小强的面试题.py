# 取出1-100的质数
list_ = []
for i in range(2, 101):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        list_.append(i)

print(list_)

b = "asdfghsd"