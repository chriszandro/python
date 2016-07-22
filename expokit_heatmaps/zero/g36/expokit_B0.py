import numpy as np
import list_creator as list_creator
import expokit_heatmap_function as expokit

#Parameter
spec="spec_g36_B0"
gate_start = 4.2
T=293
en = 0.000
bias = 0.00

#Gate End List Preparation 
gate_points_regular_grid = 550 
gate_points_sub_grid = 15 


## Resonances 
large_resonance_plus = [0.695, 2.0, 3.305,4.61,5.95]
large_resonance_minus = [-1.95, -0.61, 0.695, 2.0, 3.305]

gate_end_list =sorted(np.linspace(2.5, 4.0, gate_points_sub_grid).tolist() +  np.linspace(-3, 2.5,gate_points_regular_grid).tolist() + list_creator.resonance_refinement(large_resonance_minus, width=0.12, resolution=13))

## Function Call
k = expokit.create_expokit_heatmap(spec=spec, gate_start=gate_start, T=T, en=en, bias=bias, gate_end_list=gate_end_list) 

