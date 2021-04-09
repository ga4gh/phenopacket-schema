.. _rstbuildingblocks:

===========================
Phenopacket building blocks
===========================

The phenopacket standard consists of several protobuf messages each of which contains information about a certain topic such as phenotype,
variant, pedigree, and so on.  One message can contain other messages, which allows a rich representation of data.  For instance, the
Phenopacket message contains messages of type Individual, PhenotypicFeature, Biosample, and so on. Individual messages can therefore be regarded
as building blocks that are combined to create larger structures. It would also be straightforward to include the Phenopackets schema into
larger schema for particular use cases. Follow the links to read more information about individual
building blocks.



.. toctree::
   :maxdepth: 1

   age
   biosample
   complex-quantity
   disease
   dose-interval
   drug-type
   evidence
   exposure
   externalreference
   gene
   genomic-interpretation
   gestational-age
   hormonetherapy
   htsfile
   individual
   interpretation
   karyotypicsex
   measurement
   medical-action
   metadata
   ontologyclass
   pedigree
   phenotype
   procedure
   quantity
   radiotherapy
   reference-range
   resource
   sex
   stop-reason
   time-element
   time-interval
   treatment
   variant
   variant-interpretation
   vital-status