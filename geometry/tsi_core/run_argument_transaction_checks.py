from pathlib import Path
import subprocess,sys
for script in ['validate_argument_transaction_fresh.py','validate_argument_transaction_retention.py']:
 subprocess.run([sys.executable,str(Path(__file__).parent/script)],check=True)
