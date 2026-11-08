# Contributing

Short version; the full processes are in [`governance/`](governance/README.md).

1. **Research first.** Record findings in `research/findings/<topic>.md` using `research/FINDINGS-FORMAT.md`. Cite only pages you opened.
2. **Synthesize into the right place.** Principles → `principles/`; recurring design problems → `patterns/<scope>/`; objective requirements → `rubric/quality-gates.md`; publisher details → `sources/`.
3. **Follow the schema.** See `patterns/README.md` and `principles/README.md`. Stable IDs, never reused (`governance/pattern-lifecycle.md`).
4. **Classify evidence** with E1–E5 (`sources/evidence-classes.md`). Only normative standard text is E1.
5. **Validate** before opening a PR:
   ```bash
   python3 scripts/validate.py --write-index
   python3 scripts/validate.py --check-urls   # optional, network
   ```
6. **Open a PR** with the template filled in. Significant changes need maintainer approval and, if architectural, an ADR in `governance/decisions/`.
7. **After merge**, refresh the OpenViking resource (`integration/openviking.md` §4) and run the retrieval tests (`examples/retrieval-tests.md`).

Agents are welcome contributors. Disclose the model used. Agent PRs are never auto-merged.
