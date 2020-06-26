__Introduction to Conversational Threading Word2vec with__

<img src="img/reddit0.jpg" width=385px />

Parent Child \(R\)	          OP\-Level  \(R\)	                     Parent Child \(G\)                 OP\-Level  \(G\)

Word2Vec can detect a conversation when it is on discussion

Google News Corpus tends to underestimate the similarity of text

Google Corpus fares worse with comment chains where it largely follows around jokes

Reddit Corpus CAN detect jokes

Also good with finding meaning of the text

Potentially can signal if subreddits are less strict with the moderation with comments going off topic

Noticeable clusters of Discussions and jokes comments in a chain

can see comments where discussion goes off topic from original conversation\)

Based on research on detecting Dark Triad Traits with ML models\, Main goal was to see if machines can detect conversations between different users

Word2Vec is an unsupervised learning model that takes words makes it a vector\.

Google News Model is the base model

<img src="img/reddit1.jpg" width=390px />

<img src="img/reddit2.jpg" width=380px />

<img src="img/reddit3.jpg" width=380px />

<img src="img/reddit4.jpg" width=384px />

<img src="img/reddit5.jpg" width=380px />

<img src="img/reddit6.jpg" width=384px />

<img src="img/reddit7.jpg" width=372px />

<img src="img/reddit8.jpg" width=384px />

Questions to ask

Can machines effectively detect conversations and relate similarity between each other

Can you see based on conversations if a subreddit is poorly moderated

Do different spaces affect the similarities between threads

<img src="img/reddit9.jpg" width=384px />

<img src="img/reddit10.jpg" width=380px />

<img src="img/reddit11.jpg" width=380px />

<img src="img/reddit12.jpg" width=384px />

Questions to ask

Reddit Dataset was kind of small\. Some subreddits are very small and didn’t have the required 8 comment chain

Reddit corpus is not as large as the google news corpus\, simply due to limitations of training computer and minimal RAM

Gathered the top posts from six subreddits and took a comment chain of 8 from each post

Coronavirus

COVID19

IAmA

UnethicalLifeProTips

Machine Learning

Learn Machine Learning

Created a word2vec model with 6 million comments from November 2019

Computed the cosine distance with the Google News Corpus and Reddit Corpus

Top comment chain\, next level chain

Parent reply down the chain

Showed the results on a Violin Plot

Reddit Word2Vec space denoted as R

Google News Word2vec space denoted as G

<img src="img/reddit13.jpg" width=384px />

<img src="img/reddit14.jpg" width=380px />

<img src="img/reddit15.jpg" width=380px />

<img src="img/reddit16.jpg" width=384px />

Detecting when comments start veering off\-topics

Seeing when jokes come from the meaning of text

Gaining meaning from the text

Applications to help keep debates on topic

<img src="img/reddit17.jpg" width=384px />

<img src="img/reddit18.jpg" width=380px />

<img src="img/reddit19.jpg" width=380px />

<img src="img/reddit20.jpg" width=384px />

<img src="img/reddit21.jpg" width=390px />

<img src="img/reddit22.jpg" width=386px />

<img src="img/reddit23.jpg" width=372px />

<img src="img/reddit24.jpg" width=384px />

