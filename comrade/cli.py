#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pyfiglet
from colorama import Fore, Style

import argparse

def main():
    global site
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Target URL to scan")
    args = parser.parse_args()

    site = args.target

main()

hi = pyfiglet.figlet_format("COMRADE__END POINTS_______TRACKER", font="slant")
print(Fore.WHITE + hi + Style.RESET_ALL)
print(Fore.RED + "*" * 50 + Style.RESET_ALL)





response = requests.get(site, timeout=10)

wordlist = [
    
    "login", "signin", "logout", "signup", "register", "register.php", "auth",
    "authenticate", "account", "my-account", "profile", "user", "users",
    "password", "forgot-password", "reset-password", "change-password",
    "verify", "verify-email", "confirm", "activation",

    
    "admin", "administrator", "adminpanel", "admin/login", "wp-admin", "cpanel",
    "manage", "dashboard", "controlpanel", "site-admin", "backend", "console",
    "moderator", "moderation", "superadmin",

    
    "api", "api/v1", "api/v2", "graphql", "rest", "rpc", "v1", "v2", "v3",
    "endpoint", "service", "services", "ajax", "xhr", "data", "fetch",

    
    "billing", "payments", "payment", "checkout", "invoice", "invoices",
    "subscriptions", "subscription", "orders", "order", "cart", "subscribe",

    
    "debug", "dev", "developer", "staging", "test", "testing", "sandbox",
    "health", "status", "metrics", "logs", "monitor", "monitoring",
    "api-docs", "docs", "documentation", "swagger", "openapi", "redoc",

    
    "upload", "uploads", "download", "downloads", "files", "file", "media",
    "static", "assets", "images", "pdf", "csv", "backup", "backups",

    
    "settings", "preferences", "security", "privacy", "billing", "addresses",
    "notifications", "notifications/settings", "consent", "sessions",

    "oauth", "oauth2", "sso", "saml", "openid", "callback", "auth/callback",
    "connect", "integration", "integrations", "webhook", "webhooks", "hooks",

    
    "product", "products", "catalog", "shop", "store", "category", "categories",
    "search", "filter", "price", "inventory", "sku", "checkout/success",

    
    "help", "support", "contact", "faq", "about", "terms", "terms-of-service",
    "privacy-policy", "privacy", "policy", "careers", "blog", "news",

    
    "home", "index", "index.html", "index.php", "main", "welcome", "root",
    "portal", "portal/login", "portal/admin", "panel", "console",

    
    "administrator/index.php", "user/login", "auth/login", "accounts/login",
    "admin.php", "login.php", "signin.php", "register.html", "account.php",

    
    "ping", "heartbeat", "healthcheck", "healthcheck.php", "status.json",
    "uptime", "uptime-status", "readiness", "liveness",

    
    "sitemap.xml", "robots.txt", ".well-known/security.txt", ".well-known",
    "feed", "rss", "atom", "license", "changelog", "CHANGELOG.md",

    
    "deploy", "deployment", "pipeline", "ci", "build", "artifact", "artifacts",
    "releases", "release", "version", "versions",

    
    "phpmyadmin", "pma", "adminer", "mysql", "mongodb", "redis", "pgadmin",


    "backup.sql", "backup.zip", "db_backup", "config", "config.php", "env",
    ".env", "secrets", "secret", "keys", "key", "private", "certificate",

     
    "auth/google", "auth/facebook", "auth/github", "signin/google", "signin/facebook",

    
    "push", "notifications/push", "mobile", "app", "manifest.json",

    "admin/dashboard", "admin/settings", "admin/users", "admin/login",
    "admin/api", "admin/config", "admin/tools", "admin/reports",

    "socket", "ws", "wss", "realtime", "events", "stream", "streaming",

    "search", "lookup", "find", "suggest", "autocomplete", "suggestions",

    "token", "oauth/token", "token/refresh", "refresh", "access_token",

    
    "videos", "gallery", "media-player", "report", "reports", "analytics",
    "analytics/dashboard", "stats", "statistics", "user/settings", "members",

    
    "en", "en-us", "es", "fr", "de", "locales", "lang", "language",

    "wp-login.php", "administrator", "sites/default", "system", "settings.php",

    "adm", "adm1n", "admin1", "adm/login", "manage/login", "cp", "portal/admin",

    "users", "accounts", "sessions", "auths", "profiles", "profiles/me",
    "me", "current", "members", "memberships",

    "stripe", "stripe/webhook", "stripe/checkout", "paypal", "paypal/ipn",
    "webhook/stripe", "webhook/paypal", "notifications/webhook",

    "setup", "install", "installer", "configuration", "configure", "init",
    "initiate", "upload.php", "download.php", "support/ticket", "tickets",
    "api.php", "rest.php", "svc", "service.php", "gateway", "gateway/payment"
]



if response.status_code == 200:
    print(Fore.RED+f"\nSuccessfully fetched: {site}\n"+Style.RESET_ALL)
    
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    
    
    parsed_url = urlparse(site)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    endpoints = set()
    
    
    for link in soup.find_all('a'):
        comrade_find_href = link.get('href')  
        if comrade_find_href:  
            full_url = urljoin(base_url, comrade_find_href)  
            endpoints.add(full_url) 
    
    
    print(Fore.WHITE+f"Found {len(endpoints)} ,endpoints:\n"+Style.RESET_ALL)
    print(Fore.RED+"\n".join(sorted(endpoints))+Style.RESET_ALL)

    print(len(endpoints))

    if len(endpoints) < 1:
        for w in wordlist:
            w = w.strip().lstrip("/") 
            full_url_1 = urljoin(base_url+"/",w)
            endpoints.add(full_url_1)
            print("\n".join(sorted(endpoints)))

else:
    print(Fore.RED+f"Failed to fetch {site}, status code: {response.status_code}"+Style.RESET_ALL)





