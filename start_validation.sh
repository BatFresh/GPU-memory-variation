python3 generate_dataset.py
python3 log_gpu.py
python3 training.py -b 32 --epoch 1 -a vgg16 ./data 
sleep 10
python3 inference.py --network vgg16 demo.jpeg
sleep 25
python3 inference.py --network vgg16 demo.jpeg
sleep 45
python3 inference.py --network vgg16 demo.jpeg
