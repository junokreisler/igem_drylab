import cobra

#########################
# Helper functions for analysis of the model
#########################

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

def gene_rxn_ko_res(gene_or_rxn, list_of_str, model = EC_model):
    # knocks out the gene(s) or reaction(s) of choice, saves results
    try:
        if gene_or_rxn == "gene":
            # save boundaries on gene reacts, do KO, reset boundaries
        if gene_or_rxn == "reaction" or "rxn":
            # save boundaries on reacts, do KO, reset boundaries
    except ValueError:
        print("gene_or_rxn should be 'gene' for gene KOs and 'reaction' or 'rxn' for reaction KOs. \n")

    return 0 # solution object, print EX_Lac__D_e"