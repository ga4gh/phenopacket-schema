# examples/

The YAML examples from the current `docs/individual.rst`, copied as written. Each is validated against `generated/phenopackets.schema.json` as the v2 class its key names.

| File | Source | What it shows | Expected | Result | Warnings |
| --- | --- | --- | --- | --- | --- |
| `individual-rst-lines-67-70.yaml` | Lines 67-70, as written | The docs' Individual example, read as v2's Individual | valid | valid | `PXF-REC-INDIVIDUAL-TIME-AT-LAST-ENCOUNTER`, `PXF-REC-INDIVIDUAL-VITAL-STATUS` |
| `individual-rst-lines-117-120.yaml` | Lines 117-120, as written | The docs' Individual example, read as v2's Individual | valid | valid | `PXF-REC-INDIVIDUAL-TIME-AT-LAST-ENCOUNTER`, `PXF-REC-INDIVIDUAL-VITAL-STATUS` |
| `individual-rst-lines-126-132.yaml` | Lines 126-132, as written | v1's HtsFile example, read as v2's File, which has no `description`, `htsFormat` or `genomeAssembly`, and names `individualToSampleIdentifiers` `individualToFileIdentifiers` | `PXF-CLOSED-FILE` | `PXF-CLOSED-FILE` | `PXF-REC-FILE-INDIVIDUAL-TO-FILE-IDENTIFIERS` |

- Warnings mark missing fields that the docs recommend; they don't make an example invalid.
- `htsFile` is v1's name; v2 calls it `File`.
- In a v2 Phenopacket, an Individual sits under `subject`, not `individual`, and files sit under `files`.
