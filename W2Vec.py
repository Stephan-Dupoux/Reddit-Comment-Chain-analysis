import random
import numpy as n
import nltk
nltk.download('all')
random.seed(74)
import pandas as p
from scipy import spatial
from nltk.corpus import stopwords
from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
import scipy.stats as fps
import seaborn as mw3
# first party python apps
import os
import glob
import json
import re
import random

#function to flatten json file to a dataframe
def flatten_json(nested_json, exclude=['']):
    out = {}
    def flatten(x, name='', exclude=exclude):
        if type(x) is dict:
            for a in x:
                if a not in exclude: flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

#function to count number of words in reddit comment
def wct(strz, stop_words):
    strz = str(strz)
    counts = list()
    words = strz.split()

    for word in words:
        if word in stop_words:
            counts.append(1)
    v = sum(counts)
    lren = len(words)
    
    return v, lren

#function to add and average feature vectors for word2vec model
def avg_feature_vector(sentence, model, num_features, index2word_set):
    feature_vec = n.zeros((num_features, ), dtype='float32')
    n_words = 0
    for word in sentence:
        if word in index2word_set:
            n_words += 1
            feature_vec = n.add(feature_vec, model[word])
    if (n_words > 0):
        feature_vec = n.divide(feature_vec, n_words)
    return feature_vec


stop_words = set(stopwords.words('english'))


sw = stopwords.words('english')
punctuations = list('''!()-[]{};:'"\,<>./?@#$%^&*_~*''')
sw.append(punctuations)


tpath = 'BSAN 499/'

second = []
top = []
reply = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eigth = []
ninth = []
tenth = []
title = []
subreddit = []

westerns = []

os.chdir(tpath)
extension = 'json'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#Get the titles stuff
for i in all_filenames:
    file = tpath + i
    with open(i) as q:
        df = json.load(q)
    dataframes = p.DataFrame([flatten_json(x) for x in df[1]])
    try:
        dataframes['title'] = str(df[0]['title'])
        dataframes['subreddit'] = str(df[0]['permalink'].split('/')[2])
    except TypeError:
        print('An Error Occured')
    westerns.append(dataframes)

for i,wefw in enumerate(westerns):
    y = westerns[i]
    try:
        for x,pp,an,four,od,kk,vs,pwe, times, timess, titlez, subreddits  in zip(y.body, y.replies_0_body, y.replies_0_replies_0_body, y.replies_0_replies_0_replies_0_body,
                                                                                y.replies_0_replies_0_replies_0_replies_0_body, y.replies_0_replies_0_replies_0_replies_0_replies_0_body,
                                                                                y.replies_0_replies_0_replies_0_replies_0_replies_0_replies_0_body, y.replies_0_replies_0_replies_0_replies_0_replies_0_replies_0_replies_0_body,
                                                                                y.replies_0_replies_0_replies_0_replies_0_replies_0_replies_0_replies_0_body,
                                                                                y.replies_0_replies_0_replies_0_replies_0_replies_0_replies_0_replies_0_body,
                                                                                y.title, y.subreddit):
            second.append(an)
            third.append(four)
            top.append(x)
            reply.append(pp)
            fifth.append(od)
            sixth.append(kk)
            seventh.append(vs)
            eigth.append(pwe)
            ninth.append(times)
            tenth.append(timess)
            title.append(titlez)
            subreddit.append(subreddits)
    except AttributeError:
        print('Error')
    

dom = p.DataFrame()
dom['First'] = top
dom['Second'] = reply
dom['Third'] = second
dom['Fourth'] = third
dom['Fifth'] = fifth
dom['Sixth'] = sixth
dom['Seventh'] = seventh
dom['Eigth'] = eigth
dom['Title'] = title
dom['Subreddit'] = subreddit



q = dom
del dom

del second
del top
del reply 
del third
del fourth
del fifth 
del sixth
del seventh 
del eigth
del ninth
del tenth
del title
del subreddit



q = q[q.First!= '[removed]']
q = q[q.First != '[deleted]']

q = q[q.Second!= '[removed]']
q = q[q.Second != '[deleted]']

q = q[q.Third!= '[removed]']
q = q[q.Third!='[deleted]']

q = q[q.Fourth!= '[removed]']
q = q[q.Fourth!= '[deleted]']

q = q[q.Fifth!= '[removed]']
q = q[q.Fifth!= '[deleted]']

q = q[q.Sixth!= '[removed]']
q = q[q.Sixth!= '[deleted]']

q = q[q.Seventh!= '[removed]']
q = q[q.Seventh!= '[deleted]']

q = q[q.Eigth!= '[removed]']
q = q[q.Eigth!= '[deleted]']

