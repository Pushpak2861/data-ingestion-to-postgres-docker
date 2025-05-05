# Sentiment Data Ingestion Pipeline (PostgreSQL + Pandas)

This project reads large data files in chunks using `pandas`, processes them iteratively, and inserts them into a PostgreSQL table named `sentiment`. It uses SQLAlchemy for database connection and supports appending data chunk-by-chunk efficiently.

---

## Features

- Stream large datasets using `pandas.read_csv` with `chunksize`.
- Insert data into PostgreSQL using `to_sql()`.
- Time the ingestion process to measure performance.
- Automatically stops when all data chunks are processed.

---

## Technologies Used

- Python 3.10+
- Pandas
- SQLAlchemy
- PostgreSQL (via Docker)
- `psycopg2-binary` (PostgreSQL driver)

---
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
