import runpy,sys
from pathlib import Path
for arm in ['control','protected']:
 sys.argv=['train_context_protection_arm.py',arm]
 runpy.run_path(str(Path(__file__).with_name('train_context_protection_arm.py')),run_name='__main__')
