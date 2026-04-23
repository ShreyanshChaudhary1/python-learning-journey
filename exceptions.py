# exceptions = errors handle karo gracefully
# program crash na ho error pe

try:
    age = int(input('Shreyansh ki age batao: '))
    income = 50000  # Shreyansh ka future income goal
    risk = income / age
    print(f'Shreyansh ka risk factor: {risk}')

except ZeroDivisionError:
    print('Age 0 nahi ho sakti Shreyansh!')

except ValueError:
    # agar user number ki jagah text likhe
    print('Invalid value - sahi number likho!')