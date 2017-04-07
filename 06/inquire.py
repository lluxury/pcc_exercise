lists = ['dwq', 'bql', 'xx', 'txo']
inquier = {'bql': 'java', 'xx': 'xx', 'dwq': 'java'}

for ren in lists :
   for name in inquier.keys():
        if ren == str(name):
            print ("thank you " + ren)
            break
        else:
            print ("you hava a inquire " + ren)
            break

#注意循环的中断的位置,怪事,有个值没取到
#遍历字典的逻辑问题? 未解决

