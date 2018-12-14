import sys

sys.path.append("../")

from wrangle_data import DataWrangler
from build_model import BuildAndTrainModel
from predict_difference import PredictDifference

if __name__ == "__main__":

    input_train_text_file = "../data/training_data/rotten.txt"

    mode = "train"

    if mode == "train":
        print("\n\n~~~~~~~~~~~~~~~~~~Starting the data wrangling process in {} mode~~~~~~~~~~~~~~~~~~\n\n".format(mode))
        DataWrangler(input_train_text_file, mode="train")

        print("\n\n~~~~~~~~~~~~~~~~~~Building and training the model~~~~~~~~~~~~~~~~~~\n\n""")
        BuildAndTrainModel()

        #print("\n\n~~~~~~~~~~~~~~~~~~Predicting on {}~~~~~~~~~~~~~~~~~~\n\n".format(input_test_text_file))
        #DataWrangler(input_test_text_file, mode="test")
        #PredictDifference()

    elif mode == "test":
        print("\n\n~~~~~~~~~~~~~~~~~~Starting the data wrangling process in {} mode~~~~~~~~~~~~~~~~~~\n\n".format(mode))
        #DataWrangler(input_test_text_file, mode="test")

        #print("\n\n~~~~~~~~~~~~~~~~~~Predicting on {}~~~~~~~~~~~~~~~~~~\n\n".format(input_test_text_file))
        #PredictDifference()

    else:
        print("\n\nInvalid mode. Options are \"train\" and \"test\".\n\n")

    print("\n\n~~~~~~~~~~~~~~~~~~All processes completed~~~~~~~~~~~~~~~~~~\n\n")