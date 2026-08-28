
# ============================================================
#              🧬 CANCER GENE ANALYZER
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# CHECK EXPRESSION USING IF, ELIF, ELSE
# ============================================================

gene = "BRCA1"
expression = 85

print("\n", "." * 10, "CHECK EXPRESSION USING IF, ELIF, ELSE", "." * 10)

if expression > 80:
    print(gene, "has HIGH expression")

elif expression > 75:
    print(gene, "has MEDIUM expression")

else:
    print(gene, "has LOW expression")


# ============================================================
# USING FUNCTIONS
# ============================================================

print("\n", "." * 10, "USING FUNCTIONS", "." * 10)

def gene_expression(expression):

    if expression > 80:
        return "HIGH"

    elif expression > 75:
        return "MEDIUM"

    else:
        return "LOW"


result = gene_expression(85)

print("Gene_Expression is:", result)


# ============================================================
# CREATING LISTS
# ============================================================

print("\n", "." * 10, "CREATING LISTS", "." * 10)

genes = ["BRCA1", "TP53", "EGFR", "MYC"]

expression = [85, 45, 72, 91]

print("Genes are:", genes)
print("Expression is:", expression)


# ============================================================
# NUMPY FILTERING
# ============================================================

print("\n", "." * 10, "NUMPY FILTERING", "." * 10)

numpy_expression = np.array(expression)

high_expression = numpy_expression[numpy_expression > 70]

print("HIGH EXPRESSION IS:", high_expression)


# ============================================================
# NUMPY MEAN AND STANDARD DEVIATION
# ============================================================

array = np.array([85, 45, 72, 91, 63])

mean_expression = np.mean(array)

std_expression = np.std(array)

print("Mean of Gene_Expression is:", mean_expression)

print("STD of Gene_Expression is:", std_expression)


# ============================================================
# CREATING DATAFRAME
# ============================================================

print("\n", "." * 10, "CREATING DATAFRAME", "." * 10)

dataframe = pd.DataFrame({

    "Genes": ["BRCA1", "TP53", "EGFR", "MYC", "PTEN"],

    "Expression": [85, 45, 72, 91, 63]

})

print("DATAFRAME IS:\n", dataframe)


# ============================================================
# MISSING VALUES IN DATAFRAME
# ============================================================

print("\n", "." * 10, "MISSING VALUES IN DATAFRAME", "." * 10)

missing_values = pd.DataFrame({

    "Gene": ["BRCA1", "TP53", "EGFR", "MYC", "PTEN"],

    "Expression": [85, 45, np.nan, 91, 63]

})

print(
    "DataFrame with Missing values is:\n",
    missing_values
)


# ============================================================
# isnull()
# ============================================================

print("\n", "." * 10, "isnull()", "." * 10)

print(missing_values.isnull())


# ============================================================
# fillna()
# ============================================================

missing_values["Expression"] = missing_values[
    "Expression"
].fillna(
    missing_values["Expression"].mean()
)

print(
    "DataFrame after fillna():\n",
    missing_values
)


# ============================================================
# CANCER LIST DATAFRAME
# ============================================================

print("\n", "." * 10, "CANCER LIST DATAFRAME", "." * 10)

cancer_data = pd.DataFrame({

    "Gene": [
        "BRCA1",
        "TP53",
        "EGFR",
        "MYC",
        "PTEN"
    ],

    "Cancer_Type": [
        "Breast",
        "Lung",
        "Lung",
        "Breast",
        "Prostate"
    ],

    "Expression": [
        85,
        45,
        72,
        91,
        63
    ]

})

print(
    "CANCER DATAFRAME IS:\n",
    cancer_data
)


# ============================================================
# GROUPBY
# ============================================================

grouped = cancer_data.groupby(
    "Cancer_Type"
)["Expression"].mean()

print(
    "\nAVERAGE EXPRESSION BY CANCER TYPE:\n",
    grouped
)


# ============================================================
# SORTED VALUES
# ============================================================

print("\n", "." * 10, "SORTED VALUES", "." * 10)

sorted_values = cancer_data.sort_values(
    "Expression",
    ascending=False
)

