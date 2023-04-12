
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
import sys
import re
#from scipy.special import xlogy as log
import math as m
import os



def graph_networkx(filename, num_nodes):

  df = pd.read_csv(filename, index_col=0)
  graph_lst = []

  for i in range(len(df.index)):
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    tup_columns=[]
    for ele in df.columns:
      tup_columns.append(eval(ele))
    for e in tup_columns:
      (x,y) = e
      ei = tup_columns.index(e)
      if df.iloc[i, ei] == 1:
        G.add_edge(x, y)
        #print(list(G.edges))
    graph_lst.append(G)
    # if i==2:
    #   nx.draw(G)
  return graph_lst

def node_degree(graph_lst):
  node_degree_lst=[]
  for graph in graph_lst:
    num_of_nodes=graph.number_of_nodes()
    graph_degree_lst=[graph.degree(node_num) for node_num in range (num_of_nodes)]
    average_degree_lst=sum(graph_degree_lst)/len(graph_degree_lst)
    #print("g", graph_degree_lst)
    node_degree_lst.append(average_degree_lst)
  #print("here",node_degree_lst)
  return sum(node_degree_lst)/len(node_degree_lst)

def path_prob(graph_lst):
  path_prob_lst=[]
  for graph in graph_lst:
    node_num=graph.number_of_nodes()
    path_dict_in_dict = dict(nx.all_pairs_shortest_path(graph))
    num_path_ttl=0
    for dic in path_dict_in_dict:
      inside_dic=path_dict_in_dict[dic].keys()
      num_paths=len(inside_dic)-1
      num_path_ttl+=num_paths
    path_prob=(num_path_ttl) / (node_num*(node_num-1))
    path_prob_lst.append(path_prob)
  return sum(path_prob_lst)/len(path_prob_lst)

def avg_meeting(df):
  sm=df.sum().sum()
  col_num=len(df.columns)
  return (sm,sm/col_num)

def calc_entropy(up_prob,down_prob):
  #print("up_prob", type(up_prob))
  #print("down_prob", down_prob)
  #small = 0.00000000000000000001
  if (up_prob == 0.0) or (down_prob == 0.0):
    return 0.0
  return -up_prob* m.log(up_prob)- down_prob * m.log(down_prob)

# def entropy_data_help(df,interval):
#   for row_num in (df,)


def get_avg_entropy(df,interval):
  # first row df
  res_avg_up_entropy_lst=[]
  res_avg_down_entropy_lst=[]
  for ivl in interval:
    remainder= len(df) % (ivl)
    df_select = df.iloc[::ivl,1:]
    df_rep = df_select.loc[df_select[:-1].index.repeat(ivl)].reset_index(drop=True)
    remain_df=(df_select.iloc[[-1]]*remainder).reset_index(drop=True)
    df_new = pd.concat([df_rep,remain_df],ignore_index=True).reset_index(drop=True)
  

    # first shift the df to grab the next state of the edges
    # shifted_df=df.shift(-1)
    
    # drop the NaN values, and throw away the old index
    # nei_df=shifted_df.dropna()
    # nei_df=nei_df.iloc[:,1:]
    res_df=df_new.subtract(df)

    # find the number of down edges / up_edges in the df

    res_df["up_edges"] = df_new.sum(axis=1) # N up
    res_df["down_edges"] = df_new.eq(0).sum(axis=1) # N down
    res_df['down_up_edges'] = res_df.eq(1).sum(axis=1) # N down | up
    res_df['up_down_edges'] = res_df.eq(-1).sum(axis=1) # N up | down
    

    # to get the consistdfent edges, original number of nodes- down_edges_num
    res_df["up_up_edges"] = res_df["up_edges"] - res_df["down_up_edges"]
    res_df['down_down_edges'] = res_df["down_edges"] - res_df["up_down_edges"] # N down | down

    res_df['up_up_prob'] = res_df["up_up_edges"] / res_df["up_edges"]
    res_df["down_up_prob"] = res_df["down_up_edges"] / res_df["up_edges"]
    res_df['up_down_prob']= res_df['up_down_edges'] / res_df["down_edges"]
    res_df["down_down_prob"] = res_df['down_down_edges'] / res_df["down_edges"]

    res_df["up_entropy"] = np.vectorize(calc_entropy)(res_df['up_up_prob'], res_df['down_up_prob'])
    res_df["down_entropy"] = np.vectorize(calc_entropy)(res_df['up_down_prob'], res_df['down_down_prob'])
    
    #print(res_df)
    avg_up_entropy = res_df["up_entropy"].mean()
    avg_down_entropy = res_df["down_entropy"].mean()
  
  res_avg_up_entropy_lst.append(avg_up_entropy)
  res_avg_down_entropy_lst.append(avg_down_entropy)
  res_avg_up_entropy = sum(res_avg_up_entropy_lst)/len(res_avg_up_entropy_lst)
  res_avg_down_entropy = sum(res_avg_down_entropy_lst)/len(res_avg_down_entropy_lst)
  
  return res_avg_up_entropy, res_avg_down_entropy

