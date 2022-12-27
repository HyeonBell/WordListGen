import random

ret = ""
ret_ary = []
for i in range(0, 999999):
    ret_ary.append(str(i).zfill(6))
    
random.shuffle(ret_ary)
#print(ret_ary)
for r in ret_ary:
    ret += r + "\n"

f = open('email_pincode.txt','wb+')

f.write(ret.encode())
f.close()