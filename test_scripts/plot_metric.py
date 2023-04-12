

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from calc_metric import *
from matplotlib import cm
import sys


def metric_plot(csv_path,model_name,interval):

    metric_df= condense_stat(csv_path,model_name,interval)
    print(metric_df)
    """
    num_nodes = [3, 64, 100]
    fontsize = 16
    legendsize=6
    linewidth = 2
    markersize = 8
    xmin = 25
    xmax = 125
    ymin = 0
    ymax = 1
    marker_lst=[".","s",">","<","o","s","p","+","x"]
    color_lst=["red","green","blue", "black","brown","gray","orange","olive","cyan"]
    
    # probability path exists
    prob_path = metric_df.pivot(index="range",columns=["num_nodes", "node_speed"], values='prob_path')
    prob_path.columns = map(lambda x: ("N="+str(x[0]),"speed="+str(x[1])),prob_path.columns)
    col_lst=prob_path.columns[:]
    ind = 0
    while ind < len(marker_lst):
        prob_path[col_lst[ind]].plot(fontsize=fontsize, linewidth=linewidth, markersize=markersize,
                xlim=[xmin, xmax], ylim=[ymin, ymax], color=color_lst[ind], linestyle='-', marker = marker_lst[ind])
        ind+=1

    plt.legend(loc="upper left", fontsize=legendsize)
    pic_name = "avg_path_prob"
    plt.savefig(pic_name)
    plt.clf()

    ##################
    # avg_node_degree
    ymin = 0
    ymax = 100 #  since there is 100 nodes 
    avg_node_degree = metric_df.pivot(index="range",columns=["num_nodes","node_speed"], values='avg_node_degree')
    avg_node_degree.columns = map(lambda x: ("N="+str(x[0]),"speed="+str(x[1])),prob_path.columns)
    col_lst=avg_node_degree.columns[:]
  
    
    ind = 0
    while ind < len(marker_lst):
        avg_node_degree[col_lst[ind]].plot(fontsize=fontsize, linewidth=linewidth, markersize=markersize,
                xlim=[xmin, xmax], ylim=[ymin, ymax], color=color_lst[ind], linestyle='-', marker = marker_lst[ind])
        ind+=1

    plt.legend(loc="upper left", fontsize=legendsize)
    plt.savefig("avg_node_degree_graph.png")

    ###############

    # Heatmap / scatter_plot code
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # X=metric_df["range"].to_numpy()
    # Y=metric_df["node_speed"].to_numpy()
    # Z=metric_df["prob_path"].to_numpy()
    # ax.scatter3D(X,Y,Z)
    # plt.savefig("3D_scatterplot")
    """

    #surface plot for N=100 now
    turn_prob = [0.1, 0.3, 0.5, 0.7, 0.9]
    num_nodes = [100]
    tx_ranges = [30, 40, 50, 60, 70, 80, 90, 100 ,110, 120]
    mean_speed = [1, 2, 3]
    values=['prob_path', 'avg_node_degree', 'avg_up_entropy', 'avg_down_entropy']
    for value in values:

        if model_name == "ManhattanGrid":
            surf_prob_path = metric_df.pivot(index="range",columns=["turn_prob","node_speed"], values = value)
        else:
            surf_prob_path = metric_df.pivot(index="range",columns=["num_nodes", "node_speed"], values = value)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X = np.arange(30,130,10)
        Y = np.arange(1,4,1)
        X,Y = np.meshgrid(X,Y)
        if model_name == "ManhattanGrid":
            for prob in turn_prob:
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                Z = surf_prob_path[prob].to_numpy()
                surf = ax.plot_surface(X, Y, np.transpose(Z), cmap=cm.coolwarm, linewidth=0, antialiased=False,rstride=1, cstride=1)
                ax.set_xlabel("range", fontsize=15, rotation=60)
                ax.set_ylabel("node_speed", fontsize=15, rotation=60)
                ax.set_zlabel(value, fontsize=15, rotation=60)
                filename = model_name+ "_turn_prob_"+ str(prob) +"_"+ value+ "_3D_surface_plot" + ".png"
                print(filename)
                plt.savefig(filename)
                plt.close()
            
        else:
            #Critical parameter: rstride and cstride to plot smaller plot, save memory/ must include!!!
            Z = surf_prob_path[100].to_numpy()
            surf = ax.plot_surface(X, Y, np.transpose(Z), cmap=cm.coolwarm, linewidth=0, antialiased=False,rstride=1, cstride=1)
            ax.set_xlabel("range", fontsize=15, rotation=60)
            ax.set_ylabel("node_speed", fontsize=15, rotation=60)
            ax.set_zlabel(value, fontsize=15, rotation=60)
            filename = model_name+"_" + value + "_3D_surface_plot"
            plt.savefig(filename)
            plt.close()
            

csv_path = sys.argv[1]
model_name = sys.argv[2]
interval = [2,3]
#csv_path = "ManhattanGridScenario1_CSV"
# model_name = "ManhattanGrid"
# interval = [30, 50]
metric_plot(csv_path,model_name,interval)

"""
#surface plot
prob_path = metric_df.pivot(index="range",columns=["num_nodes", "node_speed"], values='prob_path')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(30,81,10)
Y =np.arange(1,3.5,1)
X,Y = np.meshgrid(X,Y)
Z=prob_path[3].to_numpy()


surf = ax.plot_surface(X, Y, np.transpose(Z), cmap=cm.coolwarm, linewidth=0, antialiased=False,rstride=1, cstride=1)
plt.savefig("3D_surface_plot")
"""
