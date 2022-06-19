#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pathlib import Path
import click
import time
import logging

from watchfiles import Change, DefaultFilter, run_process

class MarkdownFilter(DefaultFilter):
    allowed_extensions = ('.md',)

    def __call__(self, change: Change, path: str) -> bool:
        return (
            super().__call__(change, path) and 
            path.endswith(self.allowed_extensions)
        )

logging.basicConfig(level=logging.DEBUG)


@click.group()
def main():
    """
    set of tools for watching book folders and rebuilding
    when files change

    usage:

    ebp-watch jb book_folder
        -- this runs jb build on book_folder

    ebp-watch nb notebook_folder
        -- this runs sphinx-build on notebook_folder
    """
    pass

@main.command()
@click.argument("book_folder", type=str, nargs=1)
def jb(book_folder):
    """
    (which runs jupyter-book build book_folder)
    """
    print(f"{book_folder=}")
    command = f"jupyter-book build {book_folder}"
    print(f"{command=}")
    directory = book_folder
    run_process(directory, target = command, watch_filter = MarkdownFilter)


@main.command()
@click.argument("notebook_folder", type=str, nargs=1)
def nb(notebook_folder):
    """
    (which runs sphinx-build -v -a -b html notebook_folder notebook_folder/_build/html)
    """
    patterns = ['*.md']
    ignore_patterns = []
    output_name = Path(f"{notebook_folder}/_{notebook_folder}_build/html").resolve()
    command = f"sphinx-build -v -a -b html {notebook_folder} {output_name}"
    print(f"\nrunning\n{command}\n")
    directory = (notebook_folder,)
    run_process(directory, command, watch_filter = MarkdownFilter())

    
if __name__ == '__main__':
    main()
