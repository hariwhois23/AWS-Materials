# AWS RDS TESTING

## Databases on EC2 Instance 
### Begin Configuration (ubuntu) :
```bash
sudo apt update -y
sudo apt install -y mariadb-server wget
sudo systemctl enable mariadb
sudo systemctl start mariadb
sudo systemctl status mariadb  # Check if it's running
```
### Set Environmental Variables (NOT ON PROD ENV)
```bash
DBName=ec2db
DBPassword=admin123456
DBRootPassword=admin123456
DBUser=ec2dbuser
```
### Database Setup on EC2 Instance:
```bash
echo "CREATE DATABASE ${DBName};" >> /tmp/db.setup
echo "CREATE USER '${DBUser}' IDENTIFIED BY '${DBPassword}';" >> /tmp/db.setup
echo "GRANT ALL PRIVILEGES ON *.* TO '${DBUser}'@'%';" >> /tmp/db.setup
echo "FLUSH PRIVILEGES;" >> /tmp/db.setup
mysqladmin -u root password "${DBRootPassword}"
mysql -u root --password="${DBRootPassword}" < /tmp/db.setup
rm /tmp/db.setup
```
### Adding some dummy data to the Database inside EC2 Instance:
```bash
mysql -u root --password="${DBRootPassword}"
USE ec2db;
CREATE TABLE F1 (id INT, name VARCHAR(45));
INSERT INTO F1 VALUES(1, 'Lewis Hamilton'), (2, 'Daniel Riccardo'), (3, 'Sebastian vettel'), (4, 'kanye west');
SELECT * FROM F1;
```
# Create RDS in AWS

## Log in to AWS Console
- Open the [AWS Management Console](https://aws.amazon.com/console/)
- Navigate to **RDS** by searching "RDS" in the AWS Services search bar.

## Create a New Database
- In the **RDS Dashboard**, click on **"Create Database"**.

## Choose Database Creation Method
- Select **"Standard Create"** (for full control) or **"Easy Create"** (for default settings).

## Select Database Engine
- Choose one of the following:
  - **MySQL**
  - **PostgreSQL**
  - **MariaDB**
  - **Oracle**
  - **SQL Server**
  - **Amazon Aurora** (AWS-optimized MySQL/PostgreSQL)

## Choose Deployment Option
- Select **"Amazon RDS"** (for managed instances).
- Choose **"Multi-AZ deployment"** for high availability (optional).

## Configure Database Settings
- **DB Instance Identifier**: Provide a unique name (e.g., `my-rds-db`).
- **Master Username**: Choose a database admin username (e.g., `admin`).
- **Master Password**: Set a strong password.

## Choose Instance Type & Storage
- **DB Instance Class**: Select instance size (e.g., `db.t3.micro` for free tier).
- **Allocated Storage**: Choose a size (default is **20GB** for free tier).
- Enable **Storage Auto-Scaling** (optional).

## Configure Connectivity
- **VPC**: Select an existing **VPC** or create a new one.
- **Subnet Group**: Choose a subnet for availability.
- **Public Access**: Enable if you need **remote access** (`No` for private DB).
- **Security Group**: Configure inbound rules for allowed access.

## Database Authentication
- Choose **Password Authentication** or **IAM Authentication** (optional).

## Additional Configurations (Optional)
- **Backup Retention**: Set retention period (default **7 days**).
- **Monitoring**: Enable **Enhanced Monitoring** if needed.
- **Maintenance**: Configure updates and auto minor version upgrades.

## Create Database
- Review your selections.
- Click **"Create Database"**.
- AWS will provision the database (this may take a few minutes).

## Connect to Your Database
- Find your database in **RDS Dashboard** → Click on it.
- Copy the **Endpoint** (e.g., `my-rds-db.xyz.us-east-1.rds.amazonaws.com`).
- Connect using a client like **MySQL Workbench**, **pgAdmin**, or CLI:
  ```bash
  mysql -h <your-endpoint> -u admin -p
## Migration of Database in EC2 Instance to RDS Database:
```bash
mysqldump -u root -p ec2db > ec2db.sql
-------------------This does the migration of ec2db.sql to the RDS created Database-----------------------------------
mysql -h <replace-rds-end-point-here> -P 3306 -u rdsuser -p rdsdb (created during the creation of the RDS) < ec2db.sql
mysql -h <replace-rds-end-point-here> -P 3306 -u rdsuser -p
USE rdsdb
SELECT * FROM F1; #to verify if the data had been migrated.
```


