import cobra

# read the EC_model.xml file
EC_model = cobra.io.read_sbml_model('Paper_reconstructions/EC_model.xml')

rxns = [str(rxn).split(":")[0] for rxn in list(EC_model.reactions)]
genes = [str(gene) for gene in list(EC_model.genes)]

# effects of single gene deletion



