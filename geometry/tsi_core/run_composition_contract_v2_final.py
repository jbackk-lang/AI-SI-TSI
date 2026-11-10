from pathlib import Path
import subprocess,sys
for script in ['validate_composition_contract_v2_final.py','validate_composition_contract_v2_retention.py']:
 subprocess.run([sys.executable,str(Path(__file__).parent/script)],check=True)
