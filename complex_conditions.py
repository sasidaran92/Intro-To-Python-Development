gpa = input('Enter your GPA ')
if float(gpa) >= 0.85:
    lowest_average = input('Enter your lowest average ')
    if float(lowest_average) >= 0.7:
        print('Well Done')
    else:
        print('Better luck next time')
else:
    print('Better luck next time')
