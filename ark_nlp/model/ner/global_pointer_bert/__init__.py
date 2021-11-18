from ark_nlp.dataset import GlobalPointerNERDataset as Dataset 
from ark_nlp.dataset import GlobalPointerNERDataset as GlobalPointerBertNERDataset

from ark_nlp.processor.tokenizer.transfomer import SpanTokenizer as Tokenizer
from ark_nlp.processor.tokenizer.transfomer import SpanTokenizer as GlobalPointerBertNERTokenizer

from ark_nlp.nn import BertConfig as GlobalPointerBertConfig
from ark_nlp.nn import BertConfig as ModuleConfig

from ark_nlp.model.ner.global_pointer_bert.global_pointer_bert import GlobalPointerBert
from ark_nlp.model.ner.global_pointer_bert.global_pointer_bert import GlobalPointerBert as Module

from ark_nlp.factory.optimizer import get_default_bert_optimizer as get_default_model_optimizer
from ark_nlp.factory.optimizer import get_default_bert_optimizer as get_default_global_pointer_bert_optimizer

from ark_nlp.model.ner.global_pointer_bert.global_pointer_bert_named_entity_recognition import GlobalPointerNERTask as Task
from ark_nlp.model.ner.global_pointer_bert.global_pointer_bert_named_entity_recognition import GlobalPointerNERTask as GlobalPointerBertNERTask

from ark_nlp.factory.predictor import GlobalPointerNERPredictor as Predictor
from ark_nlp.factory.predictor import GlobalPointerNERPredictor as GlobalPointerBertNERPredictor