print(
    "SORTED VALUES ARE GIVEN BELOW:\n",
    sorted_values
)


# ============================================================
# FILTERING DATA
# ============================================================

print("\n", "." * 10, "FILTERING DATA", ">" * 10)

filtered_data = cancer_data[
    cancer_data["Expression"] > 70
]

print(
    "HIGH EXPRESSION IS:\n",
    filtered_data
)


# ============================================================
# STATISTICS SUMMARY
# ============================================================

print("\n", "." * 10, "STATISTICS SUMMARY", "." * 10)

summary = cancer_data["Expression"].describe()

print(
    "STATISTICAL SUMMARY IS:\n",
    summary
)


# ============================================================
# FINAL CANCER GENE ANALYZER REPORT
# ============================================================

print(
    "\n========== CANCER GENE ANALYZER REPORT =========="
)

print(
    "Total Genes:",
    len(cancer_data)
)

print(
    "Average Expression:",
    cancer_data["Expression"].mean()
)

print(
    "Highest Expression:",
    cancer_data["Expression"].max()
)

print(
    "Lowest Expression:",
    cancer_data["Expression"].min()
)

print("\nHigh Expression Genes:")

print(
    cancer_data[
        cancer_data["Expression"] > 70
    ][
        ["Gene", "Expression"]
    ]
)

print("\nAverage Expression by Cancer Type:")

print(
    cancer_data.groupby(
        "Cancer_Type"
    )["Expression"].mean()
)


# ============================================================
#                 📊 VISUALIZATIONS
# ============================================================

sns.set_theme(style="whitegrid")


# ============================================================
# AVERAGE EXPRESSION BY CANCER TYPE
# ============================================================

plt.figure(figsize=(8, 5))

plt.bar(
    grouped.index,
    grouped.values
)

plt.title(
    "Average Gene Expression by Cancer Type",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Cancer Type")

plt.ylabel("Average Expression")

plt.tight_layout()

plt.show()


# ============================================================
# GENE EXPRESSION COMPARISON
# ============================================================

plt.figure(figsize=(8, 5))

sns.barplot(
    data=cancer_data,
    x="Gene",
    y="Expression",
    hue="Cancer_Type"
)

plt.title(
    "Gene Expression Comparison",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Gene")

plt.ylabel("Expression")

plt.tight_layout()

plt.show()


# ============================================================
# GENE EXPRESSION DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    cancer_data["Expression"],
    bins=5,
    kde=True
)

plt.title(
    "Gene Expression Distribution",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Expression")

plt.ylabel("Frequency")

plt.tight_layout()

plt.show()


# ============================================================
# EXPRESSION BY CANCER TYPE
# ============================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=cancer_data,
    x="Cancer_Type",
    y="Expression"
)

plt.title(
    "Gene Expression by Cancer Type",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Cancer Type")

plt.ylabel("Expression")

plt.tight_layout()

plt.show()


# ============================================================
# GENE EXPRESSION HEATMAP
# ============================================================

heatmap_data = cancer_data.pivot_table(
    values="Expression",
    index="Gene",
    columns="Cancer_Type",
    aggfunc="mean"
)

plt.figure(figsize=(8, 5))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".1f",
    cmap="viridis"
)

plt.title(
    "Gene Expression Heatmap",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Cancer Type")

plt.ylabel("Gene")

plt.tight_layout()

plt.show()


# ============================================================
# HIGH EXPRESSION GENES
# ============================================================

high_expression_genes = cancer_data[
    cancer_data["Expression"] > 70
]

plt.figure(figsize=(8, 5))

sns.barplot(
    data=high_expression_genes,
    x="Gene",
    y="Expression",
    hue="Cancer_Type"
)

plt.title(
    "High Expression Genes (>70)",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Gene")

plt.ylabel("Expression")

plt.tight_layout()

plt.show()


# ============================================================
# PROJECT COMPLETED
# ============================================================

print(
    "\n========== PROJECT COMPLETED SUCCESSFULLY =========="
)

print(
    "🧬 Cancer Gene Analyzer Finished!"
)
```
