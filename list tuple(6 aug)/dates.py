import re
from datetime import datetime

class DateExtractor:
    def __init__(self, text):
        self.text = text

    def extract_and_convert(self):
        patterns = [
            (r'\b\d{1,2}/\d{1,2}/\d{4}\b', '%d/%m/%Y'),
            (r'\b\d{1,2}-\d{1,2}-\d{4}\b', '%m-%d-%Y'),
            (r'\b\d{4}\.\d{1,2}\.\d{1,2}\b', '%Y.%m.%d'),
            (r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b', '%B %d, %Y')
        ]
        results = []
        for pattern, fmt in patterns:
            for match in re.findall(pattern, self.text):
                try:
                    dt = datetime.strptime(match, fmt)
                    results.append(dt.strftime('%Y-%m-%d'))
                except ValueError:
                    continue
        return results

if __name__ == "__main__":
    user_input = input("Enter the date or text: ")
    extractor = DateExtractor(user_input)
    print(extractor.extract_and_convert())