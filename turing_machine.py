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
        return str(self._tape)

    def step(self):
        current_head_symbol = self.__tape[self.__head_position]
        x = (self.__current_state, current_head_symbol)
        if x in self.__transition_table:
            y = self.__transition_table[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]

    def final(self):
        return self.__current_state in self.__final_states


class Tape(object):

