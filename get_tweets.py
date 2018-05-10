import twint

# Configure
c = twint.Config()
c.Username = "fil_ter"
c.Store_csv = True
c.Output = 'temp.csv'

# Run
twint.Search(c)
