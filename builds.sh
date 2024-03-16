# Update package lists
sudo apt-get update

# Install required packages
sudo apt-get install vsftpd 

sudo systemctl start vsftpd
sudo systemctl enable vsftpd