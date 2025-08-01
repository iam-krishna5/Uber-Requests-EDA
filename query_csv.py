import duckdb

# Path to your CSV file
csv_file = r'E:\Desktop\Projects\Uber EDA\Uber Request Data Cleaned.csv'

# Create a view from your CSV
duckdb.query(f"""
    CREATE OR REPLACE VIEW Uber AS
    SELECT * FROM read_csv_auto('{csv_file}')
""")

queries = {
    "Total count of each status": """
        SELECT Status, COUNT(*) AS TotalRequests
        FROM Uber
        GROUP BY Status
        ORDER BY TotalRequests DESC;
    """,

    "Count of each Status by pickup point": """
        SELECT "Pickup point", Status, COUNT(*) AS NumberOfRequests
        FROM Uber
        GROUP BY "Pickup point", Status
        ORDER BY "Pickup point", NumberOfRequests DESC;
    """,

    "Top 10 drivers by assigned": """
        SELECT "Driver id", COUNT(*) AS TotalAssignedTrips
        FROM Uber
        WHERE "Driver id" IS NOT NULL
        GROUP BY "Driver id"
        ORDER BY TotalAssignedTrips DESC
        LIMIT 10;
    """,

    "Top 10 drivers by cancelled": """
        SELECT "Driver id", COUNT(*) AS CancelledTrips
        FROM Uber
        WHERE Status = 'Cancelled' AND "Driver id" IS NOT NULL
        GROUP BY "Driver id"
        ORDER BY CancelledTrips DESC
        LIMIT 10;
    """,

    "Total Requests by pickup points": """
        SELECT "Pickup point", COUNT(*) AS TotalRequests
        FROM Uber
        GROUP BY "Pickup point"
        ORDER BY TotalRequests DESC;
    """,

    "Requests with NO car Available": """
        SELECT "Pickup point", COUNT(*) AS NoCarsAvailableRequests
        FROM Uber
        WHERE Status = 'No Cars Available' AND "Driver id" IS NULL
        GROUP BY "Pickup point"
        ORDER BY NoCarsAvailableRequests DESC;
    """,

    "Percentage of Each Status per Pickup Point": """
        SELECT
            T1."Pickup point",
            T1.Status,
            COUNT(T1."Request id") AS NumberOfRequests,
            CAST(COUNT(T1."Request id") * 100.0 / T2.TotalRequests AS NUMERIC(10, 2)) || '%' AS Percentage
        FROM Uber AS T1
        JOIN (
            SELECT "Pickup point", COUNT(*) AS TotalRequests
            FROM Uber
            GROUP BY "Pickup point"
        ) AS T2
        ON T1."Pickup point" = T2."Pickup point"
        GROUP BY T1."Pickup point", T1.Status, T2.TotalRequests
        ORDER BY T1."Pickup point", CAST(COUNT(T1."Request id") * 100.0 / T2.TotalRequests AS NUMERIC(10, 2)) DESC;
    """,

    "Granular Driver Activity": """
        SELECT "Driver id", "Pickup point", Status, COUNT(*) AS NumberOfRequests
        FROM Uber
        WHERE "Driver id" IS NOT NULL
        GROUP BY "Driver id", "Pickup point", Status
        ORDER BY "Driver id", "Pickup point", NumberOfRequests DESC;
    """
}

# Execute and print each result
for title, query in queries.items():
    print(f"\n--- {title} ---\n")
    result = duckdb.query(query).to_df()
    print(result)
    
#python query_csv.py 