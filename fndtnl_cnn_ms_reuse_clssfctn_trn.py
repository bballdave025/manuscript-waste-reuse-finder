#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# @file: fndtnl_cnn_ms_reuse_clssfctn.py
# @author: Keith PRISBREY        for FamilySearch        principal author
# @author: David BLACK           GH @bballdave025        playing around
#                                                        rewriting for 
#                                                        learning
# @since: 2024-01-25 (for Dave)
#
# (Dave's notes)
#
#  It seems to me that we're using a canned CNN. I dont' know if it is
#  piggybacking off of previous shape recognition, or if it is building
#  up the recognition from scratch. Either way, it will be fun to get
#  results.
#
##############################################################################


##--------------------
## IMPORT STATEMENTS
##--------------------

import sys, os, time, glob, pickle

from PIL import Image

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.utils.class_weight import compute_class_weight
from sklearn.utils import shuffle

import tensorflow as tf
import keras
from keras import backend as K

from keras_cv.models import(ResNetBackbone, ImageClassifier,)



##---------------------------
## USEFUL RUNTIME VARIABLES
##---------------------------

##-- Verbosity
do_show_progress = True
do_show_lotta_details = False

do_debug_grayscale = True


##-- CHANGE THIS OR HAVE DATA OVERWRITTEN --##
run_id_string = "ms_reuse_2024-01-28_001"



## Find the number of GPUs
n_gpus = len(tf.config.experimental.list_physical_devices('GPU'))

if do_show_progress:
  print("Number of GPUs: ", str(n_gpus))
##endof:  if do_show_progress


##------------------------------------------
## Define filesystem paths for the dataset
#
# DWB's Windows Setup and the external drive
base_dir_path = "D:/Datasets_and_Models/P2_MSS/DatasetBinding"

if do_show_progress:
  print("base_dir_path: ", base_dir_path)
##endof:  if do_show_progress


## Define path where models will be saved
model_save_path = base_dir_path

if do_show_progress:
  print("model_save_path: ", model_save_path)
##endof:  if do_show_progress


## Define paths for each of the classes

#-----------
#   POSITIVE

positive_class_base_dir = base_dir_path

if do_show_progress:
  print("positive_class_base_dir:\n", positive_class_base_dir)
##endof:  if do_show_progress

positive_class_training_dir = \
    positive_class_base_dir + "/" + "dataset_3ch_train" + "/" + \
    "dataset_3ch_yes_train"

# positive_class_training_dir = os.path.join(positive_class_base_dir,
                                           # "dataset_3ch_train", 
                                           # "dataset_3ch_yes_train"
                              # )
# positive_class_training_dir = \
    # positive_class_training_dir.replace(r"\\", "/")

if do_show_progress:
  print("positive_class_training_dir:\n", positive_class_training_dir)
##endof:  if do_show_progress

#-----------
#   NEGATIVE
negative_class_base_dir = base_dir_path

if do_show_progress:
  print("negative_class_base_dir:\n", negative_class_base_dir)
##endof:  if do_show_progress

negative_class_training_dir = \
    negative_class_base_dir + "/" + "dataset_3ch_train" + "/" + \
    "dataset_3ch_not_train"

# negative_class_training_dir = os.path.join(negative_class_base_dir,
                                           # "dataset_3ch_train", 
                                           # "dataset_3ch_not_train"
                              # )

# negative_class_training_dir = \
    # negative_class_training_dir.replace(r"\\", r"/")

if do_show_progress:
  print("negative_class_training_dir:\n", negative_class_training_dir)
##endof:  if do_show_progress


print()
print()



##-------------------------------------------
## FETCH training images for POSITIVE CLASS
##   we'll call this the "2-class",
##   "yes_reused", or "pos"
#
files_for_yes_reused = glob.glob(positive_class_training_dir + "/*.jpg") + \
                       glob.glob(positive_class_training_dir + "/*.png")

if do_show_lotta_details:
  print("files_for_yes_reused:\n", str(files_for_yes_reused))
##endof:  if do_show_progress


##-------------------------------------------
## FETCH training images for NEGATIVE CLASS
##   we'll call this the "1-class",
##   "not_reused", or "neg"
#

