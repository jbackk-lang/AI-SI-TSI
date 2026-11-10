from pathlib import Path
import subprocess,sys
p=Path(__file__).parent/'train_footer_contrast_arm.py'
for arm in ['control','contrast']:subprocess.run([sys.executable,str(p),arm],check=True)
