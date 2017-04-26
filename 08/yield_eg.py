import random

def get_data():
    """返回0到9之间的3个随机数"""
    return random.sample(range(10), 3)

def consume():
    """显示每次传入的整数列表的动态平均值"""
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
    """产生序列集合，传递给消费函数（consumer）"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield

if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print('Producing...')
        next(producer)

#主线,不停的嵌套,结果在10以内,再生产
#对题目理解错了,个数和求和是要累计的
#消费,生产赋值,消费先置0,生产,结果在10以内,迭代生产