# Ansible playbook

* `ansible-playbook -i <your_inventory> <your_playbook.yml>`: Run a playbook.
* `ansible-inventory --list -i invetory`: List infos knowned by ansible about your inventory.

* To include a YAML file containing variables in your playbook, add:

```yaml
  vars_files:
    - vars.yml
```

## Examples of ansible modules

### Copy files

```yaml
- name: Copy configuration files.
      copy:
        src: "{{ item.src }}" # jinja template, it's also possible to use item["src"]
        dest: "{{ item.dest }}"
        owner: root
        group: root
        mode: 0644
      with_items: # With_items will be passed to copy
        - src: httpd.conf
          dest: /etc/httpd/cong/httpd.conf
        - src: httpd-vhosts.conf
          dest: /etc/httpd/conf/httpd.conf
```

### Download from the web

```yaml
- name: Download Solr.
      get_url:
        url: "https://dlcdn.apache.org/lucene/solr/{{ solr_version }}/solr-{{ solr_version }}.tgz"
        dest: "{{ download_dir}}/solr-{{ solr_version }}.tgz"
        checksum: "{{ solr_checksum }}"
      environment:
        http_proxy: http://your-proxy:80/
        https_proxy: http://your-proxy:443/
```

with the following variables yaml file:

```yaml
download_dir: /tmp
solr_dir: /opt/solr
solr_version: 8.9.0
solr_checksum: sha512:15150b7f191fd9e8d2c1bd8bb619dd4b3f27af2e0e94b7609031f7e745a2e263391c30f68865c208afb97ccaa9bde6d16050200e9bfccef65f762c2ed743c242
```

### Unzip

```yaml
- name: Expand Solr.
      unarchive:
        src: "{{ download_dir}}/solr-{{ solr_version }}.tgz"
        dest: "{{ download_dir }}"
        remote_src: true # Will search the src on the target server
        creates: "{{ download_dir }}/solr-{{ solr_version }}/README"
    
```
