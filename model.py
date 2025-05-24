import pickle

class MLModel:
    def __init__(self, model):
        self.model = model

    @classmethod
    def load_model(cls, path):
        with open(path, "rb") as f:
            model = pickle.load(f)
        return cls(model)

    def predict(self, features):
        # Example: model expects list of numeric features
        prediction = self.model.predict([features])[0]
        return "rogue" if prediction == 1 else "safe"
