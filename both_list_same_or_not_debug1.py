# def numbers_less_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:
#       list.remove(item)
#     else:
#       counter += 1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

# num_list_sub_20 = numbers_less_than_twenty(num_list)

# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20)

def numbers_less_than_twenty(list):
    counter=0
    l=[]
    while counter<len(list):
        item=list[counter]
        if item<20:
            l.append(item)
        counter+=1
    print("initial list",list)
    print("list that doesnt'n contain numbers greate than 20",l)
numbers_less_than_twenty([12,312,42,123,5,12,53,75,123,62,9])