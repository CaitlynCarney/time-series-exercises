import pandas as pd
import requests


# ______________________________________________________________________________
def update_store_data(df):
    '''This function takes the complete_data for stores
    changes the date to be datetime
    sets indesx to be date
    create a month, day of the week, and sales total features
    reutrns df'''
    # change the date
    df.sale_date = pd.to_datetime(df.sale_date)
    # set the index
    df = df.set_index('sale_date').sort_index()
    # create new features
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    #return the new df
    return df

def update_german_energy(df):
    '''takes in the german energy data frame
    changes date format
    sets date as index
    renames wind+solar
    adds month and year features
    replace null values'''
    # change date format
    df.Date = pd.to_datetime(df.Date)
    # set index
    df = df.set_index('Date').sort_index()
    # add month and yar columns
    df['month'] = df.index.month
    df['year'] = df.index.year
    # replace nulls with 0
    df.Wind[np.isnan(df.Wind)] = 0
    df.Solar[np.isnan(df.Solar)] = 0
    df.Wind_and_Solar[np.isnan(df.Wind_and_Solar)] = 0
    # df['month'] = df.index.month
    df['year'] = df.index.year
    # return df
    return df