from subprocess import run as srun
import logging
from os import path as ospath

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

UPSTREAM_REPO = 'https://github.com/darkhacker34/Video-Encoder-BOT'
UPSTREAM_BRANCH = 'beta'

def check_git_installed():
    """Check if git is installed and accessible."""
    try:
        result = srun(['git', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            logging.error('Git is not installed or not accessible')
            return False
        return True
    except FileNotFoundError:
        logging.error('Git command not found')
        return False

if UPSTREAM_REPO is not None:
    if not check_git_installed():
        logging.error('Git installation check failed. Exiting.')
        exit(1)

    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])

    update_command = f"git init -q && git add . && git commit -sm update -q && git remote add origin {UPSTREAM_REPO} && git fetch origin -q && git reset --hard origin/{UPSTREAM_BRANCH} -q"
    update = srun(update_command, shell=True)

    if update.returncode == 0:
        logging.info('Successfully updated with latest commit from UPSTREAM_REPO')
    else:
        logging.error('Something went wrong while updating, check UPSTREAM_REPO if valid or not!')

# Ensure that download_dir is set before using it
download_dir = '/path/to/download/directory'  # Replace with the actual path

if download_dir is None:
    logging.error('download_dir is None')
elif not ospath.isdir(download_dir):
    logging.error(f'{download_dir} is not a valid directory')
