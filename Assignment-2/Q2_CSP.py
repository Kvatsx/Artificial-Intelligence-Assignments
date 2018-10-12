#!/usr/bin/python
# Kaustav Vats (2016048)

class Course:
    
    def __init__(self, CourseCode, CourseName, ProfessorID):
        self.CourseCode = CourseCode
        self.CourseName = CourseName
        self.ProfessorID = ProfessorID

    def getCourseCode(self):
        return self.CourseCode

    def getProfessorID(self):
        return self.ProfessorID

    def __str__(self):
        return "CourseCode: %s\nProfessorID: %s\n" % (self.CourseCode, self.ProfessorID)


class Professor:

    def __init__(self, ID, Name, Course1, Course2):
        self.ID = ID
        self.Name = Name
        self.Course1 = Course1
        self.Course2 = Course2

    def getID(self):
        return self.ID

    def getName(self):
        return self.Name
    
    def getCourse1(self):
        return self.Course1

    def getCourse2(self):
        return self.Course2

    def __str__(self):
        return "ID: %s\nCourseCode_1: %s\nCourseCode_2: %s\n" % (self.ID, self.Course1, self.Course2)

class Room:

    def __init__(self, RoomNo):
        self.RoomNo = RoomNo

    def getRoomNo(self):
        return self.RoomNo

    def __str__(self):
        return "RoomNo: %s" % (self.RoomNo)


class Gene:

    def __init__(self, Course, Professor, Room, Day, Slot):
        self.Course = Course
        self.Professor = Professor

    # def __str__(self):
        # return "CourseID: %s\nProfessorID: %s\nRoomNo: %s\nDay: %s\nSlot: %s\n" % (self.Course.getCourseCode(), self.Professor.getID(), self.Room, self.Day, self.Slot)

class CSP:

    def __init__(self, Pop):
        self.Pop = Pop
        self.Taken = [False]*80
        Matrix = []
        for i in range(5):
            arr = []
            for j in range(8):
                arr.append([])
            Matrix.append(arr)
        self.Matrix = Matrix

    def isClash(self, x, y, z, cour):
        for i in range(y+1):
            for j in range(len(self.Matrix[x][i])):
                if ( cour.getCourseCode() == self.Matrix[x][i][j].getCourseCode()):
                    if ( y == i and j == z):
                        continue
                    return True
                if ( z == 1 ):
                    if ( cour.getProfessorID() == self.Matrix[x][y][0].getProfessorID() ):
                        return True
        return False

    def solveUtil(self, x, y, z):
        if ( x == 5 ):
            return True

        for i in range(80):
            if ( self.Taken[i] == False ):
                so = self.Pop[i]
                if ( self.isClash(x, y, z, so) == False ):
                    # print("lol")
                    self.Matrix[x][y].append(self.Pop[i])
                    self.Taken[i] = True
                    if ( z == 0 ):
                        z += 1
                    elif ( z == 1 ):
                        z = 0
                        y = y+1
                    if ( y+1 == 9 ):
                        x = x + 1
                        y = 0
                        z = 0
                    if ( self.solveUtil(x, y, z) == True ):
                        return True
                    self.Matrix[x][y].pop()
                    self.Taken[i] = False

        return False
                
    def solve(self, x, y, z):
        if ( self.solveUtil(x, y, z) == False ):
            print("No Solution")
        # print solution
        # print(self.Matrix[0][7])
        for i in range(5):
            print("Day: ",i)
            for j in range(8):
                for k in range(len(self.Matrix[i][j])):
                    print(self.Matrix[i][j][k].getCourseCode(), end=' ')
                print()
            print()
        print("Working Yeah!")



