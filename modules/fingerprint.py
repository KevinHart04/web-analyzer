import requests

def detect_technologies(url: str) -> list:
    """
    Analiza el código fuente de la página objetivo para detectar 
    tecnologías, CMS o frameworks conocidos.
    
    Args:
        url (str): La URL objetivo a analizar.
        
    Returns:
        list: Una lista de strings con las tecnologías detectadas.
    """

    signatures = {
        # ===================== CMS =====================
        "WordPress": {
            "html": ["wp-content", "wp-includes"],
            "headers": [],
            "cookies": ["wordpress_", "wp-settings-"]
        },
        "Joomla": {
            "html": ["joomla", "com_content", "/administrator/"],
            "headers": [],
            "cookies": []
        },
        "Drupal": {
            "html": ["drupal", "sites/default"],
            "headers": [],
            "cookies": ["SESS"]
        },
        "Magento": {
            "html": ["mage", "magento", "skin/frontend"],
            "headers": [],
            "cookies": ["frontend"]
        },
        "Ghost": {
            "html": ["ghost-sdk", "ghost-content-api"],
            "headers": [],
            "cookies": []
        },

        # ===================== E-COMMERCE =====================
        "Shopify": {
            "html": ["cdn.shopify.com", "shopify-payment-button"],
            "headers": [],
            "cookies": ["_shopify"]
        },
        "WooCommerce": {
            "html": ["woocommerce", "wc-"],
            "headers": [],
            "cookies": ["woocommerce_"]
        },
        "PrestaShop": {
            "html": ["prestashop"],
            "headers": [],
            "cookies": ["PrestaShop-"]
        },
        "BigCommerce": {
            "html": ["cdn.bc0a.com", "bigcommerce"],
            "headers": [],
            "cookies": []
        },

        # ===================== FRONTEND =====================
        "React": {
            "html": ["react", "__REACT_DEVTOOLS_GLOBAL_HOOK__"],
            "headers": [],
            "cookies": []
        },
        "Angular": {
            "html": ["ng-app", "angular.js"],
            "headers": [],
            "cookies": []
        },
        "Vue.js": {
            "html": ["vue", "__vue__"],
            "headers": [],
            "cookies": []
        },
        "Svelte": {
            "html": ["svelte"],
            "headers": [],
            "cookies": []
        },

        # ===================== CSS =====================
        "Bootstrap": {
            "html": ["bootstrap.min.css", "bootstrap.min.js"],
            "headers": [],
            "cookies": []
        },
        "Tailwind CSS": {
            "html": ["tailwind", "tw-"],
            "headers": [],
            "cookies": []
        },
        "Bulma": {
            "html": ["bulma.css"],
            "headers": [],
            "cookies": []
        },

        # ===================== JS LIBRARIES =====================
        "jQuery": {
            "html": ["jquery", "jquery.min.js"],
            "headers": [],
            "cookies": []
        },
        "Lodash": {
            "html": ["lodash", "_.map"],
            "headers": [],
            "cookies": []
        },
        "Moment.js": {
            "html": ["moment.js", "moment("],
            "headers": [],
            "cookies": []
        },

        # ===================== BACKEND =====================
        "Laravel": {
            "html": [],
            "headers": [],
            "cookies": ["laravel_session", "XSRF-TOKEN"]
        },
        "Django": {
            "html": ["csrfmiddlewaretoken"],
            "headers": [],
            "cookies": ["csrftoken"]
        },
        "Flask": {
            "html": [],
            "headers": ["werkzeug"],
            "cookies": []
        },
        "Spring": {
            "html": [],
            "headers": ["JSESSIONID"],
            "cookies": ["JSESSIONID"]
        },
        "ASP.NET": {
            "html": ["__VIEWSTATE"],
            "headers": ["X-AspNet-Version"],
            "cookies": ["ASP.NET_SessionId"]
        },
        "Express": {
            "html": [],
            "headers": ["x-powered-by: express"],
            "cookies": []
        },

        # ===================== SERVERS =====================
        "Apache": {
            "html": [],
            "headers": ["apache"],
            "cookies": []
        },
        "Nginx": {
            "html": [],
            "headers": ["nginx"],
            "cookies": []
        },
        "IIS": {
            "html": [],
            "headers": ["microsoft-iis"],
            "cookies": []
        },
        "LiteSpeed": {
            "html": [],
            "headers": ["litespeed"],
            "cookies": []
        },

        # ===================== CDN / INFRA =====================
        "Cloudflare": {
            "html": [],
            "headers": ["cf-ray", "cloudflare"],
            "cookies": ["__cfduid"]
        },
        "Akamai": {
            "html": [],
            "headers": ["akamai"],
            "cookies": []
        },
        "Fastly": {
            "html": [],
            "headers": ["x-fastly"],
            "cookies": []
        },

        # ===================== ANALYTICS =====================
        "Google Analytics": {
            "html": ["google-analytics.com", "gtag("],
            "headers": [],
            "cookies": ["_ga"]
        },
        "Google Tag Manager": {
            "html": ["googletagmanager.com", "GTM-"],
            "headers": [],
            "cookies": []
        },
        "Hotjar": {
            "html": ["hotjar", "hj("],
            "headers": [],
            "cookies": []
        },

        # ===================== SECURITY =====================
        "Cloudflare WAF": {
            "html": [],
            "headers": ["cf-ray", "cf-cache-status"],
            "cookies": []
        },
        "Sucuri": {
            "html": [],
            "headers": ["x-sucuri-id"],
            "cookies": []
        },
        "Imperva": {
            "html": [],
            "headers": [],
            "cookies": ["incap_ses", "_incap_"]
        },

        # ===================== LANGUAGES =====================
        "PHP": {
            "html": [".php"],
            "headers": [],
            "cookies": ["phpsessid"]
        },
        "Python": {
            "html": [],
            "headers": ["wsgi", "gunicorn"],
            "cookies": []
        },
        "Node.js": {
            "html": [],
            "headers": ["x-powered-by: express"],
            "cookies": []
        },
        "Java": {
            "html": [],
            "headers": [],
            "cookies": ["JSESSIONID"]
        },
        "Ruby": {
            "html": [],
            "headers": [],
            "cookies": ["_rails_session"]
        },

        # ===================== OTROS =====================
        "Firebase": {
            "html": ["firebaseio.com", "firebase"],
            "headers": [],
            "cookies": []
        },
        "Stripe": {
            "html": ["js.stripe.com"],
            "headers": [],
            "cookies": []
        }
    }

    
    detected = []
    
    try:
        # Hacemos la petición
        response = requests.get(url, timeout=5)
        
        # Pasamos todo el HTML a minúsculas para que sea fácil buscar
        html_content = response.text.lower()
        headers = str(response.headers).lower()
        cookies = str(response.cookies).lower()
        
        for tech, data in signatures.items():

            # Flag para saber si encontramos algo
            found = False

            # HTML
            for keyword in data["html"]:
                if keyword in html_content:
                    found = True
                    break

            # HEADERS (solo si no lo encontramos antes)
            if not found:
                for keyword in data["headers"]:
                    if keyword in headers:
                        found = True
                        break

            # COOKIES
            if not found:
                for keyword in data["cookies"]:
                    if keyword in cookies:
                        found = True
                        break

            if found:
                detected.append(tech)       
        return detected
            
    except requests.RequestException:
        return ["Error al obtener el código fuente"]