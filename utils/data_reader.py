import openpyxl

def read_excel_data(file_path, sheet_name, column_name):
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]

        # Extract the header (first row)
        header = [cell.value for cell in sheet[1]]  # Read the first row as header
        if column_name not in header:
            raise ValueError(f"Column '{column_name}' not found in sheet '{sheet_name}'.")

        # Find the index of the column
        column_index = header.index(column_name)

        # Extract data from the specified column (row 2 and beyond)
        data = [row[column_index] for row in sheet.iter_rows(min_row=2, values_only=True) if row[column_index]]

        # Ensure the data is a flat list of strings
        return [str(value) if value is not None else "" for value in data]

    except KeyError:
        print(f"Error: Worksheet '{sheet_name}' does not exist.")
        raise

    except Exception as e:
        print(f"Error reading Excel file: {e}")
        raise
