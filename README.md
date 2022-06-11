# enrichment_utils

### Introduction

This repository contains enrichment_utils, a package providing convenience functions which wrap around the useful [goatools](https://github.com/tanghaibao/goatools) package. It is designed specifically to allow gene set enrichment to be performed on single-cell datasets in [anndata](https://anndata.readthedocs.io/en/latest/) format, analysed using [CDR-g](https://cdr-g.readthedocs.io/en/latest/) (CDR-genomics) package.

### Installation

Install this package via PyPI. Alternatively, it comes bundled with CDR-g's [docker](https://hub.docker.com/repository/docker/wlc27/pycdr_jupyter) image. 

    pip install enrichment_utils

### Usage

After processing by CDR-g, enrichment_utils can be run to functionally annotate gene sets produced by CDR-g. 

    from enrichment_utils.ontology_analysis import analyse_adata

    analyse_adata(mono, INPUT_FILE_ONTOLOGY, INPUT_FILE_GENE2GO, SPECIES, ontology_subset = ONTOLOGY_SUBSET)

### References

1. Klopfenstein, D. V., Zhang, L., Pedersen, B. S., Ramírez, F., Warwick Vesztrocy, A., Naldi, A., Mungall, C. J., Yunes, J. M., Botvinnik, O., Weigel, M., Dampier, W., Dessimoz, C., Flick, P., & Tang, H. (2018). GOATOOLS: A Python library for Gene Ontology analyses. Scientific reports, 8(1), 10872. https://doi.org/10.1038/s41598-018-28948-z
