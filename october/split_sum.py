s = ("9@10@20@30@30")
s1 = (s.split("@"))
spl_list = s1
num = 0
res = [eval(i) for i in spl_list]
print(res)
for i in res:
    num += i
print("Sum =", num)