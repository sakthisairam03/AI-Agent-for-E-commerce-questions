# app/charts.py
import matplotlib.pyplot as plt
import os
import uuid

def render_bar_chart(columns, rows):
    # Only render if exactly 2 columns
    if len(columns) != 2:
        return None

    labels = [str(row[0]) for row in rows]
    values = [float(row[1]) for row in rows]

    # Unique image filename
    chart_id = str(uuid.uuid4())
    filename = f"charts/{chart_id}.png"
    os.makedirs("charts", exist_ok=True)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel(columns[0])
    plt.ylabel(columns[1])
    plt.title(f"{columns[1]} by {columns[0]}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    return filename
