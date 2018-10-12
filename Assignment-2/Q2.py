#!/usr/bin/python
# Kaustav Vats (2016048)

import sys
from random import randint as randi
from queue import PriorityQueue

class Course:

    def __init__(self, CourseCode, CourseName, ProfessorID, ClassCount):
        self.CourseCode = CourseCode
        self.CourseName = CourseName
        self.ProfessorID = ProfessorID
        self.ClassCount = ClassCount

    def getCourseCode(self):
        return self.CourseCode

    def getProfessorID(self):
        return self.ProfessorID
    
    def getClassCount(self):
        return self.ClassCount

    def __str__(self):
        return "CourseCode: %s\nProfessorID: %s\nClassCount: %s\n" % (self.CourseCode, self.ProfessorID, self.ClassCount)


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
        self.Room = Room
        self.Day = Day
        self.Slot = Slot

    def __str__(self):
        return "CourseID: %s\nProfessorID: %s\nRoomNo: %s\nDay: %s\nSlot: %s\n" % (self.Course.getCourseCode(), self.Professor.getID(), self.Room, self.Day, self.Slot)


class Chromosome:

    def __init__(self, genes, RoomCount, DaysCount, TimeSlotsCount):
        self.Genes = genes
        self.RoomCount = RoomCount
        self.DaysCount = DaysCount
        self.TimeSlotsCount = TimeSlotsCount
        self.FitnessValue = sys.maxsize
    
    def __lt__(self, other):
        return self.FitnessValue < other.FitnessValue
    
    def __eq__(self, other):
        return self.FitnessValue == other.FitnessValue

    # returns a new Chromosome
    def Jumble(self):
        newGenes = []
        for i in range(len(self.Genes)):
            opt = randi(0,2)
            if ( opt == 0 ):
                newGenes.append(Gene(self.Genes[i].Course, self.Genes[i].Professor, randi(0, 1), self.Genes[i].Day, self.Genes[i].Slot))
            elif ( opt == 1 ):
                newGenes.append(Gene(self.Genes[i].Course, self.Genes[i].Professor, self.Genes[i].Room, randi(0, 4), self.Genes[i].Slot))
            else:
                newGenes.append(Gene(self.Genes[i].Course, self.Genes[i].Professor, self.Genes[i].Room, self.Genes[i].Day, randi(0, 7)))
            
            # if ( Genes[i].Room == 0 ):
            #     newGenes.append(Gene(Genes[i].Course, Genes[i].Professor, 1, randi(0, 4), randi(0, 7)))
            # else:
            #     newGenes.append(Gene(Genes[i].Course, Genes[i].Professor, 0, randi(0, 4), randi(0, 7)))
        ch = Chromosome(newGenes, self.RoomCount, self.DaysCount, self.TimeSlotsCount)
        return ch

    def Crossover(self, other):
        newGenes1 = []
        newGenes2 = []
        for i in range(len(self.Genes)):
            newGenes1.append(Gene(self.Genes[i].Course, self.Genes[i].Professor, other.Genes[i].Room, other.Genes[i].Day, other.Genes[i].Slot))
            newGenes2.append(Gene(other.Genes[i].Course, other.Genes[i].Professor, self.Genes[i].Room, self.Genes[i].Day, self.Genes[i].Slot))
        ch1 = Chromosome(newGenes1, self.RoomCount, self.DaysCount, self.TimeSlotsCount)
        ch2 = Chromosome(newGenes2, self.RoomCount, self.DaysCount, self.TimeSlotsCount)
        return [ch1, ch2]

    def FitnessFunction(self):
        conflicts = 0
        roomcheck = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(len(self.Genes)):
            for j in range(len(self.Genes)):
                if ( i != j ):
                    if ( self.Genes[i].Course.getCourseCode() == self.Genes[j].Course.getCourseCode() ):
                        if ( self.Genes[i].Day == self.Genes[j].Day ):
                            conflicts = conflicts + 1
                    if ( self.Genes[i].Room == self.Genes[j].Room and self.Genes[i].Day == self.Genes[j].Day and self.Genes[i].Slot == self.Genes[j].Slot ):
                        roomcheck[self.Genes[i].Day][self.Genes[i].Slot] += 1
                    if ( self.Genes[i].Day == self.Genes[j].Day and self.Genes[i].Slot == self.Genes[j].Slot and self.Genes[i].Professor.getID() == self.Genes[j].Professor.getID() ):
                        conflicts = conflicts + 1
        for i in range(len(roomcheck)):
            for j in range(8):
                if ( roomcheck[i][j] > 2 ):
                    conflicts = conflicts + roomcheck[i][j] - 2
        self.FitnessValue = conflicts

    def PrintChromo(self):
        print(self.Genes)
        print(self.FitnessValue)


