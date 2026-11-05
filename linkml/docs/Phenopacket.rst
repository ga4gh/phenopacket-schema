.. _rstphenopacket:

###########
Phenopacket
###########

An anonymous phenotypic description of an individual or biosample with potential genes of interest and/or diagnoses. This is a bundle of high-level concepts with no specifically defined relational concepts. It is expected that the resources sharing the phenopackets will define and enforce their own semantics and level of requirements for included fields.

**v2 element:** ``org.phenopackets.schema.v2.Phenopacket`` (`phenopackets/schema/v2/phenopackets.proto:24 <https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa05a2da874bb45b8bf47ff41678eab0338c/src/main/proto/phenopackets/schema/v2/phenopackets.proto#L24>`__)

Data model
##########

.. list-table:: Definition of the ``Phenopacket`` element
   :widths: 25 25 15 75
   :header-rows: 1

   * - Field
     - Type
     - Multiplicity
     - Description
   * - id
     - string
     - 1..1
     - An identifier specific for this phenopacket. REQUIRED.
   * - subject
     - :ref:`rstindividual`
     - 0..1
     - The individual representing the focus of this packet - e.g. the proband in rare disease cases or cancer patient RECOMMENDED.
   * - meta\_data (``metaData``)
     - :ref:`rstmetadata`
     - 1..1
     - Structured definitions of the resources and ontologies used within the phenopacket. REQUIRED REQUIRED.

Rules
#####

.. list-table::
   :widths: 40 15 60
   :header-rows: 1

   * - Rule
     - Severity
     - What it checks
   * - ``PXF-BLANK-PHENOPACKET-ID``
     - error
     - Phenopacket.id must not be blank
   * - ``PXF-CLOSED-PHENOPACKET``
     - error
     - Unknown field in Phenopacket
   * - ``PXF-REC-PHENOPACKET-SUBJECT``
     - warning
     - Phenopacket.subject is recommended
   * - ``PXF-REQ-PHENOPACKET-ID``
     - error
     - Phenopacket.id is required
   * - ``PXF-REQ-PHENOPACKET-META-DATA``
     - error
     - Phenopacket.metaData is required

