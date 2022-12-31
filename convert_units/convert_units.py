def convert_units(val, convert_from, convert_to):
    SI = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
    return val*SI[convert_from]/SI[convert_to]
