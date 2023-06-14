import cobra
import numpy

iGEM0 = cobra.io.read_sbml_model('iGEM0.xml')

complete_reactions = numpy.load(open('complete_reactions.npy', 'rb'), None, True)

outknocked_reactions = numpy.ndarray(2 ** len(complete_reactions), 'object')
optimized_biomasses  = numpy.zeros(2 ** len(complete_reactions))
consumed_lactates    = numpy.zeros(2 ** len(complete_reactions))

### (0) Trying every, up to irrelevant order, possible analized_reactions sublist of complete_reactions

new_model = iGEM0.copy()

for i in range(0, 2 ** len(complete_reactions)) :                                                 # for analized_reactions in range([], complete_reactions) :
    indeces = numpy.array([], 'int')                                                              #
                                                                                                  #
    for j in range(0, len(complete_reactions)) :                                                  #
        if int(i / 2 ** j) % 2 == 1 :                                                             #
            indeces = numpy.append(indeces, j)                                                    #
    analized_reactions = complete_reactions[indeces]                                              #

    ### (1) Setting the bounds of analized_reactions from the model to 0 while keeping track of
    ### previous values in order to restore them in part () without having to copy the whole model

    old_upper_bounds = numpy.zeros(len(analized_reactions))
    old_lower_bounds = numpy.zeros(len(analized_reactions))
    for k in range(0, len(analized_reactions)) :                                                  #
        old_upper_bounds[k] = new_model.reactions.get_by_id(analized_reactions[k][1]).upper_bound # old_upper_bound = new_model.reactions.get_by_id(analized_reactions[:][1]).upperbound
        old_lower_bounds[k] = new_model.reactions.get_by_id(analized_reactions[k][1]).lower_bound # old_lower_bound = new_model.reactions.get_by_id(analized_reactions[:][1]).lowerbound
        new_model.reactions.get_by_id(analized_reactions[k][1]).upper_bound = 0                   # new_model.reactions.get_by_id(analized_reactions[:][1]).upperbound = 0
        new_model.reactions.get_by_id(analized_reactions[k][1]).lower_bound = 0                   # new_model.reactions.get_by_id(analized_reactions[:][1]).lowerbound = 0
    
    new_optimization = new_model.optimize('maximize')
    
    outknocked_reactions[i] = analized_reactions
    optimized_biomasses     = numpy.insert(optimized_biomasses, i, new_optimization.objective_value)
    consumed_lactates       = numpy.insert(consumed_lactates, i, new_optimization.fluxes['EX_lac__D_e'])
    
    ### (2) Restoring of the old bound for the analized_reactions 
    
    for k in range(0, len(analized_reactions)) :                                                  #
        new_model.reactions.get_by_id(analized_reactions[k][1]).upper_bound = old_upper_bounds[k] #
        new_model.reactions.get_by_id(analized_reactions[k][1]).lower_bound = old_lower_bounds[k] #
    
numpy.save(open('outknocked_reactions.npy', 'wb'), outknocked_reactions)
numpy.save(open('optimized_biomasses.npy', 'wb'), optimized_biomasses)
numpy.save(open('consumed_lactates.npy', 'wb'), consumed_lactates)