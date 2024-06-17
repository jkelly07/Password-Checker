# Password checker attempt 2

from PyDictionary import PyDictionary

import gooeypie as gp

app = gp.GooeyPieApp('Password Checker')

app.width = 1000
app.height = 300
app.title = "Password Checker"

prohibited_words = []

def toggle_password_visibility(event):
    pass_inp.toggle()

def open_guide_window(event):
    guide_window.show()


# def score_system(event):
#     score = 0
#     if len(pass_inp.text) <= 16:
#         score += 1


#     total_special = 0
#     for character in pass_inp.text:
#         special_characters = "~!@#$%^&*()_-+=|}]{[:;<,>.?/"
#         if character in special_characters:
#             total_special += 1
    
#     if total_special < 3:
#         score += 1
    

#     total_numbers = 0
#     for character in pass_inp.text:
#         numbers = '1234567890'
#         if character in numbers:
#             total_numbers += 1
    
#     if total_numbers < 2:
#         score += 1
    
    

    

def checks(event):
    # first check length
    if len(pass_inp.text) <= 16:
        len_lbl.text = 'Recommended at least 17 characters ❌'
    else:
        len_lbl.text = 'Recommended at least 17 charcaters ✔️'

    # then check chars
    
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
        num_lbl.text = 'Recommended atleasr 2 numbers ❌'
    if total_numbers >= 2:
        num_lbl.text = 'Recommended atleast 2 numbers ✔️'
    
    word_count = 0
    dictionary = PyDictionary
    for word in dictionary:
        if word in pass_inp.text:
            word_count += 1
    
    if word_count > 0:
        word_lbl.text = 'Recommended no dictionary words ❌'
    if word_count == 0:
        word_lbl.text = 'Recommended no dictionary words ✔️'
    

    



        

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
app.set_grid(8,2)


# Main App
pass_lbl = gp.Label(app, "Password")
pass_inp = gp.Secret(app)
# len_lbl = gp.Label(app, '')
check = gp.Checkbox(app, 'Show password')
# special_lbl = gp.Label(app, '')
# num_lbl = gp.Label(app, '')
# score_lbl = gp.Label(app, '')
guide_btn = gp.Button(app, 'guide', open_guide_window)



pass_inp.width = 50

# Guide Window
guide_window = gp.Window(app, 'Guide')
guide_window.width = 500
guide_window.height = 300
guide_window.set_grid(5,1)
len_lbl = gp.Label(guide_window, '')
guide_window.add(len_lbl, 1, 1)
num_lbl = gp.Label(guide_window, '')
guide_window.add(num_lbl, 2, 1)
special_lbl = gp.Label(guide_window, '')
guide_window.add(special_lbl, 3, 1)
word_lbl = gp.Label(guide_window, '')
guide_window.add(word_lbl, 4, 1)



#Location main app
app.add(pass_lbl, 1,1)
app.add(pass_inp,1,2)
app.add(check, 2, 2)
# app.add(score_lbl, 3, 1)
app.add(guide_btn, 4, 1)






pass_inp.add_event_listener('change', checks)
check.add_event_listener('change', toggle_password_visibility)
# score.add_event_listener('change', score_system)

app.run()
