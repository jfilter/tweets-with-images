# Tweets with Images

A rough approach to get all images that are posted by a user on Twitter (excluding images in replies).

First, I use [Twint](https://github.com/haccer/twint) to first get all the tweets. It doesn't use the official API but another undocumented one, so we don't need API keys. The resulting tweets, are stored in a temporary CSV (there is no way to get results directly).

Second, I check for links to meda files in the tweets. The image URLs are not linked directly so I have to scrape them off another site. All togehter it's very dirty way and it will break with the slightest UI changes, but it still may be helpful to you.

1.  install [pipenv](https://github.com/pypa/pipenv#installation)
2.  `git clone https://github.com/jfilter/tweets-with-images && cd tweets-with-images`
3.  `pipenv install`
4.  Change user handle in [get_tweets.py](get_tweets.py#L5)
5.  `pipenv run python get_tweets.py`
6.  `pipenv run python get_images.py`

## License

MIT.
