Context manager for matplotlib figures.

Example:

```python
from plox import Plox
from pathlib import Path

with Plox() as px:
    px.a.plot([1, 2, 3], [4, 3, 5], 'o--')
    px.f.savefig(Path(__file__).with_suffix('.png'))
    px.show()
```
