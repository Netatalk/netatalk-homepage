#!/usr/bin/env bash

if [ -z ${SFUSER+x} ]; then echo "Please define your SF.net username with the SFUSER env variable." && exit 1; fi

echo "Uploading web resources to sourceforge.net as $SFUSER..."
scp -r *.php css gfx docs 2.0 2.1 2.2 2.3 3.0 3.1 $SFUSER@web.sourceforge.net:/home/project-web/netatalk/htdocs/
