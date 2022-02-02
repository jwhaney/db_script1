# hello world test program using WSL and VSCode

def script():

    print('would you like to see what I have to say? Type "y" for yes and "n" for no.')
    
    hello = 'hello, world!'
    exit = 'bah bye! exiting...'
    uhoh = 'uh oh, you entered an invalid value. please try again.'
    a = ['Y', 'y', 'N', 'n']
    
    str_in = str(input())
    
    print('length of string input is:', len(str_in))

    def main():
        if len(str_in) == 1:
            if str_in in a:
                if str_in == a[0] or str_in == a[1]:
                    print(hello)
                elif str_in == a[2] or str_in == a[3]:
                    print(exit)
                else:
                    print(uhoh)
                    main()
            else:
                print('that string is not in the list of acceptable answers. please try again.')
                main()
        else:
            print('only one letter response is allowed. please try again.')
            main()

# start the script
script()
