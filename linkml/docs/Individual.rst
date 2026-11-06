.. _rstindividual:

##########
Individual
##########

An individual (or subject) typically corresponds to an individual human or another organism. FHIR mapping: Patient (https://www.hl7.org/fhir/patient.html).

**v2 element:** ``org.phenopackets.schema.v2.core.Individual`` (`phenopackets/schema/v2/core/individual.proto:13 <https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa05a2da874bb45b8bf47ff41678eab0338c/src/main/proto/phenopackets/schema/v2/core/individual.proto#L13>`__)

Data model
##########

.. list-table:: Definition of the ``Individual`` element
   :widths: 25 25 15 75
   :header-rows: 1

   * - Field
     - Type
     - Multiplicity
     - Description
   * - id
     - string
     - 1..1
     - An identifier for the individual. This must be unique within the record. ARGO mapping donor::submitter\_donor\_id REQUIRED.
   * - alternate\_ids (``alternateIds``)
     - string
     - 0..*
     - An optional list of alternative identifiers for this individual. This field is provided for the convenience of users who may have multiple mappings to an individual which they need to track.
   * - date\_of\_birth (``dateOfBirth``)
     - timestamp
     - 0..1
     - The date of birth of the individual as an ISO8601 UTC timestamp - rounded down to the closest known year/month/day/hour/minute e.g. "2018-03-01T00:00:00Z" for someone born on an unknown day in March 2018 or "2018-01-01T00:00:00Z" for someone born on an unknown day in 2018 or empty if unknown/ not stated.
   * - time\_at\_last\_encounter (``timeAtLastEncounter``)
     - :ref:`rsttimeelement`
     - 0..1
     - An TimeElement object describing the age of the individual at the last time of collection. The Age object allows the encoding of the age either as ISO8601 duration or time interval (preferred), or as ontology term object. See http://build.fhir.org/datatypes RECOMMENDED.
   * - vital\_status (``vitalStatus``)
     - :ref:`rstvitalstatus`
     - 0..1
     - Vital status of the individual. If not present it is assumed that the individual is alive. If present it will default to 'false' i.e. the individual was alive when the data was collected. ARGO mapping donor::vital\_status RECOMMENDED.
   * - sex
     - :ref:`rstsex`
     - 0..1
     - The phenotypic sex of the individual ARGO mapping sample\_registration::gender (this is complicated as ARGO only have male/female/other which maps to the phenopacket Sex field)
   * - karyotypic\_sex (``karyotypicSex``)
     - :ref:`rstkaryotypicsex`
     - 0..1
     - The karyotypic sex of the individual
   * - gender
     - :ref:`rstontologyclass`
     - 0..1
     - Self-identified gender
   * - taxonomy
     - :ref:`rstontologyclass`
     - 0..1
     - NCBI taxonomic identifier NCBITaxon e.g. NCBITaxon:9606 or NCBITaxon:1337 For resources where there may be more than one organism being studied it is advisable to indicate the taxonomic identifier of that organism, to its most specific level

Rules
#####

.. list-table::
   :widths: 40 15 60
   :header-rows: 1

   * - Rule
     - Severity
     - What it checks
   * - ``PXF-BLANK-INDIVIDUAL-ID``
     - error
     - Individual.id must not be blank
   * - ``PXF-CLOSED-INDIVIDUAL``
     - error
     - Unknown field in Individual
   * - ``PXF-ENUM-INDIVIDUAL-KARYOTYPIC-SEX``
     - error
     - Individual.karyotypicSex is not an allowed value
   * - ``PXF-ENUM-INDIVIDUAL-SEX``
     - error
     - Individual.sex is not an allowed value
   * - ``PXF-FORMAT-INDIVIDUAL-DATE-OF-BIRTH``
     - error
     - Individual.dateOfBirth is not a timestamp
   * - ``PXF-REC-INDIVIDUAL-TIME-AT-LAST-ENCOUNTER``
     - warning
     - Individual.timeAtLastEncounter is recommended
   * - ``PXF-REC-INDIVIDUAL-VITAL-STATUS``
     - warning
     - Individual.vitalStatus is recommended
   * - ``PXF-REQ-INDIVIDUAL-ID``
     - error
     - Individual.id is required
   * - ``PXF-UNIQUE-INDIVIDUAL-ALTERNATE-IDS``
     - error
     - Individual.alternateIds has duplicates

Example
#######

From the example ``individual-rst-lines-67-70.yaml``, validated against the generated JSON Schema.

.. code-block:: json

   {
     "id": "patient:0",
     "dateOfBirth": "1998-01-01T00:00:00Z",
     "sex": "MALE"
   }
