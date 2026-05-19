# Model Bank Management System - blog_1

- Explaining low level design of the project !

<h3>
Bank Management System is a project which is designed to meet operations level of a real time banking system.

Our BMS_Model_0.1
provides access to register on the system by full filling minimum information need like 
any user can create a account to avail services by entering his name generally Full Name, Phone Number, Address and email ( optional).

However in version 0.1 many development workflows are ongoing, thus developers need to work on that and made things accessible on time.
To ensure more authenicity and to generate real time team workflow, we are going to use github actions and PR Pull Requests,
In this proccess we will create and implement github workflows and an Agent to check the changes and review the PR.

If we talk about what is under process and why this project is unable to use now.
This project currently do not provide proper user registration and account access.

Developers are facing an issure regarding generating unique account functions via a generator which colloborate with object oriented Paradigm
's classmethod and staticmethods.

When we able to generate unique account_numbers and able to track them,
we will start working and implementing data persistance as data remains on the objects or on the computer untill the program runs,
if somehow program stops then all the data stored in the RAM will be erased, which erase all the existing users.
data persistance is achieved using serialization and Deserialization of the data associated with the objects.

After achieving data persistancy using storing and loading data from files and database , we will provide an authentication 
service to the users, as before it who knows the account number can get access to the account with some additional info.
 
We would work on implementing passoword based authentication pipeline which usese hashing to store hashed password then we delete the original password.
wheneve user try to log-in  using account number and password, our server convert the enterd passoword into a hash values , then this hash values is later
matched with the hashed password,
if both hash value matches then user is allowed to enter in the system, else asked for correct passowrd,
to ensure more security if an attacker or exploiter want to exploit the user account we will enforce a rate limiting on the number of attempts to access the account.

As password based authentication will be developed then we have to provide a way to reset the password,
as it is obsereved that many users can't reteain what was the  password ? , 
we will provide a confirmation code via SMS , Whatsapp, phone_call, link on email id.

It was observed from the past that if data breaches happen only the general information like phone number , email id , address wil be accessed by the 
hacker but overall your password remain in transit , which is hardly decoded.

To use our service kindly download our CLI tool from the official plateform or from opensource codebase.
we release this project as a CLI tool.

We are focused to bring you the best results possible, untill the release keep in touch !

</h3>
