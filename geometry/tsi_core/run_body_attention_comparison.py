import runpy,sys
from pathlib import Path
for arm in ['control','body_attention']:
 sys.argv=['train_body_attention_arm.py',arm]
 runpy.run_path(str(Path(__file__).with_name('train_body_attention_arm.py')),run_name='__main__')
