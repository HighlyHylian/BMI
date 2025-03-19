def calculate_bmi(heightMeters, weightKg):
    return weightKg / (heightMeters ** 2)

def get_kg_from_pounds(pounds):
    return pounds * 0.453592

def get_meters_from_inches(inches):
    return inches * 0.0254

def split_height_string(height):
    try:
        feet, inches_part = height.split("'")
        inches = inches_part.replace('"', '')
        return int(feet), int(inches)
    except ValueError:
        return None
    
def return_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight" 
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    height = input("Enter your height in feet and inches (e.g. 5'10\"): ")
    weight = input("Enter your weight in pounds: ")

    feet, inches = split_height_string(height)
    heightMeters = get_meters_from_inches(feet * 12 + inches)
    weightKg = get_kg_from_pounds(float(weight))
    bmi = calculate_bmi(heightMeters, weightKg)
    print(f"Your BMI is {bmi:.2f}, which is considered {return_bmi_category(bmi)}.")



if __name__ == "__main__":
    main()