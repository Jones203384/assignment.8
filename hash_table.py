from typing import Optional


class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name: str, number: str) -> None:
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key: str, value: Contact) -> None:
        self.key = key
        self.value = value
        self.next: Optional["Node"] = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Hash table size must be a positive integer.")
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        if not isinstance(key, str):
            raise TypeError("Hash key must be a string.")
        return sum(ord(character) for character in key) % self.size

    def insert(self, key: str, number: str) -> None:
        if not isinstance(key, str):
            raise TypeError("Hash key must be a string.")
        if not isinstance(number, str):
            raise TypeError("Contact number must be a string.")

        index = self.hash_function(key)
        contact = Contact(key, number)
        current = self.data[index]

        if current is None:
            self.data[index] = Node(key, contact)
            return

        while current is not None:
            if current.key == key:
                current.value.number = number
                return
            if current.next is None:
                current.next = Node(key, contact)
                return
            current = current.next

    def search(self, key: str) -> Optional[Contact]:
        current = self.data[self.hash_function(key)]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self) -> None:
        for index, node in enumerate(self.data):
            if node is None:
                print(f"Index {index}: Empty")
                continue

            contacts = []
            current = node
            while current is not None:
                contacts.append(f"- {current.value}")
                current = current.next
            print(f"Index {index}: {' '.join(contacts)}")


if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\nSearch result:", table.search("John"))

    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()
    print(table.search("Chris"))