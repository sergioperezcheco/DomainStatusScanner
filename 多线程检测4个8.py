import whois
import concurrent.futures

def check_domain(domain):
    try:
        w = whois.whois(domain)
        if w.status == None:
            return False
    except Exception as e:
        print(f"Error occurred while checking domain {domain}: {e}")
    return True

def has_four_eights(n):
    return str(n).count('8') == 4

def main():
    unregistered_domains = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_domain = {executor.submit(check_domain, f"{i}.xyz"): f"{i}.xyz" for i in range(100000, 1000000) if has_four_eights(i)}
        for future in concurrent.futures.as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                if not future.result():
                    unregistered_domains.append(domain)
                    print(f"Found unregistered domain: {domain}")
            except Exception as e:
                print(f"Error occurred while checking domain {domain}: {e}")
    print("All unregistered domains:")
    for domain in unregistered_domains:
        print(domain)

if __name__ == "__main__":
    main()
