from configparser import ConfigParser

def config(filename="my_db.ini", section="postgresql"):
    #parser creation
    parser = ConfigParser()
    #reading config file
    parser.read(filename)
    dict = {}
    if parser.has_section(section):
        parameters = parser.items(section)
        for each_parameter in parameters:
            dict[each_parameter[0]] = each_parameter[1]
    else:
        raise Exception("Section called {0} is not found in filename called {1}".format(section,filename))
    print(dict)
