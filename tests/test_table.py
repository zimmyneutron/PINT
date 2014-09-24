import time
t0 = time.time()
from pint import toaTable
import astropy.units as u
import pint.models as tm
from pint.phase import *

tt = toaTable.TOAs("tests/J1744-1134.Rcvr1_2.GASP.8y.x.tim")
tt.compute_planet_posvel_c(planets=True)
m = tm.StandardTimingModel()
m.read_parfile('tests/J1744-1134.basic.par')
p = m.phase_table(tt)
t1 = time.time()

print t1 - t0


