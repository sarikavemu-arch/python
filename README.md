1. Algorithm
Progressive Electricity Billing
1. Start.
2. Enter electricity units.
3. If units are less than or equal to 100, bill = units × 2.
4. Else if units are less than or equal to 200, bill = 200 + (units − 100) × 3.
5. Otherwise, bill = 500 + (units − 200) × 5.
6. Add ₹50 fixed charge to the bill.
7. If units are greater than 200, add ₹100 surcharge.
8. If units are less than or equal to 100, subtract ₹20 rebate.
9. Display the final electricity bill.
10. If bill is greater than ₹500, display "High Bill"; otherwise, display "Normal Bill".
    ```
     flowchart TD
  A([Start]) --> B[/Enter units/]
    B --> C{Units <= 100?}
    C -- Yes --> D[Bill = Units * 2]
    C -- No --> E{Units <= 200?}
    E -- Yes --> F[Bill = 200 + Units excess * 3]
    E -- No --> G[Bill = 500 + Units excess * 5]
    D --> H[Add 50 fixed charge]
    F --> H
    G --> H
    H --> I{Units > 200?}
    I -- Yes --> J[Add 100 surcharge]
    I -- No --> K{Units <= 100?}
    J --> L[Display final bill]
    K -- Yes --> M[Subtract 20 rebate]
    K -- No --> L
    M --> L
    L --> N{Bill > 500?}
    N -- Yes --> O[Display High Bill]
    N -- No --> P[Display Normal Bill]
    O --> Q([Stop])
    P --> Q
    ```

