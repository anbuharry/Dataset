import argparse
from utils.generate_dataset import Generate_Dataset
from joblib import Parallel, delayed
import configparser
import multiprocessing as mp

config = configparser.ConfigParser()
config.read('config.ini')
num_cam = config['DEFAULT']['num_cam']
print(num_cam)
# print(con)

parser = argparse.ArgumentParser(
    "Pytorch code for unsupervised video summarization with REINFORCE")
# Dataset options

parser.add_argument('--input', '--split', type=str, help="input video")
parser.add_argument('--output', type=str, default='', help="out data")

args = parser.parse_args()


def call_vsumm(input_path, output_file):
    gen = Generate_Dataset(input_path, output_file)

    process = mp.Process(target=gen._generator(input_path, output_file))


    # jobs.append(process)
if __name__ == "__main__":
    gen = Generate_Dataset(args.input, args.output)
    # gen._generate_dataset()
    # gen.h5_file.close()
    jobs = []
    for i in range(int(num_cam)):
        # import pdb;pdb.set_trace()
        file_path = "/" + "C" + str(i)
        print(file_path)
        input_path = args.input + file_path
        output_file = "./dataset" + "/" + file_path + ".h5"
        # gen = Generate_Dataset(input_path, output_file)

        process = mp.Process(target=call_vsumm(input_path, output_file))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

   
