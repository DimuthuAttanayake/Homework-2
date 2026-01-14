#Dimuthu Attanayake
#October 31, 2025. This is my Halloween homework!!!
#Homework 2

#importing libraries

import datetime 
import htmltab

#1.How old are you
age = int(input('How old are you'))
print(age)

if age < 0:
    print(int(input('Wait, you cannot be born in the future, how old are you again')))
    
#number of times user's heart has beaten 
#assuming all human beings have an average heart beat of 80 per minute
user_heartbeat = age *80*60*24*365
print('During the time you were alive, your heart has beaten', user_heartbeat,'times')
      
#2.Blue whale's heart beat in the time the user has been alive
#assuming blue whales heart beat is 20 per minute
bluewhale_heartbeat= age * 20* 60* 24*365
print('During the time you were alive, a whales heart has beaten', bluewhale_heartbeat,' times')

#3.Rabbit's heartbeat in the time the user has been alive
#assuming rabbits heart beat is 228
rabbit_heartbeat= age *228*60*24*365

#4.rabbit heartbeat in billions
rabbit_heartbeat_billions = rabbit_heartbeat 
if rabbit_heartbeat > 1000000000:
    rabbit_heartbeat_billions = rabbit_heartbeat_billions/1000000000
    print('During the time you were alive, a rabbits heart has beaten', rabbit_heartbeat_billions,'billion times')
else:
    print ('During the time you were alive, a rabbits heart has beaten', rabbit_heartbeat, 'times')

#5.whales heatbeat in the time you were alive with different formatting
print(f'During the time you were alive, a whales heart has beaten { bluewhale_heartbeat:,} times')
#when using f' strings it is easier to format the numbers with a single line of code, compared to the other method.

#6. Is the user my age
if age > 35:
    difference = age - 35
    print(f'You are {difference} years older then me')
elif age == 35:
    print(f'we are the same age')
else:
    difference = 35 - age
    print(f'You are {difference} years younger than me')   

#Was the user born in an odd year or an even year
now = datetime.datetime.now()
current_year = now.year
birth_year = current_year - age

if birth_year % 2 == 0:
    print(f'you were born in an even year')
else:
    print(f'you were born in an odd year')

#7 & 8.How many times there has been a president from the Democratic Party in office since they were born
# (1980 onward, and each president only counts once)
#if you are born before or in 2008, three democratic presidents

if birth_year <= 2008:
   print(f'There were three democrat presidents in the US since you were born') 
   print(f'Bill Clinton was in office when you were born')
elif 2009 <= birth_year <= 2017:
    print(f'There were two democrat presidents in the US since you were born')
    print(f'Barak Obama was in office when you were born')
else:
    print(f'There was one democrat president in the US since you were born')
    print(f'Joe Biden was in office when you were born')
#9. I tried to make a for loop to answer #7 & #8. But I couldn't really figure out how to work it.

#10. if someone says they are born in the future



  





