class ListPrinter(object):
    def GenerateMessage(self, charList, separator):
        message = "";
        for index, char in enumerate(charList):
            message += str(char)
            if (len(charList) - index) != 1:
                message += str(separator)
        return message
        
