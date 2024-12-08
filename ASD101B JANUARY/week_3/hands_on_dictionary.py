# 1. Course informationWrite a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet. The dictionary should have the following keyvalue pairs:
          
          
          
          
            
              
#   Course Number (key)Room Number (value)CS1013004CS1024501CS1036755NT1101244CM2411411
            
          
          
# The program should also create a dictionary containing course numbers and the names of the instructors that teach each course. The dictionary should have the following key-value pairs:
          
          
          
          
            
              
#   Course Number (key)Instructor (value)CS101HaynesCS102AlvaradoCS103RichNT110BurkeCM241Lee
            
          
          
# The program should also create a dictionary containing course numbers and the meeting times of each course. The dictionary should have the following key-value pairs:


          
          
          
          
            
              
#   Course Number (key)Meeting Time (value)CS1018:00 a.m.CS1029:00 a.m.CS10310:00 a.m.NT11011:00 a.m.CM2411:00 p.m.
            
          
          
# The program should let the user enter a course number, then it should display the course’s room number, instructor, and meeting time.

room_number = {
    'CS101' : 3004,
    'CS102' : 4501,
    'CS103' : 6755,
    'NT110' : 1244,
    'CM241' : 1411
}
instructors = {
    "CS101" : "Haynes",
    "CS102" : "Alvarado",
    "CS103" : "Rich",
    "NT110" : "Burke",
    "CM241" : "Lee"
}
meeting_times = {
    "CS101" : "8:00 a.m",
    "CS102" : "9:00 a.m.",
    "CS103" : "10:00 a.m.",
    "NT110" : "11:00 a.m.",
    "CM241" : "1:00 p.m."
}

course_number = input("Enter a course number: ")
if course_number in room_number:
    print(f"Room Number: {room_number[course_number]}")
    print(f"Instructor: {instructors[course_number]}")
    print(f"Meeting time: {meeting_times[course_number]}")
else:
    print("The course number does not exist! ")


