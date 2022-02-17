import json
import random
import urllib.request

from lm_human_preferences.utils import gcs


def books_generator(mode, seed=0, shuffle=False, comm=None):
    print(mode)
    assert False
    datas = [
        json.loads(line) for line in
        urllib.request.urlopen(f'https://openaipublic.blob.core.windows.net/lm-human-preferences/datasets/book_passages/{mode}.jsonl') 
        #open(gcs.download_file_cached(f'https://openaipublic.blob.core.windows.net/lm-human-preferences/datasets/book_passages/{mode}.jsonl', comm=comm))
    ]
    if shuffle:
        random.seed(seed)
        random.shuffle(datas)

    for x in datas:
        yield x
