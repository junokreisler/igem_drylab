import cobra
from functions import *

# read anaerobic model
EC_model = cobra.io.read_sbml_model('Paper_reconstructions/EC_model.xml')
EC_model.reactions.get_by_id("EX_lac__D_e").lower_bound = -1000

### Effects of single gene deletion

##  single genes to knock out, taken from the section in the paper

gene_annot = {"b0902":                        "pflA pyruvate formate lyase subunit A"  ,
              "b0903":                        "pflB pyruvate formate lyase subunit B"  ,
              "b2296":                        "ackA acetate kinase A"                  ,
              "b2297":                        "pta phosphate acetyltransferase"        ,
              "b0871":                        "poxB pyruvate oxidase"                  ,
              "b2133":                        "dld FAD-binding D-lactate dehydrogenase",
              "b1241":                        "adhE alcohol dehydrogenase"             ,
              "b1702":                        "pps PEP synthase"                           ,
              "b3956":                        "ppc PEP carboxylase"
             }

genes_single = list(gene_annot.keys())

# find knockdown reactions
rxn_list = []
for gene in genes_single:
    rxn_list += list_rxns_of_gene(gene_str = gene)
    rxn_list = list(set(rxn_list))

gene_obj = list_gene_obj(genes_single)
# CAUSES INFINITE LOOP, DON'T RUN
#biomass_w_single_knockout = cobra.flux_analysis.single_gene_deletion(EC_model, gene_obj)

# neither does this work
rxn_obj = list_rxn_obj(rxn_list)
#cobra.flux_analysis.single_reaction_deletion(EC_model, rxn_obj)

# try to manually change flux bounds
EC_model = cobra.io.read_sbml_model('Paper_reconstructions/EC_model.xml')
EC_model.reactions.get_by_id("EX_lac__D_e").lower_bound = -1000

#test = gene_ko_res(genes_single[0], model = EC_model)
with open("Paper_reconstructions/lactate_biomass_solutions.txt", 'w') as f:
    sol_list = []
    f.write('The results were obtained from single gene knock-outs based on suggestions from the Zhou et al 2015 paper.\n')
    f.write('The results are representative of growth under anaerobic conditions.\n')
    for gene in genes_single:
        gene_now = gene
        EC_model.genes.get_by_id(gene_now).knock_out()
        sol_list.append(EC_model.optimize())
        print(gene_annot[gene],"knocked out ||| Lactate balance: ", sol_list[-1].fluxes["EX_lac__D_e"], "||| biomass: ", sol_list[-1].objective_value)
        f.write(gene_annot[gene]+" knocked out ||| Lactate balance: " + str(sol_list[-1].fluxes["EX_lac__D_e"])+" ||| biomass: "+str(sol_list[-1].objective_value)+"\n")
        EC_model.genes.get_by_id(gene_now).functional = True

### Effects of