# Ansible introduction

<mark>Any documentation about a module,... can be found using command "ansible-doc &lt;what_youre_looking_for&gt;" (example: "ansible-doc yum")</mark>

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
