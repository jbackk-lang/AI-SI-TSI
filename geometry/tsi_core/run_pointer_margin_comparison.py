import runpy,sys
from pathlib import Path
for arm in ['control','pointer_margin']:
 sys.argv=['train_pointer_margin_arm.py',arm]
 runpy.run_path(str(Path(__file__).with_name('train_pointer_margin_arm.py')),run_name='__main__')
