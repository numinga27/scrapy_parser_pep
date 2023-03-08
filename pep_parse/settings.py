from pathlib import Path

FILE = 'results/status_summary_{0}.csv'
RESULT = 'results/pep_%(time)s.csv'
DIR_NAME = 'results'
URL_LIST = ['https://peps.python.org/']


BOT_NAME = 'pep_parse'

BASE_DIR = Path(__file__).parent.parent

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

FEEDS = {
    RESULT: {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
