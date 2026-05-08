# RedNode Attack Flow

HAR_ANALYSIS
→ ENDPOINT_EXTRACTION
→ PARAMETER_CLASSIFICATION
→ IDENTITY_BOUNDARY_GUESS
→ MUTATION_PLAN
→ SAFE_EXECUTION_GATE
→ RESPONSE_DIFF_ANALYSIS
→ FINDING_CANDIDATE
→ EVIDENCE_LINKAGE
→ CHAIN_NODE_UPDATE

---

## Key Concepts

### Identity Boundary Guessing

RedNode attempts to infer trust boundaries between identities, tenants, sessions, and authorization layers.

### Runtime Correlation

Findings are correlated across telemetry, response mutations, and attack-chain topology.

### Human Review Gates

Potential findings are escalated through safety and verification checkpoints before final reporting.

