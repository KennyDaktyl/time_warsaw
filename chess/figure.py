COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']


class Figure():

    def __init__(self, currentField):
        self.currentField = currentField

    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        if dest_field.upper() in self.list_available_moves():
            return True
        else:
            return False


class Pawn(Figure):

    def move_up(self, availableMoves, row_pos_index, col_pos_index):
        if row_pos_index + 1 in range(0, len(ROWS)):
            availableMoves.append(
                COLUMNS[col_pos_index] + ROWS[row_pos_index + 1])
        return availableMoves

    def list_available_moves(self):
        availableMoves = []
        col_pos = self.currentField[0].upper()
        row_pos = self.currentField[1]
        row_pos_index = ROWS.index(row_pos)
        col_pos_index = COLUMNS.index(col_pos)
        self.move_up(availableMoves, row_pos_index, col_pos_index)
        return availableMoves


class Rook(Figure):

    def move_up(self, availableMoves, row_pos_index, col_pos_index):
        for row in ROWS[row_pos_index + 1:]:
            availableMoves.append(COLUMNS[col_pos_index] + row)
        return availableMoves

    def move_down(self, availableMoves, row_pos_index, col_pos_index):
        for row in ROWS[:row_pos_index]:
            availableMoves.append(COLUMNS[col_pos_index] + row)
        return availableMoves

    def move_right(self, availableMoves, row_pos_index, col_pos_index):
        for col in COLUMNS[col_pos_index + 1:]:
            availableMoves.append(col + ROWS[row_pos_index])
        return availableMoves

    def move_left(self, availableMoves, row_pos_index, col_pos_index):
        for col in COLUMNS[:col_pos_index]:
            availableMoves.append(col + ROWS[row_pos_index])
        return availableMoves

    def list_available_moves(self):
        availableMoves = []
        col_pos = self.currentField[0].upper()
        row_pos = self.currentField[1]
        row_pos_index = ROWS.index(row_pos)
        col_pos_index = COLUMNS.index(col_pos)

        self.move_up(availableMoves, row_pos_index, col_pos_index)
        self.move_down(availableMoves, row_pos_index, col_pos_index)
        self.move_right(availableMoves, row_pos_index, col_pos_index)
        self.move_left(availableMoves, row_pos_index, col_pos_index)
        return availableMoves


class Knight(Figure):

    def move_up_right(self, availableMoves, row_index, col_index):
        if row_index + 2 in range(0, len(ROWS)) and \
                    col_index + 1 in range(0, len(COLUMNS)):
            availableMoves.append(COLUMNS[col_index + 1] + ROWS[row_index + 2])
            return availableMoves

    def move_up_left(self, availableMoves, row_index, col_index):
        if row_index + 2 in range(0, len(ROWS)) and \
                    col_index - 1 in range(0, len(COLUMNS)):
            availableMoves.append(COLUMNS[col_index - 1] + ROWS[row_index + 2])
            return availableMoves

    def move_down_right(self, availableMoves, row_index, col_index):
        if row_index - 2 in range(0, len(ROWS)) and \
                    col_index + 1 in range(0, len(COLUMNS)):
            availableMoves.append(COLUMNS[col_index + 1] + ROWS[row_index - 2])
            return availableMoves

    def move_down_left(self, availableMoves, row_index, col_index):
        if row_index - 2 in range(0, len(ROWS)) and \
                    col_index - 1 in range(0, len(COLUMNS)):
            availableMoves.append(COLUMNS[col_index - 1] + ROWS[row_index - 2])
            return availableMoves

    def move_right_up(self, availableMoves, row_index, col_index):
        if row_index + 1 in range(0, len(ROWS)) and \
                    col_index + 2 in range(0, len(COLUMNS)):
            availableMoves.append(COLUMNS[col_index + 2] + ROWS[row_index + 1])
            return availableMoves

    def move_left_up(self, availableMoves, row_index, col_index):
        if row_index + 1 in range(0, len(ROWS)) and \
                    col_index - 2 in range(0, len(COLUMNS)):
            availableMoves.append(COLUMNS[col_index - 2] + ROWS[row_index + 1])
            return availableMoves

    def move_right_down(self, availableMoves, row_index, col_index):
        if row_index - 1 in range(0, len(ROWS)) and \
                    col_index + 2 in range(0, len(COLUMNS)):
            availableMoves.append(COLUMNS[col_index + 2] + ROWS[row_index - 1])
            return availableMoves

    def move_left_down(self, availableMoves, row_index, col_index):
        if row_index - 1 in range(0, len(ROWS)) and \
                    col_index - 2 in range(0, len(COLUMNS)):
            availableMoves.append(COLUMNS[col_index - 2] + ROWS[row_index - 1])
            return availableMoves

    def list_available_moves(self):
        availableMoves = []
        col_pos = self.currentField[0].upper()
        row_pos = self.currentField[1]
        row_pos_index = ROWS.index(row_pos)
        col_pos_index = COLUMNS.index(col_pos)

        self.move_up_right(availableMoves, row_pos_index, col_pos_index)
        self.move_up_left(availableMoves, row_pos_index, col_pos_index)
        self.move_down_right(availableMoves, row_pos_index, col_pos_index)
        self.move_down_left(availableMoves, row_pos_index, col_pos_index)
        self.move_right_up(availableMoves, row_pos_index, col_pos_index)
        self.move_left_up(availableMoves, row_pos_index, col_pos_index)
        self.move_right_down(availableMoves, row_pos_index, col_pos_index)
        self.move_left_down(availableMoves, row_pos_index, col_pos_index)

        return availableMoves


