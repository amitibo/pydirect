import direct
import numpy as np

trans = np.array([-1, 2, -4, 3])

def func( x, iidata, ddata, cdata, n, iisize, idsize, icsize ):
    x -= trans
    return np.dot(x, x), 0


if __name__ == '__main__':

    logfile = "direct_log.txt"
    f = open( logfile, "w" )

    eps = 0.0001
    maxf = 10000
    maxT = 100
    l = np.array([-10, -10, -10, -10], dtype=np.float64)
    u = np.array([10, 10, 10, 10], dtype=np.float64)
    algmethod = 0
    fglobal = -1000000
    fglper = 0.0
    volper = 0.00001
    sigmaper = 0.001
    iidata = np.ones(10, dtype=np.int32)
    ddata = np.ones(10, dtype=np.float64)
    cdata = np.ones([10,40], dtype=np.uint8)*49

    x, fmin, ierror = direct.direct(
                        func,
                        eps,
                        maxf,
                        maxT,
                        l,
                        u,
                        algmethod,
                        logfile, 
                        fglobal,
                        fglper,
                        volper,
                        sigmaper,
                        iidata,
                        ddata,
                        cdata
                        )

    f.close()

    print x
    print fmin
                                
    
