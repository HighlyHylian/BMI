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
    pass

def main():
    pass



if __name__ == "__main__":
    pass