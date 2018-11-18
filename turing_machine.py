class TuringMachine(object):

    def __init__(self,
                 tape = "",
                 blank = " ",
                 initial_state = "",
                 final_states = None,
                 transition_table = None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank
        self.__current_state = initial_state
        if transition_table == None:
            self.__transition_table = {}
        else:
            self.__transition_table = transition_table
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        return str(self.__tape)

    def step(self):
        current_head_symbol = self.__tape[self.__head_position]

        if self.__head_position == self.__tape.length():
            self.__tape[self.__head_position] = "B"

        x = (self.__current_state, current_head_symbol)
        if x in self.__transition_table:
            y = self.__transition_table[x]
            if y[1] == "$":
                self.__tape[self.__head_position] = current_head_symbol
            else:
                self.__tape[self.__head_position] = y[1]
            if y[2] == "D":
                self.__head_position += 1
            elif y[2] == "E":
                self.__head_position -= 1
            self.__current_state = y[0]

    def final(self):
        return self.__current_state in self.__final_states


class Tape(object):

    blank = " "

    def __init__(self,
                 tape = ""):
        self.__tape = dict((enumerate(tape)))

    def length(self):
        return len(self.__tape)

    def __str__(self):
        s = ""
        min_index = min(self.__tape.keys())
        max_index = max(self.__tape.keys())

        for i in range(min_index, max_index + 1):
            s += self.__tape[i]

        s.strip('B')

        return s

    def __getitem__(self, index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank

    def __setitem__(self, key, value):
        self.__tape[key] = value


if __name__ == "__main__":

    initial_state = ">"

    #Exemplo:
    #("init", "0"): ("init", "1", "R")
    transition_function = {(">", ">"): ("0", ">", "D"),

                           ("0", "*"): ("0", "*", "D"),
                           ("0", "B"): ("1", "B", "D"),

                           ("1", "*"): ("1", "*", "D"),
                           ("1", "B"): ("2", "B", "E"),
                           ("1", "X"): ("2", "X", "E"),

                           ("2", "*"): ("3", "X", "E"),
                           ("2", "B"): ("5", "B", "D"),

                           ("3", ">"): ("4", "B", "D"),
                           ("3", "*"): ("3", "*", "E"),
                           ("3", "B"): ("3", "B", "E"),

                           ("4", "*"): ("0", ">", "D"),
                           ("4", "B"): ("8", "B", "D"),

                           ("5", "B"): ("6", "B", "D"),
                           ("5", "X"): ("5", "*", "D"),

                           ("6", "*"): ("6", "*", "D"),
                           ("6", "B"): ("7", "*", "E"),

                           ("7", "*"): ("7", "*", "E"),
                           ("7", "B"): ("2", "B", "E"),

                           ("8", ">"): ("10", "B", "D"),
                           ("8", "*"): ("8", "B", "D"),
                           ("8", "X"): ("9", "B", "D"),

                           ("9", "B"): ("10", ">", "D"),
                           ("9", "X"): ("10", ">", "D"),

                           ("10", "*"): ("FIM", "$", "N"),
                           ("10", "B"): ("11", "B", "D"),
                           ("10", "X"): ("10", "X", "D"),

                           ("11", "*"): ("11", "*", "D"),
                           ("11", "B"): ("12", "B", "D"),

                           ("12", "*"): ("12", "*", "D"),
                           ("12", "B"): ("13", "*", "E"),

                           ("13", ">"): ("14", "B", "D"),
                           ("13", "*"): ("13", "*", "E"),
                           ("13", "B"): ("13", "B", "E"),
                           ("13", "X"): ("13", "X", "E"),

                           ("14", "*"): ("FIM", "$", "N"),
                           ("14", "B"): ("14", ">", "D"),
                           ("14", "X"): ("8", "X", "E"),
                           }

    # transition_function = {
    #     (">", ">"): ("0", ">", "D"),
    #
    #     ("0", "*"): ("1", "X", "D"),
    #     ("0", "B"): ("7", "B", "D"),
    #
    #     ("1", "*"): ("2", "*", "D"),
    #     ("1", "B"): ("6", "B", "D"),
    #
    #     ("2", "*"): ("2", "*", "D"),
    #     ("2", "B"): ("3", "B", "D"),
    #
    #     ("3", "*"): ("4", "X", "E"),
    #     ("3", "B"): ("4", "X", "E"),
    #     ("3", "X"): ("3", "X", "D"),
    #
    #     ("4", "*"): ("5", "*", "E"),
    #     ("4", "B"): ("4", "B", "E"),
    #     ("4", "X"): ("4", "X", "E"),
    #
    #     ("5", "*"): ("5", "*", "E"),
    #     ("5", "B"): ("5", "B", "E"),
    #     ("5", "X"): ("0", "X", "D"),
    #
    #     ("6", "*"): ("7", "X", "D"),
    #     ("6", "B"): ("7", "X", "D"),
    #     ("6", "X"): ("6", "X", "D"),
    #
    #     ("7", "*"): ("7", "*", "D"),
    #     ("7", "B"): ("8", "B", "E"),
    #
    #     ("8", ">"): ("9", ">", "D"),
    #     ("8", "*"): ("8", "B", "E"),
    #     ("8", "B"): ("8", "B", "E"),
    #     ("8", "X"): ("8", "*", "E"),
    #
    #     ("9", "*"): ("FIM", "$", "N"),
    # }

    final_states = {"FIM"}

    t = TuringMachine(">***B**B",
                      initial_state=initial_state,
                      final_states=final_states,
                      transition_table=transition_function)

    print("Input on Tape:\n" + t.get_tape())

    while not t.final():
        t.step()

    print("Result of the Turing machine calculation:")
    print(t.get_tape())