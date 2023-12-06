#What will print if you run the following code?

value1 = 8.0
value2 = 8

Practprob = input("What type is value1? ")
if Practprob == 'float':
    print("Value1 is a float")
    print("Answer is", type(value1), "Your answer was", Practprob)
elif Practprob == 'integer':
    print("Value1 is an integer")
    print("Answer is", type(value1), "Your answer was", Practprob)

PractprobA = input("Now that you've answered the first question, what type is value2?")
if PractprobA == 'float':
    print("Value2 is a float ")
    print("Answer is", type(value2), "Your answer was", PractprobA)
elif PractprobA == 'integer':
    print("Value2 is an integer")
    print("Answer is", type(value2), "Your answer was", PractprobA)
