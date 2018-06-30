import csv
import os

import twint


def _filter_out_previous_tweets(full_path, previous_tweet_id):
    rows = []
    fieldnames = None

    with open(full_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        for row in reader:
            if int(row['id']) == previous_tweet_id:
                print('match!')
                break
            else:
                rows.append(row)

    with open(full_path, newline='', mode='w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def get_tweets(name, path, previous_tweet_id=None):
    full_path = os.path.join(path, 'temp.csv')

    c = twint.Config()
    c.Username = name
    c.Store_csv = True
    c.Output = full_path

    # Run
    twint.run.Search(c)

    if previous_tweet_id is not None:
        _filter_out_previous_tweets(full_path, previous_tweet_id)
