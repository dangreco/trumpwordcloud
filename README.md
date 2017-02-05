# trumpwordcloud
Takes most frequent words tweeted with "Donald Trump" and generates a word cloud. Also pushes it to twitter.
NOTE: both main.py and push.py have to be running on two different threads in order to work. I was too lazy to incorporate multithreading and/or a cleaner way to do both at the same time.

# main.py
This is the base file for actually collecting tweets and storing words.

# excludeDict.py
This is the handler for words you don't want in your cloud. List 'd' is for explicit words, whereas list 'i' is for words that include those strings. Obviously don't put "a" in list 'i', as it will block all words containing the letter 'a' from going into the word cloud; so you would put "a" in list 'd' as you want to block the literal "a".

# push.py
This is the program that periodically generates the word cloud (set frequency where marked in file), and publishes it to your timeline in Twitter.

# words.txt
This is the text file that stores all of the words associated with Donald Trump. It only keeps them (in my use) for 6 hours, then deletes them -- this doesn't violate Twitter's terms of hoarding tweet data. Obviously, the file size gets pretty big pretty quickly. On average, I will get a total file size (at the end of 6 hours) of roughly 200 MB. That's around 9.2 KB/s. Something to keep in mind when setting a frequency. The file size is also determined by how popular your filtered phrase is to stream. Basically, if you filter by every word alongside "the", you will end up filling up your hard drive in no time -- and if you filter by "the cat is orange", it might be a few megabytes in size. My advice is to do a test run for a minute on your phrase, and see how that goes. 
