# import requirements needed
from flask import Flask, render_template, request
from utils import get_base_url
from aitextgen import aitextgen
# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 4333
base_url = get_base_url(port)


def genre_text_generation(genre):
    if genre == 'SciFi':
        return 'scifi_model/'
    if genre == 'Horror':
        return 'horror_model/'
    if genre == 'FairyTales':
        return 'fairytale_model/'
    if genre == 'BedTime':
        return 'bedtime_model/'
    if genre == 'RussianStories':
        return 'model/superhero_files'

# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

# set up the routes and logic for the webserver
@app.route(f'{base_url}')
def home():
    return render_template('index.html')

# define additional routes here
# for example:
@app.route(f'{base_url}/model.html', methods=["GET", "POST"])
def model():
    if request.method == "POST":
        prompt = request.form.get("text")
        genre=request.form.get("options")
        story_genre = genre_text_generation(genre)
        ai = aitextgen(model_folder = story_genre, to_gpu=False)

        if prompt is not None:
            generated = ai.generate(
                n=1,
                batch_size=10,
                prompt=str(prompt),
                max_length=100,
                temperature=1.0,
                return_as_list=True
            )

            text = generated[0]
            return render_template('model.html', output=text)
    return render_template('model.html')

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'cocalc11.ai-camp.dev'
    print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
    app.run(host = '0.0.0.0', port=port, debug=True)


    