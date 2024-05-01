echo "STARTING DEPLOY SDS"
cd ~
yes | sudo apt update
yes | sudo apt upgrade

yes | sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
yes | sudo service docker start

yes | git clone https://github.com/TRTSS/SimpleDataStorage.git
cd SimpleDataStorage
docker build -t sds .
docker run -d --name SimpleDataStorage -p 80:80 sds

echo "DONE"