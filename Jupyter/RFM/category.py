
def cat(row):
    
 if ((row['r_cat'] >= 4) & (row['r_cat'] <= 5) & (row['fm_cat'] >= 4) & (row['fm_cat'] <= 5)):
    return'Champion'
 elif ((row['r_cat'] >= 2) & (row['r_cat'] <= 5) & (row['fm_cat'] >= 3) & (row['fm_cat'] <= 5)):
    return'Loyal Customers'
 elif ((row['r_cat'] >= 3) & (row['r_cat'] <= 5) & (row['fm_cat'] >= 1) & (row['fm_cat'] <= 3)):
    return'Potential Loyalist'
 elif ((row['r_cat'] >= 4) & (row['r_cat'] <= 5) & (row['fm_cat'] >= 0) & (row['fm_cat'] <= 1)):
    return'New Customers'
 elif ((row['r_cat'] >= 3) & (row['r_cat'] <= 4) & (row['fm_cat'] >= 0) & (row['fm_cat'] <= 1)):
    return'Promising'
 elif ((row['r_cat'] >= 2) & (row['r_cat'] <= 3) & (row['fm_cat'] >= 2) & (row['fm_cat'] <= 3)):
    return'Customers Needing Attention'
 elif ((row['r_cat'] >= 2) & (row['r_cat'] <= 3) & (row['fm_cat'] >= 0) & (row['fm_cat'] <= 2)):
    return'About to Sleep'
 elif ((row['r_cat'] >= 0) & (row['r_cat'] <= 2) & (row['fm_cat'] >= 2) & (row['fm_cat'] <= 5)):
    return'At Risk'
 elif ((row['r_cat'] >= 0) & (row['r_cat'] <= 1) & (row['fm_cat'] >= 4) & (row['fm_cat'] <= 5)):
    return"Can't Lose Them"
 elif ((row['r_cat'] >= 1) & (row['r_cat'] <= 2) & (row['fm_cat'] >= 1) & (row['fm_cat'] <= 2)):
    return'Hibernating'
 elif ((row['r_cat'] >= 0) & (row['r_cat'] <= 2) & (row['fm_cat'] >= 0) & (row['fm_cat'] <= 2)):
    return'Lost'