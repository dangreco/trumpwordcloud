# trumpwordcloud
Takes most frequent words tweeted with "Donald Trump" and generates a word cloud. Also pushes it to twitter.
NOTE: both main.py and push.py have to be running on two different threads in order to work. I was too lazy to incorporate multithreading and/or a cleaner way to do both at the same time.

# main.py
This is the base file for actually collecting tweets and storing words.

# excludeDict.py
This is the handler for words you don't want in your cloud. List 'd' is for explicit words, whereas list 'i' is for words that include those strings. Obviously don't put "a" in list 'i', as it will block all words containing the letter 'a' from going into the word cloud; so you would put "a" in list 'd' as you want to block the literal "a".

# push.py
This is the program that periodically generates the word cloud (set frequency where marked in file), and publishes it to your timeline in Twitter.

