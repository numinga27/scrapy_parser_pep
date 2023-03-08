import csv
import os

from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR, FILE, DIR_NAME


class PepParsePipeline:
    if not os.path.exists(DIR_NAME):
        os.makedirs(DIR_NAME)

    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1

        return item

    def close_spider(self, spider):
        time = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        path = BASE_DIR / FILE.format(time)
        with open(
            path, mode='w', encoding='utf-8'
        ) as csvfile:
            writer = csv.writer(
                csvfile, dialect=csv.unix_dialect,
                quoting=csv.QUOTE_ALL
            )
            writer.writerows(
                ['Статус', 'Количество'],
                self.status_count.items(),
                ['Тотал', sum(self.status_count.values())]
            )
