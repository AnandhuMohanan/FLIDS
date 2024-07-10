import typing
import pandas as pd
from sklearn import preprocessing
import tensorflow as tf

class DataLoader:
    def __init__(self, train_file_path: str, test_file_path: str):
        self.train_file_path = train_file_path
        self.test_file_path = test_file_path
    
    def load_data(self, file_path: str):
        data = pd.read_csv(file_path)
        data = data.drop(columns=["id", "attack_cat"])
        return data
    
    def preprocess_data(self, data):
        categorical_columns = data.select_dtypes(include=['object']).columns
        numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
        
        for column in categorical_columns:
            le = preprocessing.LabelEncoder()
            data[column] = le.fit_transform(data[column])
        
        min_max_scaler = preprocessing.MinMaxScaler()
        data[numerical_columns] = min_max_scaler.fit_transform(data[numerical_columns])
        return data
    
    def separate_features_and_labels(self, data):
        Y = data.label.to_numpy()
        X = data.drop(columns="label").to_numpy()
        return X, Y
    
    def get_data(self):
        train_data = self.load_data(self.train_file_path)
        test_data = self.load_data(self.test_file_path)

        train_data = self.preprocess_data(train_data)
        test_data = self.preprocess_data(test_data)

        X_train, Y_train = self.separate_features_and_labels(train_data)
        X_test, Y_test = self.separate_features_and_labels(test_data)

        return X_train, Y_train, X_test, Y_test

class ModelLoader:
    @staticmethod
    def get_model(sample_shape: typing.Tuple[int]) -> tf.keras.Model:
        import tensorflow as tf
        inputs = tf.keras.Input(sample_shape)
        x = tf.keras.layers.Dense(100, activation="relu")(inputs)
        x = tf.keras.layers.LayerNormalization()(x)
        x = tf.keras.layers.Dense(50, activation="relu")(x)
        x = tf.keras.layers.LayerNormalization()(x)
        x = tf.keras.layers.Dense(1, activation="sigmoid")(x)
        model = tf.keras.Model(inputs=inputs, outputs=x)
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
            loss="binary_crossentropy",
            metrics=["binary_accuracy"]
        )
        return model
