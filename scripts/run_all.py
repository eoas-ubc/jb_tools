import click
import subprocess
from pathlib import Path

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
        print(f'finally inside {os.getcwd()}')
        os.chdir(CWD)


def build_page(thedir):
    #
    # change into the directory to execute pandoc, returning
    # to the run directory once the command completes or if
    # there is an exception
    #
    with cd(the_dir.parent):
        str_dir = str(the_dir)
        build_dir = the_dir / '_build/html'
        arglist = ['sphinx-build','-N','-v', '-b html',str_dir,str(build_dir)]
        print(f"running the command \n{' '.join(arglist)}\n")
        result = subprocess.run(arglist, capture_output=True)
        if result.stdout:
            print('output: ',result.stdout)
        if result.stderr:
            print('error: ',result.stderr)

def main(target_dir):
    
            
if __name__ == "__main__":
    all_conf = list(glob.glob("**/*_src_dir"))
    for item in all_conf:
        if not item / "conf.py"
            raise ValueError(f"{str(item)} has no conf.py")
