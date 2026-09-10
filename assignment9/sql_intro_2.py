import os
import sqlite3
import pandas as pd

# Anchor all paths to this script's own directory (assignment9), so the
# database connection and the CSV output both work correctly regardless
# of the working directory the script is launched from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "..", "db", "lesson.db")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "order_summary.csv")

conn = None

try:
    conn = sqlite3.connect(DB_PATH)

    query = """
        SELECT
            line_items.line_item_id,
            line_items.quantity,
            products.product_id,
            products.product_name,
            products.price
        FROM line_items
        JOIN products
            ON line_items.product_id = products.product_id
    """

    df = pd.read_sql_query(query, conn)

    print("\nFirst five rows:")
    print(df.head())

    df["total"] = df["quantity"] * df["price"]

    print("\nFirst five rows with total:")
    print(df.head())

    summary_df = df.groupby(
        "product_id",
        as_index=False
    ).agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    })

    print("\nGrouped product summary:")
    print(summary_df.head())

    summary_df = summary_df.sort_values(by="product_name")

    summary_df.to_csv(OUTPUT_PATH, index=False)

    print("\nSorted order summary:")
    print(summary_df.head())
    print(f"\norder_summary.csv created successfully at: {OUTPUT_PATH}")

except (sqlite3.Error, pd.errors.DatabaseError) as error:
    print(f"Database error: {error}")

finally:
    if conn is not None:
        conn.close()
        print("Database connection closed.")