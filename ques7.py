# socho aapke paas 2 lists hain.
#  Aapne aisa code likhna hain jisse ek nayi list banne jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain. Socho aapki do list yeh hain:

list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
c=[]
x=list1+list2
for j in x:
    if j not in c:
        c.append(j)
print(c)