
## Docker Hub for uploading images
- Create a personal access token on docker hub
- `docker login -u <USER_NAME>`

- `docker build . --tag <USER_NAME>/lab4_container_publish`

- `docker push  <USER_NAME>/lab4_container_publish`