# Beyond basics

## Handlers

* Create handlers in yaml file:

```yaml
handlers:
    - name: restart apache
      service:
        name: httpd
        state: restarted
```

* Trigger the handler:

```yaml
tasks:
    - name: Copy test config file.
      copy:
        src: files/test.conf
        dest: /etc/httpd/conf.d/test.conf
      notify: restart apache
```

## Variables

### Add environment variables

```yaml

- name: Add an environment variable to the remote user's shell.
lineinfile:
    dest: "~/.bash_profile"
    regexp: '^ENV_var='
    line: 'ENV_VAR=value'
```

**OR**

```yaml
environment:
  variable_name: <value>
```

### Add variables in yaml file

```yaml
vars:
  proxy_vars:
    http_proxy: <val>
    https_proxy: <val>
```

or use external var file
