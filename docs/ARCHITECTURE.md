# RedNode Architecture

## Core Layers

### 1. Operator Console

The primary control plane for runtime execution, telemetry visualization, target management, and evidence correlation.

### 2. Runtime Bridge

Coordinates execution flow between UI, orchestration systems, telemetry, and offensive engines.

### 3. Execution Governance Layer

Responsible for:

- authorization validation
- execution boundaries
- scope-awareness
- runtime safety
- trust propagation

### 4. HAR / Target Workspace

Stores:

- imported HAR files
- extracted endpoints
- target metadata
- session telemetry
- workspace state

### 5. Attack Surface Intelligence

Performs:

- endpoint extraction
- auth-context mapping
- API topology analysis
- behavioral fingerprinting

### 6. API / IDOR / Fuzzing Engines

Contains offensive execution modules responsible for:

- mutation generation
- response analysis
- IDOR workflows
- fuzzing operations
- anomaly detection

### 7. Chain Graph / Runtime Topology

Tracks:

- attack-chain propagation
- runtime execution flow
- finding correlation
- evidence lineage

### 8. Evidence Ledger

Maintains:

- evidence integrity
- finding snapshots
- telemetry archives
- execution records

### 9. Report Builder

Generates:

- technical reports
- executive reports
- remediation guidance
- attack scenarios

### 10. Future AI Runtime Security Intelligence

Future-oriented layer focused on:

- autonomous reasoning
- AI runtime analysis
- cognitive offensive security
- temporal exploit intelligence

