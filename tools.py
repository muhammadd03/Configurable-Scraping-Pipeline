import json

_config = {
    'url': 'https://store.steampowered.com/specials',
    'meta': {
        'name': 'Steam Sales Scraper',
        'description': 'Extracts the highest discounted games from Steam',
        'author': 'Muhammad',
        'version': 0.1
    },
    'container':
        {
            'name': 'store_sale_div',
            'selector': 'div[class*="UlvFkP8Oew4a6VTHCvLNH _34o914Rd3YiwTjnvyTgVbb Focusable"]',
            'match': 'all',
            'type': 'node'
        },
    'item': [
        {
            'name': 'title',
            'selector': 'div[class*="_3jI467XYJLy1CQ5YZhp2q_ StoreSaleWidgetTitle"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'thumbnail',
            'selector': 'img[class*="cODQhXeXS-Yn-vLIBNwyW"]',
            'match': 'first',
            'type': 'node'
        },
        {
            'name': 'tags',
            'selector': 'div[class*="_3OSJsO_BdhSFujrHvCGLqV"] > a',
            'match': 'all',
            'type': 'text'
        },
        {
            'name': 'release_date',
            'selector': 'div[class*="_2vdJg6hB5XNf1RHeulRUFB"] > div[class*="_3eOdkTDYdWyo_U5-JPeer1"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'reviewed_by',
            'selector': 'div[class*="_1Deyvnxud-VpRoj0-ak-WK"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'review_score',
            'selector': 'div[class*="_2SbZztpb7hkhurwbFMdyhL"] > div',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'price_currency',
            'selector': 'div[class*="Wh0L8EnwsPV_8VAu8TOYr"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'sale_price',
            'selector': 'div[class*="Wh0L8EnwsPV_8VAu8TOYr"]',
            'match': 'first',
            'type': 'text'
        },
        {
            'name': 'original_price',
            'selector': 'div[class*="_1EKGZBnKFWOr3RqVdnLMRN"]',
            'match': 'first',
            'type': 'text'
        }
    ]

}



def get_config(load_from_file=False):
    if load_from_file:
        with open('config.json', 'r') as f:
            return json.load(f)
    return _config


def generate_config():
    with open('config.json', 'w') as f:
        json.dump(_config, f, indent=4)


if __name__ == '__main__':
    generate_config()
