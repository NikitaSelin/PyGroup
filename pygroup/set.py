import operator
from typing import Optional


OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
} # TODO define more operations in the future + another way to define a set of operation (without creating functions in memory)


class UnknownSet(Exception):
    pass


class NoSetProvided(Exception):
    pass


class Set:
    def __init__(self, predefined: bool = None, set_name: str = None, custom_set: Optional[list] = [], custom_set_name: Optional[str] = None) -> None:
        self.sets_list = ["R", "N", "Z"]
        self.predefined = predefined
        self.set_name = set_name
        self.custom_set = custom_set
        self.custom_set_name = custom_set_name
        if (self.predefined == None and self.set_name != None) or (self.predefined != None and self.set_name == None) or (self.predefined == None and self.set_name == None) and self.custom_set == []: # TODO make this better
            raise NoSetProvided("No sets provided")
        if self.set_name and self.set_name not in self.sets_list:
            raise UnknownSet(f"Unknown predefined set name. Choose from 'R' for real numbers, 'Z' for integers and 'N' for natural numbers. Got {self.set_name}")
        if not self.custom_set_name:
            self.custom_set_name = "Custom set"
    
    def binary_operation(self, operation: str):
        if operation == "-" and self.set_name == "N" or operation == "/" and self.set_name == "Z":
            return f"[+] Operation {operation} is not a binary operation on set {self.set_name}"
        elif self.predefined:
            return f"[+] Operation {operation} is a binary operation on set {self.set_name}"
        else:
            for element_1 in self.custom_set:
                for element_2 in self.custom_set:
                    if OPERATORS[operation](element_1, element_2) not in self.custom_set: # TODO this could be more efficient probably
                        return f"[+] Operation {operation} is not a binary operation on set {self.custom_set_name}"
    
    def get_length(self):
        if self.custom_set:
            return f"Actual set: [{self.custom_set[0]} ... {self.custom_set[-1]}]. Length: {len(self.custom_set)}"
        elif self.set_name == "N":
            return f"Actual set: [1 ... \u221E]. Length: \u221E"
        elif self.set_name == "Z":
            return f"Actual set: [-\u221E ... \u221E]. Length: \u221E"
        else:
            return f"Actual set: [-\u221E ... \u221E] (with rational and irrational numbers). Length: \u221E"
