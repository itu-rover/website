#!/bin/bash

NAME="itu-rover"  # Name of the application
DJANGODIR=/web/apps/itu-rover  # Django project directory
ENVDIR=/web/envs/itu-rover  # Django project directory
SOCKFILE=/web/apps/itu-rover/run/gunicorn.sock  # we will communicte using this unix socket
USER=itu-rover  # the user to run as
GROUP=web  # the group to run as
NUM_WORKERS=3  # how many worker processes should Gunicorn spawn
DJANGO_WSGI_MODULE=itu_rover.wsgi  # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $ENVDIR
source ./bin/activate
source ./bin/postactivate

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ./bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
