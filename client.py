import requests

# url = 'http://127.0.0.1:5000/ftp/upload'


# NOTE: This is a client script that sends a POST request to the server to upload a file to the server using FTP.

# this is the url that nginx is listening to for the upload
url = 'http://127.0.0.1:80/ftp/upload'

print("\nAttempting to upload file to server...")
print(f"POST request to {url}")

# file path of the file to be uploaded
file_path = 'D:/Documents/GitHub/DeliverableStructure/DeliverableFolderStructure/CourseProjects/nginx_flask_advanced/upload.txt'

# open the file and send it in the request
with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

# print the response
print(response.text)


# NOTE: This is a client script that sends a POST request to the server to download a file from the server using FTP.

# this is the url that nginx is listening to for the download
url = 'http://127.0.0.1:80/ftp/download'

print("\nAttempting to download file from server...")
print(f"POST request to {url}")

# send the filename in the request | since this a post request the flask server will receive the filename in the form data
data = {'filename': 'sample.txt'}

# send the request
response = requests.post(url, data=data)

# print the response
if response.status_code == 200:
    print(response.text)
else:
    print(f'Failed to download file. Status code: {response.status_code}')
    print(response.text)
