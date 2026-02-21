#!/usr/bin/env python3
import os
import sys
import subprocess
import glob
import re
import time

# Ensure we are at repo root
current_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(current_dir)
skills_root = os.path.join(repo_root, "skills")

def get_frontmatter_value(file_path, key):
    """Extract a value from YAML frontmatter using regex."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Match frontmatter block
        match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not match:
            return None
            
        frontmatter = match.group(1)
        # Find key: value (case-insensitive key)
        pattern = r"(?m)^" + re.escape(key) + r":\s*(.+)$"
        key_match = re.search(pattern, frontmatter)
        
        if key_match:
            val = key_match.group(1).strip()
            # Remove quotes if present
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            return val
            
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
    return None

def main():
    print(f"🚀 Publishing skills from: {skills_root}")
    
    if not os.path.exists(skills_root):
        print(f"Error: Skills directory not found at {skills_root}")
        sys.exit(1)

    # Find all skill directories
    skill_dirs = [d for d in os.listdir(skills_root) if os.path.isdir(os.path.join(skills_root, d))]
    skill_dirs.sort()
    
    success_count = 0
    fail_count = 0

    for i, skill_dir in enumerate(skill_dirs):
        if skill_dir.startswith("__") or skill_dir.startswith("."):
            continue
            
        full_path = os.path.join(skills_root, skill_dir)
        skill_md = os.path.join(full_path, "SKILL.md")
        
        if not os.path.exists(skill_md):
            continue
            
        # Extract slug from 'name' field
        slug = get_frontmatter_value(skill_md, "name")
        description = get_frontmatter_value(skill_md, "description")
        
        if not slug:
            print(f"⚠️  Skipping {skill_dir}: Could not find 'name' in SKILL.md frontmatter")
            continue
            
        print(f"📦 Publishing: {slug} ...")
        
        # Build command
        # clawhub publish <path> --slug <slug> --name <slug> --version <version> --changelog "Auto update" --no-input
        cmd = [
            "clawhub", "publish", full_path,
            "--slug", slug,
            "--name", slug,
            "--version", "0.0.1",
            "--changelog", "Initial release via Agent Cloud Memory automation",
            "--no-input"
        ]
        
        # Execute
        try:
            # We use shell=False for security
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Published {slug}")
                success_count += 1
            else:
                print(f"❌ Failed to publish {slug}")
                print(f"   Error: {result.stderr.strip()}")
                fail_count += 1
                if "EAUTH" in result.stderr:
                    print("   💡 Hint: Run 'clawhub login' first.")
                    sys.exit(1) # Stop on auth error
                    
        except FileNotFoundError:
            print("❌ Error: 'clawhub' CLI not found.")
            print("   Please install it: npm i -g clawhub")
            sys.exit(1)
            
        # Rate limit prevention (wait 10s between publishes, unless it's the last one)
        if i < len(skill_dirs) - 1:
            print("⏳ Waiting 10s to respect rate limits...")
            time.sleep(10)
            
    print(f"\nSummary: {success_count} published, {fail_count} failed.")

if __name__ == "__main__":
    main()
