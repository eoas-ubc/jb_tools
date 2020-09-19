# Working with jb_tools

Here's how to specify a book environment using
https://pypi.org/project/conda-lock/
and re-render a book's html whenever the book files change using
https://github.com/eoas-ubc/jb_tools and https://www.npmjs.com/package/live-server


## building an environment with conda

0) clone this repo and install conda-lock

1) in case some packages have changed, you can (optionally) redo the
   conda-lock files in this folder with:

`conda-lock -f environment.yml -p osx-64 -p linux-64 -p win-64`

which produces

```
conda-linux-64.lock	
conda-osx-64.lock	
conda-win-64.lock
```

2) use these to create a new environment with the approriate
   lock file for your os and install the pypi packages with pip
   like this

```
conda create -n jbenv --file conda-xxx-64.lock
conda activate jbenv
pip install -r requirements.txt
npm install -g live-server
```
With these packages jupyter-book should be able to build
its own documentation: https://github.com/executablebooks/jupyter-book/tree/master/docs


## working with a book

If the jupyter-book `_toc.yml` file is in folder `jupyter-book/docs`

1) cd to `jupyer-book`

2) start watching the docs folder with:

   `ebp-watch jb docs`

3) start watching the html folder with:

   `live-server docs/_build/html`

4) change https://github.com/executablebooks/jupyter-book/blob/master/docs/intro.md
   and the book should rebuild and your browser should refresh.

## working with a `myst_nb` notebooks

If you want to run sphinx using [myst-nb](https://myst-nb.readthedocs.io/en/latest/) on a set
of notebooks the procedure is the same, just replace `ebp-watch jb docs` with `ebp-watch nb docs`

## single build of a list of books or notebooks

To run `jupyter-book build` or `sphinx-build` one time on multiple notebooks, use

`ebp-build jb book1 book2 book3 ...`

or

`ebp-build nb folder1 folder2 ...`


