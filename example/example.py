import os, sys
sys.path.insert(1, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))


'''
from api import get_json
from pprint import pprint
import json
pprint(get_json(37.8267, -122.423))
sys.exit()
'''

from api import get_location
location = get_location(37.8267, -122.423)
print location