files_for_not_reused = glob.glob(negative_class_training_dir + "/*.jpg") + \
                       glob.glob(negative_class_training_dir + "/*.png")

if do_show_lotta_details:
  print("files_for_not_reused:\n", str(files_for_not_reused))
##endof:  if do_show_progress


##----------------------------
## INPUT & TRUTH
##   for the positive class
#
X2 = []
y2 = []
fnames2 = []

for this_pos_img_idx in range(len(files_for_yes_reused)):
  y2.append(2) # Following Keith, '2' is for positive
  
  this_image = files_for_yes_reused[this_pos_img_idx]
  
  if do_debug_grayscale:
    print("\n\n# GRAYSCALE DEBUG FOR POS #")
    print("this_image:", this_image)
  ##endof:  if do_show_progress
  
  original_img = Image.open(this_image)
  
  if do_debug_grayscale:
    print("\n", this_image, 
          " ; original_img.mode:", str(original_img.mode))
  ##endof:  if do_show_progress
  
  do_skip_image = True # Guilty until proven innocent
  
  if original_img.mode != "RGB":
    try:
      #  <convert to 3-channel RGB> 
      #+ Still have 9 'L' (grayscale), 1 'P' (palletized?), 
      #+ and 1 '1' (binary) ; 1706542776_2024-01-29T083936 DWB
      if do_debug_grayscale:
        print("\nAttempting to convert image to RGB (3-channel)")
      ##endof:  if do_debug_grayscale
      original_img.convert('RGB')
      do_skip_image = False
    ##endof:  try <convert to 3-channel RGB>
    except Exception as e:
      print(str(e))
      print(str(e), file=sys.stderr)
      print("That was an exception while attempting", file=sys.stderr)
      print("conversion of", file=sys.stderr)
      print("  ", this_image, file=sys.stderr)
      print("to RGB (3-channel). Here's some info.", file=sys.stderr)
      print(str(e), file=sys.stderr)
      print("This image will not be included in training/eval/testing.",
            file=sys.stderr)
      #do_skip_image = True
    ##endof:  catch <convert to 3-channel RGB>
    finally:
      if do_debug_grayscale:
        print("We've tried to make\n", this_image)
        print("3-channel RGB.")
        print("Result:\n", this_image, 
              " ; original_img.mode:", str(original_img.mode))
        print("do_skip_image: ", str(do_skip_image))
      ##endof:  if do_debug_grayscale
    ##endof:  try/catch/finally <convert to 3-channel RGB>
  ##endof:  if original_img.mode is not "RGB"
  
  if do_skip_image:
    continue
  ##endof:  if do_skip_image
  
  resized_sqr_img = original_img.resize( (128, 128),
                                         resample=Image.BILINEAR
                    ) # So much for high-res images, eh?
  np_array_of_img = np.array(resized_sqr_img)
  
  if do_debug_grayscale:
    print("\n", this_image, 
          " ; np_array_of_img.size:", str(np_array_of_img.size))
    print("\n", this_image, 
          " ; np_array_of_img.shape:", str(np_array_of_img.shape))
  ##endof:  if do_show_progress
  
  X1.append(np_array_of_img)
  
  if do_show_lotta_details:
    print("\n\nProgress for positive class images:")
    print("Input array received and added for:\n",
          str(this_image)
    )
    print("\nlen(X1): ", len(X2), 
          "\nlen(y1): ", len(y2)
    )
  ##endof:  if do_show_lotta_details
  
##endof:  for this_pos_img_idx in range(len(files_for_yes_reused))

print("\n\nFor the positive class,")
print("\nlen(X2):  ", len(X2), 
      "\nlen(y2):  ", len(y2)
 
)


print()



##----------------------------
## INPUT & TRUTH
##   for the negative class
#
X1 = []
y1 = []
fnames1 = []

