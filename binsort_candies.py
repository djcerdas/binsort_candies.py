from dataclasses import dataclass
from typing import List, Dict


# -------------------------------
# 1. Domain model: Candy object
# -------------------------------

@dataclass
class Candy:
    """
    Represents a candy with:
    - category: used to decide which bin it goes into.
    - name: a human-friendly label (brand or description).
    """
    category: str
    name: str


# ---------------------------------------
# 2. Bin configuration: ordered by cost
# ---------------------------------------
# Cheapest → Most expensive

CANDY_CATEGORY_ORDER: List[str] = [
    "chewing_gum",     # very cheap
    "lollipop",        # cheap
    "gummy",           # low/medium cost
    "white_chocolate", # medium cost
    "dark_chocolate",  # medium/high cost
    "fitness",         # most expensive
]

# Display labels (for printing)
CATEGORY_DISPLAY_LABEL: Dict[str, str] = {
    "chewing_gum": "Chewing gum",
    "lollipop": "Lollipops",
    "gummy": "Gummies",
    "white_chocolate": "White chocolate",
    "dark_chocolate": "Dark chocolate",
    "fitness": "Fitness candy",
}


# -------------------------------
# 3. Helper functions
# -------------------------------

def create_empty_bins(category_order: List[str]) -> Dict[str, List[Candy]]:
    """
    Create an empty bin for every category in the given order.
    Each bin is simply a list that will store Candy objects.
    """
    return {category: [] for category in category_order}


def distribute_candies_into_bins(
    candies: List[Candy],
    category_order: List[str]
) -> Dict[str, List[Candy]]:
    """
    Distribute all candies into their corresponding bins based on category.
    """
    bins = create_empty_bins(category_order)

    for candy in candies:
        if candy.category not in bins:
            raise ValueError(f"Unknown category: {candy.category}")
        bins[candy.category].append(candy)

    return bins


def print_bins(bins: Dict[str, List[Candy]], category_order: List[str]) -> None:
    """
    Print a visual representation of each bin and its content.
    """
    print("\n===== BINS STATE (CLASSROOM MODEL) =====")

    for index, category in enumerate(category_order, start=1):
        label = CATEGORY_DISPLAY_LABEL.get(category, category)
        candies_in_bin = bins[category]

        print(f"\n[Bin {index}] {label}:")
        if not candies_in_bin:
            print("   (empty)")
        else:
            for candy in candies_in_bin:
                print(f"   - {candy.name}")

    print("========================================\n")


def collect_candies_from_bins(
    bins: Dict[str, List[Candy]],
    category_order: List[str]
) -> List[Candy]:
    """
    Collect all candies from bins following the cost-based order.
    """
    final_list: List[Candy] = []

    for category in category_order:
        final_list.extend(bins[category])

    return final_list


# -------------------------------
# 4. High-level algorithm
# -------------------------------

def bin_sort_candies(
    candies: List[Candy],
    category_order: List[str],
    debug: bool = True
) -> List[Candy]:
    """
    High-level implementation of the Bin Sort algorithm for candy objects.
    """
    if not candies:
        return []

    bins = distribute_candies_into_bins(candies, category_order)

    if debug:
        print_bins(bins, category_order)

    sorted_candies = collect_candies_from_bins(bins, category_order)
    return sorted_candies


# -------------------------------
# 5. Demo / Classroom simulation
# -------------------------------

if __name__ == "__main__":
    mixed_candies: List[Candy] = [
        Candy(category="white_chocolate", name="White chocolate bar"),
        Candy(category="gummy",           name="Gummy bears"),
        Candy(category="dark_chocolate",  name="Dark 70% bar"),
        Candy(category="fitness",         name="Protein bar"),
        Candy(category="lollipop",        name="Strawberry lollipop"),
        Candy(category="chewing_gum",     name="Mint gum"),
        Candy(category="gummy",           name="Sour worms"),
        Candy(category="chewing_gum",     name="Bubble gum"),
        Candy(category="dark_chocolate",  name="Dark 85% bar"),
    ]

    print("Mixed candies (unordered):")
    for c in mixed_candies:
        print(f" - [{c.category}] {c.name}")

    sorted_result = bin_sort_candies(
        candies=mixed_candies,
        category_order=CANDY_CATEGORY_ORDER,
        debug=True
    )

    print("Final sorted candies (cheapest → most expensive):")
    for c in sorted_result:
        print(f" - [{c.category}] {c.name}")
