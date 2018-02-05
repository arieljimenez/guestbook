CONTAINER="the-container"
IMAGE="mysqlalpine:all-in"

ctx=`docker ps -aqf name=$CONTAINER`

if [ -z $ctx ]; then
    echo "Creating container"
    docker run \
      --name $CONTAINER -it \
      -v ${PWD}:/app \
      -p 3306:3306 -p 5000:5000 \
       $IMAGE
else
  echo "Running $CONTAINER"
  docker start -i $CONTAINER
fi
