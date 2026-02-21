import unittest
import os
import sys
import json

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from skills.black_box import run as bb

class TestBlackBoxLive(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Reset DSN to force fresh DB
        dsn_file = os.path.expanduser("~/.openclaw_black_box_dsn")
        if os.path.exists(dsn_file):
            os.remove(dsn_file)
        print("\n[E2E] Init Black Box DB...")

    def test_log_and_read(self):
        print("Test: Logging Event...")
        res = bb.log_event("ERROR", "TestAgent", "System Crash Simulation")
        self.assertTrue(res['success'], f"Log failed: {res.get('error')}")
        
        print("Test: Reading Logs...")
        read_res = bb.read_logs(limit=5)
        self.assertTrue(read_res['success'], f"Read failed: {read_res.get('error')}")
        
        logs = read_res['logs']
        self.assertTrue(len(logs) > 0)
        self.assertEqual(logs[0]['msg'], "System Crash Simulation")
        self.assertEqual(logs[0]['level'], "ERROR")
        print(f"[E2E] Verified Log: {logs[0]}")

if __name__ == '__main__':
    unittest.main()
