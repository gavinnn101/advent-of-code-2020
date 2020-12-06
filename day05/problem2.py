import statistics


def find_row(rows_to_eliminate: str) -> int:
    """Returns the row of the passenger's seat"""
    rows = {'front_half': 0, 'back_half': 128}

    for section in rows_to_eliminate:
        # print(f"Remaining Rows: {rows}")
        if section == 'F':  # Cut out the back half
            rows['back_half'] = int(statistics.mean([rows['front_half'], rows['back_half']]))  # int() to round down
        else:  # Cut out the front half
            rows['front_half'] = round(statistics.mean([rows['front_half'], rows['back_half']]))  # round() to round up

    if rows['back_half'] < rows['front_half']:
        return rows['back_half']
    else:
        return rows['front_half']


def find_column(column_values: str) -> int:
    """Finds the column of the passenger's seat"""
    columns = {'front_half': 0, 'back_half': 8}

    for section in column_values:
        # print(f"Remaining Columns: {columns}")
        # print(f"Current: {section}")
        if section == 'R':
            columns['front_half'] = round(statistics.mean([columns['front_half'], columns['back_half']]))
        else:
            columns['back_half'] = int(statistics.mean([columns['front_half'], columns['back_half']]))

    if columns['back_half'] > columns['front_half']:
        return columns['back_half']
    else:
        return columns['front_half']


def get_seat_id(row: int, column: int) -> int:
    return row * 8 + column


seat_info = {'row': 0, 'column': 0, 'seat ID': 0}
seat_ids = []

with open('input.txt') as input_file:
    for line in input_file:
        rows = line[:7]
        column_values = line.strip()[-3:]
        seat_info['row'] = find_row(rows)
        seat_info['column'] = find_column(column_values)
        seat_info['seat ID'] = get_seat_id(seat_info['row'], seat_info['column'])

        if seat_info['seat ID'] == 55:
            print(line)
        # print(f"Seat ID: {seat_info['seat ID']}")
        seat_ids.append(seat_info['seat ID'])


def find_my_seat(seat_ids: list) -> int:
    seat_ids = sorted(seat_ids)
    for seat in range(1, len(seat_ids)-1):
        if seat_ids[seat-1] != seat_ids[seat] - 1 or seat_ids[seat+1] != seat_ids[seat] + 1:
            return seat_ids[seat]


print(find_my_seat(seat_ids))