class GeneticAlgorithm:

    def __init__(self, IterationCount, PopulationCount, BestSelectCount, ChromosomesGenerateCount, Courses, Professors, Rooms, Days, TimeSlots):
        self.IterationCount = IterationCount
        self.PopulationCount = PopulationCount
        self.BestSelectCount = BestSelectCount
        self.ChromosomesGenerateCount = ChromosomesGenerateCount
        self.Courses = Courses
        self.Professors = Professors
        self.Rooms = Rooms
        self.Days = Days
        self.TimeSlots = TimeSlots
    
    def InitialPopulation(self):
        Population = []
        for i in range(self.PopulationCount):
            arr = []
            for j in range(32):
                if ( j < 16 ):
                    for k in range(3):
                        arr.append(Gene(self.Courses[j], self.Professors[int(self.Courses[j].getProfessorID())], randi(0, 1), randi(0, 4), randi(0, 7)))
                else:
                    for k in range(2):
                        arr.append(Gene(self.Courses[j], self.Professors[int(self.Courses[j].getProfessorID())], randi(0, 1), randi(0, 4), randi(0, 7)))
            Population.append(Chromosome(arr, self.Rooms, self.Days, len(self.TimeSlots)))
        return Population

    def run(self):
        Pop = self.InitialPopulation()
        Q = PriorityQueue()

        for i in range(len(Pop)):
            Pop[i].FitnessFunction()
            Q.put((Pop[i].FitnessValue, Pop[i]))

        for i in range(self.IterationCount):
            newPop = []
            value = 0
            for j in range(self.BestSelectCount):
                newPop.append(Q.get()[1])
                value += newPop[j].FitnessValue
            print("FitnessValueChromo(Combined): ",value)
            newGen = []
            # print(len(newPop))
            # if ( i < int(self.IterationCount/2) ):
            #     # CrossOver
            #     v = int(len(newPop)/2)
            #     for j in range(v):
            #         for k in range(self.ChromosomesGenerateCount):
            #             newGen = newGen + newPop[j].Crossover(newPop[j+v])
            #     newPop = newPop + newGen
            # else:
                # Mutation
            for j in range(len(newPop)):
                for k in range(self.ChromosomesGenerateCount):
                    newGen.append(newPop[j].Jumble())
            newPop = newPop + newGen
            Q = PriorityQueue()
            for j in range(len(newPop)):
                newPop[j].FitnessFunction()
                Q.put((newPop[j].FitnessValue, newPop[j]))

        newPop = []


class MemeticAlgorithm:
    
    def __init__(self, IterationCount, PopulationCount, BestSelectCount, ChromosomesGenerateCount, Courses, Professors, Rooms, Days, TimeSlots):
        self.IterationCount = IterationCount
        self.PopulationCount = PopulationCount
        self.BestSelectCount = BestSelectCount
        self.ChromosomesGenerateCount = ChromosomesGenerateCount
        self.Courses = Courses
        self.Professors = Professors
        self.Rooms = Rooms
        self.Days = Days
        self.TimeSlots = TimeSlots
    
    def InitialPopulation(self):
        Population = []
        for i in range(self.PopulationCount):
            arr = []
            for j in range(32):
                if ( j < 16 ):
                    for k in range(3):
                        arr.append(Gene(self.Courses[j], self.Professors[int(self.Courses[j].getProfessorID())], randi(0, 1), randi(0, 4), randi(0, 7)))
                else:
                    for k in range(2):
                        arr.append(Gene(self.Courses[j], self.Professors[int(self.Courses[j].getProfessorID())], randi(0, 1), randi(0, 4), randi(0, 7)))
            Population.append(Chromosome(arr, self.Rooms, self.Days, len(self.TimeSlots)))
        return Population

    def localOptimisation(self, Pop):
        newPop = []
        for i in range(self.PopulationCount):
            chromo = Pop[i]
            couDay = {}
            for j in range(len(chromo.Genes)):
                if ( chromo.Genes[j].Course.getCourseCode() not in couDay ):
                    couDay[chromo.Genes[j].Course.getCourseCode()] = [chromo.Genes[j].Day]
                else:
                    arr = couDay[chromo.Genes[j].Course.getCourseCode()]
                    if chromo.Genes[j].Day in arr:
                        ni = randi(0, 4)
                        chromo.Genes[j].Day = ni
                    else:
                        couDay[chromo.Genes[j].Course.getCourseCode()].append(chromo.Genes[j].Day)
            newPop.append(chromo)
        return newPop



    def run(self):
        Pop = self.InitialPopulation()
        Pop = self.localOptimisation(Pop)
        Q = PriorityQueue()

        for i in range(len(Pop)):
            Pop[i].FitnessFunction()
            Q.put((Pop[i].FitnessValue, Pop[i]))

        for i in range(self.IterationCount):
            newPop = []
            value = 0
            for j in range(self.BestSelectCount):
                newPop.append(Q.get()[1])
                value += newPop[j].FitnessValue
            print("FitnessValueChromo(Combined): ",value)
            newGen = []
            # print(len(newPop))
            # if ( i < int(self.IterationCount/2) ):
            #     # CrossOver
            #     v = int(len(newPop)/2)
            #     for j in range(v):
            #         for k in range(self.ChromosomesGenerateCount):
            #             newGen = newGen + newPop[j].Crossover(newPop[j+v])
            #     newPop = newPop + newGen
            # else:
                # Mutation
            for j in range(len(newPop)):
                for k in range(self.ChromosomesGenerateCount):
                    newGen.append(newPop[j].Jumble())
            newPop = newPop + newGen
            newPop = self.localOptimisation(newPop)
            Q = PriorityQueue()
            for j in range(len(newPop)):
                newPop[j].FitnessFunction()
                Q.put((newPop[j].FitnessValue, newPop[j]))

        newPop = []
            

