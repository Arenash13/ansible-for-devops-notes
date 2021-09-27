# Ansible introduction

`ansible -i inventory example -m <command> -u <user>` lancer une commande avec le fichier inventory suivant :

```ini
[example]
<ip_address>
```

* Config file ansible.cfg :

```ini
[defaults]
INVENTORY = inventory
```

## Run ad-hoc command

* Example: `ansible example -a "free -h" -u <user>`
