import numpy as np

class benchmark:
    def __init__(self):
        self.object_height = 77.75
        self.list_min = []
        self.list_max = []
        self.list_moy = []
        self.list_of_distance = []

    def data_statistics(self, data):
        for key in data:
            print(key)
            try:
                self.list_min.append(np.min(data[key]))
                self.list_max.append(np.max(data[key]))
                self.list_moy.append(np.mean(data[key]))
                self.list_of_distance.append(np.mean(data[key])-self.object_height)
                print("[INFO] Statistical lists filled.")
            except:
                print("[INFO] No minimum found.")

def file_to_dict(data):
    # Initializing the dictionary
    for k in benchmark_height:
        if k not in data:
            data[k] = []

    last_call = '0'
    for line in lines:
        if line[0:2] in benchmark_height:
            print(line,"added as a key to the dictionary.")
            last_call = line[0:2]
        if line[0:2] not in benchmark_height and last_call != '0':
            print("Data added to the dictionary")
            data[last_call].append(float("{:.2f}".format(float(line[0:6])*100)))
    return data

def auto_bench():
    return 0

if __name__ == '__main__':
    print("Start benchmark's data processing")

    benchmark_height = ['70','65','60','55','50','45','40','35','30','25','20']

    # Opening the file and cleaning the data
    file_pose_height = open("poses_height.txt")
    lines = file_pose_height.read().splitlines()
    lines = [ele for ele in lines if ele != '']

    # Creating a dictionary from the data
    data = {}
    data['70'] = [None,None,None,None,None,None,None,None,None,None]
    data['65'] = [77.47,80.58,77.65,80.12,77.35,80.14,77.23,77.32,77.98,80.31]
    data['60'] = [66.41,77.34,76.87,78.39,78.02,78.05,77.92,78.63,78.47,80.15]
    data = file_to_dict(data)
    data['15'] = [None,None,None,None,None,None,None,None,None,None]