if __name__ == "__main__":
    
    class_count = ["2", "3"]

    courses = []
    professors = []
    rooms = ["R1", "R2"]
    timeslots = ["1", "2", "3", "4", "5", "6", "7", "8"]
    
    # -------------------------------------
    courses.append(Course("0", "0", "0"))
    courses.append(Course("1", "1", "0"))
    courses.append(Course("2", "2", "1"))

    courses.append(Course("3", "3", "1"))
    courses.append(Course("4", "4", "2"))
    courses.append(Course("5", "5", "2"))

    courses.append(Course("6", "6", "3"))
    courses.append(Course("7", "7", "3"))
    courses.append(Course("8", "8", "4"))

    courses.append(Course("9", "9", "4"))
    courses.append(Course("10", "10", "5"))
    courses.append(Course("11", "11", "5"))

    courses.append(Course("12", "12", "6"))
    courses.append(Course("13", "13", "6"))
    courses.append(Course("14", "14", "7"))
    courses.append(Course("15", "15", "7"))

    courses.append(Course("0", "0", "0"))
    courses.append(Course("1", "1", "0"))
    courses.append(Course("2", "2", "1"))

    courses.append(Course("3", "3", "1"))
    courses.append(Course("4", "4", "2"))
    courses.append(Course("5", "5", "2"))

    courses.append(Course("6", "6", "3"))
    courses.append(Course("7", "7", "3"))
    courses.append(Course("8", "8", "4"))

    courses.append(Course("9", "9", "4"))
    courses.append(Course("10", "10", "5"))
    courses.append(Course("11", "11", "5"))

    courses.append(Course("12", "12", "6"))
    courses.append(Course("13", "13", "6"))
    courses.append(Course("14", "14", "7"))
    courses.append(Course("15", "15", "7"))

    courses.append(Course("0", "0", "0"))
    courses.append(Course("1", "1", "0"))
    courses.append(Course("2", "2", "1"))

    courses.append(Course("3", "3", "1"))
    courses.append(Course("4", "4", "2"))
    courses.append(Course("5", "5", "2"))

    courses.append(Course("6", "6", "3"))
    courses.append(Course("7", "7", "3"))
    courses.append(Course("8", "8", "4"))

    courses.append(Course("9", "9", "4"))
    courses.append(Course("10", "10", "5"))
    courses.append(Course("11", "11", "5"))

    courses.append(Course("12", "12", "6"))
    courses.append(Course("13", "13", "6"))
    courses.append(Course("14", "14", "7"))
    courses.append(Course("15", "15", "7"))
    # -------------------------------------------

    # Thursday & Friday
    courses.append(Course("16", "16", "8"))
    courses.append(Course("17", "17", "8"))

    courses.append(Course("18", "18", "9"))
    courses.append(Course("19", "19", "9"))
    courses.append(Course("20", "20", "10"))

    courses.append(Course("21", "21", "10"))
    courses.append(Course("22", "22", "11"))
    courses.append(Course("23", "23", "11"))

    courses.append(Course("24", "24", "12"))
    courses.append(Course("25", "25", "12"))
    courses.append(Course("26", "26", "13"))

    courses.append(Course("27", "27", "13"))
    courses.append(Course("28", "28", "14"))
    courses.append(Course("29", "29", "14"))

    courses.append(Course("30", "30", "15"))
    courses.append(Course("31", "31", "15"))

    courses.append(Course("16", "16", "8"))
    courses.append(Course("17", "17", "8"))

    courses.append(Course("18", "18", "9"))
    courses.append(Course("19", "19", "9"))
    courses.append(Course("20", "20", "10"))

    courses.append(Course("21", "21", "10"))
    courses.append(Course("22", "22", "11"))
    courses.append(Course("23", "23", "11"))

    courses.append(Course("24", "24", "12"))
    courses.append(Course("25", "25", "12"))
    courses.append(Course("26", "26", "13"))

    courses.append(Course("27", "27", "13"))
    courses.append(Course("28", "28", "14"))
    courses.append(Course("29", "29", "14"))

    courses.append(Course("30", "30", "15"))
    courses.append(Course("31", "31", "15"))
    # -------------------------------------
    csp = CSP(courses)
    csp.solve(0, 0, 0)
