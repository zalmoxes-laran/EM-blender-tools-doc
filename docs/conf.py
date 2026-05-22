# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Extended Matrix tool'
copyright = '2024–2026, Emanuel Demetrescu (CNR-ISPC)'
author = 'Emanuel Demetrescu'

# Sphinx convention: version is the short X.Y, release is the full string
# (including pre-release tags). Keeping these in sync with the addon
# release naming on GitHub (e.g. em_tools-v1.6.0-dev.NNN-...) so that the
# PDF cover, HTML header and downloadable bundle agree.
version = '1.6'
release = '1.6.0.dev0'

# Explicit titles so the HTML <title> and the PDF cover both carry the
# correct release string and don't drift back to a stale "1.5" cover.
html_title = f'Extended Matrix tool {release} documentation'
html_short_title = f'EM Tools {release}'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

# Surface .. todo:: directives in the rendered docs so they are easy
# to find while we are still filling screenshot gaps. Set to False
# before tagging a stable release.
todo_include_todos = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    # EM language manual (formal notation). EM-tools 1.6 tracks EM-doc 1.6:
    # the RTD slug `/en/1.6/` exposes a published `objects.inv` (verified
    # 2026-05-22). `/en/1.5.0/` and `/en/1.5.0dev/` are stale and return
    # 404. The 1.5 short slug still works for the 1.5.x branch of EM-doc
    # but EM-tools-doc/1.6 should cross-reference EM-doc/1.6.
    'em-doc': ('https://docs.extendedmatrix.org/en/1.6/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# Files completely excluded from the build (no HTML emitted, no warnings).
# To re-enable a page, remove it from this list and reference it from a toctree.
exclude_patterns = [
    '_build',
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Enable numref
numfig = True