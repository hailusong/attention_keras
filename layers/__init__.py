# expose everything in attention.py directly
# so the consumer doens't need to do
#     from attention_keras.layers.attention import AttentionLayer
# instead they can do
#     from attention_keras.layers import AttentionLayer
from .attention import *

