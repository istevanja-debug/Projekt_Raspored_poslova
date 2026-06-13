from flask import Flask, render_template, request, redirect
from pony.orm import db_session, commit

from entities import Posao


app = Flask(__name__)

@app.route("/test")
@db_session
def test():

    Posao(
        adresa="Pulska 10",
        datum="2026-06-15",
        vrijeme="10:00",
        klima="Daikin",
        radnik="Ivan",
        cijena=1200.0
    )

    commit()

    return "Posao dodan!"


@app.route("/poslovi")
@db_session
def poslovi():

    svi_poslovi = Posao.select()

    return render_template(
        "index.html",
        poslovi=svi_poslovi
    )


@app.route("/dodaj", methods=["GET", "POST"])
@db_session
def dodaj():

    if request.method == "POST":

        Posao(
            adresa=request.form["adresa"],
            datum=request.form["datum"],
            vrijeme=request.form["vrijeme"],
            klima=request.form["klima"],
            radnik=request.form["radnik"],
            cijena=float(request.form["cijena"])
        )

        return redirect("/poslovi")

    return render_template("add_job.html")


@app.route("/obrisi/<int:id>")
@db_session
def obrisi(id):

    posao = Posao.get(id=id)

    if posao:
        posao.delete()

    return redirect("/poslovi")


@app.route("/zavrsi/<int:id>")
@db_session
def zavrsi(id):

    posao = Posao.get(id=id)

    if posao:
        posao.obavljeno = True

    return redirect("/poslovi")


if __name__ == "__main__":
    app.run(debug=True)