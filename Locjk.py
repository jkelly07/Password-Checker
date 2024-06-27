
import pwnedpasswords

import english_dictionary_words

import gooeypie as gp

import time

import pyperclip

app = gp.GooeyPieApp('Locjk')

app.width = 1000
app.height = 300
app.title = "Locjk"

prohibited_words = []

def toggle_password_visibility(event):
    pass_inp.toggle()

def copy_to_clipboard(event):
    pyperclip.copy(pass_inp.text)

def open_guide_window(event):
    guide_window.show()

def open_progress_guide_window(event):
    progress_guide_window.show()



# score = 100
# def score_system(score):
#     pro_bar_update_2
#     if len(pass_inp.text) <= 5:
#         score -= 20
#         pro_bar_update_2
#     if len(pass_inp.text) > 5 and len(pass_inp.text) <= 10:
#         score -= 15
#     if len(pass_inp.text) > 10 and len(pass_inp.text) <= 16:
#         score -= 5
#     if len(pass_inp.text) > 16:
#         score -= 0
    

#     if pwnedpasswords.check(pass_inp.text) >= 1:
#         score -= 35
#     else:
#         score -= 0
    

#     word_count = 0
#     for word in english_dictionary_words.dictionary:
#         if word in pass_inp.text:
#             word_count += 1
#     if word_count > 1:
#         score -= 15
#     if word_count == 1:
#         score -= 10
#     if word_count == 0:
#         score -= 0


#     total_numbers = 0
#     for character in pass_inp.text:
#         numbers = '1234567890'
#         if character in numbers:
#             total_numbers += 1
#     if total_numbers == 0:
#         score -= 10
#     if total_numbers == 1:
#         score -= 5
#     if total_numbers >= 2:
#         score -= 0



#     total_special = 0
#     for character in pass_inp.text:
#         special_characters = "~!@#$%^&*()_-+=|}]{[:;<,>.?/"
#         if character in special_characters:
#             total_special += 1
#     if total_special == 0:
#         score -= 10
#     if total_special == 1:
#         score -= 7
#     if total_special == 2:
#         score -= 3
#     if total_special >= 3:
#         score -= 0


#     total_uppercase = 0
#     for character in pass_inp.text:
#         uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         if character in uppercase_letters:
#             total_uppercase += 1
#     if total_uppercase == 0:
#         score -= 5
#     if total_uppercase == 1:
#         score -= 3
#     if total_uppercase >= 2:
#         score -= 0



#     total_lowercase = 0
#     for character in pass_inp.text:
#         lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
#         if character in lowercase_letters:
#             total_lowercase += 1
#     if total_lowercase == 0:
#         score -= 5
#     if total_lowercase == 1:
#         score -= 3
#     if total_lowercase >= 2:
#         score -= 0

#     return score






# def pro_bar_update_2():
#     global score
#     print(f"{score} pro_bar_update_2")
#     score_rating_pb.value = 0
#     for steps in range(1):
#         score_rating_pb.value += score
#         time.sleep(0.0)
#     pass_inp.focus()
    





