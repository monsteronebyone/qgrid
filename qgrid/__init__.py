from ._version import version_info, __version__

from .grid import (
    enable,
    disable,
    set_defaults,
    set_grid_option,
    show_grid,
    QgridWidget,
    QGridWidget
)

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'qgrid',
        'require': 'qgrid/extension'
    }]

__all__ = [
    'enable',
    'disable',
    'set_defaults',
    'set_grid_option',
    'show_grid',
    'QgridWidget',
    'QGridWidget'
]
