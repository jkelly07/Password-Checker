# Password checker attempt 2
import pwnedpasswords

import english_dictionary_words

import gooeypie as gp

import time

app = gp.GooeyPieApp('Password Checker')

app.width = 1000
app.height = 300
app.title = "Password Checker"

prohibited_words = []

def toggle_password_visibility(event):
    pass_inp.toggle()

def open_guide_window(event):
    guide_window.show()

score = 100
def score_system(score):
    if len(pass_inp.text) <= 5:
        score -= 20
    if len(pass_inp.text) > 5 and len(pass_inp.text) <= 10:
        score -= 15
    if len(pass_inp.text) > 10 and len(pass_inp.text) <= 16:
        score -= 5
    if len(pass_inp.text) > 16:
        score -= 0
    

    if pwnedpasswords.check(pass_inp.text) >= 1:
        score -= 35
    else:
        score -= 0
    

    word_count = 0
    for word in english_dictionary_words.dictionary:
        if word in pass_inp.text:
            word_count += 1
    if word_count > 1:
        score -= 15
    if word_count == 1:
        score -= 10
    if word_count == 0:
        score -= 0


    total_numbers = 0
    for character in pass_inp.text:
        numbers = '1234567890'
        if character in numbers:
            total_numbers += 1
    if total_numbers == 0:
        score -= 10
    if total_numbers == 1:
        score -= 5
    if total_numbers >= 2:
        score -= 0



    total_special = 0
    for character in pass_inp.text:
        special_characters = "~!@#$%^&*()_-+=|}]{[:;<,>.?/"
        if character in special_characters:
            total_special += 1
    if total_special == 0:
        score -= 10
    if total_special == 1:
        score -= 7
    if total_special == 2:
        score -= 3
    if total_special >= 3:
        score -= 0


    total_uppercase = 0
    for character in pass_inp.text:
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if character in uppercase_letters:
            total_uppercase += 1
    if total_uppercase == 0:
        score -= 5
    if total_uppercase == 1:
        score -= 3
    if total_uppercase >= 2:
        score -= 0



    total_lowercase = 0
    for character in pass_inp.text:
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        if character in lowercase_letters:
            total_lowercase += 1
    if total_lowercase == 0:
        score -= 5
    if total_lowercase == 1:
        score -= 3
    if total_lowercase >= 2:
        score -= 0

    return score











def pro_bar_update(event):
    score_rating_pb.value = 0
    for steps in range(1):
        score_rating_pb.value += 5
        time.sleep(0.0)
    pass_inp.focus()
    



# score = 0
# def score_system(event):
#     if len(pass_inp.text) > 16:
#         score += 1


#     total_special = 0
#     for character in pass_inp.text:
#         special_characters = "~!@#$%^&*()_-+=|}]{[:;<,>.?/"
#         if character in special_characters:
#             total_special += 1
    
#     if total_special >= 3:
#         score += 1
    

#     total_numbers = 0
#     for character in pass_inp.text:
#         numbers = '1234567890'
#         if character in numbers:
#             total_numbers += 1
    
#     if total_numbers >= 2:
#         score += 1
    

#     for word in english_dictionary_words.dictionary:
#         if word in pass_inp.text:
#             word_count += 1
    

#     if word_count == 0:
#         score += 1
    
#     if score == 0:
#         score_lbl.text = 'Bad Password'
#     if score == 1:
#         score_lbl.text = 'ok'
#     if score_system == 2:
#         score_lbl.text = 'good'
#     if score_system == 3:
#         score_lbl.text = '🟢🟢🟢'
#     if score_system == 4:
#         score_lbl.text = '🟢🟢🟢🟢'



# def score_system(event):
#     global score
#     score = 0

#     if len(pass_inp.text) > 16:
#         score += 1

#     total_special = 0
#     special_characters = "~!@#$%^&*()_-+=|}]{[:;<,>.?/"
#     for character in pass_inp.text:
#         if character in special_characters:
#             total_special += 1
    
#     if total_special >= 3:
#         score += 1

#     total_numbers = 0
#     numbers = '1234567890'
#     for character in pass_inp.text:
#         if character in numbers:
#             total_numbers += 1
    
#     if total_numbers >= 2:
#         score += 1


#     word_count = 0
#     for word in english_dictionary_words.dictionary:
#         if word in pass_inp.text:
#             word_count += 1
    
#     if word_count == 0:
#         score += 1

#     if score == 0:
#         score_lbl.text = 'Bad Password'
#     elif score == 1:
#         score_lbl.text = 'ok'
#     elif score == 2:
#         score_lbl.text = 'good'
#     elif score == 3:
#         score_lbl.text = '🟢🟢🟢'
#     elif score == 4:
#         score_lbl.text = '🟢🟢🟢🟢'


    

# if score == 0:
#     score_lbl.text = 'Bad Password'
# if score == 1:
#     score_lbl.text = '🟢'
# if score == 2:
#     score_lbl.text = '🟢🟢'
# if score == 3:
#     score_lbl.text = '🟢🟢🟢'
# if score == 4:
#     score_lbl.text = '🟢🟢🟢🟢'

    
    

    
    

    

