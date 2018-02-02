cont_exist=`docker ps -aqf name=mysql`
if [ -z $cont_exist ]; then
    echo "Creating db service on 3306"
    docker run \
      --name mysql -d \
      -p 3306:3306 \
      frismaury/mysqlalpine:v1
else
  echo "Running db service on 3306"
  docker start mysql
fi
