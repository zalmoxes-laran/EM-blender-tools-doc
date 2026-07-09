# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Extended Matrix tool'
copyright = '2024–2026, Emanuel Demetrescu (CNR-ISPC), Simone Berto'
author = 'Emanuel Demetrescu, Simone Berto'

# Sphinx convention: version is the short X.Y, release is the full string
# (including pre-release tags). Keeping these in sync with the addon
# release naming on GitHub (e.g. em_tools-v1.5.0-dev.140-...) so that the
# PDF cover, HTML header and downloadable bundle agree.
version = '1.5'
release = '1.5.0-dev'

# Explicit titles so the HTML <title> and the PDF cover both carry the
# correct release string and don't drift back to a stale "1.4" cover.
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
    # sphinx-design — provides .. badge::, .. dropdown::, .. tab-set::
    # used in the tutorial pages (clip_03, clip_04, clip_12, ...).
    # Without it, those directives raise ERROR "Unknown directive type".
    'sphinx_design',
]

# Surface .. todo:: directives in the rendered docs so they are easy
# to find while we are still filling screenshot gaps. Set to False
# before tagging a stable release.
todo_include_todos = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    # EM language manual (formal notation). The slug `/en/1.5/` is the
    # RTD short version that tracks the 1.5.x branch on the EM-doc repo —
    # `/en/1.5.0/` and `/en/1.5.0dev/` are stale and return 404.
    'em-doc': ('https://docs.extendedmatrix.org/en/1.5/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# Files completely excluded from the build (no HTML emitted, no warnings).
# To re-enable a page, remove it from this list and reference it from a toctree.
exclude_patterns = [
    '_build',
    # `_includes/` is the canonical home of reusable RST snippets pulled
    # in via `.. include:: _includes/<file>.rst` from other pages.
    # If Sphinx also discovers them as STANDALONE docs, every label
    # they declare gets parsed twice and surfaces as `duplicate label`
    # — turning the strict CI red. Excluding the whole directory from
    # the build keeps the includes consumable but unindexed.
    '_includes/**',
]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Enable numref
numfig = True
# -- PDF (LaTeX) cover -------------------------------------------------
# Make explicit that this is the *documentation*, credited to its own
# author(s) (4th tuple field = the name printed on the PDF cover), so it
# is not mistaken for the software's author.
latex_documents = [
    ('index', 'ExtendedMatrixTool.tex',
     f'{project} Documentation',
     'Documentation written by Emanuel Demetrescu\newline and Simone Berto',
     'manual'),
]
