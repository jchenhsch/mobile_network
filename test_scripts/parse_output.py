# Parse the csv duplicated df without square brackets
import pandas as pd
import numpy as np
import sys

# raise the df[df[]] warning
pd.options.mode.chained_assignment = None

def header_help(num_node):
    columns=[]
    for i in range(num_node):
        ind=i
        ind_lst=list(range(num_node))
        #print(ind_lst)
        ind_lst.pop(i)
        for j in ind_lst:
            inside_ind=j
            name=(ind,inside_ind)
            columns.append(name)
    return columns
def tuple_help(tup):
    if tup[0]> tup[1]:
        return (tup[1],tup[0])
    else:
        return tup
def data_parse(file_path, num_node,inrange,filename):
    columns=header_help(num_node)
    df=pd.read_csv(file_path,index_col=0,delim_whitespace=True,header=None)
    df.index = list(range(1, len(df)+1))
    #df=df.rename(columns={"0":"Time"})
    df.columns=columns
    
    mod_set=list(set(map(tuple_help,columns)))
    new_df=df[mod_set]
    # new_df[new_df<inrange]=1
    # new_df[new_df>=inrange]=0
    #print(new_df)
    new_df.to_csv(filename)
    
    return new_df


data_parse(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])


#  df=pd.read_csv(file_path,index_col=0,delim_whitespace=True,header=None)
# df=df.rename(columns={"0":"Time"})
# df.columns=columns
# print(df)

# df[df<inrange]=1
# df[df>=inrange]=0
# return df
