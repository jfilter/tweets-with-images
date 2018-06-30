from .get_images import get_images
from .get_tweets import get_tweets


def by_user(user, media_path='./media', previous_tweet_id=None):
    tweets = get_tweets(user, previous_tweet_id)
    return get_images(tweets, media_path)
