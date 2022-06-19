"""
info
"""
import click
import subprocess
from pathlib import Path
import contextlib
import os
import shlex

@contextlib.contextmanager
def cd(path):
    print(f'initially inside {os.getcwd()}')
    CWD = os.getcwd()
    os.chdir(path)
    print(f'inside {os.getcwd()}')
    try:
        yield
    except Exception as e:
        print(f'Exception caught: {e}')
    finally:
        print(f'returning to {os.getcwd()}')
        os.chdir(CWD)


@click.group()
def main():
    """
    set of tools for building a list of books (using jb build)
    or notebooks (using sphinx-build)

    usage:

    ebp-build jb book1 book2 ...
        -- this runs jb build bookx in turn

    ebp-build nb folder1 folder2 ...
        -- this runs sphinx-build on folders in turn
    """
    pass



@main.command()
@click.argument("notebook_list",type=str, nargs= -1)
def nb(notebook_list):
    """
    (which runs sphinx-build -v -a -b html notebook_folder notebook_folder/_build/html)
    on all notebooks in the list
    """
    for the_dir in notebook_list:
        the_dir=Path(the_dir)
        if not the_dir.is_dir():
            raise ValueError(f"don't see {the_dir} in this folder")
        with cd(the_dir.parent):
            str_dir = str(the_dir)
            print(f"currently in {Path().resolve()}")
            build_dir = (the_dir / f'_build/html').resolve()
            arglist = ['sphinx-build','-a','-v', '-b html',str_dir,str(build_dir)]
            argstring = ' '.join(arglist)
            print(f"running the command \n{argstring}\n")
            result = subprocess.run(argstring, capture_output=True, shell=True)
            if result.stdout:
                print(f"stdout message: {result.stdout.decode('utf-8')}")
            if result.stderr:
                print(f"stderror message: {result.stderr.decode('utf-8')}")

@main.command()
@click.argument("book_list",type=str, nargs= -1)
def jb(book_list):
    """
    (which runs jupyter-book build book_folder on all folders in the list)
    """
    for the_dir in book_list:
        the_dir = Path(the_dir)
        with cd(the_dir.parent):
            str_dir = str(the_dir)
            arglist = ['jupyter-book','build',f"{the_dir}"]
            print(f"running the command \n{' '.join(arglist)}\n")
            result = subprocess.run(arglist, capture_output=True)
            if result.stdout:
                print(f"stdout message: {result.stdout.decode('utf-8')}")
            if result.stderr:
                print(f"stderror message: {result.stderr.decode('utf-8')}")

if __name__ == "__main__":
    main()
