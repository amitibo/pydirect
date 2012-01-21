# -*- coding: utf-8 -*-
"""
DIRECT - A python wrapper to the DIRECT algorithm.
==================================================

DIRECT is a method to solve global bound constraint optimization problems and
was originally developed by D. R. Jones, C. D. Perttunen and B. E. Stuckmann.

The DIRECT package uses the fortan implementation of DIRECT written by
Joerg.M.Gablonsky, DIRECT Version 2.0.4.

Author: Amit Aides <amitibo@tx.technion.ac.il>
License: MIT
"""

import numpy as np
from direct import direct


def solve(
    objective,
    l,
    u,
    eps=10e-4,
    maxf=10000,
    maxT=100,
    algmethod=0,
    fglobal=-1000000,
    fglper=0.0,
    volper=0.00001,
    sigmaper=0.001,
    logfilename='DIRresults.txt',
    user_data=None
    ):
    
    iidata = np.ones(10, dtype=np.int32)
    ddata = np.ones(10, dtype=np.float64)
    cdata = np.ones([10,40], dtype=np.uint8)*49

    x, fmin, ierror = direct(
                        objective,
                        eps,
                        maxf,
                        maxT,
                        l,
                        u,
                        algmethod,
                        logfilename, 
                        fglobal,
                        fglper,
                        volper,
                        sigmaper,
                        iidata,
                        ddata,
                        cdata
                        )

    return x, fmin, ierror
