# RA, 2020-06-16

import matplotlib.pyplot as plt


class Plox:
    # https://matplotlib.org/3.2.1/tutorials/introductory/customizing.html
    _default_style = {
        'savefig.bbox': "tight",
        'savefig.pad_inches': 0.01,
        'savefig.transparent': False,
    }

    def __init__(self, style=None):
        style = {**self._default_style, **(style or {})}
        try:
            self._style_context = plt.style.context(style)
        except:
            raise

    def __enter__(self):
        self._style_context.__enter__()
        (self._f, self._a) = plt.subplots(dpi=180)
        return self

    @property
    def f(self) -> plt.Figure:
        return self._f

    @property
    def a(self) -> plt.Axes:
        return self._a

    def __exit__(self, exc_type, exc_val, exc_tb):
        plt.close(self.f)
        self._style_context.__exit__(exc_type, exc_val, exc_tb)

    @staticmethod
    def show():
        plt.show()


if __name__ == '__main__':
    with Plox() as plx:
        plx.a.plot([0, 1, 2], [1, -1, 1])
        plx.show()
