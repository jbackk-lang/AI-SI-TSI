from pathlib import Path
import subprocess,sys
p=Path(__file__).parent/'train_context_vocabulary_arm.py'
for arm in ['control','diverse']:subprocess.run([sys.executable,str(p),arm],check=True)
