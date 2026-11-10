from pathlib import Path
import subprocess,sys
for script in ['validate_operator_capacity_fresh.py','validate_operator_capacity_retention.py']:
 subprocess.run([sys.executable,str(Path(__file__).parent/script)],check=True)
