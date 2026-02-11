
# Tunings are formatted in string order 6-5-4-3-2-1

tuning_standard = ['E', 'A', 'D', 'G', 'B', 'E']
tuning_drop_d = ['D', 'A', 'D', 'G', 'B', 'E']
tuning_e_flat = ['Eb', 'Ab', 'Db', 'Gb', 'Bb', 'Eb']

tuning_dict = {'Standard': tuning_standard, 'Drop D': tuning_drop_d, 'E Flat': tuning_e_flat}


def get_standard_tuning():
    return tuning_standard

def get_tuning(name):
    return tuning_dict[name]

def load_tuning(tuning):
    
    return