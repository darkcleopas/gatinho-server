from keras.models import model_from_json

def load_model(model_path: str):

    json_file = open(model_path + 'model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)

    model.load_weights(model_path + "model.h5")

    return model