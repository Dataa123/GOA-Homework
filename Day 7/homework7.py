#Ticket price is 25 gel, but it's free for children. There are 13 people: 10 adult, 3 children. We have to count how many gel do they need.

ticket_price = 25

sum = 0
i = 0
while i <= 13:
    sum += ticket_price
    i += 1
    if i >= 10:
        break

print(sum)   

#Done