try:
    unit=int(input("Enter the consumed units: "))
    amount = 0
    if (unit > 0):
        amount=(unit*1.5)
    if (unit > 100 and unit <= 300 ):
        amount=(150+(unit-100)*2.5)
    if (unit > 300 and unit <= 400):
        amount=(150+500+(unit-300)*3.5)
    if (unit > 400):
        amount=(150+500+350+(unit-400)*4)
except ValueError:
        print("Enter a valid unit number")
else:
    print("The electricity bill is", amount)
finally:
    print("Bill calculation completed")