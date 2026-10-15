import csv

def calculate_grade(marks):
    """Calculates letter grade based on numerical marks."""
    try:
        m = float(marks)
    except ValueError:
        raise ValueError(f"Invalid mark value: {marks}")
    
    # Reject marks outside [0, 100]
    if m < 0 or m > 100:
        raise ValueError(f"Marks {m} out of valid range [0, 100]")
    
    if m >= 80:
        return 'A'
    elif m > 60:
        return 'B'
    elif m >= 40:
        return 'C'
    else:
        return 'F'

def process_student_records(file_path):
    """Reads CSV and calculates grades for each student."""
    records = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            try:
                grade = calculate_grade(row['Marks'])
                records.append({'Name': name, 'Marks': float(row['Marks']), 'Grade': grade})
            except ValueError as e:
                print(f"Skipping record for {name}: {e}")
    return records

if __name__ == "__main__":
    results = process_student_records('students.csv')
    print("\n--- IMPROVED GRADING LOGIC OUTPUT ---")
    for student in results:
        print(f"Student: {student['Name']} | Score: {student['Marks']} | Grade: {student['Grade']}")
    