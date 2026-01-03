"""
====================================================
DATA ENGINEERING MASTER PIPELINE
====================================================
"""

# =========================
# CONFIGURATION
# =========================
DATA_FILE = "sales.csv"
LOG_FILE = "pipeline.log"


# =========================
# LOGGER (MONITORING)
# =========================
def log(message):
    """
    Writes logs for monitoring pipeline
    """
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")


# =========================
# EXTRACT (READ DATA)
# =========================
def extract_data(file_path):
    """
    Reads raw data from CSV
    """
    data = []

    try:
        with open(file_path, "r") as f:
            header = f.readline().strip().split(",")

            for line in f:
                values = line.strip().split(",")
                record = dict(zip(header, values))
                data.append(record)

        log("Data extraction successful")

    except Exception as e:
        log(f"Extraction error: {e}")

    return data


# =========================
# TRANSFORM (CLEAN DATA)
# =========================
def transform_data(records):
    """
    Cleans and converts data types
    """
    clean_data = []

    for record in records:
        try:
            clean_record = {
                "order_id": int(record["order_id"]),
                "product": record["product"].strip(),
                "price": float(record["price"]),
                "quantity": int(record["quantity"]),
                "total": float(record["price"]) * int(record["quantity"])
            }
            clean_data.append(clean_record)

        except Exception as e:
            log(f"Bad record skipped: {record}")

    log("Data transformation completed")
    return clean_data


# =========================
# VALIDATION LOGIC
# =========================
def validate_data(records):
    """
    Validates business rules
    """
    valid_records = []

    for r in records:
        if r["price"] > 0 and r["quantity"] > 0:
            valid_records.append(r)
        else:
            log(f"Invalid record removed: {r}")

    return valid_records


# =========================
# LOAD (STORE DATA)
# =========================
def load_data(records):
    """
    Simulates loading data into warehouse
    """
    for r in records:
        print(r)

    log(f"{len(records)} records loaded successfully")


# =========================
# DATA QUALITY METRICS
# =========================
def calculate_metrics(records):
    """
    Calculates metrics for analytics
    """
    total_revenue = sum(r["total"] for r in records)
    avg_price = total_revenue / len(records) if records else 0

    print("Total Revenue:", total_revenue)
    print("Average Revenue per Order:", avg_price)


# =========================
# PIPELINE ORCHESTRATION
# =========================
def run_pipeline():
    """
    Controls full ETL pipeline
    """
    log("Pipeline started")

    raw_data = extract_data(DATA_FILE)
    transformed_data = transform_data(raw_data)
    valid_data = validate_data(transformed_data)

    calculate_metrics(valid_data)
    load_data(valid_data)

    log("Pipeline completed")


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    run_pipeline()
