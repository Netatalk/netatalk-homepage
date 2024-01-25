#!/usr/bin/env bash

echo "Uploading web resources to sourceforge.net as $USER..."
scp -r *.php css gfx docs 2.0 2.1 2.2 2.3 3.0 3.1 $USER@web.sourceforge.net:/home/project-web/netatalk/htdocs/
