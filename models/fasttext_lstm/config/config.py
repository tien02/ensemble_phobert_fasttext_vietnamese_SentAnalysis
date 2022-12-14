import os

# DATA PATH
TRAIN_PATH = ""
VALIDATION_PATH = ""
TEST_PATH = ""

# DATASET CONFIG
LABEL = "sentiments"
FAST_TEXT_PRETRAINED = ""

# DATALOADERCONFIG
BATCH_SIZE = 128
NUM_WORKERS = 4

# MODEL
LEARNING_RATE = 1e-3
VECTOR_SIZE = 300
DROP_OUT = 0.4
OUT_CHANNELS = 3

# TENSORBOARD LOG
TENSORBOARD = {
    "DIR": "WeightedLoss_LOG",
    "NAME": f"LSTM_FASTTEXT_VEC{VECTOR_SIZE}_DROP{DROP_OUT}_LABEL{LABEL}_LR{LEARNING_RATE}",
    "VERSION": "1",
}

# CHECKPOINT
CHECKPOINT_DIR = os.path.join(TENSORBOARD["DIR"], TENSORBOARD["NAME"], TENSORBOARD["VERSION"], "CKPT")

# TRAINER
ACCELERATOR = "gpu"
NUM_EPOCHS = 300
EVAL_EVERY_EPOCHS = 4

# EVALUATE
TEST_CKPT_PATH = None

# KEEP_TRAINING
CONTINUE_TRAINING = None