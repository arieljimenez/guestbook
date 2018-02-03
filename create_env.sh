#!/bin/bash
ENV="env"

ctx=`pip freeze | grep virtualenv`

echo "+==================================+"

if [ -z $ctx ]; then
    echo "Installing virtualenv"
    sudo -H pip install virtualenv
else
    echo "Virtualenv found"
fi

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
    pip install -r requirements.txt && \
    deactivate

echo "+========+"
echo "| Donete |"
echo "+========+"
