x=['places','seat','seats','des']
count=0
for e in x:
    if e.endswith('s'):
        count+=1
print(count)