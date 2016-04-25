import paramiko

host = raw_input("Enter IP Address to login: ")
username = raw_input("Username: ")
password = raw_input("Password: ")

print "Trying SSH connection to host: " + host

try:
  session = paramiko.SSHClient()
  
  #Following line automatically adds  keys for SSH if not found.
  session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
  session.connect(host, username = username, password = password)
  print "[!] SSH Connection Established!"

except Exception, e:
  print e
