import csv
from datetime import datetime

from collections import defaultdict
from pep_parse.settings import BASE_DIR

FILE = 'results/status_summary_{0}.csv'


class PepParsePipeline:
    status_count = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if item['status'] not in PepParsePipeline.status_count:
            PepParsePipeline.status_count[item['status']] = 0
        PepParsePipeline.status_count[item['status']] += 1

        return item

    def close_spider(self, spider):
        time = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        path = BASE_DIR / FILE.format(time)
        with open(path, mode='w', encoding='utf-8') as csvfile:
            dialects = csv.unix_dialect
            writer = csv.writer(csvfile, dialect=dialects,
                                quoting=csv.QUOTE_ALL)
            total = sum(self.status_count.values())
            writer.writerows(['Статус', 'Количество'],
                             self.status_count.items(), ['Total', total])
