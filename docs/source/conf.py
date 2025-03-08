# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PIF Club'
copyright = '2025, PayItForWard'
author = 'PayItForWard'
release = '1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_rtd_theme",'sphinx_copybutton','sphinx_new_tab_link','sphinx_rtd_dark_mode','sphinxemoji.sphinxemoji','sphinx_favicon','sphinxcontrib.video']

favicons = [
   {
      "sizes": "32x32",
      "href": "logo.png",
   }
]

templates_path = ['_templates']
exclude_patterns = []

language = 'Eng'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_logo = "_static/logo.png"

html_static_path = ['_static']


favicons = [
{
    "sizes": "32x32",
    "href": "favicon.png",
}
]
