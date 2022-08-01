
import sys
  
# setting path
sys.path.append('../src')
  
# importing
impoart src.main 

# Simulate a single cell
run(
    ligand_densities = [.1], 
    kunbind_list = [0.042], 
    endtime=60, 
    plotTimeTraces=True, 
    nLATthreshold=3, 
    early_termination_option=True,
    probabilistic_activation=False,
    )
