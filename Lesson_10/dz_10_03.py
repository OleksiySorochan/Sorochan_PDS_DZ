class MyUserError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return "MyUserError,{0}".format(self.message)
        else:
            return "MyUserError has been raised"

raise MyUserError('We have a problem')