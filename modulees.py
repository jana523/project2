def validemail(email):
    if '@' in email and '.' in email:
        try:
            username, domain = email.split('@')
            if username and domain:
                x,y=domain.split('.')
                if username and x and y:
                    print("valid")
                    return True
        except ValueError:
            return False
    return False

def emails_domain(emails):
     domains = list(map(lambda x: x.split("@")[1], emails))
     print(domains)
