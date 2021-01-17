from ListPrinter import ListPrinter
from StatisticCalculator import StatisticCalculator

class StatisticAnalyses(object):
    def RunAnalyses(self, values):
        statisticCalculator = StatisticCalculator()
        average = statisticCalculator.CalculateArritmeticAvg(values)
        ordenedList = statisticCalculator.OrdenateValues(values)
        rol = statisticCalculator.OrdenateValues(values)
        standartDeviation = statisticCalculator.GetStandartDeviation(values)

        print("\nAverage:")
        print(str(average) + "\n")
        print("Rol:")
        print(ListPrinter().GenerateMessage(rol, ", ") + "\n")
        print("Standart Deviation:")
        print(str(standartDeviation) + "\n")



