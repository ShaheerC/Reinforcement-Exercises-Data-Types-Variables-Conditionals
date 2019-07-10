documentary = "Baraka."
drama = "OldBoy."
comedy = "This is the End."
dramedy = "Being John Malkovich."

print ("Please rate your appreciation for documentaries from 1 to 5, 5 being the most.")
user_doc = int(input())

print ("Please rate your appreciation for dramas from 1 to 5, 5 being the most.")
user_drama = int(input())

print ("Please rate your appreciation for comedies from 1 to 5, 5 being the most.")
user_comedy = int(input())

if user_doc > 3:
    print ('I recommend watching {}'.format(documentary))
elif user_doc < 4 and user_comedy > 3 and user_drama > 3:
    print ('I recommend watching {}'.format(dramedy))
elif user_drama > 3:
    print ('I recommend watching {}'.format(drama))
elif user_comedy > 3:
    print('I recommend watching {}'.format(comedy))
else:
    print('I recommend reading the foundation series by Isaac Asimov.')