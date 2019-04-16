from flask import Flask, request
import classifier
import index_view

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        weight = request.form.get('weight')
        can_fly = request.form.get('can-fly')
        can_fly = can_fly == 'yes'

        is_mammal = classifier.is_mammal(weight, can_fly)
        animal_type = 'mammal' if is_mammal else 'bird'

        msg = 'The animal is probably {0}!'.format(animal_type)

        return index_view.get_index_view(msg)

    # GET
    return index_view.get_index_view('')

if __name__ == "__main__":
    app.run(debug=True, host="localhost")