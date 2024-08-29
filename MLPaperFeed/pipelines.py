from itemadapter import ItemAdapter
from pathlib import Path
import csv

class GeneralPipeline:
    def process_item(self, item, spider):
        if isinstance(item, dict):
            directory = Path('results')
            file_path = directory / spider.file_name
            path_exists = file_path.exists()
            
            with file_path.open(mode = 'a', newline = '') as file:
                writer = csv.DictWriter(file, fieldnames=item.keys())
                if not path_exists:
                    writer.writeheader()
                writer.writerow(item)

