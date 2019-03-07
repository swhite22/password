correct_pass = "meme"

password = input('Please enter password: ')

if password == correct_pass:
    print('correct password entered, logging in...')
else:
    while password != correct_pass:
        
        password = input('incorrect password, please try again: ')
        
        if password == correct_pass:
            print('correct password entered, logging in...')
        
