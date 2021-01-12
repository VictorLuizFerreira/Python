class Files:

    def readFile(self, file_name):

        file = open(file_name, "r+")

        lines = file.readlines()

        file.close()

        return lines

    def writeToFile(self, text, file_name):

        file = open(file_name, "a+")

        file.write(text)

        file.close()

    def deleteFile(self, text, file_name):

        file = open(file_name)

        result = []

        for line in file:

            if not text in line:
                result.append(line)

        file.close()

        file = open(file_name, 'w+')

        file.writelines(result)

        file.close()


