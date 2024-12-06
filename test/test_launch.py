import subprocess
import os

def test_launch_all_runs_successfully():
    result = subprocess.run(['python3', 'script/launch_all.py'], capture_output=True, text=True)
    assert result.returncode == 0, f"launch_all.py failed with error: {result.stderr}"
