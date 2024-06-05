import pynetbox
from os import getenv, path
import subprocess

# Configuration of the connection to Netbox
netbox_url = 'https://10.36.194.221'  # Replace with your Netbox URL
token = '7753bd02412c1b01eb1ef83662e86fe3a5dbc390'  # Replace with your API token
## Proxy script execution ##
script_dir = path.dirname(path.realpath(__file__))
shell_script_path = path.join(script_dir, 'tests', 'setproxy.sh')
subprocess.run(f'source "{shell_script_path}"',shell=True)
##
nb = pynetbox.api(netbox_url, token=token)
nb.http_session.verify= False

def delete_all(items):
    for item in items:
        item.delete()

# Deleting IP addresses
delete_all(nb.ipam.ip_addresses.all())

# Deleting interfaces
delete_all(nb.dcim.interfaces.all())

# Deleting devices
delete_all(nb.dcim.devices.all())

# Deleting device roles
delete_all(nb.dcim.device_roles.all())

# Deleting device types
delete_all(nb.dcim.device_types.all())

# Deleting manufacturers
delete_all(nb.dcim.manufacturers.all())

# Deleting sites
delete_all(nb.dcim.sites.all())

# Deleting regions
delete_all(nb.dcim.regions.all())

# Deleting tenants
delete_all(nb.tenancy.tenants.all())

# Deleting platforms
delete_all(nb.dcim.platforms.all())

# Deleting custom fields (assuming direct access is possible)
delete_all(nb.extras.custom_fields.all())  # Make sure the custom fields endpoint is correct

print("Netbox has been emptied.")
