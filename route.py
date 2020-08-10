import pandas as pd

def transform(filePath):
    '''Read in order and route data, transform the data into a form that can
    be processed by the operation research model.'''
    order = pd.read_excel(filePath, sheet_name='Order Information')
    route = pd.read_excel(filePath, sheet_name='Route Information')
    # order['Tax Percentage'][order['Journey Type'] == 'Domestic'] = 0

    order.loc['Tax Percentage',(order['Journey Type'] == 'Domestic')] = 0

    route['Cost'] = route[route.columns[7:12]].sum(axis=1)
    route['Time'] = np.ceil(route[route.columns[14:18]].sum(axis=1) / 24)
    route = route[list(route.columns[0:4]) + ['Fixed Freight Cost', 'Time', \
                                              'Cost', 'Warehouse Cost', 'Travel Mode', 'Transit Duty'] + list(
        route.columns[-9:-2])]
    route = pd.melt(route, id_vars=route.columns[0:10], value_vars=route.columns[-7:] \
                    , var_name='Weekday', value_name='Feasibility')
    route['Weekday'] = route['Weekday'].replace({'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, \
                                                 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7})

    return order, route



order, route = transform("model data.xlsx")
