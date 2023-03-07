from pathlib import Path

from constants import RESULT

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
