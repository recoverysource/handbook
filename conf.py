# Project information
project = 'Recovery Source Handbook'
copyright = '2022, Recovery Source'

# General configuration
extensions = []
master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['static']
html_extra_path = ['CNAME']
html_favicon = 'favicon.ico'

# Theme options
html_theme = 'furo'
html_show_sphinx = False
html_theme_options = {
  'source_repository': 'https://github.com/recoverysource/handbook/',
  'announcement': '<b>ACTIVE DEVELOPMENT:</b><br />For current documentation, please visit <a href="https://docs.recoverysource.net">docs.recoverysource.net</a>',
}
html_title = 'Recovery Source Handbook'
html_css_files = ['style.css']
