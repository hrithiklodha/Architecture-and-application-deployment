#### Volume Mount Lab
- `docker build . --tag volumes_container`
- `docker run --volume local_directory:/mounted_directory_in_container --publish 5003:5003 lab6_volumes_container`
- check if folder's content is read by flask api
- change file content and see if flask api reads updated file contet.
- alternative `docker-compose up --build`

- create docker volume by `docker volume create mounted_volume`
- run docker container with mountaed volume `docker run -v mounted_volume:/data -it ubuntu`
