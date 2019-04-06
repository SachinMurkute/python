import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('target_host_ip',username='user',password='user_password')

stdin,stdout,stderr = ssh.exec_command("uptime")
print stdout.readlines()

#copy_file.py

sftp = ssh.open_sftp()
sftp.put("copy_file.py","/root/copy_file.py")
sftp.close()
ssh.close()
