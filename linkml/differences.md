# Differences that need a decision

Examples, from the four modules here, where v2's proto, phenopacket-tools' JSON Schema (the validator) and the Read the Docs pages disagree or are unclear. Converting to LinkML has to pick one answer for each so the schema can be generated; the answers below are placeholders until maintainers decide.

Some differences are broad (like "recommended" being in docs) while some are more nuanced and may need reconcilation (curie ids or any string?)

## 1. A resource's `version`: the docs say leave it blank, the validator rejects blank

- **What the sources say:** The docs say a resource without a release version should leave `version` blank ([resource.rst:108](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/docs/resource.rst#L108)). The validator requires `version` ([meta-data.json:85](https://github.com/phenopackets/phenopacket-tools/blob/7df8ecd/phenopacket-tools-validator-jsonschema/src/main/resources/org/phenopackets/phenopackettools/validator/jsonschema/v2/meta-data.json#L85)). Its command line reads the file into protobuf before checking, and protobuf drops an empty string, so a blank version is reported as missing (tested).
- **For now:** The LinkML requires a non-blank `version`, following the validator.
- **Question:** What should a resource with no release version put here? Fix the rule or the docs.

## 2. `MetaData.resources`: required in the docs, optional in the validator

- **What the sources say:** The docs table says `resources` is 1..* ([metadata.rst:33](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/docs/metadata.rst#L33)), so required. The validator's JSON Schema doesn't require it ([meta-data.json:41](https://github.com/phenopackets/phenopacket-tools/blob/7df8ecd/phenopacket-tools-validator-jsonschema/src/main/resources/org/phenopackets/phenopackettools/validator/jsonschema/v2/meta-data.json#L41)) and only asks for at least one entry when present ([meta-data.json:23](https://github.com/phenopackets/phenopacket-tools/blob/7df8ecd/phenopacket-tools-validator-jsonschema/src/main/resources/org/phenopackets/phenopackettools/validator/jsonschema/v2/meta-data.json#L23)); on its command line an empty list passes anyway, because protobuf drops it (tested). But its MetaData check reports any ontology term with no matching resource ([MetaDataValidator.java](https://github.com/phenopackets/phenopacket-tools/blob/7df8ecd/phenopacket-tools-validator-core/src/main/java/org/phenopackets/phenopackettools/validator/core/metadata/MetaDataValidator.java#L59-L60)), so in practice a phenopacket that uses ontology terms needs resources.
- **For now:** The LinkML makes it optional, with at least one entry when present.
- **Question:** Is `resources` required, or only required to cover the ontologies used? Should `[]` be allowed?

## 3. `OntologyClass.label`: only `id` is marked required in v2

- **What the sources say:** v2's comment marks `id` as REQUIRED ([base.proto:17](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/src/main/proto/phenopackets/schema/v2/core/base.proto#L17)) and says nothing about `label` ([base.proto:21](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/src/main/proto/phenopackets/schema/v2/core/base.proto#L21)). The validator requires both ([base.json:23](https://github.com/phenopackets/phenopacket-tools/blob/7df8ecd/phenopacket-tools-validator-jsonschema/src/main/resources/org/phenopackets/phenopackettools/validator/jsonschema/v2/base.json#L23)). phenopacket-tools also has a schema for recommended fields that lists `label` ([base-recommended.json:20](https://github.com/phenopackets/phenopacket-tools/blob/7df8ecd/phenopacket-tools-validator-jsonschema/src/main/resources/org/phenopackets/phenopackettools/validator/jsonschema/v2/base-recommended.json#L20)), but no code loads it.
- **For now:** The LinkML requires `label`, following the validator.
- **Question:** Is `label` required, or recommended? The proto comments suggest not required.

## 4. `Individual.alternate_ids`: CURIEs, or any string?

- **What the sources say:** The docs say alternate ids are CURIEs ([individual.rst:27](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/docs/individual.rst#L27)). The proto ([individual.proto:21](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/src/main/proto/phenopackets/schema/v2/core/individual.proto#L21)) and the validator accept any string.
- **For now:** The LinkML accepts any string, as the proto and validator do.
- **Question:** Should the CURIE form be enforced? Existing data could start failing.

## 5. RECOMMENDED exists only in the docs

- **What the sources say:** The docs mark `time_at_last_encounter` ([individual.rst:37](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/docs/individual.rst#L37)) and `vital_status` ([individual.rst:41](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/docs/individual.rst#L41)) as RECOMMENDED. Protobuf can't express this. phenopacket-tools gives no warning when they're missing (tested): its schema for recommended fields covers only OntologyClass and ExternalReference, and no code loads it. The same page's examples leave both out.
- **For now:** The LinkML marks them `recommended`, which warns when they're missing but doesn't reject.

## 6. Stale comments on `VitalStatus`

- **What the sources say:** Two v2 comments describe an older boolean field: `vital_status` "will default to 'false'" ([individual.proto:36](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/src/main/proto/phenopackets/schema/v2/core/individual.proto#L36)), and the `Status` enum's comment stops mid-sentence: "MUST be true if" ([individual.proto:57](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/src/main/proto/phenopackets/schema/v2/core/individual.proto#L57)). `status` is now an enum.
- **For now:** The LinkML keeps the comments word for word and applies no default.
- **Question:** How should these comments read? Generated docs would then show the fix.

## 7. Out-of-date examples on the Individual page

- **What the sources say:** Both Individual examples sit under `individual:` ([individual.rst:67](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/docs/individual.rst#L67)), but the Phenopacket field is `subject`. The file example uses v1's `htsFile` ([individual.rst:126](https://github.com/ga4gh/phenopacket-schema/blob/b4d1aa0/docs/individual.rst#L126)), with fields v2's File doesn't have.
- **For now:** The test cases in `examples/` check these examples as written; generated pages only show examples that pass.
- **Question:** Update the examples, and keep them as files a check runs on.
