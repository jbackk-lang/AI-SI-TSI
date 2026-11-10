import runpy
from pathlib import Path
for script in ['validate_lexical_scale_small.py','check_lexical_scale_same_arguments.py']:
 runpy.run_path(str(Path(__file__).with_name(script)),run_name='__main__')
