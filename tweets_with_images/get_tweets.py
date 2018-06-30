import csv
import os
import tempfile

import twint


def get_tweets(name, previous_tweet_id=None):
    tweets = []
    # save in temp file because this is how twint works #shrug
    with tempfile.TemporaryDirectory() as tempdir:
        full_path = os.path.join(tempdir, 'temp.csv')
        c = twint.Config()
        c.Username = name
        c.Store_csv = True
        c.Output = full_path

        # Run
        twint.run.Search(c)

        with open(full_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if previous_tweet_id is not None and int(row['id']) == previous_tweet_id:
                    print('match!')
                    break
                else:
                    tweets.append(row)
    return tweets
