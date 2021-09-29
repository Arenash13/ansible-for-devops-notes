# Ansible custom 'blue' test plugin definition

def is_blue(string):
    blue_values = [
        'blue',
        '#0000ff',
        '#00f',
        'rgb(0,0,255)',
        'rgb(0%,0%,100%)',
    ]
    return string in blue_values

class TestModule(object):
    ''' Ansible core jinja2 tests '''

    def tests(self):
        return {
            'blue': is_blue,
        }