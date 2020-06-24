#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:04:49 2020

@author: stephandupoux
"""

from gensim.models import Word2Vec, KeyedVectors
import re
import string
import zstandard as zstd
import ujson as json
import random
random.seed(74)

class Zreader:

    def __init__(self, file, chunk_size=16384):
        '''Init method'''
        self.fh = open(file,'rb')
        self.chunk_size = chunk_size
        self.dctx = zstd.ZstdDecompressor()
        self.reader = self.dctx.stream_reader(self.fh)
        self.buffer = ''


    def readlines(self):
        '''Generator method that creates an iterator for each line of JSON'''
        while True:
            chunk = self.reader.read(self.chunk_size).decode()
            if not chunk:
                break
            lines = (self.buffer + chunk).split("\n")

            for line in lines[:-1]:
                yield line

            self.buffer = lines[-1]

wordss = []
# Adjust chunk_size as necessary -- defaults to 16,384 if not specified
reader = Zreader('/Users/stephandupoux/OneDrive - Drexel University/BSAN 499/Pushshift/RC_2019-11.zst')
# Read each line from the reader
ß = 0
Pushshift = []
remove = set(['[removed]', '[deleted]'])
for line in reader.readlines():
    j = json.loads(line)
    pushshift = {'ids' : j['id'],
                 'edited' : j['edited'],
                 'link_id' :j['link_id'],
                 'author' : j['author'],
                 'parent_id' :j['parent_id'],
                 'Subreddit' :j['subreddit'],
                 'body' : j['body'],
                 'Controversial' : j['controversiality'],
                 'Score' : j['score'],
                 'created_utc' : j['created_utc']}
    Pushshift.append(pushshift)

#started at 10:40PM on May 20th 2020.....
#It at 2015901 for the condition lol
print('This bullshit is currently training')
model = Word2Vec(wordss, size = 300, seed = 74)
print('Now to save this fat ass model')
filename = f'Reddit nov 2019 {len(wordss)} words model.bin'
model.wv.save_word2vec_format(filename, binary=True)
print('Finished all of this bullshit')

model.most_similar('faggot')

penis = KeyedVectors.load_word2vec_format("Reddit nov 2019 6355290 words model.bin", binary=True)


