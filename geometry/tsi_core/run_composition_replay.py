from pathlib import Path
import subprocess,sys
p=Path(__file__).parent/'train_composition_replay_arm.py'
for arm in ['control','expanded_replay']:subprocess.run([sys.executable,str(p),arm],check=True)
