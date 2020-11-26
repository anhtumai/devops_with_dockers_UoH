# Parse information from inventory

git_url=$(awk 'BEGIN {FS="="} $1=="git_url" {print $2; exit}' inventory)
if [ -z "$git_url" ]
then
    echo "git_url is not defined in inventory"
    exit 1
fi

username=$(awk 'BEGIN {FS="="} $1=="username" {print $2; exit}' inventory)
if [ -z "$username" ]
then
    echo "username is not defined in inventory"
    exit 1
fi

image_name=$(awk 'BEGIN {FS="="} $1=="image_name" {print $2; exit}' inventory)
if [ -z "$image_name" ]
then
    echo "image_name is not defined in inventory"
    exit 1
fi

password=$(awk 'BEGIN {FS="="} $1=="password" {print $2; exit}' inventory)
if [ -z "$password" ]
then
    echo "password is not defined in inventory"
    exit 1
fi

# Build image to push to docker hub

tag=latest

git clone $git_url app

if [ ! -d "app/" ]; then
    echo "Failed to clone git repository. Please rechek git url or your internet connection"
    exit 2
fi

cd app

docker build . -t $image_name

echo $password | docker login --username=$username --password-stdin

if [ ! $? -eq 0 ]; then
    echo "Get https://registry-1.docker.io/v2/: unauthorized: incorrect username or password"
    exit 3
fi

image_repo=${username}/${image_name}

docker tag $image_name $image_repo

docker push ${image_repo}:${tag}

docker logout
