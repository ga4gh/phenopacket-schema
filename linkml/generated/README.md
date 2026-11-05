# generated/

Generated from `schema/` with LinkML 1.12.1.

| File | Made by |
| --- | --- |
| `proto/` | A custom generator (151 lines) that keeps v2's names, numbers, comments, oneofs and file layout |
| `stock-gen-proto.proto` | LinkML's `gen-proto`, for comparison |
| `phenopackets.schema.json` | `gen-json-schema`, plus `uniqueItems`, which it omits |

## Check

Compared with v2's protos, cut to the same scope:
- **Compared:** 87 elements, including 18 messages and 62 fields.
- **Differences:** 0.
- **Comments:** all 60 of v2's comments come back word for word. Only spacing changes, such as `//for` becoming `// for`.
- **`buf breaking`:** WIRE 0, WIRE_JSON 0, FILE 0.

protoc warns that `phenopackets.proto` doesn't use its `base.proto` import. v2's file, trimmed the same way, gets the same warning.
