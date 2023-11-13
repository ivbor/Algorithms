# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.extend([os.path.abspath('../../'),
                 os.path.abspath('../../Algorithms/python_solutions'),
                 os.path.abspath('../../Algorithms/researches')])

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Algorithms'
copyright = '2023, Ivan Baravoi'
author = 'Ivan Baravoi'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'nbsphinx',
]

templates_path = ['_templates']
exclude_patterns = []

latex_documents = [
   (os.path.abspath('index.rst'), 'algorithms.tex', 'Algorithms Documentation',
    author, 'manual'),
]
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url': '',
    'analytics_id': 'UA-XXXXXXX-1',
    'logo_only': False,
    # Add more theme options as needed
}
