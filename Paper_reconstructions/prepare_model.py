import cobra
import wget

# download and read model

wget.download('http://bigg.ucsd.edu/static/models/iJO1366.xml')

EC_model = cobra.io.read_sbml_model('iJO1366.xml')
EC_model.description = 'E. coli anaerobic model'

# set objective to biomass growth
EC_model.objective = 'BIOMASS_Ec_iJO1366_core_53p95M'

# set environment to anaerobic
EC_model.reactions.get_by_id('EX_o2_e').upper_bound = 0
EC_model.reactions.get_by_id('EX_o2_e').lower_bound = 0

# save adjusted model
cobra.io.write_sbml_model(EC_model, 'Paper_reconstructions/EC_model.xml')