from ListPrinter import ListPrinter
from StatisticCalculator import StatisticCalculator

class StatisticAnalyses(object):
    def RunAnalyses(self, values):
        statisticCalculator = StatisticCalculator()
        average = statisticCalculator.CalculateArritmeticAvg(values)
        ordenedList = statisticCalculator.OrdenateValues(values)
        rol = statisticCalculator.OrdenateValues(values)
        standartDeviation = statisticCalculator.GetStandartDeviation(values)
        median = statisticCalculator.GetMedian(values)

        print("Average: " + str(average) + "\n")
        print("Rol: " + ListPrinter().GenerateMessage(rol, ", ") + "\n")
        print("Standart Deviation: " + str(standartDeviation) + "\n")
        print("Median: " + str(median) + "\n")
