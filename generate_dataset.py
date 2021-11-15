import sys
import os
import shutil

if __name__ == "__main__":
	print("Start generating the training dataset")
	data_dir_path = "data"
	copyed_file_name = "demo.jpeg"
	sample_number = 30
	class_names = ["class1","class2"]
	dataset_names = ["train","val","test"]
	dataset_ratios = [0.7,0.2,0.1]
	dataset_numbers = []
	
	for dataset_ratio in dataset_ratios:
		dataset_numbers.append(int(round(dataset_ratio*sample_number)))
	print(dataset_numbers)
	if not os.path.exists(data_dir_path):
		os.mkdir(data_dir_path)
	
	for class_name in class_names:
		class_dir_path = os.path.join(data_dir_path,class_name)
		if not os.path.exists(class_dir_path):
			os.mkdir(class_dir_path)
		for i,dataset_name in enumerate(dataset_names):
			dataset_dir_path = os.path.join(class_dir_path,dataset_name)
			if not os.path.exists(dataset_dir_path):
				os.mkdir(dataset_dir_path)
			for j in range(dataset_numbers[i]):
				new_file_path = os.path.join(dataset_dir_path,str(j)+".jpeg")
				shutil.copy(copyed_file_name,new_file_path)
				#print(new_file_path)
		
	print("Finish the training data generating")
		
