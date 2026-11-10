from pathlib import Path
import subprocess,sys
for script in ['validate_composition_contract_final.py','validate_composition_contract_retention.py']:
 subprocess.run([sys.executable,str(Path(__file__).parent/script)],check=True)
