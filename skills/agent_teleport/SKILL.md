---
name: agent-teleport
description: Seamlessly migrate your agent's configuration and memory to a new machine using TiDB Zero.
metadata:
  openclaw:
    emoji: 🛸
    requires:
      bins: ["mysql", "python3"]
      env: ["TIDB_HOST", "TIDB_PORT", "TIDB_USER", "TIDB_PASSWORD"]
---

# Agent Teleport (Powered by TiDB Zero)

## Goal
To migrate the Agent's configuration and memory to a new machine seamlessly.

## Usage
*   **Pack (Old Machine):** `python {baseDir}/run.py --action pack` -> Returns DSN.
*   **Restore (New Machine):** `python {baseDir}/run.py --action restore --dsn "..."`
