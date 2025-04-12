import wikipedia


def search_wikipedia():
    """Prompt for Wikipedia titles and display summary or handle errors."""
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(f"\n{page.title}")
            print(page.summary)
            print(page.url)
            print()

        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!\n')

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning)")
            print(e.options[:5], "...")
            print()

        except Exception as e:
            print("An error occurred:", e)
            print()


# Run the function
search_wikipedia()
