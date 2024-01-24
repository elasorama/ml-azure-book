# Azure ML Python documentation 

The code is to create a jupyter book regarding how to leverage Azure, Python and Machine Learning to solve real world problems.

# Virtual environment 

To create a virtual environment, run the following command:

```bash
python3.11 -m venv book-env
```

To activate the virtual environment, run the following command:

```bash
# Linux
source book-env/bin/activate

# PS on Windows
.\book-env\Scripts\activate
```

# Building the book 

To build the book, run the following command:

```bash
jupyter-book build azure-docs
```

# Setting the book up online 

To set the book up online, run the following command:

```bash
ghp-import -n -p -f azure-docs/_build/html
```