from distutils.core import setup
setup(
  name = 'dnadrive',
  packages = ['dnadrive'], # this must be the same as the name above
  version = '0.1',
  description = 'This Package contains utility wrappers for dnadrive',
  author = 'Wington Sharon',
  author_email = 'wingston@helix.works',
  url = 'https://github.com/wingie/dnadrive', # use the URL to the github repo
  download_url = 'https://github.com/wingie/dnadrive/tarball/0.1', # I'll explain this in a second
  keywords = ['dnadrive', 'biopython'], # arbitrary keywords
  classifiers = [],
  scripts=['dnadrive/dnadrive'] 
)
