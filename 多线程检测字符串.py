import whois
import concurrent.futures

def check_domain(domain):
    try:
        w = whois.whois(domain)
        if w.status == None:
            return domain
    except Exception as e:
        print(f"Error occurred while checking domain {domain}: {e}")
    return None

def main():
    unregistered_domains = []
    domains_to_check = [f"{i}.xyz" for i in range(100000, 1000000) if '888' in str(i)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_domain = {executor.submit(check_domain, domain): domain for domain in domains_to_check}
        for future in concurrent.futures.as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                result = future.result()
                if result is not None:
                    unregistered_domains.append(result)
                    print(f"Found unregistered domain: {result}")
            except Exception as e:
                print(f"Error occurred while checking domain {domain}: {e}")

    print("All unregistered domains:")
    for domain in unregistered_domains:
        print(domain)

if __name__ == "__main__":
    main()