def condense_stat(csv_path,model_name,interval):
  master_dic={}
  master_dic["num_nodes"]=[]
  master_dic["avg_node_degree"]=[]
  master_dic["prob_path"]=[]
  master_dic["range"]=[]
  master_dic["avg_meeting"]=[]
  master_dic["ttl_meeting"]=[]
  master_dic['node_speed']=[]
  master_dic['avg_up_entropy']=[]
  master_dic['avg_down_entropy']=[]

  num_nodes = [100]
  tx_ranges = [30, 40, 50, 60, 70, 80, 90, 100 ,110, 120]
  mean_speed = [1, 2, 3]
  turn_prob = [""]
  if model_name == "ManhattanGrid":
    turn_prob = [0.1, 0.3, 0.5, 0.7, 0.9]
    master_dic["turn_prob"]=[]
  for n in num_nodes:
    for prob in turn_prob:
      for node_speed in mean_speed:
          for t in tx_ranges:
            if model_name == "ManhattanGrid":
              filename = model_name + "_" + str(n) + '_' + str(t) + '_' + str(node_speed) + "_" + str(prob) + '.csv'
              master_dic["turn_prob"].append(prob)
            else:
              filename = model_name + "_" + str(n) + '_' + str(t) + '_' + str(node_speed) + '.csv'
            
            #print("filename", filename)
            csv_file = os.path.join(csv_path,filename)
            #print("csv_file",csv_file)
            df = pd.read_csv(csv_file)

            ttl_meet,avg_meet=avg_meeting(df)
            # range = re.search(r"\_(.+)\.",csv_file).group()
            # #print(range)
            # range = int(range[1:-1])
            # ind = filename.index("_")
            # num_nodes=int(filename[:ind])
            
            #print("filename", csv_file)
            graph_lst = graph_networkx(csv_file,n)
            avg_degree = node_degree(graph_lst)
            prob_path = path_prob(graph_lst)
            avg_up_entropy, avg_down_entropy = get_avg_entropy(df,interval)
            # try:
            #   avg_entropy =get_avg_entropy(df)
            # except:
            #   print("error_filename", csv_file)
            #   # print("error_df", df)
            #   # avg_entropy = 0
            #   break
            
            master_dic["num_nodes"].append(n)
            master_dic["avg_node_degree"].append(avg_degree)
            master_dic["prob_path"].append(prob_path)
            master_dic["range"].append(t)
            master_dic["avg_meeting"].append(avg_meet)
            master_dic["ttl_meeting"].append(ttl_meet)
            master_dic['node_speed'].append(node_speed)
            master_dic['avg_up_entropy'].append(avg_up_entropy)
            master_dic['avg_down_entropy'].append(avg_down_entropy)
    
  metric_df = pd.DataFrame.from_dict(master_dic)
  #print(metric_df)
  return metric_df



# csv_path = sys.argv[1]
# model_name = sys.argv[2]
# interval = sys.argv[3]
# condense_stat(csv_path, model_name, interval)
 
