band = {
    'vocals':'plant',
    'guitar':'page'}

# print(band)
# print(type(band))
# print(len(band))

# #####ACESS items
# print(band['vocals'])
# print(band.get('guitar'))

# # list all keys

# print(band.keys())

# # list all values

# print(band.values())

# # list of key/value pairs as tuples

# print(band.items())

# #verify a key exists

# print('guitar' in band)
# print('triangle' in band)

# #change values 

# band['vocals'] = 'coverdale'
# band.update({'bass':'jpj'})
# print(band)

# #remove items

# print(band.pop('bass'))
# print(band)

# band['drums'] = 'bonham'
# print(band)

# print(band.popitem())
# print(band)

# #delete and clear
# band['drums'] = 'bonham'
# del band['drums']
# print(band)

#copy dictionaries

# band2 = band #creates a reference
# print("bad copy")
# print("band2")
# print("band")

# band2['drums'] = 'dave'
# print(band)

# good copy
# band2 = band.copy()
# band2['drums'] = 'dave'
# print(band)
# print(band2)

#nested dictionaries

member1 = {
    'name':'plant',
    'instrument':'vocals'
}
member2 = {
    'name':'page',
    'instrument':'guitar'
}
band = {
    'member1':member1,
    'member2':member2
}
print(band)

print(band['member1']['name'])

