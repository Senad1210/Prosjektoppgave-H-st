from flask import Flask, render_template, request, jsonify

# Importerer mysql.connector for å koble til mariadb/sql databasen
import mysql.connector

# lager selve flask applikasjonen
app = Flask(__name__)



# DATabase konfihurasjon
# lager en tilkobling til databasen
conn = mysql.connector.connect(
    host="localhost",              # databsen kjører på samme maskin
    user="flaskuser",              # sql brukern du har lagd
    password="strongpassword",     # passord du har lagd
    database="chitchat",           # navn på database
    auth_plugin="mysql_native_password"  # dette er viktig for å unngå auth feil
)



# ROutes til nettsider/api endpoints

# KJØres når noen går inn i /main
@app.route("/main")
def home():
    # henter render html filen fra templates>index
    return render_template("index.html")









# Denne ruten henter alle brukere fra databasen
@app.route("/users", methods=["GET"])
def users():
    # det lager en database peker som returnerer data i form av dictionary
    cur = conn.cursor(dictionary=True)
    # kjør sql spøring fpr å hente alle rader fra user tabels
    cur.execute("SELECT * FROM users")
    # hetner alle resulatater
    data = cur.fetchall()
    cur.close()
    # returner data som json til nettlesr
    return jsonify(data)






# koden her brukes for å legge til en ny bruker i databasen
@app.route("/users", methods=["POST"])
def add_user():
    # den henter json data som sendes in i post-forespørselen
    data = request.json
    cur = conn.cursor()

    # sql sprøing for å sette inn en ny bruker i users-tabellen
    cur.execute(
        "INSERT INTO users (userid, username, email, password) VALUES (%s, %s, %s, %s)",
        (data["userid"], data["username"], data["email"], data["password"])
    )

    # lagrer endringer i database
    conn.commit()
    cur.close()
    # returner bekreftelse
    return "User added"



# STarter server

# koden kjører bare hvis filen er direkte
if __name__ == "__main__":
    # starter flask server på alle nettverksgrensesnitt på port 12100 i debug modus
    app.run(host="0.0.0.0", port=12100, debug=True)
