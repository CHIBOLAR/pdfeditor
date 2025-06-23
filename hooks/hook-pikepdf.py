# Hook for pikepdf
from PyInstaller.utils.hooks import collect_all, collect_submodules

# Collect all pikepdf data and binaries
datas, binaries, hiddenimports = collect_all('pikepdf')

# Additional hidden imports
hiddenimports += [
    'pikepdf._cpphelpers',
    'pikepdf._methods',
    'pikepdf._core',
    'pikepdf.models',
    'pikepdf.codec',
    'pikepdf._qpdf',
    'lxml',
    'lxml.etree',
    'lxml._elementpath',
    'lxml.objectify'
]

# Collect all submodules
hiddenimports += collect_submodules('pikepdf')
