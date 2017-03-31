guests_list = ['laobian', 'wenhao1','wenhao2']
for name in guests_list:
    print ("I would like to invite " + name + " to dinner")

print (guests_list[1] + " could't make it for the appointment.\n")

guests_list[1] = ('tianjia')
for name in guests_list:
    print ("I would like to invite " + name + " to dinner")
print("\nI found a bigger dining table")
guests_list.insert(0, 'first')
guests_list.insert(2, 'middle')
guests_list.append('last')
number = len(guests_list)
print("I invited " + str(number) + " people to dinner")
for name in guests_list:
    print("I would like to invite " + name + " to dinner")
print("\nI could only invite two guest for dinner.")
for name in guests_list[:-2]:
    sorry_guest = guests_list.pop()
    print("sorry, " + sorry_guest + " I can't invite you for dinner")
for name in guests_list:
    print("I would like to invite " + name + " to dinner")
del guests_list[0]
del guests_list[0]
print(guests_list)
