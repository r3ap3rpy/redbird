import logging
from redbird.logging import RepoHandler
from redbird.repos import MemoryRepo

log_repo = MemoryRepo()
handler = RepoHandler(repo=log_repo)
logger = logging.getLogger('mylogger')
logger.addHandler(handler)


logger.debug('Debug message')
logger.info('Informational message')
logger.warning('Warning message')

for message in list(log_repo.filter_by(levelname='INFO').all()):
    print(message)