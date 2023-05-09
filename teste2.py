#Adicionar arquivos e retronar tamanho usando queries
def solution(queries):
    file_saved = False
    saved_files = []
    opt = []
    for i, row in enumerate(queries):
        for j, value in enumerate(row):

            if value == "ADD_FILE":
                file_name = row[1]
                file_size = row[2]
                for k, file in enumerate(saved_files):
                    if file != file_name:
                        file_saved = False
                    else:
                        file_saved = True
                if not file_saved:
                    act = "created"
                    saved_files.append(file_name)
                else:
                    act = "rewrited"
                opt.append(act)

            elif value == "GET_FILE_SIZE":

                for n, row2 in enumerate(queries):
                    file_name = row[1]
                    for m, value2 in enumerate(row2):
                        if value2 == "ADD_FILE" and row2[1] == file_name:
                            file_size = row2[2]
                opt.append(file_name)
                opt.append(file_size)


    return opt


class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size


queries = [
    ["ADD_FILE", "/a.txt", "4"],
    ["ADD_FILE", "/b.txt", "8"],
    ["GET_FILE_SIZE", "/b.txt"],
    ["ADD_FILE", "/b.txt", "8"],
    ["ADD_FILE", "/c.txt", "16"],
    ["GET_FILE_SIZE", "/c.txt"]
]

print(solution(queries))
