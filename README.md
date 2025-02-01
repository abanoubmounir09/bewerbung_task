## bewerbung_task App

# Description:
* Send User Info like first name , last name and number of logins and send it in daily mail in attached csv file.

# How to Install and Run the App
- go to frappe bench directory
- write below commands:
- bench get-app https://github.com/abanoubmounir09/bewerbung_task.git --branch main
- bench --site {site_name} install-app bewerbung_task
- bench migrate

# How to Use the app
* open doctype (Daily Email Login) it's single doctype
* add emails in child table 
* and it should be a default email account is active as default Outgoing  in (email account) doctype
* if you want to test it manually open doctype  (Scheduled Job Type)
* search to method (init_mail_user_login) and press execute button

#### License

mit