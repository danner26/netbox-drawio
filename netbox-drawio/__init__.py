from extras.plugins import PluginConfig

class NetBoxDrawIOConfig(PluginConfig):
    name = 'netbox_drawio'
    verbose_name = 'NetBox DrawIO Plugin'
    description = 'NetBox plugin to integrate DrawIO'
    version = '0.1'
    base_url = 'drawio'
    
config = NetBoxDrawIOConfig