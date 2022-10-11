# list of dinner invetees. All former print statements have been removed so you don't have to see the same chunks of code over and over wen you run it.
dinner_invetees = ['ada lovelace', 'steve jobs', 'bill gates']
cannot_make = 'steve jobs'
dinner_invetees.remove(cannot_make)
dinner_invetees.append('tim cook')
dinner_invetees.insert(0, 'paul galvin')
dinner_invetees.insert(2, 'andy rubin')
dinner_invetees.append('jack dorsey')
# shrinking the guest list
print("Unfortunately, the new dinner table has not arrived yet. As a result, some of you will not be able to attend. Messages will be sent out for those who are not invited.")
uninv_i = dinner_invetees.pop(0)
uninv_ii = dinner_invetees.pop(2)
uninv_iii = dinner_invetees.pop()
uninv_vi = dinner_invetees.pop()
print(f"{uninv_i}, I am sorry to say you have been uninvited to the dinner. Thank you for understanding and have a great day.")
print(f" {uninv_ii}, I am sorry to say you have been uninvited to the dinner. Thank you for understanding and have a great day.")
print(f" {uninv_iii}, I am sorry to say you have been uninvited to the dinner. Thank you for understanding and have a great day.")
print(f" {uninv_vi}, I am sorry to say you have been uninvited to the dinner. Thank you for understanding and have a great day.")
print(f"{dinner_invetees[0]}, You are still invited to the dinner. I hope to see you there.")
print(f"{dinner_invetees[1]}, You are still invited to the dinner. I hope to see you there.")
del dinner_invetees[1]
del dinner_invetees[0]
print(dinner_invetees)