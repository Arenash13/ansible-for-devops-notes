# Plugins and collections

## Why should you use it

* As Ansible evolved over the years, hundreds even thousands modules emerged and it became nearly impossible to maintain it in the ansible-core.
* With plugins, it's not necessary to implement it in core, maitain it in core (fixes can take some time to merge in). You can just build it on the side
* As plugins logic (merged in collections) is extracted from the core (for instance php plugins), these can be maintained by the one that use it rather than being maintained in a centralized manner.

`ansible-playbook <playbook> -c local -i "localhost,"`: run playbook on local
`ansible-galaxy collection init local.colors --init-path ./collections/ansible_collections`: create a collection for namespace local.colors

`ansible-galaxy collection install -r requirements.yml`: Install collections specified in the requirements.yml file