if __name__ == "__main__":

    class_count = ["2", "3"]

    courses = []
    professors = []
    rooms = ["R1", "R2"]
    timeslots = ["1", "2", "3", "4", "5", "6", "7", "8"]

    courses.append(Course("0", "0", "0", "1"))
    courses.append(Course("1", "1", "0", "1"))
    courses.append(Course("2", "2", "1", "1"))

    courses.append(Course("3", "3", "1", "1"))
    courses.append(Course("4", "4", "2", "1"))
    courses.append(Course("5", "5", "2", "1"))

    courses.append(Course("6", "6", "3", "1"))
    courses.append(Course("7", "7", "3", "1"))
    courses.append(Course("8", "8", "4", "1"))

    courses.append(Course("9", "9", "4", "1"))
    courses.append(Course("10", "10", "5", "1"))
    courses.append(Course("11", "11", "5", "1"))

    courses.append(Course("12", "12", "6", "1"))
    courses.append(Course("13", "13", "6", "1"))
    courses.append(Course("14", "14", "7", "1"))
    courses.append(Course("15", "15", "7", "1"))

    # Thursday & Friday
    courses.append(Course("16", "16", "8", "0"))
    courses.append(Course("17", "17", "8", "0"))

    courses.append(Course("18", "18", "9", "0"))
    courses.append(Course("19", "19", "9", "0"))
    courses.append(Course("20", "20", "10", "0"))

    courses.append(Course("21", "21", "10", "0"))
    courses.append(Course("22", "22", "11", "0"))
    courses.append(Course("23", "23", "11", "0"))

    courses.append(Course("24", "24", "12", "0"))
    courses.append(Course("25", "25", "12", "0"))
    courses.append(Course("26", "26", "13", "0"))

    courses.append(Course("27", "27", "13", "0"))
    courses.append(Course("28", "28", "14", "0"))
    courses.append(Course("29", "29", "14", "0"))

    courses.append(Course("30", "30", "15", "0"))
    courses.append(Course("31", "31", "15", "0"))

    professors.append(Professor("0", "A", "0", "1"))
    professors.append(Professor("1", "B", "2", "3"))
    professors.append(Professor("2", "C", "4", "5"))
    professors.append(Professor("3", "D", "6", "7"))

    professors.append(Professor("4", "E", "8", "9"))
    professors.append(Professor("5", "F", "10", "11"))
    professors.append(Professor("6", "G", "12", "13"))
    professors.append(Professor("7", "H", "14", "15"))

    professors.append(Professor("8", "I", "16", "17"))
    professors.append(Professor("9", "J", "18", "19"))
    professors.append(Professor("10", "K", "20", "21"))
    professors.append(Professor("11", "L", "22", "23"))

    professors.append(Professor("12", "M", "24", "25"))
    professors.append(Professor("13", "N", "26", "27"))
    professors.append(Professor("14", "O", "28", "29"))
    professors.append(Professor("15", "P", "30", "31"))

    geneticAlgorithm = GeneticAlgorithm(500, 100, 10, 9, courses, professors, 2, 5, timeslots)
    # geneticAlgorithm = GeneticAlgorithm(1000, 500, 50, 19, courses, professors, 2, 5, timeslots)
    geneticAlgorithm.run()

    memeticAlgorithm = MemeticAlgorithm(500, 100, 10, 9, courses, professors, 2, 5, timeslots)
    memeticAlgorithm.run()
