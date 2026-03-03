departs = {'HR' : 10, 'Marketing' : 5, 'Sales' : 3, 'Admistrative' : 5}
departs['HR'] -= 2
departs['Finance'] = 1
del departs['Admistrative']
print(departs)
count = 0
for i in departs:
    count += departs[i]

print(count)