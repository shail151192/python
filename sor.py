def custom_sort(a, b):
    return a['freq'] - b['freq']


ob = [{'id': 5, 'freq':4},{'id': 1, 'freq':3},{'id': 3, 'freq':19},{'id': 6, 'freq':12},{'id': 4, 'freq':1}]
ob.sort(custom_sort)

print ob

