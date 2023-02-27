#!/usr/bin/env bash

if [ -z ${SFUSER+x} ]; then echo "Please define your SF.net username with the SFUSER env variable." && exit 1; fi

echo "Uploading web resources to sourceforge.net as $SFUSER..."
scp -r *.php css gfx $SFUSER@web.sourceforge.net:/home/project-web/netatalk/htdocs/
