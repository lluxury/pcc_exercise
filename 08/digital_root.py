
import unittest

def digital_root(n):
    # ...
    strNumbers = [i for i in str(n)]
    #print (strNumbers)
    answer = sum(map(int, strNumbers))
    #print (answer)
    return answer

# class SimplisticTest(unittest.TestCase):
#     def test(self):
#          test.assert_equals( digital_root(16), 7 )



#import get_formatted_name

class SumTestCase(unittest.TestCase):
    '''测试digital_root'''

    def test_summary(self):
        '''能够正确处理获得结果'''
        # sum = digital_root(16)
        # self.assertEqual(sum, 7)
        self.assert_equal(digital_root(16),7)

unittest.main()