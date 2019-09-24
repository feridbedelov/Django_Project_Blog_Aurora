import math
import re
import datetime
from django.utils.html import strip_tags

# def count_words(html_string):
#     word_string=strip_tags(html_string)
#     matching_words = re.findall(r'\w+',word_string)
#     count=len(matching_words)
#     return count
    


def count_words(sentence):
    counts = sentence.split()
    return len(counts)

def get_read_time(sentence):
    count=count_words(sentence)
    read_time_min = math.ceil(count/200.0)
    # read_time=str(datetime.timedelta(minutes=read_time_min))
    return int(read_time_min)
