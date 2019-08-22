hours = input("Enter Hours")
rate = input("Enter Rate")
try:
     fhours = float(hours)
     frate = float(rate)
except:
    print("Error: Enter a numerical value")
    quit()

base = 40.00
overtime = 1.5 * frate
pay =fhours * frate
extra_pay = base * frate + overtime * (fhours - base)

if fhours < base:
      print(pay)
if fhours > base:
      print(extra_pay)
