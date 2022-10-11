# I bet that the abundance of printed invitations would be a lot to read, so I have deleted all of the old print statements from the last assignment so there is not so much to read. Also, invitations are shorter.
# list of dinner invetees
dinner_invetees = ['ada lovelace', 'steve jobs', 'bill gates']
# Steve Jobs cannot make it to the dinner, so he wil be removed from the list.
cannot_make = 'steve jobs'
dinner_invetees.remove(cannot_make)
# printing statement to inform guests.
print(f"{cannot_make.title()} could not make it to the dinner. Therefore new invetations will be sent out and Tim Cook will be invited to take his place.")
dinner_invetees.append('tim cook')
# Printing new invetations.
print(f"Dear {dinner_invetees[0].title()}, \n You are invited to attend a dinner with some of the greatest minds in the tech industry. It will take place at Apple headquarters on April 1, 2023. Please RSVP as soon as possible. ")
print(f"Dear {dinner_invetees[1].title()}, \n You are invited to attend a dinner with some of the greatest minds in the tech industry. It will take place at Apple headquarters on April 1, 2023. Please RSVP as soon as possible. ")
print(f"Dear {dinner_invetees[2].title()}, \n You are invited to attend a dinner with some of the greatest minds in the tech industry. It will take place at Apple headquarters on April 1, 2023. Please RSVP as soon as possible. ")
