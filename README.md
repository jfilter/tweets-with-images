# Tweets with Images

A rough approach to get all images that are posted by a user on Twitter (excluding images in replies).

First, I use [Twint](https://github.com/haccer/twint) to first get all the tweets. It doesn't use the official API but another undocumented one, so we don't need API keys. The resulting tweets, are stored in a temporary CSV (there is no way to get results directly).

Second, I check for links to meda files in the tweets. The image URLs are not linked directly so I have to scrape them off another site. All togehter it's very dirty way and it will break with the slightest UI changes, but it still may be helpful to you.

## Usage

```console
pip install git+https://github.com/jfilter/tweets-with-images#egg=tweets_with_images
```

```python
import tweets_with_images

tweets = tweets_with_images.by_user('fil_ter')
print(tweets) # tweets with images
# the images are inside the folder 'media'. The location can be specified with the second argument.

# only select tweets that are newer than the given tweet (id)
# tweets_with_images.by_user('fil_ter', './data', 608045345201881088)
```

## License

MIT.
