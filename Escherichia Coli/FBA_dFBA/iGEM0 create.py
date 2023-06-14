import cobra

iGEM0 = cobra.io.read_sbml_model("iJO1366.xml")

iGEM0.description = "iGEM00"

iGEM0.objective = "BIOMASS_Ec_iJO1366_core_53p95M"

iGEM0.reactions.get_by_id("EX_o2_e").upper_bound = 0
iGEM0.reactions.get_by_id("EX_o2_e").lower_bound = 0

iGEM0.reactions.get_by_id("EX_lac__D_e").upper_bound = 0
iGEM0.reactions.get_by_id("EX_lac__D_e").lower_bound = -1000

cobra.io.write_sbml_model(iGEM0, "iGEM0.xml")