q = q.dropna()
q = q.reset_index(drop=True)





swdf = p.DataFrame()
CC = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eigth']
for z in CC:
    sw = []
    lens = []
    pcnt = []
    for i in q[z]:
        a, b = wct(i, stop_words)
        sw.append(a)
        lens.append(b)
        pcnt.append(a/b)
    swdf[z + ' SW'] = sw
    swdf[z + ' Length'] = lens
    swdf[z + ' Percent SW'] = pcnt
    print(z)

swdf.boxplot(column=['First Percent SW', 'Second Percent SW', 'Third Percent SW',
                     'Fourth Percent SW', 'Fifth Percent SW', 'Sixth Percent SW',
                     'Seventh Percent SW', 'Eigth Percent SW'])

swdf.boxplot(column=['First Length', 'Second Length', 'Third Length',
                     'Fourth Length', 'Fifth Length', 'Sixth Length',
                     'Seventh Length', 'Eigth Length'])




parent = []
for i in q.First:
    i = i.encode('ascii', 'ignore').decode('ascii')
    i = re.sub(r'^https?:\/\/.*[\r\n]*', '', i, flags=re.MULTILINE)
    w = i.split()
    parent.append(w)

child = []
for i in q.Second:
    i = i.encode('ascii', 'ignore').decode('ascii')
    i = re.sub(r'^https?:\/\/.*[\r\n]*', '', i, flags=re.MULTILINE)
    w = i.split()
    child.append(w)

childdos = []
for i in q.Third:
    i = i.encode('ascii', 'ignore').decode('ascii')
    i= re.sub(r'^https?:\/\/.*[\r\n]*', '', i, flags=re.MULTILINE)
    w = i.split()
    childdos.append(w)

childtres = []
for i in q.Fourth:
    i = i.encode('ascii', 'ignore').decode('ascii')
    i = re.sub(r'^https?:\/\/.*[\r\n]*', '', i, flags=re.MULTILINE)
    w = i.split()
    childtres.append(w)

childfive = []
for i in q.Fifth:
    i = i.encode('ascii', 'ignore').decode('ascii')
    i = re.sub(r'^https?:\/\/.*[\r\n]*', '', i, flags=re.MULTILINE)
    w = i.split()
    childfive.append(w)

childsix = []
for i in q.Sixth:
    i = i.encode('ascii', 'ignore').decode('ascii')
    i = re.sub(r'^https?:\/\/.*[\r\n]*', '', i, flags=re.MULTILINE)
    w = i.split()
    childsix.append(w)

childseven = []
for i in q.Seventh:
    i = i.encode('ascii', 'ignore').decode('ascii')
    i = re.sub(r'^https?:\/\/.*[\r\n]*', '', i, flags=re.MULTILINE)
    w = i.split()
    childseven.append(w)

childeight = []
for i in q.Eigth:
    i = i.encode('ascii', 'ignore').decode('ascii')
    i = re.sub(r'^https?:\/\/.*[\r\n]*', '', i, flags=re.MULTILINE)
    w = i.split()
    childeight.append(w)



for starr in parent:
    for star in starr:
        if star in stop_words: 
            starr.remove(star)

for starr2 in child:
    for star in starr2:
        if star in stop_words: 
            starr2.remove(star)

for starr3 in childdos: 
    for star in starr3:
        if star in stop_words: 
            starr3.remove(star)

for starr4 in childtres:
    for star in starr4:
        if star in stop_words: 
            starr4.remove(star)

for starr5 in childfive:
    for star in starr5:
        if star in stop_words: 
            starr5.remove(star)

for starr6 in childsix:
    for star in starr6:
        if star in stop_words: 
            starr6.remove(star)

for starr7 in childseven:
    for star in starr7:
        if star in stop_words: 
            starr7.remove(star)

for starr8 in childeight:
    for star in starr8:
        if star in stop_words: 
            starr8.remove(star)


q['f'] = parent
q['s'] = child
q['t'] = childdos
q['fo'] = childtres
q['fi'] = childfive
q['si'] = childsix
q['se'] = childseven
q['e'] = childeight




redmess = KeyedVectors.load_word2vec_format("Reddit nov 2019 6355290 words model.bin", binary=True)
smokes = set(redmess.vocab)

filename = 'GoogleNews-vectors-negative300.bin.gz'
Gmodel = KeyedVectors.load_word2vec_format(filename, binary=True)
smokes = set(Gmodel.vocab)


Gmodel.most_similar('protester')
one2two = []
one2three = []
one2four = []
one2five = []
one2six = []
one2seven = []
one2eight = []

