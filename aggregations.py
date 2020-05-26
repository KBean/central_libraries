def group_and_sort(dataframe, L_group_cols, L_group_keys, agg_function, bool_sort_ascending):
    """
    This function goal is to compute an agregation in a pandas DataFrame. Then the DataFrame's 
    rows will be sorted.
    
    Used variables :
    - 'dataframe' [pandas.core.frame.DataFrame] : The pandas DataFrame object you want to use
    - 'L_group_cols' [list] : The complete list of columns you need for your aggregation (with both
        the group keys and the dimensions to aggregate).
    - 'L_group_keys' [list] : The list of columns you want to make aggregation on.
    - 'agg_function' ['string'] : The aggregation function you want to use.
        You have to whoose between 'min', 'max', 'mean' and 'median'.
    - 'bool_sort_ascending' : A boolean which indicates if you want to sort the resulting DataFrame in
        the ascending order (if set to True) or in the descending one (if set to False)
        
        changed
    """
    if agg_function=='min':
        df_aggregated = dataframe[L_group_cols].groupby(L_group_keys).min()

    elif agg_function=='max':
        df_aggregated = dataframe[L_group_cols].groupby(L_group_keys).max()

    elif agg_function=='mean':
        df_aggregated = dataframe[L_group_cols].groupby(L_group_keys).mean()

    elif agg_function=='median':
        df_aggregated = dataframe[L_group_cols].groupby(L_group_keys).median()

    L_aggregated_cols = [col for col in L_group_cols if not col in L_group_keys]
    df_aggregated.sort_values(by=L_aggregated_cols, ascending=bool_sort_ascending, inplace=True)
    df_aggregated.reset_index(inplace=True)

    return df_aggregated
