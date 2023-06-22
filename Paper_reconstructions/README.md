# Reconstruction of the modeling done in papers

## Zhou et al. Metabolic engineering strategies for D-lactate over production in Escherichia coli
https://doi.org/10.1002/jctb.4856

Replication of the analysis was done using the COBRApy module. 

Relevant paragraphs:

### Effects of single gene deletion

> *The effects of the competing routes have primarily been identified by 
single gene deletions in wild type E. coli. The most effective gene deletions 
in improving lactate production are found to be the deletions of pflA/pflB 
(pyruvate formate lyase, but not pflC and pflD), ackA (acetate kinase) and pta 
(phosphotransacetylase).*

Delete either one of pflA, pflB, ackA, pta for best results.

Explanation:

> *Pyruvate formate lyase is the main decomposition 
pathway of pyruvate under anaerobic conditions, with formate and acetylcoenzyme A 
(acetyl-CoA) as the products [..] the phosphotransacetylase 
and acetate kinase catalyze the conversion of pyruvate via acetyl-CoA and 
acetyl-phosphate to acetate with ATP generation, which is the main pathway for 
acetate production in E. coli (Fig. 2). The deletions of pflA/pflB, ackA or 
pta genes significantly reduced the yields of acetate (by 53.5, 77.6 and 52.1%, 
respectively) and formate (by 100, 71 and 93.5%, respectively) and resulted 
in a decrease in ATP generation under the oxygen-limited condition. 
Consequently [..] higher D-lactate production **(lactate yield increased by 
39.6, 25.2 and 39.4%, respectively, in the pflA/pflB, ackA and pta mutants)** 
[..] *

![Figure 2](https://onlinelibrary.wiley.com/cms/asset/b4fb6804-e9fe-44ef-8847-1c1fac05dca5/jctb4856-fig-0002-m.jpg)

> A few minor helpful gene deletions were also investigated. 
Pyruvate oxidase (poxB) catalyzes the direct conversion of pyruvate to acetate. 
Despite the inactivation of poxB, the acetate accumulation did not change, 
indicating the gene's minor function in acetate synthesis; 
the D-lactate yield and productivity were slightly improved (by 7.9 and 4.5%, 
respectively) with the poxB mutant. These parameters could also be improved 
(by 14.2 and 9.1%, respectively) by the single-gene deletion of dld 
(FAD-binding D-lactate dehydrogenase is required for aerobic growth on D-lactate). 
The deletion of fumarate reductase (frdA), which catalyzes the conversion of 
fumarate to succinate, resulted in a significantly lower succinate yield 
(by 82.2%) but a slightly higher lactate yield (improved by 16.8%). 
On the other hand, although alcohol dehydrogenase (adhE) and 
phosphoenolpyruvate synthase (pps) are also in the competing routes, 
the deletions of these genes in wild type E. coli unfavourably affected lactate 
accumulation during the aerobic and oxygen-limited two-phase fermentation.

Evaluate effects of poxB, dld, frdA, adhE, pps, *ppc*

Note that ppsA has a regulatory protein ppsR (gene b1703) which is
not present in the FBA model. 
Therefore, knocking down b1703 might be helpful so that amino acids are
not wasted on a regulatory protein which won't have anything to work on.


> The single-gene deletion of phosphoenolpyruvate carboxylase (ppc) 
> significantly improved the lactate yield from glucose (by about 27-fold) 
> under microaerobic conditions with merely trace generation of succinate, 
> but the cells barely grew on the minimal media when glucose was used as 
> the sole carbon source, which is unfavourable in large scale fermentation.

### Effects of multiple gene deletions



## Fong et al. In silico design and adaptive evolution of Escherichia coli for production of lactic acid
https://doi.org/10.1002/bit.20542open_in_new