mosdef = p.DataFrame()
r = range(0,1511)
for i in r:
    wdd = q.f[i]
    woo = q.s[i]
    woooo = q.t[i]
    wooooo = q.fo[i]
    yer = q.fi[i]
    yerr = q.si[i]
    yerrr = q.se[i]
    yerrrr = q.e[i]
    
    s1_afv = avg_feature_vector(wdd, model=Gmodel, num_features=300, index2word_set=smokes)
    s2_afv = avg_feature_vector(woo, model=Gmodel, num_features=300, index2word_set=smokes)
    s3_afv = avg_feature_vector(woooo, model=Gmodel, num_features=300, index2word_set=smokes)
    s4_afv = avg_feature_vector(wooooo, model=Gmodel, num_features=300, index2word_set=smokes)
    s5_afv = avg_feature_vector(yer, model=Gmodel, num_features=300, index2word_set=smokes)
    s6_afv = avg_feature_vector(yerr, model=Gmodel, num_features=300, index2word_set=smokes)
    s7_afv = avg_feature_vector(yerrr, model=Gmodel, num_features=300, index2word_set=smokes)
    s8_afv = avg_feature_vector(yerrrr, model=Gmodel, num_features=300, index2word_set=smokes)
    
    sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
    one2two.append(sim)
    sim = 1 - spatial.distance.cosine(s1_afv, s3_afv)
    one2three.append(sim)
    sim = 1 - spatial.distance.cosine(s1_afv, s4_afv)
    one2four.append(sim)
    sim = 1 - spatial.distance.cosine(s1_afv, s5_afv)
    one2five.append(sim)
    sim = 1 - spatial.distance.cosine(s1_afv, s6_afv)
    one2six.append(sim)
    sim = 1 - spatial.distance.cosine(s1_afv, s7_afv)
    one2seven.append(sim)
    sim = 1 - spatial.distance.cosine(s1_afv, s8_afv)
    one2eight.append(sim)

mosdef['one-two'] = one2two
mosdef['one-three'] = one2three
mosdef['one-four'] = one2four
mosdef['one-five'] = one2five
mosdef['one-six'] = one2six
mosdef['one-seven'] = one2seven
mosdef['one-eight'] = one2eight
mosdef['Sub'] = q['Subreddit']




lml = mosdef[mosdef.Sub == 'learnmachinelearning']
IAmA = mosdef[mosdef.Sub == 'IAmA']
ULPT = mosdef[mosdef.Sub == 'UnethicalLifeProTips']
COVID19 = mosdef[mosdef.Sub == 'COVID19']
SARS = mosdef[mosdef.Sub == 'Coronavirus']
ml = mosdef[mosdef.Sub == 'MachineLearning']

mw3.violinplot(data = SARS).set_title('coronavirus Top-Low')
mw3.violinplot(data = COVID19).set_title('COVID19 Top-Low')
mw3.violinplot(data = IAmA).set_title('IAmA Top-Low')
mw3.violinplot(data = ULPT).set_title('Unethical LPT Top-Low')
mw3.violinplot(data = ml).set_title('Machine Learning Top-Low')
mw3.violinplot(data = lml).set_title('Learn ML Top-Low')



mosdef.boxplot(column=['one-two', 'one-three', 'one-four', 'one-five', 'one-six', 'one-seven', 'one-eight'])
SARS.boxplot(column=['one-two', 'one-three', 'one-four', 'one-five', 'one-six', 'one-seven', 'one-eight'])
COVID19.boxplot(column=['one-two', 'one-three', 'one-four', 'one-five', 'one-six', 'one-seven', 'one-eight'])
IAmA.boxplot(column=['one-two', 'one-three', 'one-four', 'one-five', 'one-six', 'one-seven', 'one-eight'])
ULPT.boxplot(column=['one-two', 'one-three', 'one-four', 'one-five', 'one-six', 'one-seven', 'one-eight'])
SARS.boxplot(column=['one-two', 'one-three', 'one-four', 'one-five', 'one-six', 'one-seven', 'one-eight'])
ml.boxplot(column=['one-two', 'one-three', 'one-four', 'one-five', 'one-six', 'one-seven', 'one-eight'])



filename = 'GoogleNews-vectors-negative300.bin.gz'
Gmodel = KeyedVectors.load_word2vec_format(filename, binary=True)





Gone2two = []
Gtwo2three = []
Gthree2four = []
Gfour2five = []
Gfive2six = []
Gsix2seven = []
Gseven2eight = []
Geight2nine = []
Gnine2ten = []


