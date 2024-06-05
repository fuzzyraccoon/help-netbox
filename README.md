
# Netbox Data Deletion Script

## Description
This script is designed to connect to a Netbox instance and delete all existing data, including IP addresses, interfaces, devices, device roles, device types, manufacturers, sites, regions, tenants, platforms, and custom fields. 

## Prerequisites
- Python3
- pynetbox library
- Netbox instance URL
- Netbox API token
- virtual environment activated.
- 'setproxy.sh' script  must be present in 'tests' directory.


## Configuration
Before running the script, ensure that you have replaced the placeholders for `netbox_url` and `token` with your actual Netbox URL and API token.

## Usage
1. Run the script with this command 

```
python3 vider_netbox.py
```

