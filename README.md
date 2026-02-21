# ☁️ Agent Cloud Memory

**The Serverless "Soul" for AI Agents.**
*Powered by [TiDB Cloud Zero](https://tidb.cloud).*

> **The Problem:** AI Agents are like goldfish in a bowl. They have 7-second memories (Context Window) and are trapped in their local machine (Stateless).
>
> **The Solution:** Agent Cloud Memory gives them a **Cloud Soul**. It allows them to remember facts, teleport to new devices, and survive server crashes.

---

## 📦 The 4 Superpowers (Skills)

### 1. 🧳 Agent Teleport (Soul Transfer)
> *The "Time Machine" Backup.*

*   **Metaphor:** Like **saving your game** in an RPG, or **Apple Time Machine**.
*   **Use Case:** You worked on a project on your Office PC. Now you're at a coffee shop with your Laptop. You don't want to start over.
*   **Action:**
    *   *Office:* "Teleport Pack." -> Generates a Code.
    *   *Laptop:* "Teleport Restore [Code]." -> **Boom!** Your files, memory, and personality are instantly restored.

### 2. 🧠 Hive Mind (Cloud Synapse)
*   **Metaphor:** Like **iCloud Sync** for your Agent's brain.
*   **Use Case:** Your Desktop Agent learned that you hate "verbose code". Your Mobile Agent shouldn't need to be told again.
*   **Action:**
    *   *Agent A:* Saves preference `style="terse"` to Hive Mind.
    *   *Agent B:* Reads `style` from Hive Mind on startup.
    *   **Result:** All your agents act like a single, unified consciousness.

### 3. 📚 Knowledge Vault (Infinite Library)
*   **Metaphor:** A **Search Engine** inside your Agent's head.
*   **Use Case:** You feed the Agent 100 PDF contracts. A week later, you ask: "Which contract had the 30-day clause?"
*   **Action:**
    *   Agent stores text embeddings in the Vault.
    *   Agent queries the Vault using vector search.
    *   **Result:** It recalls the exact paragraph instantly, without re-reading the files.

### 4. 📼 Black Box (Flight Recorder)
*   **Metaphor:** The **Black Box** on an airplane.
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
