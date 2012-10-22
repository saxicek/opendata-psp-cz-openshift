#!/bin/sh
# This script downloads exports from psp.cz and imports them into the database.

source $OPENSHIFT_GEAR_DIR/virtenv/bin/activate
export DJANGO_SETTINGS_MODULE=openshift.settings

echo "Executing import script."
python "$OPENSHIFT_REPO_DIR"wsgi/psp_cz_import.py -d $OPENSHIFT_TMP_DIR >> "$OPENSHIFT_TMP_DIR"psp_cz_import_`date +%Y-%m-%d`.log 2>&1
