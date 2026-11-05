# Task 3a: Variables and Data Types (AI-related example)
model_name = "SpamDetector"      # str
accuracy = 92.5                  # float
epochs = 20                      # int
is_trained = True                # bool
features = ["length", "links", "keywords"]   # list
config = {"learning_rate": 0.01, "batch_size": 32}  # dict
labels = ("spam", "not spam")    # tuple

print("Model name :", model_name, "->", type(model_name))
print("Accuracy   :", accuracy, "->", type(accuracy))
print("Epochs     :", epochs, "->", type(epochs))
print("Trained?   :", is_trained, "->", type(is_trained))
print("Features   :", features, "->", type(features))
print("Config     :", config, "->", type(config))
print("Labels     :", labels, "->", type(labels))
