import pypyodbc


def map_acces_to_leuko_register():

    pypyodbc.lowercase = False
    conn = pypyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
        r"Dbq=C:\Users\Ju\Desktop\Dark Summoner.accdb;")
    cur = conn.cursor()
    cur.execute("SELECT Number, Name, Atk, Def, HP, BP, Species, Special FROM Impulse AA+");
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print(u"Creature with Number {1} is {1} ({2})".format(
            row.get("CreatureID"), row.get("Name_EN"), row.get("Name_JP")))
    cur.close()
    conn.close()

if __name__ == '__main__':
    map_acces_to_leuko_register()