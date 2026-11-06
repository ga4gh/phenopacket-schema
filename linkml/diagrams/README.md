# diagrams/

`5-flow.mmd` (Mermaid source) and `5-flow.svg` show the flow:
1. The v2 protos are imported into draft LinkML.
2. The drafts are curated into the LinkML source by code that applies evidence rules (from phenopacket-tools' JSON Schema and the docs tables) and recorded decisions.
3. The outputs are generated from it.
4. The outputs are compared with v2.

`6-review-loop.mmd` and `6-review-loop.svg` show the proposed next step:
1. Curation and the checks find where the sources disagree, or a comment is unclear.
2. The differences are listed by module and field, as in `differences.md`.
3. AM and MMT create GitHub issues.
4. Maintainers decide on contradictory or unclear points. The process can vary: for example, MMT plans the issue, AM opens a PR, and people decide in its review.
5. AM records each decision; the curation code applies it, and AM updates the current v2 docs.

This proof of concept covers the import, curation, the `.proto`, the JSON Schema and the docs. The full study also generates Python classes and runs every evaluation layer.
