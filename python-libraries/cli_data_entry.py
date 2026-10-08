import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()

# Example Greek mythology data
mythology_data = [
    {
        "title": "The Myth of Persephone",
        "figure": "Persephone",
        "theme": "Death, rebirth, and the changing seasons",
    },
    {
        "title": "The Myth of Theseus and the Minotaur",
        "figure": "Theseus",
        "theme": "Heroism, courage, and overcoming danger",
    },
    {
        "title": "The Myth of Heracles",
        "figure": "Heracles",
        "theme": "Strength, perseverance, and redemption",
    },
]

console.print(
    "\n[bold cyan]Greek Mythology Cultural Data Collection[/bold cyan]\n"
)

# Display example data
table = Table(title="Example Greek Mythology Stories")

table.add_column("Title", style="magenta")
table.add_column("Main Figure", style="cyan")
table.add_column("Theme")

for myth in mythology_data:
    table.add_row(
        myth["title"],
        myth["figure"],
        myth["theme"],
    )

console.print(table)

console.print(
    "\n[bold cyan]Now you can add your own Greek mythology story.[/bold cyan]"
)

# Collect user data
while True:
    console.print("\n[bold]Enter information about a Greek mythology story:[/bold]")

    title = input("Enter the title of the myth: ")
    figure = input("Enter the main figure or character: ")
    theme = input("Enter the main theme or cultural meaning: ")

    # Show the user's entry
    console.print("\n[bold yellow]Your entry:[/bold yellow]")

    entry_table = Table(title="New Mythology Entry")
    entry_table.add_column("Title", style="magenta")
    entry_table.add_column("Main Figure", style="cyan")
    entry_table.add_column("Theme")

    entry_table.add_row(title, figure, theme)

    console.print(entry_table)

    # Confirm the data
    confirmation = input("\nIs this information correct? (yes/no): ").lower()

    if confirmation in ["yes", "y"]:
        new_myth = {
            "title": title,
            "figure": figure,
            "theme": theme,
        }

        mythology_data.append(new_myth)
        console.print("[bold green]Entry confirmed![/bold green]")
        break

    console.print(
        "[bold red]Entry not confirmed. Please enter the information again.[/bold red]"
    )

# Ask whether the user wants to add another entry
while True:
    another = input("\nWould you like to add another myth? (yes/no): ").lower()

    if another in ["yes", "y"]:
        title = input("Enter the title of the myth: ")
        figure = input("Enter the main figure or character: ")
        theme = input("Enter the main theme or cultural meaning: ")

        while True:
            console.print("\n[bold yellow]Your entry:[/bold yellow]")

            entry_table = Table(title="New Mythology Entry")
            entry_table.add_column("Title", style="magenta")
            entry_table.add_column("Main Figure", style="cyan")
            entry_table.add_column("Theme")

            entry_table.add_row(title, figure, theme)

            console.print(entry_table)

            confirmation = input(
                "\nIs this information correct? (yes/no): "
            ).lower()

            if confirmation in ["yes", "y"]:
                mythology_data.append(
                    {
                        "title": title,
                        "figure": figure,
                        "theme": theme,
                    }
                )

                console.print(
                    "[bold green]Entry confirmed and added![/bold green]"
                )
                break

            title = input("Enter the title of the myth again: ")
            figure = input("Enter the main figure or character again: ")
            theme = input("Enter the main theme or cultural meaning again: ")

    elif another in ["no", "n"]:
        break

    else:
        console.print(
            "[bold red]Please enter yes or no.[/bold red]"
        )

# Save the data to a JSON file
output_path = Path(__file__).parent / "greek_mythology_data.json"

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(mythology_data, file, indent=4, ensure_ascii=False)

console.print(
    f"\n[bold green]Your data has been saved![/bold green]"
)
console.print(f"File location: {output_path}")