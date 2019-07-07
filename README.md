# GO_Translator
Simple utility functions for handling GO Terms in Python.

Provides dictionaries for the GO Terms in the go.obo file which allow simple lookups to GO Terms.
See the Term class definition in `GO_Translator/__init__.py` to view available datafields for each GO term.

## Usage

### Install
```bash
git clone https://github.com/blengerich/GO_Translator
cd GO_Translator
pip install -e .
```

### Use the Available Dicts in Python
```python
>>> from GO_Translator import *
>>> go_terms_by_id
>>> go_terms_by_name
```
