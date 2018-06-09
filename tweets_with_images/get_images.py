import csv
import pathlib
import re
from io import StringIO

import requests
from lxml import etree


def get_images(path):

    pathlib.Path(path + '/media').mkdir(parents=True, exist_ok=True)
    errors = []

    rows_with_images = []
    fieldnames = []

    with open(path + '/temp.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        fieldnames = reader.fieldnames
        print(fieldnames)

        for row in reader:
            text = row['tweet']

            # filter out replies (but the more recent tweets don't have it, we have
            # to filter out later on when scraping)
            if text.startswith('@') or text.startswith('"@'):
                continue

            m = re.search(r'pic.twitter.com/\w*', text)
            if m:
                found = m.group(0)
                print(found)

                try:
                    r = requests.get('https://' + found)
                except Exception as e:
                    print('failed: ' + found)
                    continue

                res_text = r.text
                parser = etree.HTMLParser()
                tree = etree.parse(StringIO(res_text), parser)

                # get the images, we have to exclude profile images and emojis
                # also only take 'root' tweets
                imgs = tree.xpath(
                    '//*[contains(@class, "js-initial-focus") and not (@data-has-parent-tweet="true")]//img[not(contains(@class, "profile") or contains(@class, "Emoji"))]')
                for i in imgs:
                    # use the HQ / orginal version
                    url = i.get('src') + ':large'
                    print(url)

                    # take filename from url (but omit the :large)
                    fn = url.split('/')[-1].split(':')[0]

                    # try for 3 times and otherwise collect error and go on
                    tries = 3
                    while tries > 0:
                        try:
                            media_res = requests.get(url)

                            if not media_res.ok:
                                raise Exception(media_res.status_code)

                            with open(path + '/media/' + fn, 'wb') as f:
                                f.write(media_res.content)
                            row.update({'filename': path + '/media/' + fn})
                            rows_with_images.append(row)
                            tries = 0
                        except Exception as e:
                            print(str(e))
                            errors.append(url + ',' + found + ',' + str(e))
                            tries -= 1

                    print()

    with open(path + '/tweets_with_images.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames + ['filename'])
        writer.writeheader()
        writer.writerows(rows_with_images)

    print(errors)