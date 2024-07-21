from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# List of image filenames (you can add more)
image_filenames = os.listdir('static/images')

@app.route('/')
def index():
    # Get a random image filename
    random_image = random.choice(image_filenames)
    return render_template('index.html', random_image=random_image)

if __name__ == '__main__':
    app.run(debug=True)