for this_neg_img_idx in range(len(files_for_not_reused)):
  y1.append(1) # Following Keith, '1' is for negatives
  
  this_image = files_for_not_reused[this_neg_img_idx]
  
  if do_debug_grayscale:
    print("\n\n# GRAYSCALE DEBUG FOR NEG #")
    print("this_image:", this_image)
  ##endof:  if do_show_progress
  
  original_img = Image.open(files_for_not_reused[this_neg_img_idx])
  
  if do_debug_grayscale:
    print("\n", this_image, 
          " ; original_img.mode:", str(original_img.mode))
  ##endof:  if do_show_progress
  
  do_skip_image = True # Guilty until proven innocent
  
  if original_img.mode != "RGB":
    try:
      #  <convert to 3-channel RGB> 
      #+ Still have 9 'L' (grayscale), 1 'P' (palletized?), 
      #+ and 1 '1' (binary) ; 1706542776_2024-01-29T083936 DWB
      if do_debug_grayscale:
        print("\nAttempting to convert image to RGB (3-channel)")
      ##endof:  if do_debug_grayscale
      original_img.convert("RGB")
      do_skip_image = False
    ##endof:  try <convert to 3-channel RGB>
    except Exception as e:
      print(str(e))
      print(str(e), file=sys.stderr)
      print("That was an exception while attempting", file=sys.stderr)
      print("conversion of", file=sys.stderr)
      print("  ", this_image, file=sys.stderr)
      print("to RGB (3-channel). Here's some info.", file=sys.stderr)
      print(str(e), file=sys.stderr)
      print("This image will not be included in training/eval/testing.",
            file=sys.stderr)
      do_skip_image = True
    ##endof:  catch <convert to 3-channel RGB>
    finally:
      if do_debug_grayscale:
        print("We've tried to make\n", this_image)
        print("3-channel RGB.")
        print("Result:\n", this_image, 
              " ; original_img.mode:", str(original_img.mode))
        print("do_skip_image: ", str(do_skip_image))
      ##endof:  if do_debug_grayscale
    ##endof:  try/catch/finally <convert to 3-channel RGB>
  ##endof:  if original_img.mode is not "RGB"
  
  if do_skip_image:
    continue
  ##endof:  if do_skip_image
  
  resized_sqr_img = original_img.resize( (128, 128),
                                         resample=Image.BILINEAR
                    ) # So much for high-res images, eh?
  np_array_of_img = np.array(resized_sqr_img)
  
  if do_debug_grayscale:
    print("\n", this_image, 
          " ; np_array_of_img.size:", str(np_array_of_img.size))
    print("\n", this_image, 
          " ; np_array_of_img.shape:", str(np_array_of_img.shape))
  ##endof:  if do_show_progress
  
  X1.append(np_array_of_img)
  
  if do_show_lotta_details:
    print("\n\nProgress for negative class images:")
    print("Input array received and added for:\n",
          str(this_image)
    )
    print("\nlen(X1): ", len(X2), 
          "\nlen(y1): ", len(y2)
    )
  ##endof:  if do_show_lotta_details
  
##endof:  for this_neg_img_idx in range(len(files_for_not_reused))

print("\n\nFor the negative class,")
print("\nlen(X1): ", len(X1), 
      "\nlen(y1): ", len(y1)
)


print()



##---------------------------------------------------------
## COMBINE NEGs and POSs FOR TRAINING
##
##?????????????????????????????????????????????????????????
##   Why are we not shuffling in some way?
#
#    ref for shuffling arrays in unison
#    https://stackoverflow.com/questions/4601373
#
#    NON-OPTIMAL
## def shuffle_in_unison(a, b):
#  # assert len(a) == len(b)
#  # shuffled_a = numpy.empty(a.shape, dtype=a.dtype)
#  # shuffled_b = numpy.empty(b.shape, dtype=b.dtype)
#  # permutation = numpy.random.permutation(len(a))
#  # for old_index, new_index in enumerate(permutation):
#    # shuffled_a[new_index] = a[old_index]
#    # shuffled_b[new_index] = b[old_index]
#  # return shuffled_a, shuffled_b
#
#   For example:
#
#  # >>> a = numpy.asarray([[1, 1], [2, 2], [3, 3]])
#  # >>> b = numpy.asarray([1, 2, 3])
#  # >>> shuffle_in_unison(a, b)
#  # (array([[2, 2],
#          # [1, 1],
#          # [3, 3]]), array([2, 1, 3]))
#
# > clunky, inefficient, and slow, and it requires 
# > making a copy of the arrays ...
# > I'd rather shuffle them in-place ...
# >
# > Faster execution and lower memory usage are my 
# > primary goals, but elegant code would be nice, too.
#
#  OP'S SELF-NAMED 'SCARY' ANSWER - which most people
#  don't think is so scary
#
## def shuffle_in_unison_scary(a, b):
#    # rng_state = numpy.random.get_state()
#    # numpy.random.shuffle(a)
#    # numpy.random.set_state(rng_state)
#    # numpy.random.shuffle(b)
#
# That's actually the first thought I had - just use the
# same random seed to shuffle one after the other. -DWB
#
#
# Answer 1 (faster, does create copies)
#
## def unison_shuffled_copies(a, b):
#    # assert len(a) == len(b)
#    # p = numpy.random.permutation(len(a))
#    # return a[p], b[p]

