from openpyxl import load_workbook
import pandas as pd

def extract_hyperlinks_from_excel(excel_path, header_name='URL'):
    wb = load_workbook(filename=excel_path)
    sheet = wb.active
    header_row = next(sheet.iter_rows(values_only=True))
    column_letter = None
    for idx, value in enumerate(header_row):
        if value == header_name:
            column_letter = chr(65 + idx) 
            break
    if not column_letter:
        raise ValueError(f"Header '{header_name}' not found in the Excel sheet.")
    
    urls = []
    for row in range(2, sheet.max_row + 1):  
        cell = sheet[f'{column_letter}{row}']
        if cell.hyperlink:
            urls.append(cell.hyperlink.target)
    return urls

# Final dataframe with transcript links
excel_path = "data/transcripts_urls.xlsx" 
urls = extract_hyperlinks_from_excel(excel_path, header_name='URL')
df_urls = pd.DataFrame(urls, columns=['URL'])
print(df_urls)
#final
