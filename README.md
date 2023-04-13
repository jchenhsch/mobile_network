# mobile_network
Ad hoc mobile network analysis on mobility models 

## Project overview
This project aims to explore approaches to characterize device mobility in a MANET with the eventual goal of using these characterizations to improve routing. We explore different mobility models and propose metrics to characterize how mobility varies in these models. By identifying key metrics that characterize mobility, we get closer to being able to map any arbitrary device movement to a common feature space, allowing routing decisions to be made on that feature space rather than requiring individualized approaches to routing for different kinds of mobility.


## Implementation Guide & Dependency requirement
  ### To run the project
    git clone git@github.com:jchenhsch/mask_classification.git 
    sudo bash gen_file_new.sh
  > do I need to make the script executable and no need to type sudo bash?

  ### Dependency requirement
  
    To install Bonnmotion(mobility model scenarios generation tool): 
    https://sys.cs.uos.de/bonnmotion/
    pip3 install -r requirements.txt 
    
  >In case the requirements not working: pip install pipreqs<br/>
  >pipreqs /path/to/project<br/>
    

## Script Description
