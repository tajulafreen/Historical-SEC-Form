import pandas as pd

def process_data(input_file: str, output_file: str):
    # Step 1: Load the raw data
    df = pd.read_csv(input_file)

    # Step 2: Clean column names
    df.columns = df.columns.str.strip()  # Remove any extra spaces from column names

    # Step 3: Clean specific columns (remove spaces or unwanted characters)
    df['Form__File'] = df['Form__File'].str.strip()  # Clean Form__File column
    df['Filed'] = df['Filed'].str.strip()            # Clean Filed column
    df['Filing_entityperson'] = df['Filing_entityperson'].str.strip()  # Clean Filing_entityperson

    # Step 4: Rename columns for clarity
    df.rename(columns={
        'Form__File': 'Form',  # Rename column Form__File to Form
        'Filed': 'Filing_Date',  # Rename Filed to Filing_Date
        'Filing_entityperson': 'Entity_Person'  # Rename Filing_entityperson to Entity_Person
    }, inplace=True)

    # Step 5: Handle missing values
    df.dropna(subset=['Form', 'Filing_Date', 'Entity_Person'], inplace=True)  # Remove rows with missing important data

    # Step 6: Drop rows that are completely empty
    df.dropna(how='all', inplace=True)

    # Step 7: Reset index after dropping rows
    df.reset_index(drop=True, inplace=True)

    # Step 8: Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Data has been cleaned and saved to {output_file}")
