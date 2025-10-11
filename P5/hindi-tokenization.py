from indicnlp.tokenize import indic_tokenize
text = "मैं एमसीसी का छात्र हूँ."

#word tokenization
tokens = list(indic_tokenize.trivial_tokenize(text))
print("word tokens: ",tokens)
