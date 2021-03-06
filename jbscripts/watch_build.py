#!/usr/bin/env python
# -*- coding: utf-8 -*-

from watchdog.tricks import ShellCommandTrick
from watchdog.observers import Observer
from pathlib import Path
import click
import time



def observe_with(observer, event_handler, pathnames, recursive):
    """
    Single observer thread with a scheduled path and event handler.

    :param observer:
        The observer thread.
    :param event_handler:
        Event handler which will be called in response to file system events.
    :param pathnames:
        A list of pathnames to monitor.
    :param recursive:
        ``True`` if recursive; ``False`` otherwise.
    """
    for pathname in set(pathnames):
        observer.schedule(event_handler, pathname, recursive)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def shell_command(command,patterns,ignore_patterns,directories):
    ignore_directories = False
    wait_for_process = False
    drop_during_process = False
    timeout = 2.0
    recursive = True
    handler = ShellCommandTrick(shell_command=command,
                                patterns=patterns,
                                ignore_patterns=ignore_patterns,
                                ignore_directories=ignore_directories,
                                wait_for_process=wait_for_process,
                                drop_during_process=drop_during_process)
    observer = Observer(timeout=timeout)
    observe_with(observer, handler, directories, recursive)

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
    patterns = ['*.md']
    ignore_patterns = []
    command = f"jupyter-book build {book_folder}"
    directories = [book_folder]
    shell_command(command, patterns, ignore_patterns, directories)


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
    directories = [notebook_folder]
    shell_command(command, patterns, ignore_patterns, directories)
    
if __name__ == '__main__':
    main()
