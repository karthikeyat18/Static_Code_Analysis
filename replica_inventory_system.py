import json
from datetime import datetime

# Global variable
stock_data = {}


def addItem(item="default", qty=0, logs=None):
    if logs is None:
        logs = []
    if not item:
        return
    # Type validation
    if not isinstance(qty, (int, float)):
        print(f"Error: Quantity must be a number, got {type(qty).__name__}")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def removeItem(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory")
    except ValueError:
        print(f"Invalid quantity for item '{item}'")


def getQty(item):
    return stock_data[item]


def loadData(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"File {file} not found. Starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in {file}. Starting with empty inventory.")
        stock_data = {}


def saveData(file="inventory.json"):
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=2))


def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types, no check
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    print("System operation completed")  # Safe alternative to eval


main()
