# Approach for discounts

- Can get "race condition" for discounts

  - 2Bs => save 15, but 2Es => save 30
  - Want to apply the bigger discount first ("favor the customer") or just apply both discounts?

- Store all pending discounts in a separate tracker?

  - {"B": [(1, 15), (1, 30)]}

    - It changes dynamically and must be recalculated in some order
    - Simpler to assume both discounts are applied; eg "EEBB" => 45 discount?

  - Running with that since "all offers are well balanced"
  - This logic also implies that "as long as you make an offer you benefit from it"
