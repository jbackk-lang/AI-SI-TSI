# Integration into existing TSI system.py

In the `TSISystem` class in `TSI/integrated_math/code/tsi_core/system.py`, the tested archive includes:

```python
 def geometry_candidate_reply(self,left,right):
  """Opt-in geometry classifier; separate from active inference and verified logic."""
  from geometry_candidate_adapter import classify_geometry
  return classify_geometry(left,right)
```

The source files in this directory are exported from the tested snapshot. The full `system.py` and binary `geometry_candidate.pt` are **not** included in this Git branch yet. The classifier requires its exact checkpoint with SHA-256 `c253c857486a7b5eb248b8f254956f5c565445f3445b8ea79ff15d6a9e3c7343`.

This folder is not a deployable replacement for the complete TSI runtime.