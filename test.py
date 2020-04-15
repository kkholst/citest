#!/usr/bin/env python3

import targeted
from targeted.formula import riskreg


def test():
    d = targeted.getdata()
    val = riskreg(d, 'y~a', nuisance='x+z')
    return(val)


if __name__ == "__main__":
    # execute only if run as a script
    print('\n'+'_'*50+'\n')
    print('targeted version ' + targeted.__version__)
    print(test())
    print('_'*50+'\n')
