# Ad hoc

## Faire une commande ad-hoc sur plusieurs serveurs
`ansible -i inventory multi -a "hostname"`

* Par défaut, ansible fonctionne avec 5 forks (=> la commande du dessus sera exécutée en même temps pour chaque serveur)
=> Forcer une commane à la fois `ansible -i inventory multi -a "<command>" -f 1`