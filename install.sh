echo "STARTING DEPLOY SDS"
cd ~
yes | sudo apt update
yes | sudo apt upgrade

yes | sudo apt-get update
yes | sudo apt-get install ca-certificates curl
yes | sudo install -m 0755 -d /etc/apt/keyrings
yes | sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
yes | sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
yes | sudo apt-get update

yes | sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
yes | sudo service docker start

yes | git clone https://github.com/TRTSS/SimpleDataStorage.git
cd SimpleDataStorage
docker build -t sds .
docker run -d --name SimpleDataStorage -p 80:80 sds

echo "DONE"