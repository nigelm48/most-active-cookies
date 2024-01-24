import sys

def get_most_active_cookies(filename, date):
    active_cookies = {}
    target_date = date

    with open(filename, 'r') as file:
        for line in file:
            cookie, timestamp = line.strip().split(',')
            cookie_date = timestamp[:10]

            if cookie_date == target_date:
                active_cookies[cookie] = active_cookies.get(cookie, 0) + 1
            elif cookie_date < target_date:
                break

    max_count = max(active_cookies.values(), default=0)
    most_active_cookies = [cookie for cookie, count in active_cookies.items() if count == max_count]

    return most_active_cookies

def main():
    if len(sys.argv) != 5 or sys.argv[1] != '-f' or sys.argv[3] != '-d':
        print("Usage: {} -f <filename> -d <date>".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[2]
    date = sys.argv[4]
    most_active_cookies = get_most_active_cookies(filename, date)

    for cookie in most_active_cookies:
        print(cookie)

if __name__ == '__main__':
    main()
