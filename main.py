import pandas as pd
from config.db_config import db_engine
from extract import extract as ex
from transform import transform as tr
import db_auth.db_auth as db

# Number of pages to return. You can ask user input as an alternative
pages = 20


# Extract data
def main(page_count):
    extracted_data = ex.extract_dataframe(page_count)
    transformed_data = tr.clean_df(extracted_data)

    # Insert the DataFrame into the "t_stg_realestate" staging table database
    transformed_data.to_sql('t_stg_realestate',
                            db_engine(db.PWD, db.USR, db.HOST, db.DBASE),
                            schema='public',
                            if_exists='append',
                            index=False)


if __name__ == "__main__":
    main(pages)
    print("Success!")
