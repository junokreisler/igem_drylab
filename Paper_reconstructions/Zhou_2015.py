import cobra
from functions import *

# read anaerobic model
EC_model = cobra.io.read_sbml_model('Paper_reconstructions/EC_model.xml')

EC_model.reactions.get_by_id("EX_lac__D_e").lower_bound = -1000

### Effects of single gene deletion

##  single genes to knock out, taken from the section in the paper

genes_single = ["b0902", "b0903",                        # pflA, pflB pyruvate formate lyase subunits A and B
                "b2296",                                 # ackA acetate kinase A
                "b2297",                                 # pta phosphate acetyltransferase
                "b0871",                                 # poxB pyruvate oxidase
                "b2133",                                 # dld FAD-binding D-lactate dehydrogenase,
                                                         # ...required for aerobic growth on D-lactate
                "b2297",                                 # adhE alcohol dehydrogenase
                "b1702",                                 # pps PEP synthase
                "b3956"                                  # ppc PEP carboxylase
                ]

# find knockdown reactions
rxn_list = []
for gene in genes_single:
    rxn_list += list_rxns_of_gene(gene_str = gene)
    rxn_list = list(set(rxn_list))

# idk why this doesn't work
gene_obj = list_gene_obj(genes_single)
cobra.flux_analysis.single_gene_deletion(EC_model, gene_obj)

# neither does this work
rxn_obj = list_rxn_obj(rxn_list)
cobra.flux_analysis.single_reaction_deletion(EC_model, rxn_obj)

# try to manually change flux bounds

EC_model.genes.get_by_id(genes_single[0]).knock_out()
EC_model.optimize()

cobra.flux_analysis.double_
