string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
c=[]
i=0
while i<len(string_list):
    if string_list[i] not in c:
        c.append(string_list[i])
    i=i+1
print(c)


