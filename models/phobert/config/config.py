import os

# PRETRAINED MODEL
CHECKPOINT = "vinai/phobert-base"

# DATA PATH
TRAIN_PATH = ""
VALIDATION_PATH = ""
TEST_PATH = ""

# DATALOADER
LABEL = "sentiments"
NUM_WORKERS = 0

# TRAINER
EPOCHS = 200
VAL_EACH_EPOCH = 2
NUM_CLASSES = 3
BATCH_SIZE = 64
THRESHOLD=0.5
LEARNING_RATE = 1e-4
ACCELERATOR = "gpu"

# MODEL
SEED = 42
MODEL = "FeedForward-base"   # "FeedForward"/"LSTM" + '-' +  'base'/'large'
DROP_OUT = 0.1

# TENSORBOARD LOG
TENSORBOARD = {
    "DIR": "WeightLoss_LOG",
    "NAME": f"{MODEL}_DROP{DROP_OUT}_LABEL{LABEL}_LR{LEARNING_RATE}",
    "VERSION": "0",
}

# CHECKPOINT
CHECKPOINT_DIR = os.path.join(TENSORBOARD["DIR"], TENSORBOARD["NAME"], TENSORBOARD["VERSION"], "CKPT")

# EVALUATE
TEST_CKPT_PATH = None

# KEEP_TRAINING PATH
CONTINUE_TRAINING = None