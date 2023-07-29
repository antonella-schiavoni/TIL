import xgboost as xgb

def stock_boost(X_train, y_train, X_test):
    # Convert data into d matrix which is what xgboost library takes in.
    # We have categorical features (sector) in our db so we need to use enable_categorical flag
    d_train = xgb.DMatrix(X_train, label=y_train, enable_categorical=True)

    # Remember to check no leaking data here
    d_test = xgb.DMatrix(X_test, enable_categorical=True)

    # Instantiate xgboost model
    stock_boost_model = xgb.train({"objective": "binary:logistic",
                                   "tree_method": "exact", # As data is not that lage, we want an exact method. This has a tradeoff of performance.
                                   "max_cat_to_onehot":11, # How many sectors we have
                                    "eta": .32, # Learning rate of the algorithm
                                    "max_depth": 7}, d_train) 

    # Let's obtain predictions in the test set
    raw_predictions = stock_boost_model.predict(d_test)

    # Binary LR generates predictions between 0 and 1 to represent probabilities
    # We need to determine a probability cut off to determine which values are 1 and which values are 0
    # I will start with 0.5 and tune that parameter
    probability_cutoff = 0.44
    threshold_predictions = [1 if value > probability_cutoff else 0 for value in raw_predictions]

    X_test['buy_signal'] = threshold_predictions
    y_test_predictions = X_test[['buy_signal']].copy()
    X_test.drop('buy_signal', axis=1, inplace=True)
    
    return y_test_predictions



