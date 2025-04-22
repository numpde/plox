# plox

**plox** is a lightweight context manager for creating and managing matplotlib figures and axes easily and safely.

## Features

- Automatic creation and cleanup of 'matplotlib' figures.
- Simple access to the figure ('px.f') and main axes ('px.a').
- Clean separation of plotting and figure decoration.
- Optional figure styling using 'rcParams'.
- Tiny, no external dependencies beyond 'matplotlib'.

## Basic Usage

```python
from plox import Plox, rcParam
from pathlib import Path

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

## Advanced Pattern: Plot Functions with @contextmanager

Encapsulate your plots in reusable functions while giving users the chance to modify and save figures afterwards:

```python
from contextlib import contextmanager
from plox import Plox

@contextmanager
def plot_example(style=None):
    with Plox(style) as px:
        px.a.plot([1, 2, 3], [4, 3, 5], 'o--')
        yield px

# Usage:
from pathlib import Path

with plot_example() as px:
    px.a.set_title("Customized Title")
    px.f.savefig(Path("example_plot.png"))
    px.show()
```

This keeps your code modular and flexible.

## Installation

'plox' is a small pure-Python library. Clone and import it locally

```bash
git clone https://github.com/numpde/plox.git
```

or install with pip

```bash
pip install plox
```

## License

MIT License.