class Bishop(Figure):

    def move_up_right(self, availableMoves, indexCol, indexRow):
        new_field_col_right = indexCol + 1
        new_field_row_up = indexRow + 1
        while new_field_col_right < len(COLUMNS) and \
                new_field_row_up < len(ROWS):
            availableMoves.append(
                COLUMNS[new_field_col_right] + ROWS[new_field_row_up])
            new_field_col_right += 1
            new_field_row_up += 1
        return availableMoves

    def move_up_left(self, availableMoves, indexCol, indexRow):
        new_field_col_left = indexCol - 1
        new_field_row_up = indexRow + 1
        while new_field_col_left >= 0 and \
                new_field_row_up < len(ROWS):
            availableMoves.append(
                COLUMNS[new_field_col_left] + ROWS[new_field_row_up])
            new_field_col_left -= 1
            new_field_row_up += 1
        return availableMoves

    def move_down_right(self, availableMoves, indexCol, indexRow):
        new_field_col_right = indexCol + 1
        new_field_row_down = indexRow - 1
        while new_field_col_right < len(COLUMNS) and \
                new_field_row_down >= 0:
            availableMoves.append(
                COLUMNS[new_field_col_right] + ROWS[new_field_row_down])
            new_field_col_right += 1
            new_field_row_down -= 1
        return availableMoves

    def move_down_left(self, availableMoves, indexCol, indexRow):
        new_field_col_left = indexCol - 1
        new_field_row_down = indexRow - 1
        while new_field_col_left >= 0 and new_field_row_down >= 0:
            availableMoves.append(
                COLUMNS[new_field_col_left] + ROWS[new_field_row_down])
            new_field_col_left -= 1
            new_field_row_down -= 1
        return availableMoves

    def list_available_moves(self):
        availableMoves = []
        indexCol = COLUMNS.index(self.currentField[0].upper())
        indexRow = ROWS.index(self.currentField[1])
        new_indexRow = indexRow
        new_indexCol = indexCol

        self.move_up_right(availableMoves, new_indexCol, new_indexRow)
        self.move_up_left(availableMoves, new_indexCol, new_indexRow)
        self.move_down_right(availableMoves, new_indexCol, new_indexRow)
        self.move_down_left(availableMoves, new_indexCol, new_indexRow)

        return availableMoves


class Queen(Figure):

    def list_available_moves(self):
        availableMoves = []

        rook = Rook(self.currentField)
        bishop = Bishop(self.currentField)
        availableMoves = (
            rook.list_available_moves() + bishop.list_available_moves())
        return availableMoves


class King(Figure):

    def move_up(self, availableMoves):
        pawn = Pawn(self.currentField)
        availableMoves = pawn.list_available_moves()
        return availableMoves

    def move_up_right(self, availableMoves, row_pos_index, col_pos_index):
        if row_pos_index + 1 in range(0, len(ROWS)) and \
                col_pos_index + 1 in range(0, len(COLUMNS)):
            availableMoves.append(
                COLUMNS[col_pos_index + 1] + ROWS[row_pos_index + 1])
        return availableMoves

    def move_right(self, availableMoves, row_pos_index, col_pos_index):
        if col_pos_index + 1 in range(0, len(COLUMNS)):
            availableMoves.append(
                COLUMNS[col_pos_index + 1] + ROWS[row_pos_index])
        return availableMoves

    def move_down_right(self, availableMoves, row_pos_index, col_pos_index):
        if row_pos_index - 1 in range(0, len(ROWS)) and \
                col_pos_index + 1 in range(0, len(COLUMNS)):
            availableMoves.append(
                COLUMNS[col_pos_index + 1] + ROWS[row_pos_index - 1])
        return availableMoves

    def move_down(self, availableMoves, row_pos_index, col_pos_index):
        if row_pos_index - 1 in range(0, len(ROWS)):
            availableMoves.append(
                COLUMNS[col_pos_index] + ROWS[row_pos_index - 1])
        return availableMoves

    def move_down_left(self, availableMoves, row_pos_index, col_pos_index):
        if row_pos_index - 1 in range(0, len(ROWS)) and \
                col_pos_index - 1 in range(0, len(COLUMNS)):
            availableMoves.append(
                COLUMNS[col_pos_index - 1] + ROWS[row_pos_index - 1])
        return availableMoves

    def move_left(self, availableMoves, row_pos_index, col_pos_index):
        if col_pos_index - 1 in range(0, len(COLUMNS)):
            availableMoves.append(
                COLUMNS[col_pos_index - 1] + ROWS[row_pos_index])
        return availableMoves

    def move_up_left(self, availableMoves, row_pos_index, col_pos_index):
        if row_pos_index + 1 in range(0, len(ROWS)) and \
                col_pos_index - 1 in range(0, len(COLUMNS)):
            availableMoves.append(
                COLUMNS[col_pos_index - 1] + ROWS[row_pos_index + 1])
        return availableMoves

    def list_available_moves(self):
        availableMoves = []
        indexCol = COLUMNS.index(self.currentField[0].upper())
        indexRow = ROWS.index(self.currentField[1])
        new_indexRow = indexRow
        new_indexCol = indexCol

        self.move_up_right(availableMoves, new_indexCol, new_indexRow)
        self.move_right(availableMoves, new_indexCol, new_indexRow)
        self.move_down_right(availableMoves, new_indexCol, new_indexRow)
        self.move_down(availableMoves, new_indexCol, new_indexRow)
        self.move_down_left(availableMoves, new_indexCol, new_indexRow)
        self.move_left(availableMoves, new_indexCol, new_indexRow)
        self.move_up_left(availableMoves, new_indexCol, new_indexRow)

        availableMoves += self.move_up(availableMoves)
        return availableMoves


PAWNS = {
    'pawn': Pawn,
    'rook': Rook,
    'knight': Knight,
    'bishop': Bishop,
    'queen': Queen,
    'king': King
}
