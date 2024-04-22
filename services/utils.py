import re
import numpy as np

class Utils:
  def dataClean(text):
      text = text.lower()
      
      text = re.sub(r'<.*?>', '', text)
      
      punc = r'[#$%&\'()*+,\-./:;<=>@\[\\\]^_`{|}~]'
      text = re.sub(punc, '', text)

      text = " ".join(text.split())

      url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
      text = re.sub(url_pattern, '', text)

      return text