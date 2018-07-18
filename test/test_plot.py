import sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, 'src/')

from utils import *

order, Nx, Nt, T, L, rc, qc, rho, mesh_location, locations, names =\
	read_output('output/data.cfg')

T = redimensionalise(rc, qc, rho, T, 'time')

t = np.linspace(0, T, Nt)

for i, name in enumerate(names):

	for j in range(2**order-1):
	
		x = np.linspace(0, L[j], Nx)
		
		M = XDMF_to_matrix(Nx, Nt, mesh_location,
			'%s/%s_%i.xdmf' % (locations[i], name, j), name)
			
		M = redimensionalise(rc, qc, rho, M, name)
		
		plot_matrix(t, x, M, name,
					'%s/%s_%i.png' % (locations[i], name, j))
