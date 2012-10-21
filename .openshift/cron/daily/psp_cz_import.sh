#!/bin/sh
# This script downloads exports from psp.cz and imports them into the database.

source $OPENSHIFT_GEAR_DIR/virtenv/bin/activate

echo "Executing import script."
python "$OPENSHIFT_REPO_DIR"wsgi/psp_cz_import.py -d $OPENSHIFT_TMP_DIR
