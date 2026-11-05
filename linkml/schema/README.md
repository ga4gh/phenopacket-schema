# schema/

Curated LinkML for the proof of concept, one module per v2 `.proto` file. These files are generated; nobody edits them by hand.

| File | Contents |
| --- | --- |
| `phenopackets.yaml` | `Phenopacket` |
| `base.yaml` | `OntologyClass`, `ExternalReference`, `Evidence`, `Procedure`, `GestationalAge`, `Age`, `AgeRange`, `TimeInterval`, `TimeElement`, `File`, `FileIndividualToFileIdentifiersEntry`, `FileFileAttributesEntry` |
| `individual.yaml` | `Individual`, `VitalStatus`, `VitalStatusStatus`, `Sex`, `KaryotypicSex` |
| `meta_data.yaml` | `MetaData`, `Resource`, `Update` |

## Origin

- **Imported** from `src/main/proto` at `b4d1aa0`. The import keeps names, field numbers (`rank`), JSON names (`alias`), comments (`description`) and oneofs. Each element's v2 name is in `proto_ref`.
- **Curated by code:** evidence rules read phenopacket-tools' JSON Schema (required fields, patterns, uniqueness) and the Read the Docs tables (recommended fields) and change the matching fields; recorded decisions cover rulings and exceptions. The rules and decisions live in phenopacket-linkml.
- **Trimmed:** `phenopackets.yaml` keeps only Phenopacket's `id`, `subject` and `meta_data`.

The record of each change, with its evidence, stays with the curation code in phenopacket-linkml. Where the sources disagree, see [`../differences.md`](../differences.md).
