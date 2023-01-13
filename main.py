import datetime
from git import Repo

def was_it_rufus(git_dir):
    # Open repository
    repo = Repo(git_dir)

    # Get active branch
    active_branch = repo.active_branch.name == 'main'
    print(f'active branch: {active_branch}')

    # Check if the repo files have been modified
    modified = repo.is_dirty()
    print(f'local changes: {modified}')

    # Get the author and date of the current head commit
    head_commit = repo.head.commit
    author = head_commit.author.name
    date = head_commit.authored_datetime.date()

    # Check if the current head commit was authored in the last week
    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=7)
    authored_in_last_week = date >= last_week
    print(f'recent commit: {authored_in_last_week}')

    # Check if the current head commit was authored by Rufus
    authored_by_rufus = author =='Rufus'
    print(f'blame Rufus: {authored_by_rufus}')

    pass

was_it_rufus(r"C:\Users\eetur\github_projects\commoncrave")