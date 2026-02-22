from datetime import datetime, timezone


def main() -> None:
    print("ai-ad-fraud-detector initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
