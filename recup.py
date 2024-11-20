from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def recup():
    return '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>recup</title>
    </head>
    <body>
        <form action="/submit" method="post">
            <label for="name">Nom :</label>
            <input type="text" id="name" name="name" required><br><br>

            <label for="email">Email :</label>
            <input type="email" id="email" name="email" required><br><br>

            <button type="submit">Envoyer</button>
        </form>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def soumettre():
    nom = request.form['name']
    email = request.form['email']

    with open("donnees_recup.txt", "a") as fichier:
        fichier.write(f"Nom: {nom}, Email: {email}\n")

    return f"Merci {nom}, vos données ont été enregistrées !"

if __name__ == '__main__':
    app.run(debug=True)