hmap = []
afv = []
#len(q)
of = 1
r = range(0,1511)
for i in r:
    wdd = q.f[i]
    woo = q.s[i]
    woooo = q.t[i]
    wooooo = q.fo[i]
    yer = q.fi[i]
    yerr = q.si[i]
    yerrr = q.se[i]
    yerrrr = q.e[i]

    s1_afv = avg_feature_vector(wdd, model=Gmodel, num_features=300, index2word_set=smokes)
    s2_afv = avg_feature_vector(woo, model=Gmodel, num_features=300, index2word_set=smokes)
    s3_afv = avg_feature_vector(woooo, model=Gmodel, num_features=300, index2word_set=smokes)
    s4_afv = avg_feature_vector(wooooo, model=Gmodel, num_features=300, index2word_set=smokes)
    s5_afv = avg_feature_vector(yer, model=Gmodel, num_features=300, index2word_set=smokes)
    s6_afv = avg_feature_vector(yerr, model=Gmodel, num_features=300, index2word_set=smokes)
    s7_afv = avg_feature_vector(yerrr, model=Gmodel, num_features=300, index2word_set=smokes)
    s8_afv = avg_feature_vector(yerrrr, model=Gmodel, num_features=300, index2word_set=smokes)

    sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
    Gone2two.append(sim)
    sim = 1 - spatial.distance.cosine(s2_afv, s3_afv)
    Gtwo2three.append(sim)
    sim = 1 - spatial.distance.cosine(s3_afv, s4_afv)
    Gthree2four.append(sim)
    sim = 1 - spatial.distance.cosine(s4_afv, s5_afv)
    Gfour2five.append(sim)
    sim = 1 - spatial.distance.cosine(s5_afv, s6_afv)
    Gfive2six.append(sim)
    sim = 1 - spatial.distance.cosine(s6_afv, s7_afv)
    Gsix2seven.append(sim)
    sim = 1 - spatial.distance.cosine(s7_afv, s8_afv)
    Gseven2eight.append(sim)


    afv.append(s1_afv)
    afv.append(s2_afv)
    afv.append(s3_afv)
    afv.append(s4_afv)
    afv.append(s5_afv)
    afv.append(s6_afv)
    afv.append(s7_afv)
    afv.append(s8_afv)

    line = {'PC1' : s1_afv, 'PC2' : s2_afv, 'PC3' : s3_afv, 'PC4' : s4_afv, 
            'PC5' : s5_afv, 'PC6' : s6_afv, 'PC7' : s7_afv, 'PC8' : s7_afv}
    hmap.append(line)
    
    print('Finished {} rows'.format(of))
    of = of + 1


Google = p.DataFrame()
Google['Title'] = q['Title']
Google['Sub'] = q['Subreddit']
Google['onetwo'] = Gone2two
Google['twothree'] = Gtwo2three
Google['threefour'] = Gthree2four
Google['fourfive'] = Gfour2five
Google['fivesix'] = Gfive2six
Google['sixseven'] = Gsix2seven
Google['seveneight'] = Gseven2eight

lml = Google[Google.Sub == 'learnmachinelearning']
IAmA = Google[Google.Sub == 'IAmA']
ULPT = Google[Google.Sub == 'UnethicalLifeProTips']
COVID19 = Google[Google.Sub == 'COVID19']
SARS = Google[Google.Sub == 'Coronavirus']
ml = Google[Google.Sub == 'MachineLearning']

Google.boxplot(column=['onetwo', 'twothree', 'threefour', 'fourfive', 'fivesix', 'sixseven', 'seveneight'])

lml.boxplot(column=['onetwo', 'twothree', 'threefour', 'fourfive', 'fivesix', 'sixseven', 'seveneight'])
IAmA.boxplot(column=['onetwo', 'twothree', 'threefour', 'fourfive', 'fivesix', 'sixseven', 'seveneight'])
ULPT.boxplot(column=['onetwo', 'twothree', 'threefour', 'fourfive', 'fivesix', 'sixseven', 'seveneight'])
COVID19.boxplot(column=['onetwo', 'twothree', 'threefour', 'fourfive', 'fivesix', 'sixseven', 'seveneight'])
SARS.boxplot(column=['onetwo', 'twothree', 'threefour', 'fourfive', 'fivesix', 'sixseven', 'seveneight'])
ml.boxplot(column=['onetwo', 'twothree', 'threefour', 'fourfive', 'fivesix', 'sixseven', 'seveneight'])

mw3.violinplot(data = SARS).set_title('Coronavirus Parent-Child')
mw3.violinplot(data = COVID19).set_title('COVID19 Parent-Child')
mw3.violinplot(data = IAmA).set_title('IAmA Parent-Child')
mw3.violinplot(data = ULPT).set_title('Unethical LPT Parent-Child')
mw3.violinplot(data = ml).set_title('Machine Learning Parent-Child')
mw3.violinplot(data = lml).set_title('Learn ML Parent-Child')
