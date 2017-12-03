from celery import Celery
from git import Repo, refs, HEAD
import os
import unittest

app = Celery('tasks', broker='redis://root@192.168.221.145', backend='redis://root@192.168.221.145')


@app.task
def run_tests(commit_id):
    # pull the latest commit
    repo_dir = '/root/znci_venv/zn_ci/test_repo_ci'
    repo = Repo(repo_dir)
    repo.remotes.origin.pull('master:master')
    repo.head.reset(commit=commit_id,
                    index=True,
                    working_tree=True)
    # run the tests
    test_dir = os.path.join(repo_dir, "tests")
    suite = unittest.TestLoader().discover(test_dir)
    result_file = open("results", "w")
    unittest.TextTestRunner(result_file).run(suite)
    result_file.close()
    result_file = open("results", "r")
    result=result_file.read()
    result_file.close()
    return result
