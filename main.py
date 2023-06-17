import requests
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Gud Baldr")
print(ascii_banner)

def analyze_security_headers():
    url = input("Enter the website URL to analyze: ")
    response = requests.get(url)
    headers = response.headers

    security_headers = {
        'Strict-Transport-Security': {
            'description': 'The site should enforce HTTPS and specify the maximum age of the HSTS policy.',
            'expected_value': 'max-age=31536000'
        },
        'Content-Security-Policy': {
            'description': 'The site should specify a Content Security Policy to mitigate against XSS attacks.',
            'expected_value': 'default-src \'self\''
        },
        'X-Content-Type-Options': {
            'description': 'The site should use the X-Content-Type-Options header to prevent MIME-type sniffing.',
            'expected_value': 'nosniff'
        },
        'X-Frame-Options': {
            'description': 'The site should use the X-Frame-Options header to prevent clickjacking attacks.',
            'expected_value': 'deny'
        },
        'X-XSS-Protection': {
            'description': 'The site should use the X-XSS-Protection header to enable the XSS Auditor built into modern web browsers.',
            'expected_value': '1; mode=block'
        }
    }

    print(f'Security Headers Analysis for {url}:\n')

    for header, data in security_headers.items():
        if header in headers:
            header_value = headers[header]
            if header_value == data['expected_value']:
                status = '✓'
            else:
                status = '✗'
        else:
            header_value = 'Not found'
            status = '✗'

        print(f'{header}: {header_value}')
        print(f'Description: {data["description"]}')
        print(f'Status: {status}\n')

# Example usage
analyze_security_headers()
