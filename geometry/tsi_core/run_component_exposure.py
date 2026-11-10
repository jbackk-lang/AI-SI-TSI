from pathlib import Path
import subprocess,sys
p=Path(__file__).parent/'train_component_exposure_arm.py'
for arm in ['separate','joint_context']:subprocess.run([sys.executable,str(p),arm],check=True)
