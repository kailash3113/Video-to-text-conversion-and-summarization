from tensorflow import summary
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.corpus import stopwords
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from gtts import gTTS 
import os
import nltk
import pytube
import speech_recognition as sr 
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import moviepy.editor as mp
import os
nltk.download('stopwords')
nltk.download('punkt')