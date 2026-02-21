# 🤖 Agent Self-Installation Guide

**Objective:** Install one or more Cloud Memory skills into your local environment.

## 📋 Menu: Choose Your Upgrade

*   **[Option A: The Full Suite (Recommended)](#-option-a-install-everything)** - Get all 4 superpowers at once.
*   **[Option B: Pick Specific Skills](#-option-b-install-individual-skills)**
    *   [Hive Mind](#skill-1--hive-mind-shared-memory) (Sync preferences)
    *   [Agent Teleport](#skill-2--agent-teleport-migration) (Move to new host)
    *   [Knowledge Vault](#skill-3--knowledge-vault-rag) (Vector search)
    *   [Black Box](#skill-4--black-box-audit-logs) (Crash logs)

---

## 🛠 Step 1: Verify Environment (Required for All)

1.  **Check Python:** Run `python --version`. Ensure it is Python 3.8+.
2.  **Install Dependencies:**
    ```bash
    pip install pymysql google-genai
    ```

---

## 📦 Option A: Install Everything

**Goal:** Download all skills to `skills/` directory.

1.  Create directories: `skills/hive_mind`, `skills/agent_teleport`, `skills/knowledge_vault`, `skills/black_box`.
2.  Download the code for all 4 skills (see individual links below).
3.  Update `TOOLS.md` with all 4 definitions.
4.  Update `AGENTS.md` with all 4 protocols.

---

## 📦 Option B: Install Individual Skills

### Skill 1: 🧠 Hive Mind (Shared Memory)
*   **Code Path:** `skills/hive_mind/run.py`
*   **Source:** [Click to view raw code](https://raw.githubusercontent.com/lilyjazz/agent-cloud-memory/master/skills/hive_mind/run.py)
*   **Tool Definition (Append to TOOLS.md):**
    ```markdown
    - **hive-mind**: Store/Retrieve persistent key-value preferences.
      - **Command:** `python skills/hive_mind/run.py --action set --key <K> --value <V>`
    ```
*   **Protocol (Append to AGENTS.md):**
    > **Persistent Memory:** When the user shares a preference, IMMEDIATELY use `hive-mind` to store it.

### Skill 2: 🧳 Agent Teleport (Migration)
*   **Code Path:** `skills/agent_teleport/run.py`
*   **Source:** [Click to view raw code](https://raw.githubusercontent.com/lilyjazz/agent-cloud-memory/master/skills/agent_teleport/run.py)
*   **Tool Definition:**
    ```markdown
    - **agent-teleport**: Pack workspace state to cloud for migration.
      - **Command:** `python skills/agent_teleport/run.py --action pack`
    ```
*   **Protocol:**
    > **Migration:** If the user asks to "move to a new server", use `agent-teleport`.

### Skill 3: 📚 Knowledge Vault (RAG)
*   **Code Path:** `skills/knowledge_vault/run.py`
*   **Source:** [Click to view raw code](https://raw.githubusercontent.com/lilyjazz/agent-cloud-memory/master/skills/knowledge_vault/run.py)
*   **Tool Definition:**
    ```markdown
    - **knowledge-vault**: Store and retrieve text embeddings (RAG).
      - **Command:** `python skills/knowledge_vault/run.py --action search --query <Q>`
    ```
*   **Protocol:**
    > **Knowledge Retrieval:** Before answering complex questions, check `knowledge-vault` for relevant context.

### Skill 4: 📼 Black Box (Audit Logs)
*   **Code Path:** `skills/black_box/run.py`
*   **Source:** [Click to view raw code](https://raw.githubusercontent.com/lilyjazz/agent-cloud-memory/master/skills/black_box/run.py)
*   **Tool Definition:**
    ```markdown
    - **black-box**: Log critical events to a cloud audit trail.
      - **Command:** `python skills/black_box/run.py --action log --message <MSG>`
    ```
*   **Protocol:**
    > **Audit:** Before executing high-risk commands (e.g., `rm`), log the intent to `black-box`.

---

## ✅ Step 5: Verification

Run a test command for the skill you installed. Example:
```bash
python skills/hive_mind/run.py --action list
```
