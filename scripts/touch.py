import os


def touch(**_):
    with open(os.path.join(os.getcwd(), 'touched'), 'wb') as fobj:
        fobj.write('Hey!')
