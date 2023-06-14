import cobra
import numpy

iGEM0   = cobra.io.read_sbml_model('iGEM0.xml')

iGEM0.reactions.get_by_id('PPS').upper_bound = 0
iGEM0.reactions.get_by_id('PPS').lower_bound = 0

iGEM0.reactions.get_by_id('LDH_D2').upper_bound = 0
iGEM0.reactions.get_by_id('LDH_D2').lower_bound = 0

iGEM0.reactions.get_by_id('POX').upper_bound = 0
iGEM0.reactions.get_by_id('POX').lower_bound = 0

iGEM0.reactions.get_by_id('FRD2').upper_bound = 0
iGEM0.reactions.get_by_id('FRD2').lower_bound = 0

solution = iGEM0.optimize('maximize')

print(solution.objective_value)
print(solution.fluxes['EX_lac__D_e'])

outknocked_reactions = numpy.load(open('outknocked_reactions.npy', 'rb'), None, True)

optimized_biomasses = numpy.load(open('optimized_biomasses.npy', 'rb'))
consumed_lactates   = numpy.load(open('consumed_lactates.npy', 'rb'))

print(optimized_biomasses[549:559])
print(consumed_lactates[549:559])