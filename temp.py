def convert(celsius):
    return (celsius * 9/5) + 32


# Example usage
temp_c = 25
temp_f = convert(temp_c)
print(f"{temp_c}°C = {temp_f}°F")