import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("triggers_inventory.db") 
cursor = conn.cursor()


# Create a products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer TEXT NOT NULL,
    model TEXT NOT NULL,           
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock_quantity INTEGER NOT NULL,
    description TEXT,
    sku TEXT UNIQUE NOT NULL
)
''')



# Product data
products = [
    ("Glock", "19 Gen 5", "Handgun", 549.99, 10, "Compact 9mm pistol", "HG001"),
    ("Glock", "43x MOS", "Handgun", 499.99, 8, "Concealed carry 9mm pistol, optic-ready", "HG002"),
    ("Sig Sauer", "P320", "Handgun", 599.99, 8, "Compact 9mm pistol, optic-ready", "HG003"),
    ("HK", "USP", "Handgun", 099.99, 8, "Full-sized .45ACP pistol", "HG004"),
    ("Beretta", "92FS", "Handgun", 699.99, 8, "Full-sized 9mm pistol", "HG005"),
    ("BCM", "M4", "Long Gun", 1399.99, 5, "Semi-automatic rifle, 5.56x45", "LG001"),
    ("Remington", "700", "Long Gun", 899.99, 5, "Bolt-action hunting rifle, .308 Winchester", "LG002"),
    ("Zastava", "ZPAP", "Long Gun", 999.99, 5, "Semi-automatic rifle, 7.62x39", "LG003"),
    ("Sig Sauer", "MCX Spear LT", "Long Gun", 2599.99, 5, "Semi-automatic rifle, 5.56x45", "LG004"),
    ("Mossberg", "500", "Long Gun", 399.99, 7, "Pump-action shotgun, 12GA", "LG005"),
    ("Vortex Optics", "Strike Eagle 1-6x24", "Optic", 299.99, 12, "Variable zoom rifle scope", "OP001"),
    ("EOTech", "EXPS3", "Optic", 599.99, 4, "Holographic weapon sight", "OP002"),
    ("Trijicon", "RMR Type 2", "Optic", 779.99, 4, "Pistol-mounted optic", "OP003"),
    ("Magpul", "PMAG 30rd AR/M4", "Accessory", 15.99, 50, "30-round polymer magazine", "AC001"),
    ("Streamlight", "TLR-1 HL", "Accessory", 129.99, 6, "Weapon-mounted tactical light", "AC002"),
    ("Surefire", "Scout Light Pro ", "Accessory", 369.99, 6, "Weapon-mounted tactical light", "AC003"),
]

# Insert data 
cursor.executemany('''
INSERT INTO products (manufacturer, model, category, price, stock_quantity, description, sku)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', products)

# Commit changes
conn.commit()






cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

for row in rows:
    print(row)


conn.close()
