# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MIMIC Wizard'
copyright = 'GNU GPLv3'
author = 'Lucas DUVAL'

release = '0.6'
version = '0.6.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {

}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
