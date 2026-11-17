def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == "__main__":
    print("20 ºC =", celsius_a_fahrenheit(20), "ºF")
    print("68 ºF =", fahrenheit_a_celsius(68), "ºC")
