# 🛠 How to Enable Password Authentication for SSH on a Linux Server

## Prerequisites

- You must have **sudo** privileges or **root** access.
- You should have `vim` installed (most servers do by default).

---

## Steps

### 1. Switch to the Root User

Gain root access to make system-wide changes:

```bash
sudo su -
```

### 2. open the folllowing file

```bash
vim /etc/ssh/sshd_config.d/60-cloudimg-settings.conf
```

### 3. Edit the configuration 
Inside the file, locate the following line

```PasswordAuthentication no``` 
 and change it to 
```PasswordAuthentication yes```


### 4.Restart the SSH service
To apply the new configuration, restart the SSH service
```bash
systemctl restart ssh
```
