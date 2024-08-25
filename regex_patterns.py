flipkart_url_patterns = [
    r'https?://www\.flipkart\.com/.+',
    r'https?://flipkart\.com/.+',
    r'https?://m\.flipkart\.com/.+',
    r'https?://dl\.flipkart\.com/.+',
    r'https?://flipkart\.in/.+',
    r'https?://www\.flipkart\.in/.+',
    r'https?://dl\.flipkart\.in/.+',
    r'https?://m\.flipkart\.in/.+',
    # Add more patterns if needed
]

amazon_url_patterns = [
    r'https?://www\.amazon\.com/.+',
    r'https?://amazon\.com/.+',
    r'https?://www\.amazon\.in/.+',
    r'https?://amazon\.in/.+',
    r'https?://m\.amazon\.com/.+',
    r'https?://m\.amazon\.in/.+',
    ]

all_url_patterns = amazon_url_patterns + flipkart_url_patterns