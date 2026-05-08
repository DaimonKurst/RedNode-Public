# RedNode Execution Pipeline

TARGET_INIT
→ HAR_UPLOAD
→ ENDPOINT_EXTRACTION
→ ATTACK_SURFACE_MAPPING
→ AUTH_CONTEXT_ANALYSIS
→ IDOR/API_MUTATION
→ SIGNAL_DETECTION
→ CHAIN_CORRELATION
→ EVIDENCE_CAPTURE
→ HUMAN_REVIEW
→ REPORT_GENERATION

---

## Pipeline Philosophy

RedNode treats vulnerabilities as dynamic execution chains instead of isolated findings.

The system focuses on:

- behavioral analysis
- runtime correlation
- authorization integrity
- evidence-aware execution
- telemetry-driven reasoning

