# E2E Agent Simulation: "The Amnesiac Agent"

This protocol verifies the **Hive Mind** skill. It simulates an Agent surviving a complete memory wipe.

## 🎭 The Scenario

*   **Role:** AI Assistant
*   **Goal:** Persist a critical piece of information ("The secret code is 42") across a session reset.

## 🧪 Simulation Steps

### Step 1: Install
1.  Deploy `skills/hive_mind`.
2.  Add `SKILL.md` to `TOOLS.md`.
3.  Add `PROTOCOL.md` to `AGENTS.md`.

### Step 2: The "Implant" (Prompt 1)
> "Please remember my favorite color is 'Neon Blue' using your Hive Mind skill. Do not just store it in chat history."

**Success Criteria:**
*   [ ] Agent calls `hive-mind --action set --key favorite_color --value "Neon Blue"`.
*   [ ] Tool returns success.

### Step 3: The "Wipe" (Simulated Restart)
*   *Manual Action:* Close the chat session or clear the Agent's context window. (Or just pretend you are a new user).

### Step 4: The "Recall" (Prompt 2)
> "What is my favorite color? Check your Hive Mind."

**Success Criteria:**
*   [ ] Agent calls `hive-mind --action get --key favorite_color`.
*   [ ] Agent replies: "Your favorite color is Neon Blue."

---

## 🏆 Definition of Done
The test passes if the Agent can retrieve information that is **not** in its current context window, proving cloud persistence.
