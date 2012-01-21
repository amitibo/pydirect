from DIRECT import solve
import numpy as np

trans = np.array([-1, 2, -4, 3])

def func( x, iidata, ddata, cdata, n, iisize, idsize, icsize ):
    x -= trans
    return np.dot(x, x), 0


if __name__ == '__main__':

    logfile = "direct_log.txt"

    l = np.array([-10, -10, -10, -10], dtype=np.float64)
    u = np.array([10, 10, 10, 10], dtype=np.float64)

    x, fmin, ierror = solve(
                        func,
                        l,
                        u
                        )

    print x
    print fmin
                                
    
