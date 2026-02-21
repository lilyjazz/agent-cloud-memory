# ☁️ Agent Cloud Memory

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)
[![Serverless](https://img.shields.io/badge/Serverless-TiDB%20Zero-pink.svg)](https://tidb.cloud)

**The Serverless "Soul" for AI Agents.**
*Give your agent persistence, mobility, and infinite memory in 30 seconds.*

</div>

> **The Problem:** AI Agents are like goldfish in a bowl. They have 7-second memories (Context Window) and are trapped in their local machine (Stateless).
>
> **The Solution:** Agent Cloud Memory gives them a **Cloud Soul**. It allows them to remember facts, teleport to new devices, and survive server crashes.

---

## ⚡️ Quick Links

| Skill | Superpower | Metaphor |
| :--- | :--- | :--- |
| **[🧳 Agent Teleport](skills/agent_teleport)** | **Migration** | *Save State / Load State* |
| **[🧠 Hive Mind](skills/hive_mind)** | **Sync Preference** | *iCloud Keychain* |
| **[📚 Knowledge Vault](skills/knowledge_vault)** | **Vector RAG** | *Private Library* |
| **[📼 Black Box](skills/black_box)** | **Audit Logs** | *Flight Data Recorder* |

---

## 📦 The 4 Superpowers (Deep Dive)

### 1. 🧳 Agent Teleport (Soul Transfer)
> *The "Save Game" for Work.*

*   **Metaphor:** Like **saving your game state** before a boss fight, or moving your save file to a new console.
*   **Use Case:** You worked on a project on your Office PC. Now you're at a coffee shop with your Laptop.
*   **Action:**
    *   *Office:* "Teleport Pack." -> Generates a Code.
    *   *Laptop:* "Teleport Restore [Code]." -> **Boom!** Your files, memory, and personality are instantly restored.

### 2. 🧠 Hive Mind (Cloud Synapse)
*   **Metaphor:** Like **iCloud Keychain** for your Agent's preferences.
*   **Use Case:** Your Desktop Agent learned that you hate "verbose code". Your Mobile Agent shouldn't need to be told again.
*   **Action:**
    *   *Agent A:* Saves preference `style="terse"` to Hive Mind.
    *   *Agent B:* Reads `style` from Hive Mind on startup.
    *   **Result:** All your agents act like a single, unified consciousness.

### 3. 📚 Knowledge Vault (Infinite Library)
*   **Metaphor:** A **Private Library** with a semantic librarian.
*   **Use Case:** You feed the Agent 100 PDF contracts. A week later, you ask: "Which contract had the 30-day clause?"
*   **Action:**
    *   Agent stores text embeddings in the Vault.
    *   Agent queries the Vault using vector search.
    *   **Result:** It retrieves the exact paragraph instantly from its long-term storage.

### 4. 📼 Black Box (Flight Recorder)
*   **Metaphor:** The **Flight Data Recorder** on an airplane.
*   **Use Case:** You sent an Agent to update your production server overnight. You wake up, and the server is dead. Local logs are gone.
*   **Action:**
    *   The Agent streamed its last thoughts to the Black Box (TiDB Cloud) *before* it crashed.
    *   You open the DB and see the last command: `rm -rf /` (Oops).
    *   **Result:** You know exactly what happened.

---

## 🚀 Quick Start

No Docker. No Sign-up. Just Python.

```bash
# 1. Install
pip install pymysql google-genai

# 2. Use Hive Mind (Example)
python skills/hive_mind/run.py --action set --key "my_name" --value "Lux"
```

## 🏗 Architecture

*   **Zero Config:** Uses TiDB Cloud Zero API to provision serverless databases on-the-fly.
*   **Ephemeral:** Resources auto-recycle after 30 days (Perfect for working memory).
*   **Standardized:** All skills output strict JSON.

---

**License:** MIT
