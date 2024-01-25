from flask import Flask, render_template, make_response, request
import secrets

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = secrets.token_hex(16)

ANIMALS = ["dog","dragon","goat","horse","monkey","ox","pig","rabbit","rat","rooster","snake","tiger"]

@app.route('/', methods=['GET', 'POST'])
def index():
    animal_random = secrets.choice(ANIMALS)
    image_filename = f"{animal_random}.jpg"
    animal = request.cookies.get('animal')

    if animal == '':
        template_data = {
            'animal': animal_random,
            'image_filename': image_filename,
        }
    elif animal[::-1] == 'msecer':
        image_filename = "no_brute_file.jpg"
        template_data = {
            'animal': "msecer. Alright, here is your flag:",
            'image_filename': image_filename
        }
    else:
        template_data = {
            'animal': animal_random,
            'image_filename': image_filename,
        }
    resp = make_response(render_template('index.html',**template_data))
    resp.set_cookie('animal', animal_random[::-1])
    return resp

if __name__ == '__main__':
    app.run(port=8902, debug=False)
