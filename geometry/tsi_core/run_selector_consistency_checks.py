import runpy
from pathlib import Path
for script in ['check_selector_same_arguments.py','validate_selector_consistency_retention.py']:
 runpy.run_path(str(Path(__file__).with_name(script)),run_name='__main__')
