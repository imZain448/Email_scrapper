#Email Scrapper
---
this a utility script to scrap emails from a given email 

to run the scripts 
- download the whole repo
- extract it and open the extracted folder in a code editor (VS Code recommended)
- make changes in the test.py script in the following places
  ```python
    HOST_NAME = "@your_host.name" # example @gmail.com
    USER_ID = "username"+ HOST_NAME # example xyz123
    PWD = "password"
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993
  ```
- then execute the test.py script in your runtime environment
- make sure you have pandas already installed in your runtime environment

main.py script contains the utility function `parse_email_messages` which featches the contents of an email. This function returns a pandas dataframe containing all the content in respective columns

The test.py then selects only those rows whose subject contain the required substring <b>"Thank you for applying"</b>
and saves these as a csv file.

this script can be used for any other substring also to use it for a diferent substring just change the following line
```python
df = data.loc[data['Subject'].str.contains('Thank you for applying')]
```
in replace the `'Thank you for applying'` string with your desired string

###<b>*IMPORTANT*</b>
- In order to let this script read the mails of the user you need to allow less secure apps from your google accounts settings. which I don't recoomend.
but if this script is used inside an app which satisfies the security criteria of google than the above could be avoided

- reading the emails of a user is privacy issue therefore I don't encourage to perform this task without the consent of the user in any possible way.\
User consent must be taken before accessing there emails