stopWords = set(stopwords.words('english'))


# creating a function to encapsulate preprocessing, to mkae it easy to replicate on  submission data
def processing(df):
    # lowering and removing punctuation
    df['processed'] = df['text'].apply(lambda x: re.sub(r'[^\w\s]', '', x.lower()))

    # numerical feature engineering
    # total length of sentence
    df['length'] = df['processed'].apply(lambda x: len(x))
    # get number of words
    df['words'] = df['processed'].apply(lambda x: len(x.split(' ')))
    df['words_not_stopword'] = df['processed'].apply(lambda x: len([t for t in x.split(' ') if t not in stopWords]))
    # get the average word length
    df['avg_word_length'] = df['processed'].apply(
        lambda x: np.mean([len(t) for t in x.split(' ') if t not in stopWords]) if len(
            [len(t) for t in x.split(' ') if t not in stopWords]) > 0 else 0)
    # get the average word length
    df['commas'] = df['text'].apply(lambda x: x.count(','))

    return (df)


df = processing(df)
