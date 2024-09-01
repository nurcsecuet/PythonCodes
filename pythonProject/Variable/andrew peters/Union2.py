import hoomd
import math
import numpy
import gsd.hoomd
import hoomd.hpmc_energy

# Parameters
A = 50
a = 1
rho = 2.5
phi = 0.05
b = a / rho
c = b
dcharge = ((0.6 * b * b) * ((rho) ** 2 - 1)) ** 0.5

# Setup simulation
cpu = hoomd.device.CPU()
simulation = hoomd.Simulation(device=cpu, seed=1)

# Set up HPMC integrator with ellipsoid shapes
mc = hoomd.hpmc.integrate.Ellipsoid(default_d=0.3, default_a=0.4, translation_move_probability=1.0)
mc.shape["A"] = dict(a=a, b=b, c=c)
mc.shape["B"] = dict(a=0.01, b=0.01, c=0.01)
mc.shape["C"] = dict(a=0.01, b=0.01, c=0.01)
mc.shape["D"] = dict(a=a, b=b, c=c)

print('Ellipsoids parameters (a,b,c) = ',
      mc.shape["D"]["a"],
      mc.shape["D"]["b"],
      mc.shape["D"]["c"])

simulation.operations.integrator = mc

# Define pair potentials using ExamplePair
Yuk = hoomd.hpmc_energy.ExamplePair()
Yuk.params[(['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'])] = dict(A=0, B=0, r_cut=0)
Yuk.params[('B', 'B')] = dict(A=A, B=0, r_cut=10)
Yuk.params[('B', 'C')] = dict(A=-A, B=0, r_cut=10)
Yuk.params[('C', 'C')] = dict(A=A, B=0, r_cut=10)
Yuk.params[('D', 'D')] = dict(A=0, B=0, r_cut=10)

# Set up the union shape for particles of type D
union = hoomd.hpmc.pair.Union(constituent_potential=Yuk)
union.body['D'] = dict(types=['B', 'C'],
                       positions=[(dcharge, 0, 0), (-dcharge, 0, 0)])
union.body['A'] = None
union.body['B'] = None
union.body['C'] = None

simulation.operations.integrator.pair_potentials = [union]

# Logger setup
logger = hoomd.logging.Logger()
logger.add(mc, quantities=['type_shapes'])

# GSD file writer
gsd_writer = hoomd.write.GSD(
    filename='trajectory.gsd',
    trigger=hoomd.trigger.Periodic(1),
    mode='wb',
    filter=hoomd.filter.All(),
    logger=logger,
)
simulation.operations.writers.append(gsd_writer)

# Initialize simulation state
simulation.create_state_from_gsd(filename='trajectory1.gsd')

# Run the simulation
simulation.run(0)
print(dcharge)
print(mc.pair_energy)

for i in range(100):
    simulation.run(1)
    print(mc.pair_energy)

exit()

for i in range(50):
    simulation.run(100)
    gsd_writer.flush()