from subprocess import run as srun
import logging
from os import path as ospath

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

UPSTREAM_REPO = 'https://github.com/darkhacker34/Video-Encoder-BOT'
UPSTREAM_BRANCH = 'beta'

if UPSTREAM_REPO is not None:
    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])

    update_command = f"git init -q && git add . && git commit -sm update -q && git remote add origin {UPSTREAM_REPO} && git fetch origin -q && git reset --hard origin/{UPSTREAM_BRANCH} -q"
    update = srun(update_command, shell=True)

    if update.returncode == 0:
        logging.info('Successfully updated with latest commit from UPSTREAM_REPO')
    else:
        logging.error('Something went wrong while updating, check UPSTREAM_REPO if valid or not!')
