from flask import Flask, render_template, request, redirect, jsonify
from pony.orm import db_session

from entities import Posao


app = Flask(__name__)


@app.route("/api/poslovi")
@db_session
def api_poslovi():

    svi_poslovi = list(Posao.select())

    rezultat = []

    for p in svi_poslovi:
        rezultat.append({
            "id": p.id,
            "adresa": p.adresa,
            "datum": p.datum,
            "vrijeme": p.vrijeme,
            "klima": p.klima,
            "radnik": p.radnik,
            "cijena": p.cijena,
            "obavljeno": p.obavljeno
        })

    return jsonify(rezultat)

@app.route("/api/posao/<int:id>")
@db_session
def api_posao(id):

    p = Posao.get(id=id)

    if not p:
        return jsonify({"error": "Posao ne postoji"}), 404

    return jsonify({
        "id": p.id,
        "adresa": p.adresa,
        "datum": p.datum,
        "vrijeme": p.vrijeme,
        "klima": p.klima,
        "radnik": p.radnik,
        "cijena": p.cijena,
        "obavljeno": p.obavljeno
    })

@app.route("/poslovi")
@db_session
def poslovi():

    svi_poslovi = list(Posao.select())

    broj_poslova = len(svi_poslovi)

    broj_obavljenih = len(
        [p for p in svi_poslovi if p.obavljeno]
    )

    broj_neobavljenih = len(
        [p for p in svi_poslovi if not p.obavljeno]
    )

    ukupna_zarada = sum(
        p.cijena
        for p in svi_poslovi
        if p.obavljeno
    )

    return render_template(
        "index.html",
        poslovi=svi_poslovi,
        broj_poslova=broj_poslova,
        broj_obavljenih=broj_obavljenih,
        broj_neobavljenih=broj_neobavljenih,
        ukupna_zarada=ukupna_zarada
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


@app.route("/uredi/<int:id>", methods=["GET", "POST"])
@db_session
def uredi(id):

    posao = Posao.get(id=id)

    if not posao:
        return "Posao ne postoji"

    if request.method == "POST":

        posao.adresa = request.form["adresa"]
        posao.datum = request.form["datum"]
        posao.vrijeme = request.form["vrijeme"]
        posao.klima = request.form["klima"]
        posao.radnik = request.form["radnik"]
        posao.cijena = float(request.form["cijena"])

        return redirect("/poslovi")

    return render_template(
        "edit_job.html",
        posao=posao
    )

@app.route("/statistika")
@db_session
def statistika():

    poslovi = list(Posao.select())

    svi_poslovi = len(poslovi)

    obavljeni = len(
        [p for p in poslovi if p.obavljeno]
    )

    neobavljeni = len(
        [p for p in poslovi if not p.obavljeno]
    )

    ukupna_zarada = sum(
        p.cijena for p in poslovi
        if p.obavljeno
    )

    return render_template(
        "statistika.html",
        svi_poslovi=svi_poslovi,
        obavljeni=obavljeni,
        neobavljeni=neobavljeni,
        ukupna_zarada=ukupna_zarada
    )

@app.route("/neobavljeni")
@db_session
def neobavljeni():

    svi_poslovi = list(Posao.select())

    poslovi = [
        p for p in svi_poslovi
        if not p.obavljeno
    ]

    return render_template(
        "index.html",
        poslovi=poslovi
    )

@app.route("/obavljeni")
@db_session
def obavljeni():

    svi_poslovi = list(Posao.select())

    poslovi = [
        p for p in svi_poslovi
        if p.obavljeno
    ]

    return render_template(
        "index.html",
        poslovi=poslovi
    )

@app.route("/radnik")
@db_session
def radnik():

    ime = request.args.get("ime")

    svi_poslovi = list(Posao.select())

    poslovi = [
        p for p in svi_poslovi
        if p.radnik == ime
    ]

    return render_template(
        "index.html",
        poslovi=poslovi
    )

@app.route("/datum")
@db_session
def datum():

    trazeni_datum = request.args.get("datum")

    svi_poslovi = list(Posao.select())

    poslovi = [
        p for p in svi_poslovi
        if p.datum == trazeni_datum
    ]

    return render_template(
        "index.html",
        poslovi=poslovi
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )