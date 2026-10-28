import re

class HtmlCleaner:
    def __init__(self, html_content):
        self.html_content = html_content

    def clean(self):
        pattern = r'<[^>]+>'
        return re.sub(pattern, '', self.html_content)

if __name__ == "__main__":
    html_input = input("Enter HTML content: ")
    cleaner = HtmlCleaner(html_input)
    print(cleaner.clean())