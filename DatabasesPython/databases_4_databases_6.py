import datetime
import pytz
import sqlite3

db = sqlite3.connect("accounts3.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL,"
           " balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history(time TIMESTAMPS NOT NULL,"
           "account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time,"
           " account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT"
           " strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS"
           " localtime, history.account, history.amount FROM history"
           " ORDER BY history.time")
# Added these lines from databases_4_databases_5.py code and used it to
# create a VIEW
# Now we can use this VIEW to more easily check the data in the databases_4_databases_7
# code


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name: str, opening_balance: float = 0.0):
        cursor = db.execute("SELECT name, balance FROM accounts "
                            "WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row is not None:
            self.name, self.balance = row
            print("Retrieved record for {}. ".format(self.name), end="")
        else:
            self.name = name
            self.balance = opening_balance
            cursor.execute("INSERT INTO accounts (name, balance) VALUES "
                           "(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {0}".format(self.name, end=""))

        self.show_balance()

    def _save_update(self, amount):
        new_balance = self.balance + amount
        deposit_time = Account._current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)",
                   (new_balance, self.name))
        db.execute("INSERT INTO history VALUES (?, ?, ?)",
                   (deposit_time, self.name, amount))
        db.commit()
        self.balance = new_balance

    def deposit(self, money_deposited: float) -> float:
        if money_deposited > 0.0:
            self._save_update(money_deposited)
            print("You have deposited {0} dollars in your account and now "
                  "have {1}".format(money_deposited, self.balance))
        return self.balance

    def withdraw(self, money_withdrawn: float) -> float:
        if 0.0 < money_withdrawn <= self.balance:
            self._save_update(-money_withdrawn)
            print("You have withdrawn {0} dollars from your account and now "
                  "have {1}".format(money_withdrawn, self.balance))
            return money_withdrawn
        else:
            print("Please enter a value that is greater than 0 and less "
                  "than the money you have in your account.")
            return 0.0

    def show_balance(self):
        print("The balance on {0}'s account is {1} dollars"
              .format(self.name, self.balance))


if __name__ == "__main__":
    maria = Account("Maria", 200.0)
    maria.show_balance()
    maria.deposit(352.13)
    maria.deposit(982.67)
    maria.withdraw(126.09)
    maria.show_balance()

    print("-" * 80)

    antonio = Account("Antonio", 25.0)
    antonio.deposit(400.00)
    antonio.withdraw(329.09)
    antonio.deposit(789.87)
    antonio.show_balance()

    print("-" * 80)

    antoinette = Account("Antoinette", 2030.3)
    antoinette.withdraw(427.9)
    antoinette.withdraw(238.74)
    antoinette.deposit(4528.97)
    antoinette.show_balance()

    print("-" * 80)

    adriano = Account("Adriano")
    adriano.deposit(3009.99)
    adriano.show_balance()

    print("-" * 80)

    ionete = Account("Ionete", 530)
    ionete.show_balance()

    print("-" * 80)

    antoine = Account("Antoine", 365.97)
    antoine.show_balance()

    db.close()