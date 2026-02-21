import unittest
import os
import sys
import shutil
import subprocess
import json
import time

# Paths
# __file__ = agent-cloud-memory/tests/e2e_two_agents.py
# dirname = agent-cloud-memory/tests
# .. = agent-cloud-memory
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
SKILLS_DIR = os.path.join(REPO_ROOT, 'skills')
ENV_PYTHON = sys.executable # Use current python

class TwoAgentSimulation(unittest.TestCase):
    
    def setUp(self):
        # Create isolated workspaces for Agent A and Agent B
        self.work_a = os.path.abspath("sim_agent_a")
        self.work_b = os.path.abspath("sim_agent_b")
        
        # Cleanup first
        if os.path.exists(self.work_a): shutil.rmtree(self.work_a)
        if os.path.exists(self.work_b): shutil.rmtree(self.work_b)
        
        os.makedirs(self.work_a)
        os.makedirs(self.work_b)
        
        # Copy skills to both agents (installing skills)
        shutil.copytree(SKILLS_DIR, os.path.join(self.work_a, 'skills'))
        shutil.copytree(SKILLS_DIR, os.path.join(self.work_b, 'skills'))

    def tearDown(self):
        # Cleanup workspaces
        if os.path.exists(self.work_a): shutil.rmtree(self.work_a)
        if os.path.exists(self.work_b): shutil.rmtree(self.work_b)

    def run_skill(self, work_dir, skill_name, args):
        """Simulate an Agent running a tool in their workspace."""
        script = os.path.join(work_dir, 'skills', skill_name, 'run.py')
        cmd = [ENV_PYTHON, script] + args
        
        # Capture DSN files created in that workspace to simulate local config
        env = os.environ.copy()
        # Mock HOME to keep DSN files inside the isolated workspace
        env['HOME'] = work_dir 
        
        res = subprocess.run(cmd, cwd=work_dir, env=env, capture_output=True, text=True)
        if res.returncode != 0:
            raise Exception(f"Agent crashed: {res.stderr}")
        try:
            return json.loads(res.stdout)
        except:
            raise Exception(f"Invalid JSON from Agent: {res.stdout}")

    def test_hive_mind_sync(self):
        print("\n--- Test: Hive Mind (Sync) ---")
        # Agent A: Sets preference
        print("Agent A: Setting 'theme' = 'matrix_green'")
        res_a = self.run_skill(self.work_a, 'hive_mind', ['--action', 'set', '--key', 'theme', '--value', 'matrix_green'])
        self.assertTrue(res_a['success'])
        
        # Simulating Cloud Sync:
        # In reality, Agent A would give Agent B the DSN connection string.
        # Or they share the same ~/.openclaw_hive_mind_dsn file via sync.
        # Here we manually copy the DSN file from A to B to simulate "User provided the DSN" or "Shared Config".
        dsn_file_a = os.path.join(self.work_a, '.openclaw_hive_mind_dsn')
        dsn_file_b = os.path.join(self.work_b, '.openclaw_hive_mind_dsn')
        shutil.copy(dsn_file_a, dsn_file_b)
        
        # Agent B: Gets preference
        print("Agent B: Reading 'theme'...")
        res_b = self.run_skill(self.work_b, 'hive_mind', ['--action', 'get', '--key', 'theme'])
        
        print(f"Agent B saw: {res_b.get('value')}")
        self.assertEqual(res_b.get('value'), 'matrix_green')

    def test_agent_teleport(self):
        print("\n--- Test: Agent Teleport (Migration) ---")
        # Agent A: Creates a memory file
        secret_file = os.path.join(self.work_a, 'secret_plans.txt')
        with open(secret_file, 'w') as f:
            f.write("World Domination")
            
        # Agent A: Packs up
        print("Agent A: Teleporting out...")
        res_a = self.run_skill(self.work_a, 'agent_teleport', ['--action', 'pack'])
        self.assertTrue(res_a['success'])
        teleport_code = res_a['teleport_code']
        print(f"Transfer Code: {teleport_code}")
        
        # Agent B: Restores (Empty workspace initially)
        print("Agent B: Teleporting in...")
        res_b = self.run_skill(self.work_b, 'agent_teleport', ['--action', 'restore', '--dsn', teleport_code])
        self.assertTrue(res_b['success'])
        
        # Verify file exists in B
        restored_file = os.path.join(self.work_b, 'secret_plans.txt')
        self.assertTrue(os.path.exists(restored_file))
        with open(restored_file, 'r') as f:
            content = f.read()
        print(f"Agent B found file content: {content}")
        self.assertEqual(content, "World Domination")

    def test_knowledge_vault_rag(self):
        print("\n--- Test: Knowledge Vault (RAG) ---")
        # Check API Key
        if not os.environ.get("GEMINI_API_KEY"):
            print("Skipping (No API Key)")
            return

        # Agent A: Learns something weird
        fact = "The moon is made of cheese."
        print(f"Agent A: Memorizing '{fact}'")
        res_a = self.run_skill(self.work_a, 'knowledge_vault', ['--action', 'add', '--content', fact])
        self.assertTrue(res_a['success'])
        
        # Share DSN (Simulate user giving Agent B access to the same brain)
        dsn_file_a = os.path.join(self.work_a, '.openclaw_knowledge_vault_dsn')
        dsn_file_b = os.path.join(self.work_b, '.openclaw_knowledge_vault_dsn')
        shutil.copy(dsn_file_a, dsn_file_b)
        
        # Agent B: Asks question
        query = "What material is the moon?"
        print(f"Agent B: Asking '{query}'")
        res_b = self.run_skill(self.work_b, 'knowledge_vault', ['--action', 'search', '--query', query])
        
        top_answer = res_b['results'][0]['content']
        print(f"Agent B retrieved: {top_answer}")
        self.assertIn("cheese", top_answer)

    def test_black_box_audit(self):
        print("\n--- Test: Black Box (Audit) ---")
        # Agent A: Logs a crash
        print("Agent A: Logging fatal error...")
        res_a = self.run_skill(self.work_a, 'black_box', ['--action', 'log', '--level', 'FATAL', '--message', 'Kernel Panic'])
        
        # Share DSN (Auditor access)
        dsn_file_a = os.path.join(self.work_a, '.openclaw_black_box_dsn')
        dsn_file_b = os.path.join(self.work_b, '.openclaw_black_box_dsn')
        shutil.copy(dsn_file_a, dsn_file_b)
        
        # Agent B (Auditor): Reads logs
        print("Agent B: Auditing logs...")
        res_b = self.run_skill(self.work_b, 'black_box', ['--action', 'read'])
        
        logs = res_b['logs']
        print(f"Auditor found: {logs[0]['msg']}")
        self.assertEqual(logs[0]['msg'], 'Kernel Panic')

if __name__ == '__main__':
    unittest.main()
