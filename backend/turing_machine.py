from backend.tables import *


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

        s = s.strip('B').replace('B', ' ')

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

    tables = {
        "division_table": division_table,
        "equals_table": equals_table
    }

    final_states = {"FIM"}

    t = TuringMachine(">***B**B",
                      initial_state=initial_state,
                      final_states=final_states,
                      transition_table=tables["division_table"])

    print("Input on Tape:\n" + t.get_tape())

    while not t.final():
        t.step()

    print("Result of the Turing machine calculation:")
    print(t.get_tape())