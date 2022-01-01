class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate  # Now Penguin, even though it isn't a subclass
        # of Duck, can fly. Therefore, for our purposes, it "is" a duck.
        # However, its fly method equals aviate, which prints a different
        # message.

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")

    def aviate(self):
        print("Look, I am flying!")


# Creating a subclass of duck called Mallard 
class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    # Below we are helping the user by telling him/her what object we should
    # use in our method. In this case, Duck, because Penguins don't have
    # the fly() method.
    def add_duck(self, duck: Duck) -> None:
        # if isinstance(duck, Duck):  # If the object duck is part of the class
            # Duck, or a subclass of duck, then the object duck will be
            # used in our code. Since Mallard is a subclass of Duck, then
            # the code will work.
            # This is still not Pythonic, though, as Python is not interested
            # in what the object IS, but in its BEHAVIOUR. So the better
            # way to approach this is: if it flies like a duck, then it
            # is a duck. So let's check if duck has the fly() method.
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        # If the object is callable (a function, a method or a class), then
        # the object created using the class that has this method/function
        # will be added to self.flock.
        # THIS is the Pythonic way of approaching our problem.
        else:
            raise TypeError("Cannot add duck. Are you sure it's not a "
                            + str(type(duck).__name__) + "?")
        # Now an exception will be raised even before any object duck is
        # actually appended to flock. Now the user or the programmer using
        # this code will be able to more quickly figure out where the error
        # is, and what is causing it.

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                # raise AttributeError("Testing exception handler in migrate")
                # One way to test your exception handler is to raise an error
                # in your try block
                # TODO remove this raise before release
                # With this IntelliJ can remind you of removing this raise,
                # which is only there to test error handling
                # Notice the TO DO tab at the bottom of IntelliJ!!!
            except AttributeError as e:  # Giving the error an alias
                problem = e  # If the AttributeError happens, it will get
                # the alias e, which in turn will become problem
                print("This type of bird can't fly")
                # raise  # Use it to raise the exception/error when needed
            if problem:
                raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
