import requests
from bs4 import BeautifulSoup

def get_jd_price(keyword):
    url = f"https://search.jd.com/Search?keyword={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('i', class_='J_price')
        if price_element:
            return float(price_element.text)
    except Exception as e:
        print(f"获取京东价格时出错: {e}")
    return None

def get_taobao_price(keyword):
    url = f"https://s.taobao.com/search?q={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('strong')
        if price_element:
            return float(price_element.text)
    except Exception as e:
        print(f"获取淘宝价格时出错: {e}")
    return None

def compare_prices(keyword):
    jd_price = get_jd_price(keyword)
    taobao_price = get_taobao_price(keyword)

    if jd_price is not None and taobao_price is not None:
        if jd_price < taobao_price:
            print(f"商品 {keyword} 在京东的价格更低，为 {jd_price} 元。")
        elif jd_price > taobao_price:
            print(f"商品 {keyword} 在淘宝的价格更低，为 {taobao_price} 元。")
        else:
            print(f"商品 {keyword} 在京东和淘宝的价格相同，均为 {jd_price} 元。")
    elif jd_price is not None:
        print(f"仅获取到商品 {keyword} 在京东的价格，为 {jd_price} 元。")
    elif taobao_price is not None:
        print(f"仅获取到商品 {keyword} 在淘宝的价格，为 {taobao_price} 元。")
    else:
        print(f"未获取到商品 {keyword} 在京东和淘宝的价格信息。")

if __name__ == "__main__":
    keyword = "iPhone 15"
    compare_prices(keyword)