from pathlib import Path

FILE = '{0}/status_summary_{time}.csv'
DIR_NAME = 'results'
DOMAIN = 'peps.python.org'

BOT_NAME = 'pep_parse'

BASE_DIR = Path(__file__).parent.parent
SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{DIR_NAME}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
