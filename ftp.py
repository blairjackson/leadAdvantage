import os, pysftp

def connect():
    print("not working yet....")

    with pysftp.Connection(host, username=username, password=password) as sftp:
        print('connected!')
        host = 'ftp://bvsftp.tnsmi-cmr.com/0000000843'
        username = 'bvs_leadadv'
        password = 'leadadv1120'
        with sftp.cd(filepath):
            print("uploading...." + username)
            print("uploading via SFTP.....")
            sftp.put(filename)
            print("successfully dropped to " + username)