import requests
from datetime import datetime

def fetch_cad_usd_rate():
    url = "https://api.frankfurter.app/latest?from=CAD&to=USD"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["rates"]["USD"]

def display_rate(rate: float):
    inverse = 1 / rate
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("=" * 40)
    print("        TỶ GIÁ CAD / USD")
    print("=" * 40)
    print(f"  1 CAD  =  {rate:.4f} USD")
    print(f"  1 USD  =  {inverse:.4f} CAD")
    print("-" * 40)
    print(f"  Cập nhật: {now}")
    print(f"  Nguồn:    ECB via Frankfurter API")
    print("=" * 40)

def main():
    print("Đang lấy tỷ giá CAD/USD...")
    try:
        rate = fetch_cad_usd_rate()
        display_rate(rate)
    except requests.exceptions.ConnectionError:
        print("Lỗi: Không có kết nối mạng.")
    except requests.exceptions.HTTPError as e:
        print(f"Lỗi HTTP: {e}")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
