
def outer():
    def inner():
       print('This is inner.')

    print('This is outer, invoking inner.')
    inner()
