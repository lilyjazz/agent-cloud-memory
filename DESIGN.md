# System Design: Agent Cloud Memory

This document outlines the architecture, security model, and data flow of the Agent Cloud Memory system.

---

## 🏗 High-Level Architecture

The system follows a **Client-Serverless** model. The Agent (Client) interacts directly with ephemeral TiDB Zero instances (Serverless) via standard MySQL protocols.

```mermaid
graph TD
    A["Agent (Local)"] -->|Provision curl| B["TiDB Cloud API"]
    B -->|Returns DSN| A
    A -->|SQL pymysql| C["TiDB Zero Database"]
    
    subgraph "Skill: Hive Mind"
    A -- "SET key=val" --> C
    A -- "GET key" --> C
    end
    
    subgraph "Skill: Teleport"
    A -- "Pack tar.gz" --> C
    C -- "Restore blob" --> D["New Agent (Remote)"]
    end
```

---

## 🔒 Security Model

### 1. DSN as Capability Token
We use the **Object-Capability Model**.
*   The Connection String (DSN) `mysql://user:pass@host:4000/db` acts as a **Bearer Token**.
*   Anyone who possesses the DSN has full access to that specific memory context.
*   **Storage:** The DSN is stored locally in `~/.openclaw_<skill>_dsn` with user-only read permissions (`0600`).

### 2. Ephemeral by Design
*   **TTL:** All databases automatically expire and are securely wiped after **30 days**.
*   **Impact:** This system is for *Working Memory* (active context), not *Cold Storage* (archival).
*   **Benefit:** Reduces data liability. "Data you don't have can't be leaked."

### 3. Client-Side Encryption (Optional Future)
*   Currently, data is stored in plain text/blob in the DB.
*   *Future Work:* Agent can encrypt blobs with a local symmetric key before INSERTing, ensuring TiDB Cloud sees only opaque data.

---

## 💾 Data Schema Strategy

### 1. Key-Value Store (`hive_mind`)
Optimized for frequent, small reads/writes.
```sql
CREATE TABLE user_prefs (
    pref_key VARCHAR(255) NOT NULL PRIMARY KEY,
    pref_value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### 2. Blob Store (`agent_teleport`)
Optimized for infrequent, large throughput.
```sql
CREATE TABLE teleport (
    id INT PRIMARY KEY,
    data LONGBLOB, -- Supports up to 4GB (theoretical), constrained by packet size
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
*Note:* The Python client uses in-memory `io.BytesIO` buffering. Large workspaces (>100MB) are currently rejected to prevent OOM.

### 3. Vector Store (`knowledge_vault`)
Optimized for semantic search.
```sql
CREATE TABLE knowledge_vault (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    embedding VECTOR(3072), -- Matches Gemini Embedding dimensions
    created_at TIMESTAMP
);
```

---

## ⚠️ Limitations & Trade-offs

| Limitation | Impact | Workaround |
| :--- | :--- | :--- |
| **No Multi-Statement** | Cannot execute dump files with `;` in one go. | Client parses and executes sequentially. |
| **30-Day Life** | Memory is lost after a month of inactivity. | Agent must "refresh" or export data if long-term storage is needed. |
| **Public Endpoint** | DB is accessible from 0.0.0.0/0. | Security relies entirely on strong password complexity (handled by TiDB). |

---

## 🔄 Data Flow: The Teleport Protocol

1.  **Pack Phase:**
    *   Agent scans `cwd`.
    *   Filters ignore list (`.git`, `node_modules`).
    *   Creates `tar.gz` in RAM.
    *   Provisions DB -> `INSERT INTO teleport`.
    *   Returns DSN to user.

2.  **Transfer Phase:**
    *   User copies DSN string (via secure channel like Signal/Pastebin).

3.  **Restore Phase:**
    *   User inputs DSN.
    *   Agent connects -> `SELECT data`.
    *   Validates Archive (Check for `../` Zip Slip).
    *   Extracts to `cwd`.
