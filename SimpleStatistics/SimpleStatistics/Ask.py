class Ask(object):
    def AskForNumberList(self, stopCondition):
        count = 0
        values = []
        print(">>> Press " + stopCondition + " if you're done\n")

        while 1:
            value = input("> Val " + str(count + 1) + " -> ")

            if value == stopCondition:
                break
            else:
                values.append(int(value))

            count += 1

        return values

