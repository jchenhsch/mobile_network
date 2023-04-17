# Mobile ad hoc network simulations
Ad hoc mobile network analysis on mobility models 

## Project overview
This project aims to explore approaches to characterize device mobility in a MANET with the eventual goal of using these characterizations to improve routing. We explore different mobility models and propose metrics to characterize how mobility varies in these models. By identifying key metrics that characterize mobility, we get closer to being able to map any arbitrary device movement to a common feature space, allowing routing decisions to be made on that feature space rather than requiring individualized approaches to routing for different kinds of mobility.


## Implementation Guide & Dependency requirement

  ### To run this project
    git clone git@github.com:jchenhsch/mask_classification.git 
    ./gen_file_new.sh

  ### Dependency requirement
  
    To install Bonnmotion(mobility model scenarios generation tool): 
    https://sys.cs.uos.de/bonnmotion/
    pip3 install -r requirements.txt 
    
## Script Description
gen_params.sh/gen_params_manhattan.sh/gen_params_gauss.sh: <br/>
create the parameters file for models that we are running simulation on

parse_output.py: <br/> 
    take in raw traces data and generate usable dataframes for metric calculation<br/> 
 <br/> 
calc_metric.py: <br/> 
      calculate the metrics by taking averages of traces dataframes of each time step and general a result dataframe containing metric data.<br/> 
<br/> 
  plot_metric.py: <br/> 
    plot the metric dataframe and generate surface plot for each set of parameters in each model.r<br/> 
<br/> 
  gen_files_new.sh:<br/> 
    1. main console file that generates the traces, calls the python scripts to generate the metric dataframes and plot the metric dataframes.<br/> 
    2. generate directories for traces, plot outputs and traces dataframes. <br/> 
    3. output the final result by moving the relevant files to the corresponding directory. <br/> 
    
## Authors
Jiaxuan Chen

## Version history
1.0 --> initial release 

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License
