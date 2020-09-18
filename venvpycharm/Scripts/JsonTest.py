import json

data = {}
data['objCalcs'] = []
data['objCalcs'].append({
    'a': 60,
    'b': 30,
    'somar': 90,
    'subr': 30,
    'multr': 1800,
    'divr': 2,
})
data['objCalcs'].append({
    'a': 15,
    'b': 5,
    'somar': 20,
    'subr': 10,
    'multr': 75,
    'divr': 3,
})
data['objCalcs'].append({
    'a': 12,
    'b': 24,
    'somar': 36,
    'subr': -12,
    'multr': 288,
    'divr': 0.5,
})

with open('Test/data.txt', 'w') as outfile:
    json.dump(data, outfile)