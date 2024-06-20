# Inside a method we can declear another method

class Test:
    def m1(self):
        # some repeated code is there so let's create one 
        # function inside this m1() function and whenever required
        # we can calll it 
        def sum(a,b):
            print('First Arguments: ',a)
            print('Second Arguments:', b)
            print('The sum', a+b)
            print('The product: ', a*b)
            print('*'*20)

        # lets call this function inside m1()
        sum(10,20)
        sum(100,200) 
        sum(1000,2000)

t = Test()
t.m1() 
