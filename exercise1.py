documentary = "Baraka."
drama = "OldBoy."
comedy = "This is the End."
dramedy = "Being John Malkovich."

print ("Do you like documentaries? Please type y/n.")
user_doc = input()

print ("Do you like dramas? Please type y/n.")
user_drama = input()

print ("Do you like comedies? Please type y/n.")
user_comedy = input()

if user_doc.lower() == 'y':
    print ('I recommend watching {}'.format(documentary))
elif user_drama.lower() == 'y' and user_comedy.lower() == 'y':
    print ('I recommend watching {}'.format(dramedy))
elif user_drama.lower() == 'y':
    print ('I recommend watching {}'.format(drama))
elif user_comedy.lower() == 'y':
    print ('I recommend watching {}'.format(comedy))
else:
    print('I recommend reading the Foundation series by Isaac Asimov.')