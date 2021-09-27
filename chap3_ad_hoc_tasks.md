# Ad hoc

* `ansible -i inventory multi -a "hostname"`: Faire une commande ad-hoc sur plusieurs serveurs. Le fichier inventory:

```ini
# Application servers
[app]
192.168.60.4
192.168.60.5

# Database server
[db]
192.168.60.6

# Groups has all the servers
[multi:children]
app
db
# Varialbles for all the servers
[multi:vars]
ansible_ssh_user=vagrant
ansible_ssh_private_key_file=~/.vagrant.d/insecure_private_key

```

* Par défaut, ansible fonctionne avec 5 forks (=> la commande du dessus sera exécutée en même temps pour chaque serveur)
=> Forcer une commane à la fois `ansible -i inventory multi -a "<command>" -f 1`

* `ansible -a "df -h"` : voir l'espace qu'il reste sur le système
* `ansible -a "free -h"` : voir l'utilisation de la ram/swap
* `ansible -m setup` : voir le setup de la machine
* `ansible -i inventory multi -b -m yum -a "name=ntp state=present"` : -b (become sudo), -m (module) -a (argument) => vérifie que le paquet ntp a bien été installé via yum sur les serveurs
* `ansible -i inventory multi -b -m service -a "name=ntpd state=started enabled=yes"` : vérifier que le service ntp est bien lancé
* `ansible app -b -m group -a "name=admin state=present"` : Ajouter un groupe admin
* `ansible app -b -m user -a "name=johndoe group=admin createhome=yes"` : Ajouter un utilisateur
* `ansible ... -B 3600 -P 0 ...` : lancer une commande en background (-B 3600 secondes), -P (polling sur le serveur toutes les x secondes)