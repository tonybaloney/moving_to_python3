print "Configure the engine"

dbloc = raw_input('Location to database: ')

with open('config.py', 'w') as config_py:
    config_py.write("DB_LOCATION='{0}'".format(dbloc))

print "File saved"
