graph TD
    A[Start: Access System] --> B[Security Check: Planned]
    B --> C{Authenticated?}
    
    B --> D[Validate API Key]
    B --> E[Rate-Limit, HTTPS]
    
    C -->|Yes| F[Role-Based Dashboard]
    C -->|No| G[Options]
    
    G --> H[Login: POST /api/auth/login/]
    G --> I[Register: POST /api/auth/register/]
    
    H -->|Valid JWT| F
    H -->|Invalid| J[Error: Retry Login]
    J --> H
    
    I -->|Valid| K[User Created]
    I -->|Invalid| L[Error: Retry Register]
    K --> H
    L --> I
    
    F --> M{User Role?}
    M --> N[Super Admin]
    M --> O[CSR]
    M --> P[Client]
    M --> Q[Consultant]
    M --> R[Staff]
    
    N --> S[Manage Users: /api/users/]
    N --> T[Manage Devices: /api/devices/]
    N --> U[View Alerts: GET /api/alerts/]
    N --> V[Resolve Alerts: PATCH /api/alerts/{id}/resolve/]
    N --> W[Admin Panel: Custom]
    N --> X[View Logs: Planned]
    N --> Y[Logout]
    
    O --> Z[View Clients: GET /api/users/?role=CLIENT]
    O --> AA[View Devices: GET /api/devices/]
    O --> AB[View Alerts: GET /api/alerts/]
    O --> AC[Support Clients: Manual]
    O --> AD[Logout]
    
    P --> AE[Register Device: POST /api/devices/register/]
    P --> AF[View Devices: GET /api/devices/]
    P --> AG[Assign Users: POST /api/clients/{id}/assign/]
    P --> AH[View Sensor Data: GET /api/sensor-data/{id}/]
    P --> AI[Update Sensor Data: PATCH /api/sensor-data/{id}/update/]
    P --> AJ[View Alerts: GET /api/alerts/]
    P --> AK[Resolve Alerts: PATCH /api/alerts/{id}/resolve/]
    P --> AL[Dashboard: GET /api/dashboard/...]
    P --> AM[Logout]
    
    Q --> AN[View Devices: GET /api/devices/?assigned]
    Q --> AO[View Sensor Data: GET /api/sensor-data/{id}/]
    Q --> AP[Analyze Trends: GET /api/dashboard/data-summary/]
    Q --> AQ[View Alerts: GET /api/alerts/]
    Q --> AR[Recommend: Planned]
    Q --> AS[Logout]
    
    R --> AT[View Devices: GET /api/devices/?assigned]
    R --> AU[Update Sensor Data: PATCH /api/sensor-data/{id}/update/]
    R --> AV[View Alerts: GET /api/alerts/]
    R --> AW[Logout]
    
    AX[Background Processes] --> AY[Sensor Data: POST /api/sensor-data/]
    AX --> AZ[Anomaly Detection]
    AX --> BA[Discrepancy Check]
    AX --> BB[Analytics]
    AX --> BC[Data Cleanup: Planned]
    AX --> BD[Testing: Planned]
    
    AY --> BE[Validate]
    BE -->|Valid| BF[Store: SQLite]
    BF --> AZ
    AZ -->|Threshold| BG[Create Alert]
    AZ -->|Statistical| BH[Create Alert: Planned]
    BA -->|Mismatch| BI[Create Alert]
    BI --> BJ[Log Discrepancy: Planned]
    BG --> BK[WebSocket Notification]
    BI --> BK
    BB --> BL[Update Dashboard APIs]
    BC --> BM[Delete Old Data]
    
    AX --> BN[Monitoring: Planned]
    BN --> BO[Log Events]
    BN --> BP[Track Errors]
    
    Y --> A
    AD --> A
    AM --> A
    AS --> A
    AW --> A