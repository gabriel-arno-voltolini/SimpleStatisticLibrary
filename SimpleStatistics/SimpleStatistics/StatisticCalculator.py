import math

class StatisticCalculator(object):
     def CalculateArritmeticAvg(self, values):
         sum = 0
         for value in values:
             sum += value
         return sum/len(values)

     def OrdenateValues(self, values):
         inputs = values.copy()
         ordenatedValues = []

         for value in values:
            smaller = self.GetSmaller(inputs)

            for index, x in enumerate(inputs):
               if smaller == int(x):
                   ordenatedValues.append(int(x))
                   inputs.pop(index)

         return ordenatedValues

     def GetSmaller(self, values):
         if  len(values) > 0:
             smaller = float('inf')
             for x in values:
                 if x <= smaller:
                  smaller = x

             return int(smaller)

     def GetStandartDeviation(self, values):
         average = self.CalculateArritmeticAvg(values)
         deviations = []

         for value in values:
             deviation = pow(value - average, 2)
             deviations.append(deviation)   
        
         variance = self.CalculateArritmeticAvg(deviations)
         return math.sqrt(variance)