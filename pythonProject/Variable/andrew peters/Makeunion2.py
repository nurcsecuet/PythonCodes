import hoomd
import math
import numpy
import gsd.hoomd
import itertools
import hoomd.hpmc_energy




position=[(-1,0,0),(-1.1,0,0)]
orientation=[(1,0,1,0)]
orientation=numpy.tile(orientation,(2,1))


frame = gsd.hoomd.Frame()
frame.particles.N = 2
frame.particles.position = position
frame.particles.orientation = orientation
frame.particles.typeid = [3] * 2
frame.particles.types = ['A','B','C','D']
frame.configuration.box = [50,50,50, 0, 0, 0]
with gsd.hoomd.open(name='trajectory1.gsd', mode='w') as f:
    f.append(frame)