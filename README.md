flowchart TD
  ```  A([Start]) --> B[/Enter units/]
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
    P --> Q```
