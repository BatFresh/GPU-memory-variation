# GPU-memory-variation
GPU memory variation for the influence of the co-training-inference 
# Environment
Jetson TX2 8GB version
# Dependency
## TensorRT Inference Engine:
jetson-inference  ->  https://github.com/dusty-nv/jetson-inference.git
## GPU Monitoring
jeston-status
## Pytorch
torch==1.7.0
torchvision==0.8.1
# Variation Description
## File Declaration
train.py       		----->       training job wih pytorch framework  
log_gpu.py     		----->       gpu monitoring program  
inference.py   		----->       inference task with TensorRT engine  
/data          		----->       training dataset dir  
-----/class1  
------------/train  
------------/val  
------------/test  
-----/class2  
------------/train  
------------/val  
------------/test  
start_validation.sh	----->	     variation procedure execution script  
generate_dataset.py  
demo.jpg  
## Validation Process 
1. Finish the system setting including installation above dependencies.
2. Run start_validation.sh
3. Get the GPU memory variation from log.txt
