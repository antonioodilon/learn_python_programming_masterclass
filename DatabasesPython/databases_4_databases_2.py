# Now using sqlite to create a database for our account
import sqlite3

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL,"
           " balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS transactions(time TIMESTAMPS NOT NULL,"
           "account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time,"
           " account))")  # Notice that the primary key here is created differently
# Can also create UNIQUE KEY


class Account(object):

    def __init__(self, name: str, opening_balance: float = 0.0):
        cursor = db.execute("SELECT name, balance FROM accounts "
                            "WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row is not None:
            self.name, self.balance = row
            print("Retrieved record for {}. ".format(self.name), end="")
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts (name, balance) VALUES "
                           "(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {0}".format(self.name, end=""))

        self.show_balance()

    def deposit(self, money_deposited: float) -> float:
        if money_deposited > 0.0:
            self._balance += money_deposited
            print("You have deposited {0} dollars in your account and now "
                  "have {1}".format(money_deposited, self._balance))
        return self._balance
    # Tim said that float numbers can sometimes cause problems due to the
    # conversion from binary numbers to decimal. So sometimes it might be
    # a good idea to use integers and then either multiply by 100 to get
    # the cents, or divide by 100, and make changes to the program accordingly.

    def withdraw(self, money_withdrawn: float) -> float:
        if 0.0 < money_withdrawn <= self._balance:
            self._balance -= money_withdrawn
            print("You have withdrawn {0} dollars from your account and now "
                  "have {1}".format(money_withdrawn, self._balance))
            return money_withdrawn
        else:
            print("Please enter a value that is greater than 0 and less "
                  "than the money you have in your account.")
            return 0.0

    def show_balance(self):
        print("The balance on {0}'s account is {1} dollars"
              .format(self.name, self._balance))


if __name__ == "__main__":
    # maria = Account("Maria", 200.0)
    # maria.show_balance()
    # maria.deposit(352.13)
    # maria.deposit(982.67)
    # maria.withdraw(126.09)
    # maria.show_balance()

    antonio = Account("Antonio", 25.0)
    antonio.deposit(400.00)
    antonio.withdraw(329.09)
    antonio.deposit(789.87)
    antonio.show_balance()

    antoinette = Account("Antoinette", 2030.3)
    antoinette.withdraw(427.9)
    antoinette.withdraw(238.74)
    antoinette.deposit(4528.97)
    antoinette.show_balance()

    adriano = Account("Adriano")
    adriano.deposit(3009.99)
    adriano.show_balance()

    db.close()