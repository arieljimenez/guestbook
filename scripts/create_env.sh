#!/bin/bash
ENV="env"

CURRENT_DIR=${PWD}

cd $APPDIR

echo "+==================================+"

if [ -d $ENV ]; then
    echo "Environment dir found"
else
    echo "Creating $ENV environment"
    virtualenv $ENV
fi

echo "+==================================+"

echo "Checking requirements"
. $ENV/bin/activate && \
    pip install -r ./scripts/requirements.txt -q

echo "+========+"
echo "| Donete |"
echo "+========+"

cd $CURRENT_DIR