def checks(event):
    # first check length
    if len(pass_inp.text) <= 16:
        len_lbl.text = 'Recommended at least 17 characters ❌'
    else:
        len_lbl.text = 'Recommended at least 17 charcaters ✔️'

    # then check chars

    total_lowercase = 0
    for character in pass_inp.text:
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        if character in lowercase_letters:
            total_lowercase += 1
    
    if total_lowercase < 2:
        lowercase_lbl.text = 'Recommended atleast 2 lowercase characters ❌'
    if total_lowercase >= 2:
        lowercase_lbl.text = 'Recommended atleast 2 lowercase characters ✔️'


    total_uppercase = 0
    for character in pass_inp.text:
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if character in uppercase_letters:
            total_uppercase += 1
    
    if total_uppercase < 2:
        uppercase_lbl.text = 'Recommended atleast 2 uppercase characters ❌'
    if total_uppercase >= 2:
        uppercase_lbl.text = 'Recommended atleast 2 uppercase characters ✔️'
    
    
    total_special = 0
    for character in pass_inp.text:
        special_characters = "~!@#$%^&*()_-+=|}]{[:;<,>.?/"
        if character in special_characters:
            total_special += 1
        
    if total_special < 3:
        special_lbl.text = 'Recommended atleast 3 special characters ❌'
     
    if total_special >= 3:
        special_lbl.text = 'Recommended atleast 3 special characters ✔️'

    total_numbers = 0
    for character in pass_inp.text:
        numbers = '1234567890'
        if character in numbers:
            total_numbers += 1

    if total_numbers < 2:
        num_lbl.text = 'Recommended atleast 2 numbers ❌'
    if total_numbers >= 2:
        num_lbl.text = 'Recommended atleast 2 numbers ✔️'
    
    word_count = 0
    # with open('C:\\Users\\Jaden\\Desktop\\Year 11 Software Engineering Practical Work\\Password Checker\\English_dictionary') as D:
        # dictionary = [line.strip() for line in D]
    for word in english_dictionary_words.dictionary:
        if word in pass_inp.text:
            word_count += 1
    

    if word_count > 0:
        word_lbl.text = 'Recommended no dictionary words ❌'
    if word_count == 0:
        word_lbl.text = 'Recommended no dictionary words ✔️'
    


    if pwnedpasswords.check(pass_inp.text) >= 1:
        pwned_lbl.text = 'Recommended no already pwned passwords ❌'
    else:
        pwned_lbl.text = 'Recommended no already pwned passwords ✔️'
    


 

    

    



        

# def check_len(event):
#     if len(pass_inp.text) <= 16:
#         len_lbl.text = 'Password too short, longer than 16 characters please'
#     else:
#         len_lbl.text = 'Password length is good, however the more characters the better'

# special_characters = "`~!@#$%^&*()_-+={[}]|;:'<,>.?/"

# # 
# def check_special_characters(event):

#     special_characters = "!"

#     total = 0
#     for character in pass_inp.text:
 
#         if character in special_characters:
#             total += 1
    



#     if total < 3:
#         special_lbl.text = 'Not enough special characters, at least 3 please'
#     # if special_characters >= 3:
#     #     special_lbl.text = 'Good job, you have enough special characters but the more the better'

    
        
    




# setup a grid
app.set_grid(4,2)


# Main App
pass_lbl = gp.Label(app, "Password")
pass_inp = gp.Secret(app)
check = gp.Checkbox(app, 'Show password')
guide_btn = gp.Button(app, 'guide', open_guide_window)
score_rating_pb = gp.Progressbar(app, 'determinate')



pass_inp.width = 100

# Guide Window
guide_window = gp.Window(app, 'Guide')
guide_window.width = 500
guide_window.height = 500
guide_window.set_grid(7,1)
len_lbl = gp.Label(guide_window, '')
guide_window.add(len_lbl, 1, 1)
num_lbl = gp.Label(guide_window, '')
guide_window.add(num_lbl, 2, 1)
special_lbl = gp.Label(guide_window, '')
guide_window.add(special_lbl, 3, 1)
word_lbl = gp.Label(guide_window, '')
guide_window.add(word_lbl, 4, 1)
pwned_lbl = gp.Label(guide_window, '')
guide_window.add(pwned_lbl, 5, 1)
lowercase_lbl = gp.Label(guide_window, '')
guide_window.add(lowercase_lbl, 6, 1)
uppercase_lbl = gp.Label(guide_window, '')
guide_window.add(uppercase_lbl, 7, 1)



#Location main app
app.add(pass_lbl, 1,1)
app.add(pass_inp,1,2)
app.add(check, 2, 2)
app.add(score_rating_pb, 3, 1, column_span=2, fill=True)
app.add(guide_btn, 4, 1)




pass_inp.add_event_listener('change', checks)
check.add_event_listener('change', toggle_password_visibility)
# score_rating_pb.add_event_listener('key_press', pro_bar_update)


app.run()
