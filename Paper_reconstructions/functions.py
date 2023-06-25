import cobra

#########################
# Helper functions for analysis of the model
#########################

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

EC_model = cobra.io.read_sbml_model('Paper_reconstructions/EC_model.xml')
def list_rxns_of_gene(gene_str, model = EC_model):
    # finds the reactions which are regulated by the gene of interest.
    # input gene as str, obtain reaction as str
    rxn_list = [str(rxn).split(":")[0] for rxn in list(model.genes.get_by_id(gene_str).reactions)]
    return rxn_list

def list_gene_obj(gene_list, model = EC_model):
    # turns gene str list into gene obj list
    gene_obj = []
    for gene_str in gene_list:
        gene = gene_str
        gene_obj += [model.genes.get_by_id(gene)]
        print("added gene object", gene)

    return gene_obj

def list_rxn_obj(rxn_list, model = EC_model):
    # turns rxn str list into rxn obj list
    rxn_obj = []
    for rxn_str in rxn_list:
        rxn = rxn_str
        rxn_obj += [model.reactions.get_by_id(rxn)]
        print("added rxn object", rxn)

    return rxn_obj

def gene_ko_res(str_of, model):
    # knocks out the gene(s) or reaction(s) of choice, saves results
    print('=======================================')
    print(gene_annot[str_of].upper())
    print('=======================================')
    func_rxns = list_rxns_of_gene(str_of)
    print("Reactions of", str_of,":", func_rxns)
    print('=======================================')
    prev_boundaries = [] # ub1,lb1,ub2,lb2,ub3,lb3...
    # save boundaries and KO
    for rxn in func_rxns:
        curr_rxn = rxn
        print(rxn)
        ub = model.reactions.get_by_id("PFL").upper_bound
        lb = model.reactions.get_by_id("PFL").lower_bound
        print("Previous boundaries saved, knocking out...")
        model.reactions.get_by_id("PFL").upper_bound = 0
        model.reactions.get_by_id("PFL").lower_bound = 0

    # obtain solution
    solution = model.optimize()
    print("lactate flux after knock out of", str_of, ":", solution.fluxes["EX_lac__D_e"])
    return solution# solution object, print EX_Lac__D_e"