#
#
# Answer sklearn (faster, does create copies)
#
# # X = np.array([[1., 0.], [2., 1.], [0., 0.]])
# # y = np.array([0, 1, 2])
# # from sklearn.utils import shuffle
# # X, y = shuffle(X, y, random_state=0)
#
# I like the readability of this one
#
#
# ##endof:  shuffling discussion

X = X1 + X2
y = y1 + y2
print("\n\nFor the combined set,")
print("\nlen(X): ", len(X), 
      "\nlen(y): ", len(y)
)

print()
print()


##-----------------------------
## SHUFFLE THE TRAINING DATA
##   (maybe)
#

#  Choose:
#+   One of the shuffling methods below
#+   Both of the shuffling methods below
#+   Neither of the shuffling methods below
#  I'm going to start with _just_ the in-place
#+ shuffle, but we'll see how things end up
do_in_place_shuf = False
do_sklearn_shuf  = False

if do_in_place_shuf:
  ## Try 1 : same seed
  rng_state = np.random.get_state()
  X_shuff = np.asarray(X)
  np.random.shuffle(X_shuff)
  np.random.set_state(rng_state)
  y_shuff = np.asarray(y)
  np.random.shuffle(y_shuff)
  np.random.set_state(rng_state)
  
##endof:  if do_in_place_shuf

if do_sklearn_shuf:
  ## Try 2 : sklearn
  X_shuff, y_shuff = shuffle(X, y, random_state=0)
  
  X_shuff = X
  y_shuff = y
##endof:  if do_sklearn_shuf

if do_debug_shuf:

##endof:  if do_debug_shuf


##--------------------------------------------------
## COMPUTATION OF THE CLASS WEIGHTS
##   What does this mean? Does it have to do with
##   the number of examples in each class? with
##   the fact that we care about one class more
##   than another? What?
#
class_weights = compute_class_weight(class_weight='balanced',
                                     classes=np.unique(y_shuff), 
                                     y=y_shuff
                )

class_weights = dict(enumerate(class_weights))


##---------------------------------------------
## PREPARE DATA STRUCTURES FOR TRAINING
##   Transform (list) X to (np.array) X_arr    (X1 for Keith)
##   (One-hot) Encode y and get it to y_ready  (y1 for Keith)
#
X_arr = np.array(X_shuff)

if do_debug_grayscale:
  print("\n# GRAYSCALE DEBUG #")
  print("np.shape(X_arr) = ", np.shape(X_arr))
##endof:  if do_show_progress

enc = OneHotEncoder(sparse_output=False,
                    handle_unknown='ignore'
      )
a = np.array(y_shuff).reshape(-1, 1)
enc.fit(a)
y_ready = enc.transform(a)

if do_debug_shuf:
  print("\na: ", "\n", str(a))
  print("y_ready: ", str(y_ready))
##endof:  if do_show_progress


##--------------------------------------------------------------------------
## Using keras_cv stuff
##   rem.    from keras_cv.models import(ResNetBackbone, ImageClassifier,)
#
b = enc.categories_
n_classes = b[0].shape[0]

if do_debug_shuf:
  print("\nb: ", "\n", str(b))
  print("n_classes: ", str(n_classes))
##endof:  if do_show_progress

my_backbone = ResNetBackbone.from_preset('resnet50_imagenet',)


