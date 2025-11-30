# Candy Bin Sort – Classroom Game for Data Structures

This repository contains a small educational project for a **Data Structures** course.

The goal is to:
- Demonstrate the **Bin Sort** (bucket-style) algorithm using a **real-world classroom game** with candies.
- Provide a **clean, well-documented Python implementation** that maps directly to the classroom activity.
- Help students connect an abstract algorithm to a concrete, playful experience.

---

## 1. Concept Overview: What Is Bin Sort?

**Bin Sort** (also called a simple form of bucket sort) is a sorting technique that:

1. Creates multiple **bins** (or buckets).
2. Distributes each element from the input into the **appropriate bin** based on some key (value, category, range, etc.).
3. Then **collects all elements** from the bins in a predefined order, producing a sorted list.

For this project:

- Each **bin** represents a **candy category**.
- The **order of the bins** reflects an assumed order from **cheapest to most expensive** candy type.

---

## 2. Classroom Game – Candy Bins with 6 Tables

This project is designed to be used with a **live classroom activity**.

### 2.1. Physical Setup

You need:

- **6 tables**.
- **Labels for each table** (one per bin).
- A **bowl or bag of mixed candy**.

Assign one **bin (table)** per candy category:
1. **Chewing gum**
2. **Lollipops**
3. **Gummies**
4. **White chocolate**
5. **Dark chocolate**
6. **Fitness candy**

These categories are assumed to be ordered by **typical cost**:

> Cheapest → Most expensive  
> Chewing gum → Lollipops → Gummies → White chocolate → Dark chocolate → Fitness candy

This order is the **logical sort order** we want to simulate with Bin Sort.

---

### 2.2. Roles and Game Flow

1. **Mixed bowl of candy (unsorted input)**  
   - You have a bowl full of mixed candy types.
   - This represents the **unsorted list** in the algorithm.

2. **Distribution phase (distribute into bins)**  
   For each candy:

   - Look at its **type** (chewing gum, gummy, etc.).
   - Decide which **table (bin)** it belongs to.
   - Place the candy on that table.

   This corresponds to the algorithm step:

   ```text
   for each candy in mixed_bowl:
       put candy into bin[candy.category]
