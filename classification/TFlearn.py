# import tflearn

# from tflearn 					import *
from tflearn					import DNN
from tflearn.data_utils 		import shuffle, to_categorical
from tflearn.layers.core 		import input_data, dropout, flatten, reshape, fully_connected
from tflearn.layers.conv 		import conv_2d, highway_conv_2d, max_pool_2d, upsample_2d, upscore_layer, residual_bottleneck
from tflearn.layers.merge_ops 	import merge
from tflearn.layers.estimator 	import regression
from tflearn.data_utils 		import shuffle, to_categorical
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation  import ImageAugmentation


