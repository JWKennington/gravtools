"""Visualization tools for GWaves

These visuals rely primarily on Bokeh plotting library
"""
import typing

from bokeh.plotting import output_file, output_notebook, figure, show
from pycbc.types import TimeSeries


_OUTPUT_INITIALIZED = False


def is_notebook():
    return True # TODO fix this


def check_output():
    global _OUTPUT_INITIALIZED
    if not _OUTPUT_INITIALIZED:
        if is_notebook():
            output_notebook(hide_banner=True)
            _OUTPUT_INITIALIZED = True
        else:
            raise NotImplementedError


def plot_strain(ts: typing.Union[TimeSeries, typing.Iterable[TimeSeries]], height: int = 300, width: int = 800,
                names: typing.Union[str, typing.Iterable[str]] = None, show_plot: bool = True, title: str = None):
    f = figure(title='Strain Plot' if title is None else title,
               x_axis_type='datetime',
               x_axis_label='GPS Time (s)',
               y_axis_label='Strain',
               plot_height=height,
               plot_width=width)

    # "box" ts into a list
    if isinstance(ts, TimeSeries):
        ts = [ts]

    # "box" names into a list
    if names is None:
        names = ['Source{:d}'.format(n+1) for n in range(len(ts))]
    elif isinstance(names, str):
        names = [names]

    # Check that we have a name for each series
    if len(names) != len(ts):
        raise ValueError('Must specify 1 name per TimeSeries if passing multiple')

    for name, t in zip(names, ts):
        f.line(x=t.sample_times.numpy(), y=t.numpy(), legend_label=name)

    if show_plot:
        check_output()
        show(f)
    else:
        return f
