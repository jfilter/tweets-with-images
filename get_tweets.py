import argparse

import twint

parser = argparse.ArgumentParser()
parser.add_argument("name")
args = parser.parse_args()

print(args.name)

# Configure
c = twint.Config()
c.Username = args.name
c.Store_csv = True
c.Output = 'temp.csv'

# Run
twint.Search(c)
