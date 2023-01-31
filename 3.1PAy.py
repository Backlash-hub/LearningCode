hrs = input("Enter Hours:")
cash = input("Enter Rate:")
hours = float(hrs)
rate = float(cash)


if hours > 40:
    reg = hours * rate
    overtime = (hours - 40.0) * (rate * 0.5)
    total = reg + overtime
print('Pay:', total)