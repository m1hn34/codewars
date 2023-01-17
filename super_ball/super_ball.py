'''
Create a class Ball. Ball objects should accept one argument for "ball type" 
when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" 
of "regular."

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"

'''


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)


# p1 = Person("John", 36)
# p1.myfunc()


class Ball(object):
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type
