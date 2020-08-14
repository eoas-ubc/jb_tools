# Tools for working with jupyter books and md:myst notebooks

* buildjb:  build a list of jupyter-books or a myst_nb notebook

* watchjb:  use watchdog to trigger a notebook or jupyter-book build


```
pip install -e .
buildjb --help
watchjb --help
```

To trigger a browser refresh when  watchjb changes the html, we use
[live-server](https://www.npmjs.com/package/live-server) installed
from conda-forge

```
conda install -c conda-forge nodejs
npm install -g live-server
```
