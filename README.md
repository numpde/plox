Context manager for matplotlib figures.

Example:

```python
from plox import Plox, rcParam
from pathlib import Path

# https://matplotlib.org/tutorials/introductory/customizing.html
style = {
    rcParam.Legend.fontsize: "large",
    rcParam.Xtick.labelsize: "large",
    rcParam.Ytick.labelsize: "large",
}

with Plox(style) as px:
    px.a.plot([1, 2, 3], [4, 3, 5], 'o--')
    px.f.savefig(Path(__file__).with_suffix('.png'))
    px.show()
```
