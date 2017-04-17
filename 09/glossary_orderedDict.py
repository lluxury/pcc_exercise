from collections import OrderedDict
friend = OrderedDict()
friend['print'] = 'print'
friend['elif'] = 'if'


# friend = {'printf': 'print', 'elif': 'if','END': 'end', 'BEGIN':'begin', 'break':'stop'}

# print('printf:\t'+friend['printf'])
# print('elif:\t'+friend['elif'])
# print('END:\t'+friend['END'])
# print('BEGIN:\t'+friend['BEGIN'])
# print('break:\t'+friend['break'])

for command, mean in friend.items():
    print(command + ' like ' + mean)