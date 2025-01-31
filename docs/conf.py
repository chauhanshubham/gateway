import os
import re

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autosectionlabel',
]

html_theme = 'alabaster'

# The master toctree document.
master_doc = 'index'

# General information about the project.

fullversion = os.environ["BUILD_VERSION"]
release = fullversion

version = fullversion

m = re.match(r"^(v\d+\.\d+\.\d+)(-rc\d+)", version)

if m:
    version = "".join(m.groups())

release = version

project = f'Envoy Gateway {version}'
author = 'Envoy Gateway Project Authors'

copyright = '2022 Envoy Gateway Project Authors | ' + fullversion
