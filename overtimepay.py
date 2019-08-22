hours = input("Enter Hours")
rate = input("Enter Rate")
fhours = float(hours)
frate = float(rate)

base = 40.00
overtime = 1.5 * frate
pay =fhours * frate
extra_pay = base * frate + overtime * (fhours - base)

if fhours < base:
      print(pay)
elsif fhours > base:
print(extra_pay)
