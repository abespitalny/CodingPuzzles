"""
Input: a 2-D array of strings where each row is in the format
[date (MM-DD), student, class start time and arrival time (minutes since midnight)]
Output: name of the student with the greatest total relative lateness
"""
def latestStudent(attendanceData):
    if attendanceData is None or len(attendanceData) == 0:
        return ""

    # keys are the days and the values are the avg. lateness of all the students
    days = {}
    # keys are the students' names and values are arrays of tuples containing the day and lateness of the student
    students = {}

    for i in attendanceData:
        lateness = int(i[3]) - int(i[2])
        if lateness < 0:
            lateness = 0

        day = i[0]
        if day in days:
            sigma, n = days[day]
            days[day] = (sigma + lateness, n + 1)
        else:
            days[day] = (lateness, 1)

        name = i[1]
        if name in students:
            (students[name]).append((day, lateness))
        else:
            students[name] = [(day, lateness)]

    # Calculate avg. lateness for each day
    for i in days:
        sigma, n = days[i]
        days[i] = sigma/n

    # Calculate total relative lateness for each student and store the max
    max_total = -1
    # lowest name (compared alphabetically) if there is a tie
    max_name = ""
    for i in students:
        total = 0
        for j in students[i]:
            rel_lateness = j[1] - days[j[0]]
            if rel_lateness < 0:
                rel_lateness = 0

            total += rel_lateness

        if total > max_total:
            max_total = total
            max_name = i
        elif total == max_total:
            max_name = min(i, max_name)

    return max_name
