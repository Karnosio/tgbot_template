codename=$(lsb_release -cs)

echo "Installing Docker for Ubuntu $codename..."

sudo apt-get update -y && sudo apt-get upgrade -y

sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $codename stable"

sudo apt-get update

sudo apt-get install -y docker-ce

sudo reboot
