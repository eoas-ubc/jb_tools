# Working with jupyter-books

Here's how to specify a book environment using
https://pypi.org/project/conda-lock/
and re-renender a book's html whenever the book files change using
https://github.com/eoas-ubc/jb_tools and https://www.npmjs.com/package/live-server

## building an environment with conda

0) install conda-lock

1) conda-lock -f environment.yml -p osx-64 -p linux-64 -p win-64

produces

conda-linux-64.lock	conda-osx-64.lock	conda-win-64.lock

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

   `ebp-watch docs`

3) start watching the html folder with:

   `live-server docs/_build/html`

4) change https://github.com/executablebooks/jupyter-book/blob/master/docs/intro.md
   and the book shold rebuild and your browser should refresh.


