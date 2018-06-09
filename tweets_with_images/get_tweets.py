import twint


def get_tweets(name, path):
    # Configure
    c = twint.Config()
    c.Username = name
    c.Store_csv = True
    c.Output = path + '/temp.csv'

    # Run
    twint.run.Search(c)
