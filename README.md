# wedding

`wedding` is a Django based web project for your wedding site.

"For perfectionists with deadlines." Indeed.

## Project requirements

1. Map for location with spouses homes, church and party location
2. Information page with interesting places to visit nearby
3. BnB information for guests (allocation, sold-out, let us handle it, etc)
4. Guest confirmations
5. Gifts (Send e-mail (mailgun) with bank transfer information (to not have bank credentials online))
6. Contact information (e-mail, phone, address (send by e-mail))

## Cheatsheet

Push to production by

    ansible-playbook -i production site.yml --ask-vault-pass -vvvv


### References

Borrowed ansible wisdom from:

[jcalazan](https://www.calazan.com/ansible-playbook-for-a-django-stack-nginx-gunicorn-postgresql-memcached-virtualenv-supervisor/)

[jcalazan's ansible-django-stack](https://github.com/jcalazan/ansible-django-stack)

[jcalazan's youtube-audio-dl](https://github.com/jcalazan/youtube-audio-dl)
