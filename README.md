# NetBox DrawIO Plugin

A [Netbox](https://github.com/netbox-community/netbox) plugin for Access List management.

We are following the [NetBox Plugin Tutorial](https://github.com/netbox-community/netbox-plugin-tutorial).

Currently on [Step 01](https://github.com/netbox-community/netbox-plugin-tutorial/blob/main/tutorial/step01-initial-setup.md).

## Features

This plugin provides the following models:

## Compatibility

This plugin was first developed using 3.4.2.

| NetBox Version | Plugin Version |
|----------------|----------------|
|                |                |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/danner26/netbox-drawio.git@dev
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+https://github.com/danner26/netbox-drawio.git@dev
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    'netbox_drawio'
]

PLUGINS_CONFIG = {
    "netbox_drawio": {},
}
```

## Developing

### VSCode + Docker + Dev Containers

To develop this plugin further one can use the included .devcontainer configuration. This configuration creates a docker container which includes a fully working netbox installation. Currently it should work when using WSL 2. For this to work make sure you have Docker Desktop installed and the WSL 2 integrations activated.

1. In the WSL terminal, enter `code` to run Visual studio code.
1. Install the devcontainer extension "ms-vscode-remote.remote-containers"
1. Press Ctrl+Shift+P and use the "Dev Container: Clone Repository in Container Volume" function to clone this repository. This will take a while depending on your computer
1. If you'd like the netbox instance to be prepopulated run `make Makefile example_initializers` and `make Makefile load_initializers`
1. Start the netbox instance using `make Makefile all`

Your netbox instance will be served under 0.0.0.0:8000 so it should now be available under localhost:8000.

## Screenshots
