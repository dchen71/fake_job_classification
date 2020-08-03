from spacy.lang.en import English
nlp = English()

def tokenizer(corpus, model = nlp):
  """
  Tokenizer to keep alpha numeric, remove stop words, lemmatize text , remove url, remove emails, remove numbers
  """
  bag_of_words = nlp(corpus)

  parsed_words = [i.lemma_ for i in bag_of_words if not i.is_stop and i.is_alpha and not i.like_url and not i.like_num and not i.like_email]

  return(parsed_words)