# def pro_bar_update(event):
#     global score
#     score_rating_pb.value = 0
#     for steps in range(1):
#         score_rating_pb.value += score
#         time.sleep(0.0)
#     pass_inp.focus()
    



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

    
    

    
    

    
#add all score stuff in here
score = 100
def checks(event):
    global score
    score = 100

      # first check length
    if len(pass_inp.text) < 1:
        score -= 70
    if len(pass_inp.text) > 0 and len(pass_inp.text) <= 5:
        len_lbl.text = 'Recommended at least 17 characters ❌'
        score -= 20
    if len(pass_inp.text) > 5 and len(pass_inp.text) <= 10:
        len_lbl.text = 'Recommended at least 17 characters ❌'
        score -= 15
    if len(pass_inp.text) > 10 and len(pass_inp.text) <= 16:
        len_lbl.text = 'Recommended at least 17 characters ❌'
        score -= 5
    if len(pass_inp.text) > 16:
        len_lbl.text = 'Recommended at least 17 charcaters ✔️'
        score -= 0





    # then check chars

    total_lowercase = 0
    for character in pass_inp.text:
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        if character in lowercase_letters:
            total_lowercase += 1

    if total_lowercase ==0:
        lowercase_lbl.text = 'Recommended atleast 2 lowercase characters ❌'
        score -= 5
    if total_lowercase ==1:
        lowercase_lbl.text = 'Recommended atleast 2 lowercase characters ❌'
        score -= 3
    if total_lowercase >= 2:
        lowercase_lbl.text = 'Recommended atleast 2 lowercase characters ✔️'
        score -= 0



    total_uppercase = 0
    for character in pass_inp.text:
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if character in uppercase_letters:
            total_uppercase += 1
    if total_uppercase == 0:
        uppercase_lbl.text = 'Recommended atleast 2 uppercase characters ❌'
        score -= 5
    if total_uppercase == 1:
        uppercase_lbl.text = 'Recommended atleast 2 uppercase characters ❌'
        score -= 3
    if total_uppercase >= 2:
        uppercase_lbl.text = 'Recommended atleast 2 uppercase characters ✔️'
        score -= 0
    
    




    
    total_special = 0
    for character in pass_inp.text:
        special_characters = "~!@#$%^&*()_-+=|}]{[:;<,>.?/"
        if character in special_characters:
            total_special += 1
        
    if total_special == 0:
        special_lbl.text = 'Recommended atleast 3 special characters ❌'
        score -= 10
    if total_special == 1:
        special_lbl.text = 'Recommended atleast 3 special characters ❌'
        score -= 7
    if total_special == 2:
        special_lbl.text = 'Recommended atleast 3 special characters ❌'
        score -= 3
    if total_special >= 3:
        special_lbl.text = 'Recommended atleast 3 special characters ✔️'
        score -= 0





    total_numbers = 0
    for character in pass_inp.text:
        numbers = '1234567890'
        if character in numbers:
            total_numbers += 1

    if total_numbers == 0:
        num_lbl.text = 'Recommended atleast 2 numbers ❌'
        score -= 10
    if total_numbers == 1:
        num_lbl.text = 'Recommended atleast 2 numbers ❌'
        score -= 5  
    if total_numbers >= 2:
        num_lbl.text = 'Recommended atleast 2 numbers ✔️'
        score -= 0
    




    word_count = 0
    for word in english_dictionary_words.dictionary:
        if word in pass_inp.text:
            word_count += 1
    

    if word_count > 1:
        word_lbl.text = 'Recommended no dictionary words ❌'
        score -= 15
    if word_count == 1:
        word_lbl.text = 'Recommended no dictionary words ❌'
        score -= 10
    if word_count == 0:
        word_lbl.text = 'Recommended no dictionary words ✔️'
        score -= 0
    

    if pwnedpasswords.check(pass_inp.text) >= 1:
        pwned_lbl.text = 'Recommended no already pwned passwords ❌'
        score -= 35
    else:
        pwned_lbl.text = 'Recommended no already pwned passwords ✔️'
        score -= 0




    score_rating_pb.value = 0
    for steps in range(1):
        score_rating_pb.value += score
        time.sleep(0.0)
    pass_inp.focus()
    
 

 

    

    



        

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

    
        
    







# Main App
pass_lbl = gp.Label(app, "Password")
pass_inp = gp.Secret(app)
check = gp.Checkbox(app, 'Show password')
guide_btn = gp.Button(app, 'Guide', open_guide_window)
progress_guide_btn = gp.Button(app, 'Progress bar guide', open_progress_guide_window )
score_rating_pb = gp.Progressbar(app)
copy_button = gp.Button(app, 'Copy to Clipboard', copy_to_clipboard)




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
guide_window.add(word_lbl, 6, 1)
pwned_lbl = gp.Label(guide_window, '')
guide_window.add(pwned_lbl, 7, 1)
lowercase_lbl = gp.Label(guide_window, '')
guide_window.add(lowercase_lbl, 4, 1)
uppercase_lbl = gp.Label(guide_window, '')
guide_window.add(uppercase_lbl, 5, 1)

#Progress bar guide window
progress_guide_window = gp.Window(app, 'Progress Bar Guide')
progress_guide_window.width = 500
progress_guide_window.height = 500
progress_guide_window.set_grid(7,1)
len_guide_lbl = gp.Label(progress_guide_window, 'The length component of your password takes up 20% of the your progress bar score.')
progress_guide_window.add(len_guide_lbl, 1, 1)
num_guide_lbl = gp.Label(progress_guide_window, 'The numbers component of your password takes up 10% of the your progress bar score.')
progress_guide_window.add(num_guide_lbl, 2, 1)
special_guide_lbl = gp.Label(progress_guide_window, 'The special charcaters component of your password takes up 10% of the your progress bar score.')
progress_guide_window.add(special_guide_lbl, 3, 1)
word_guide_lbl = gp.Label(progress_guide_window, 'The dictionary words component of your password takes up 15% of the your progress bar score.')
progress_guide_window.add(word_guide_lbl, 6, 1)
pwned_guide_lbl = gp.Label(progress_guide_window, 'The pwned password component of your password takes up 35% of the your progress bar score.')
progress_guide_window.add(pwned_guide_lbl, 7, 1)
lowercase_guide_lbl = gp.Label(progress_guide_window, 'The lowercase characters component of your password takes up 5% of the your progress bar score.')
progress_guide_window.add(lowercase_guide_lbl, 4, 1)
uppercase_guide_lbl = gp.Label(progress_guide_window, 'The uppercase characters component of your password takes up 5% of the your progress bar score.')
progress_guide_window.add(uppercase_guide_lbl, 5, 1)



# set up a grid
#Location main app
app.set_grid(4,3)
app.add(pass_lbl, 1,1)
app.add(pass_inp,1,2)
app.add(copy_button, 1, 3)
app.add(check, 2, 2)
app.add(score_rating_pb, 3, 1, column_span=3, fill=True)
app.add(guide_btn, 4, 1)
app.add(progress_guide_btn, 4, 2)




pass_inp.add_event_listener('change', checks)
check.add_event_listener('change', toggle_password_visibility)
# score_rating_pb.add_event_listener('double_click', pro_bar_update)


app.run()
