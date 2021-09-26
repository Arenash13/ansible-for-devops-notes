## Run command
`ansible -i inventory example -m <command> -u <user>` with an inventory file that looks like that :
```
[example]
<ip_address>
```
* Config file ansible.cfg : 
```
[defaults]
INVENTORY = inventory
```
## Run ad-hoc command
* Example: `ansible example -a "free -h" -u <user>` 