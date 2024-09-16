class Cell:
    def __init__(self, pos, value=0):
        """_summary_

        Args:
            value (int, optional): Value in the cell. Defaults to 0 if the cell in unknown yet.

        Raises:
            RuntimeError: _description_
        """
        self.pos = pos
        self.value = int(value)
        self.candidate_values = set()

    def __str__(self):
        return str(self.value)
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        return self.value == other.value and self.value == other.value
    
    def is_known(self):
        return self.value is not None

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        # if self.value != 0:
        #     raise RuntimeError(f'Trying to set a value of a known cell')
        self.value = value
    
    def get_candidate_values(self):
        return self.candidate_values

    def get_prohibited_values(self):
        prohibited_values = sorted(set([i for i in range(1, 10)]) - self.candidate_values)
        return prohibited_values
    

if __name__ == '__main__':
    unknown_cell = Cell()
    known_cell = Cell(value=9)