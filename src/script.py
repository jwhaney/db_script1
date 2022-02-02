# hello world test program using WSL and VSCode for native linux dev feel, ya!

class Doer(object):

    def __init__(self, h, ex, uhoh, a, str_in):
        self.h = h
        self.ex = ex
        self.uhoh = uhoh
        self.a = a
        self.str_in = str_in

        print('is this working')
    
    def requestor(self, str_in):
        print('entering requestor method')
        # main print statement
        print('would you like to see what I have to say? Type "y" for yes and "n" for no.')
        print('length of string input is:', len(str_in))
        # send str_in to resolver method
        self.resolver(str_in)

    def resolver(self, h, ex, uhoh, a, str_in):
        if len(str_in) == 1:
            if str_in in a:
                if str_in == a[0] or str_in == a[1]:
                    print(h)
                elif str_in == a[2] or str_in == a[3]:
                    print(ex)
                else:
                    print(uhoh)
                    self.requestor
            else:
                print('that string is not in the list of acceptable answers. please try again.')
                self.resolver()
        else:
            print('only one letter response is allowed. please try again.')
            self.resolver()

# start the script
if __name__ == "__main__":
    h = 'hello, world!'
    ex = 'bah bye! exiting...'
    uhoh = 'uh oh, you entered an invalid value. please try again.'
    a = ['Y', 'y', 'N', 'n']
    str_in = str(input())

    print('is this working?')

    script = Doer(h, ex, uhoh, a, str_in)