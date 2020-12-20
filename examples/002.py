# RA, 2020-12-20

from plox import Plox
from pathlib import Path

# https://matplotlib.org/tutorials/introductory/customizing.html
style = {
    'legend.fontsize': "large",
    'xtick.labelsize': "large",
    'ytick.labelsize': "large",
}

with Plox(style) as px:
    px.a.plot([1, 2, 3], [4, 3, 5], 'o--')
    px.f.savefig(Path(__file__).with_suffix('.png'))
    px.show()
