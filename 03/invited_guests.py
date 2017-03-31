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
for name in guests_list:
    print("I would like to invite " + name + " to dinner")
