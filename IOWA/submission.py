import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OrdinalEncoder

# Read the data
X_full = pd.read_csv('C:/Users/Harold Uribe Romero/Downloads/PERSONAL/ML/30daysofml/IOWA/train.csv', index_col='Id') 
X_test_full = pd.read_csv('C:/Users/Harold Uribe Romero/Downloads/PERSONAL/ML/30daysofml/IOWA/test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X_full.SalePrice
X_full.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll use only numerical predictors
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,random_state=0)

# Function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Fill in the line below: get names of columns with missing values
cols_with_missing=[col for col in X_train.columns if X_train[col].isnull().any()] # Your code here
#print(cols_with_missing)

# Fill in the lines below: drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

print('_________________________________')
print("MAE (Drop columns with missing values):")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))
print('_________________________________')

print("categorical variables")
# Categorical columns in the training data
object_cols = [col for col in reduced_X_train.columns if reduced_X_train[col].dtype == "object"]

# Columns that can be safely ordinal encoded
good_label_cols = [col for col in object_cols if set(X_valid[col]).issubset(set(reduced_X_train[col]))]
        
# Problematic columns that will be dropped from the dataset
bad_label_cols = list(set(object_cols)-set(good_label_cols))

# Drop categorical columns that will not be encoded
label_X_train = reduced_X_train.drop(bad_label_cols, axis=1)
label_X_valid = reduced_X_valid.drop(bad_label_cols, axis=1)

# Apply ordinal encoder 
Ordinal_Encoder=OrdinalEncoder()
label_X_train[good_label_cols]=Ordinal_Encoder.fit_transform(reduced_X_train[good_label_cols])
label_X_valid[good_label_cols]=Ordinal_Encoder.transform(reduced_X_valid[good_label_cols])


print('_________________________________')
print("MAE from Approach 2 (Ordinal Encoding):") 
print(score_dataset(label_X_train, label_X_valid, y_train, y_valid))
#print(label_X_train)
print('_________________________________')

#Get predictions
model=RandomForestRegressor(n_estimators=100,random_state=0)
model.fit(label_X_train,y_train)
preds_valid=model.predict(label_X_valid)
#print("MAE valid: ",mean_absolute_error(y_valid,preds_valid))

final_X_test=pd.DataFrame(Ordinal_Encoder.transform(X_test))
preds_test=model.predict(label_X_valid)
print('Completed')
#

# output = pd.DataFrame({'Id': X_test.index,'SalePrice': preds_test})
# output.to_csv('submission.csv', index=False)