#####################################
## DEFINING AND COMPILING THE MODEL
#
model = ImageClassifier(backbone=my_backbone, 
                        num_classes=n_classes
)
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy']
)


######################################
## HERE, WE VIEW THE INPUT/SAMPLE, X
##   (at least a bit)
##   I'm interested to see it.
##   I believe this is
##   interactive.
#
min_sample_id = 0
max_sample_id = len(X_arr) # 50
max_for_range = max_sample_id + 1
sample_step_size = 10
for this_sample in range(min_sample_id,
                         max_for_range,
                         sample_step_size
                   ):
  plt.imshow(X[this_sample])
  plt.grid('off') # It's a scan
  plt.axis('off') # It's a scan
  plt.show()
  print()
  print(y[this_sample])
  print(y_ready[this_sample])

##endof:  for this_sample in range(<params>)

##.......................................
## Get the target and output compatible
##   What does this mean?
#
y_try = model.predict(X1[4:6])

######################################
##                                  ##
##    T R A I N I N G - TRAINING    ##
##                                  ##
######################################

print("\n\n STARTING TRAINING\n")


##------------------
## HYPERPARAMETERS
##   Changeable
#
n_epochs = 30   # Have/will we vary this?
my_batch_size = 32 # Have/will we vary this?

# Where is our learning rate? Auto?

## Let's time this
start = time.time()

## Keep track of how the model progresses (learns)

##===========================##
## HERE IS THE REAL TRAINING ##
##
history = model.fit(X_arr, y_ready,
                    epochs=n_epochs,
                    batch_size=my_batch_size,
                    verbose=2,
                    class_weight=class_weights
          )

## How long did it take?
n_seconds =  time.time() - start
n_minutes = n_seconds / 60
n_hours = n_minutes / 60

print("\n")
print("time_elapsed: ", "%0.1f " % n_seconds, "total seconds;\n",
      "              ", "%0.1f " % n_minutes, "total minutes;\n",
      "              ", "%0.1f " % n_hours,   "total hours;\n")


##-----------------
## SAVE THE MODEL
#
model_save_fname_base = run_id_string
model_save_fname_common = "keras_model_" + \
                          model_save_fname_base
                         

# Actual model (weights/parameters/topography
model_out = os.path.join(model_save_path, 
                         model_save_fname_common)
tf.keras.models.save_model(model, model_out)

# Encoder
encoder_out = os.path.join(model_save_path,
                           model_save_fname_common + ".p")
with open(encoder_out, 'wb') as ofh:
  pickle.dump(enc, ofh)
##endof:  with open(encoder_out, 'wb') as ofh

print("\nmodel and encoder saved")


##---------------------------------
## PLOT HOW THE MODEL LEARNED
##   Also shows the final accuracy
#
plt.figure(1)
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['loss'], label='loss')
plt.title("MS-Reuse-Find Train", fontsize=20)
plt.xlabel("Epoch", fontsize=18)
plt.ylabel("Accuracy & Loss", fontsize=18)
plot.legend(fontsize=14)
plot.show()




##########################################################################
## EXAMPLE OF LOADING & USING THE MODEL (which also requires the encoder)
##   This also includes comparison to
##   truth data, which is available in
##   this case.
#
model_in = os.path.join(model_save_path, 
                        model_save_fname_common)
model_for_prediction = tf.keras.models.load_model(model_in)

encoder_in = os.path.join(model_save_path,
                          model_save_fname_common + ".p")
with open(encoder_in, 'rb') as ifh:
  enc_for_prediction = pickle.load(ifh)
##endof:  with open(encoder_in, 'rb') as ifh


## Just using 10 examples from the training set, right here
start = 0
stop = 10

y_actual = y[start:stop]
y_encoded = model_for_prediction.predict(X1[start:stop])
y_predicted = enc_for_prediction.inverse_transform(y_encoded)


print()
print()
print('predicted/actual')
for my_sample in range(len(y_predicted)):
  print(y_predicted[my_sample][0], "/", y_actual[my_sample])
##endof:  for my_sample in range(len(y_predicted))

print()
print("Exiting.")
print()

sys.exit()

