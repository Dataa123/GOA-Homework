#Asking user his grades and then judging them about it.
user_score1 = float(input("enter score N1: "))
user_score2 = float(input("enter score N2: "))
user_score3 = float(input("enter score N3: "))
user_score4 = float(input("enter score N4: "))

avg_score = (user_score1 + user_score2 + user_score3 + user_score4) / 4

if avg_score >=9 and avg_score <=10:
  print("გილოცავ მატრიცელო, შენი ქულაა: " + str(avg_score) + " შენ გადმოგეცა 300 ლარიანი შითობა ლეპტოპი, რასაც შეალიე შენი ცხოვრების წლები")
elif avg_score <=5 and avg_score >=0:
  print("შენი ქულაა: " + str(avg_score) + "გილოცავ შენ გაექეცი მატრიცას")
elif avg_score >5 and avg_score <9:
  print("შენი ქულაა: " + str(avg_score) + "You are mid")
else:
  print("შენი ქულაა: " + str(avg_score) + "There is something wrong with you")


#Asking user his salary and judging them about it.
user_salary = int(input("What's your salary?"))
if user_salary >=10000:
    print("Were you learning in GOA?")
elif user_salary >=1000 and user_salary <10000:
    print("You are mid.")
elif user_salary <1000:
    print("You should join GOA, slave of Matrix.")