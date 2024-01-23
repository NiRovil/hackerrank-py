def gradingStudents(grades):
    # Write your code here
    
    new_grade = 0
    
    for grade in range(len(grades)):
        if grades[grade] >= 38:
            multiple = grades[grade] % 5
            while multiple != 0:
                new_grade += 1
                multiple = (grades[grade] + new_grade) % 5
            
            if new_grade < 3:
                grades[grade] += new_grade

    for i in grades:
        print(i)

grade = [73,38]

gradingStudents(grade)