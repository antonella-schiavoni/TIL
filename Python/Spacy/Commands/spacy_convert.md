# Sapcy Convert

Convert files into spaCy’s binary training data format, a serialized DocBin, for use with the train command and other experiment management functions.
The converter can be specified on the command line, or chosen based on the file extension of the input file.

# How To Use
1. Convert data from .conll to spacy's binary training data format
```
spacy convert input.conll -c conll ./output/
```

For more information, visit: https://spacy.io/api/cli#convert
