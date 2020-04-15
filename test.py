#!/usr/bin/env python3

import targeted
from targeted.formula import riskreg


def test():
    d = targeted.getdata()
    val = riskreg(d, 'y~a', nuisance='x+z')
    return(val)


if __name__ == "__main__":
    # execute only if run as a script
    print(test())
