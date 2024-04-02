from openpyxl import load_workbook
import pandas as pd

def extract_hyperlinks_from_excel(excel_path, header_name='URL'):
    """
    Extracts hyperlinks from a column under a specified header name in an Excel sheet.

    :param excel_path: Path to the Excel file.
    :param header_name: Name of the header above the column from which to extract hyperlinks.
    :return: List of extracted URLs.
    """
    wb = load_workbook(filename=excel_path)
    sheet = wb.active
    
    # Find the column number for the given header name
    header_row = next(sheet.iter_rows(values_only=True))
    column_letter = None
    for idx, value in enumerate(header_row):
        if value == header_name:
            column_letter = chr(65 + idx)  # Convert column index to letter
            break
    if not column_letter:
        raise ValueError(f"Header '{header_name}' not found in the Excel sheet.")
    
    urls = []
    for row in range(2, sheet.max_row + 1):  # Assuming row 1 is the header
        cell = sheet[f'{column_letter}{row}']
        if cell.hyperlink:
            urls.append(cell.hyperlink.target)
    return urls


excel_path = "data/transcript_urls.xlsx"  # Adjusted for the file inside 'data' folder
urls = extract_hyperlinks_from_excel(excel_path, header_name='URL')


df_urls = pd.DataFrame(urls, columns=['URL'])
print(df_urls)
