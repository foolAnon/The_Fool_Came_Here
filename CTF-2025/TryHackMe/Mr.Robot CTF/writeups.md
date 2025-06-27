![image](https://github.com/user-attachments/assets/7710f007-cafb-4680-b6ed-c4f70dfef0b8)1. Begin with nmap, of course:
![image](https://github.com/user-attachments/assets/d1f4c7f6-828e-4691-98b0-ec2b68681c52)

My thoughts: As we can see, port 80-http and 443-https are accessible, port 22 will be a hint for finding credentials to log in target machine

2. Go to http://IP on port 80:
![image](https://github.com/user-attachments/assets/973a77ae-ece9-4f0a-9a0c-ddaf1ad0da79)

My thoughts: A website was made to invite new members into their fsociety, using Wappalyzer, I found that website is using Wordpress

3. Enumerate Directory:
![image](https://github.com/user-attachments/assets/3244c569-e167-4916-a39a-38982bc39a7a)

My thoughts: Of course we should check robots.txt for information, but notice wp-admin, can we find any credentials to log in wp dashboard?

4. Check robots.txt
![image](https://github.com/user-attachments/assets/012efca0-ecdd-4063-9616-ebdeb367ed32)

My thougts: **It's clearly that the first flag will be hidden in key-1-of-3.txt**, so I'm going to examine the second file - fsociety.dic

5. fsociety.dic
![image](https://github.com/user-attachments/assets/200c2889-ea21-4790-962c-f53aaea9ef4b)

![image](https://github.com/user-attachments/assets/bcb8afc2-7667-44d5-8ed3-0a5a0cc77ed3)

Based on result, we can point that the wordlists have duplicate words which enlarge the wordlists more than 800k words. To solve this problem, I decide to use sort fsociety.dic | uniq > fsociety_unique.dic, then we short it to 11k words
![image](https://github.com/user-attachments/assets/c10aab2a-5057-4f36-aa42-4ef3c3ece9bd)

6. Brute force
My thoughts: At the first glance I think this wordlists for directory, but combine the list with gobuster bring out nothing, and wpscan cannot found any users, then I came up with the idea using this wordlist for user enumeration
![image](https://github.com/user-attachments/assets/b792edb3-6f27-4256-9845-a62323c66577)

My thoughts: Continue to exploit the password with wordlists
![image](https://github.com/user-attachments/assets/29a1c0ff-5d8f-4dbc-a584-edd8d087c953)

7. Access to admin dashboard successfully
![image](https://github.com/user-attachments/assets/8c75d849-55f5-4834-9343-a788b5501d96)

My thoughts: Of course I want a reverse shell. After analyzing on google search, I discovered a way to exploit reverse shell on wp. Go to Appearance -> Editor -> 404 Template (404.php) -> Replace the code with php-reverse-shell.php -> Listen with netcat on attacker machine -> Go to any page that not exist to activate 404 page -> RCE!
![image](https://github.com/user-attachments/assets/56d16053-ec95-44d5-afe2-285a1f7e9f12)

8. Exploit other user password
![image](https://github.com/user-attachments/assets/c566c36c-4090-48d4-9b86-ea14fb26c88b)

![image](https://github.com/user-attachments/assets/37b133c7-4343-44f7-9669-a9cbda87b119)

My thoughts: Using these credential user:abcdefghijklmnopqrstuvwxyz to log in ssh and got second key in robot's home
![image](https://github.com/user-attachments/assets/8ca64e83-42d9-489c-b1c6-664c1f344d9e)

9. 
