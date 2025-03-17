# SafeVault

<h2><b>Project Overview  </b></h2>
SafeVault is a password management software using MySQL for secure storage of online credentials, combined with an intuitive, customizable GUI built using Python’s CustomTkinter, which provides enhanced security and user control. This approach ensures data remains protected locally while offering a modern, user-friendly interface for seamless password management.
	
Storing credentials locally on a user's system, rather than on external cloud servers, significantly reduces the risk of breaches associated with online password managers. With this offline solution, the password database is stored in a MySQL database on the user's device, protecting sensitive information from online hacking attempts or server-side vulnerabilities.
	
Since the data is not stored on a remote server, there's no need to worry about data being compromised through cloud service provider breaches or third-party access. Users can manage their credentials in a way that aligns with their own security practices, such as frequent encryption and local database backups.

## Features
* Encrypted Storage of Master Password
* Theme based User Interface (Light/Dark)
* Password Strength Checker
* Forgot Password for Master Password
* Encrypted Storage of user password
* Local Storage (MySQL)
* No Subscription Fees
* Export Password
* Only Saves Strong Passwords
* User Friendly Interface
* View and Hide Passwords

## GUI Framework
* customtkinter
* tkinter

## Modules / Libraries Used
* CustomTkinter
* Tkinter
* PIL
* Time
* PyMySQL
* Pandas
* Random
	
## Commands to install libraries
 
Customtkinter
```bash
pip install customtkinter
```

Tkinter 
```bash 
pip install tkinter
```
PIL 
```bash
pip install Pillow
```

Time 
```bash 
pip install time
```
PyMySQL
```bash 
pip install PyMySQL
```
Pandas
```bash
pip install pandas
```

## USERNAME & PASSWORDS
Default Username for Master login : (test1234)
Default Master Password : (1234)
Answer for Forgot Password : (answer)
	
## FOR DATABASE CONNECTION
host(default) : localhost
username(default) : root
password : (chosen by you)
