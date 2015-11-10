#!/bin/bash

export DJANGO_SECRET_KEY="fx7tmh*d_kfau!)qx!m--o=%n-^do7b78y=x=2e1e300i!2ax6"
export DATABASE_URL="postgresql://wedding:wedding@localhost/wedding"
export DJANGO_SETTINGS_MODULE="wedding.settings.local"
export WEDDING_SENTRY_DSN='http://830726eb5a804be4a8d8eb8f08784778:b1d4d5f5760e4cc08996816ffaafb85d@127.0.0.1:9000/1'

#Only set the app-root/data dir if not already set
: ${MEDIA_ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"}
export MEDIA_ROOT_DIR
