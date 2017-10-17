from types import ModuleType

import requests

from . import resources, utility

# Create a dict of resource classes
RESOURCE_CLASSES = {}
for resource_name, resource_module in resources.__dict__.items():

    if isinstance(resource_module, ModuleType) and resource_name.capitalize() in resource_module.__dict__:
        RESOURCE_CLASSES[resource_name] = resource_module.__dict__[resource_name.capitalize()]

UTILITY_CLASSES = {}
for utility_name, utility_module in utility.__dict__.items():
    if isinstance(utility_module, ModuleType) and utility_name.capitalize() in utility_module.__dict__:
        UTILITY_CLASSES[utility_name] = utility_module.__dict__[utility_name.capitalize()]


class Client(object):

    VERSION = '1.0.1'

    def __init__(self, access_id="", secret_key=""):
        self.session = requests.Session()
        self.access_id = access_id
        self.secret_key = secret_key

        self.cert_path = False
        self.app_info = {}

        # intializes each resource
        # injecting this client object into the constructor
        for resource_class_name, resource_klass in RESOURCE_CLASSES.items():
            setattr(self, resource_class_name, resource_klass(self))

        for utility_class_name, utility_klass in UTILITY_CLASSES.items():
            setattr(self, utility_class_name, utility_klass(self))

    def set_app_info(self, app_name, app_version="", app_url=""):
        self.app_info = {
            'name': app_name,
            'version': app_version,
            'url': app_url,
        }

    def get_app_info(self):
        return self.app_info
