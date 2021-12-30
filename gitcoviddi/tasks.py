import re

from celery import shared_task
from dateutil.parser import parse
from django.conf import settings
from django.db.utils import IntegrityError
from git_adapter.git import Git, CmdError

COMMIT_RE = re.compile(r'^commit\s+([a-f0-9]+)$')
DATE_RE = re.compile(r'^Date:\s+(.+)$')


def _build_git_or_die_tryin():
    g = Git(settings.GITCOVIDDI_PATH)
    g.status()
    return g


@shared_task
def update_repository():
    from .models import GitUpdate
    try:
        g = _build_git_or_die_tryin()

    except CmdError:
        g = Git.clone_repo(settings.GITCOVIDDI_REPO, settings.GITCOVIDDI_PATH, verbose=True)
    last_commit = g.log("-1")
    update = GitUpdate()
    for line in last_commit:
        m = COMMIT_RE.match(line)
        if m:
            update.commit_id = m.group(1)
        m = DATE_RE.match(line)
        if m:
            update.timestamp = parse(m.group(1))
    try:
        update.save()
    except IntegrityError:
        # We already have that commit
        pass
