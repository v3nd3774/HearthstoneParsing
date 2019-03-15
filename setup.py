import setuptools
with open("README.md", "r") as f:
  long_description = f.read()
setuptools.setup(
  name="hearthstone-parsing-converter-v3nd3774",
  version="0.0.5",
  author="Josue Caraballo",
  author_email="josue.caraballo@gmail.com",
  description="Converting hearthstone entity strings into fixed length vectors!",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/v3nd3774/HearthstoneParsing",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ]
)
