#dictionary = a changeable, unordered collection of unique key4
#               It is fast cause it uses hashing, and it allows the user to access a value quickly
capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'New York '})
capitals.pop('China')


#print(capitals['Russia'])

#print(capitals.get('Germany'))

#print(capitals.keys())

#print(capitals.values())

#print(capitals.items())

for key,value in capitals.items():
    print(key, value)