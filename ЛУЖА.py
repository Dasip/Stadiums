from mymapapi import show_map
from mygeocoder import get_coordinates as get_core

def main():
    stads = ['Динамо', 'Лужники', 'Москва, стадион Спартак']
    map_locations = None
    map_type = 'sat'
    map_param = []
    for i in stads:
        c = get_core(i)
        map_param.append('{},{},pmwtm{}'.format(c[0], c[1], stads.index(i) + 1))
    map_param = 'pt=' + '~'.join(map_param)
    show_map(map_locations, map_type, map_param)
    
if __name__ == '__main__':
    main()