class Store:
    name = ''
    city = ''
    state = ''

    def __init__(self, name, city, state):
        self.name = name
        self.city = city
        self.state = state

    def __str__(self):
        return "{0} in {1}, {2}".format(
            self.name,
            self.city,
            self.state)

    def __unicode__(self):
        return u"{0} in {1}, {2}".format(
            self.name,
            self.city,
            self.state)
