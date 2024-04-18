import re
import numpy as np

class DataCleaning:
    def __init__(self,text):
        self.text = text

    def __str__(self):
        return self.text

    def low_cast_data(self):
        self.text = self.text.lower()

    def remove_punc(self):
        punc = r'[#$%&\'()*+,\-./:;<=>@\[\\\]^_`{|}~]'
        self.text = re.sub(punc, '', self.text)

    def extra_space(self):
        self.text = " ".join(self.text.split())

    def remove_html_tags(self):
        self.text = re.sub(r'<.*?>', '', self.text)

    def remove_urls(self):
        url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
        self.text = re.sub(url_pattern, '', self.text)
    
    def clean(self):
        self.low_cast_data()
        self.remove_html_tags()
        self.remove_punc()
        self.extra_space()
        self.remove_urls()
        return self.text
    
def batch_clean(texts):
    return np.array([DataCleaning(text).clean() for text in texts])