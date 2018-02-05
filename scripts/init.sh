#!/bin/sh
cd $APPDIR/scripts
# Checks and activate enviroment
. ./create_env.sh
# start and config the db
sh ./mysql.config.sh
cd $APPDIR
# Run the app
python main.py
