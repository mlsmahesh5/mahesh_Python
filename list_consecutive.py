my_list=[3,4,5,6,7]
data=0
for i in range(1,len(my_list)):
    if my_list[i] != my_list[i-1]+1:
        data=1
        break
if data==0:
    print("List is having consecutive numbers")
else:
    print("List is not having consecutive numbers")