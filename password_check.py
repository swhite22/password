correct_pass = "meme"
failed_attempts = 0

password = input('Please enter password: ')

if password == correct_pass:
    print('correct password entered, logging in...')
    
else:
    while password != correct_pass:
        
        failed_attempts += 1
        
        password = input('incorrect password, please try again: ')
        
        if password == correct_pass:
            print('correct password entered, failed attempts: ', failed_attempts, ', logging in...')
        
