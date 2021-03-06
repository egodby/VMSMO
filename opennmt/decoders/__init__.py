"""Module defining decoders."""

from opennmt.decoders.rnn_decoder import RNNDecoder
from opennmt.decoders.rnn_decoder import AttentionalRNNDecoder
from opennmt.decoders.rnn_decoder import MultiAttentionalRNNDecoder
from opennmt.decoders.rnn_decoder import RNMTPlusDecoder

from opennmt.decoders.self_attention_decoder import SelfAttentionDecoder
from opennmt.decoders.self_attention_decoder import SelfAttentionDecoderV2

from opennmt.decoders.pointer_generator_helper import PointerAttentionalRNNDecoder
from opennmt.decoders.pointer_generator_helper import PointerRNNDecoder
