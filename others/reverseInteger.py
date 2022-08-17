class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x < -2 **31) or x > (2**31-1):
            return 0
        s =''
        a = ''
        for i in str(x):
            if i == '-':
                a+=i
            if i.isdigit():
                s= i+s
                
        if int(a+s)>= -2 **31 and int(a+s)<=(2**31-1):
            return int(a+s)
        else:
            return 0