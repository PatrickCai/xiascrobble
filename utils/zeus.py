import os

from constants.main import BASE_DIR


def read_constants_file(filename):
    '''
    Read file from constants like port.secret,
    Pay attention the type value of return is string
    '''
    file_path = os.path.join(BASE_DIR, 'constants/%s' % (filename))
    with open(file_path) as txt:
        var = txt.read()
    return var
