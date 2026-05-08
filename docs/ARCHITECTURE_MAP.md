# RedNode Architecture Map

RedNode is structured as a runtime-aware offensive security intelligence platform.

This document maps the internal architectural concepts into a public-safe view.

---

## High-Level Architecture

| Layer | Public Description |
|---|---|
| Operator Console | Human-facing control plane for target context, telemetry, runtime state, and evidence review. |
| Runtime Bridge | Connects operator actions, backend execution, telemetry flow, and runtime chain graph updates. |
| Execution Governance Layer | Controls execution mode, authorization boundaries, scope validation, human review, and safety state. |
| Runtime Intelligence | Tracks execution state, queue pressure, health, telemetry status, and runtime decisions. |
| Event Bus / Telemetry | Propagates runtime events, execution state changes, findings, and signal updates. |
| Attack Surface Intelligence | Extracts endpoints, classifies parameters, maps API structure, and builds attack surface context. |
| Attack Intelligence Overlay | Correlates signals into chains, hypotheses, runtime graph nodes, and reviewable findings. |
| Evidence Ledger | Maintains traceability between observations, telemetry, signals, and reportable evidence. |
| Reporting Layer | Converts validated findings and runtime evidence into technical and executive reporting. |

---

## Runtime Intelligence Topology

```text
Operator Console
      |
      v
Runtime Bridge
      |
      v
Execution Governance Layer
      |
      v
Runtime Intelligence Engine
      |
      +--> Event Bus / Telemetry Stream
      |
      +--> Runtime Chain Graph
      |
      +--> Attack Intelligence Overlay
      |
      +--> Evidence Ledger
      |
      v
Human Review / Report Generation
