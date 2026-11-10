import runpy,sys
from pathlib import Path
for arm in ['control','lexical']:
 sys.argv=['train_lexical_arm.py',arm]
 runpy.run_path(str(Path(__file__).with_name('train_lexical_arm.py')),run_name='__main__')
