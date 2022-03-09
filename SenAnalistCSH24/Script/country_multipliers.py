#country_multipliers.py

import numpy as np
import pandas as pd
import sys


def compute_country_multipliers(input_fname):
    case_study_table = pd.read_csv(input_fname)
    # filter data for PRICE API
    id_df = pd.DataFrame(case_study_table['id'].str.split('_').tolist(), columns=['unknown', 'o_country',
                                                                                  'im_country', 'id'])

    all_im_countries = np.unique(id_df['im_country'].tolist())
    all_categories = case_study_table[['main_category', 'sub_category'
                                       ]].drop_duplicates().sort_values(['main_category', 'sub_category'])

    new_mult_list = []
    for imc in all_im_countries:
        if imc == 'DE':
            continue
        for m_c, s_c in all_categories.values:
            base_price = case_study_table.loc[case_study_table['id'].str.contains('_de_DE_'), :]
            base_price = base_price.loc[(base_price['main_category'] == m_c) & (base_price['sub_category'] == s_c)]
            all_prices = base_price['google_shopping_price'].dropna().tolist() + base_price[
                'priceAPI'].dropna().tolist()
            base_price = np.mean(all_prices) if len(all_prices) > 0 else np.nan
            temp_slice = case_study_table.loc[case_study_table['id'].str.contains(imc), :]
            temp_slice = temp_slice.loc[(temp_slice['main_category'] == m_c) & (temp_slice['sub_category'] == s_c)]
            all_prices = temp_slice['google_shopping_price'].dropna().tolist() + temp_slice['priceAPI'].dropna().tolist()
            temp_slice = np.mean(all_prices) if len(all_prices) > 0 else np.nan
            if not (np.isnan(base_price) or np.isnan(temp_slice)):

                mult = float("{:.2f}".format(temp_slice/base_price))
                new_mult_list.append([imc, m_c, s_c, mult])
                pass
    out_df = pd.DataFrame(new_mult_list, columns=['country', 'main_cat', 'sub_cat1', 'new_mult'])
    out_df.to_csv('../Data/New_multiplier.csv', index=False)
    pass


def main():
    case_study_fname = '../Data/MarketPriceSampleCaseStudy.csv'
    compute_country_multipliers(case_study_fname)
    return 0


if __name__ == '__main__':
    sys.exit(main())