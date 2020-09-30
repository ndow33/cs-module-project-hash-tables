from llist import LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            self.capactiy = MIN_CAPACITY
            self.buckets = [None]*MIN_CAPACITY
        else:
            self.capacity = capacity
            self.buckets = [None]*capacity
        # keeps track of how many hash table entries we have
        self.entries = 0    

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.entries/self.capacity


     
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # $%$Start
        # 64-bit constants
        FNV_offset_basis_64 = 0xcbf29ce484222325
        FNV_prime_64 = 0x100000001b3
        # Cast the key to a string and get bytes
        str_key = str(key).encode()
        hash = FNV_offset_basis_64
        for b in str_key:
            hash *= FNV_prime_64
            hash ^= b
            hash &= 0xffffffffffffffff  # 64-bit hash
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        index = self.fnv1(key) % self.capacity
        return index


    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # find the index
        index = self.hash_index(key)
        # create a hash table entry object
        hash_obj = HashTableEntry(key=key, value=value)

        # if there is no hash table entry at the index
        if self.buckets[index] is None:
            # create a linked list
            ll = LinkedList()
            # set the hash table entry as the head
            ll.head = hash_obj
            # store the linked list at the index of the hash table
            self.buckets[index] = ll

            # update entries
            self.entries += 1

        # if there is a linked list of hash table entries at the index
        else:
            # get the head hash entry
            cur = self.buckets[index].head
            # traverse the linked list
            while cur is not None:
                # If the key has been used before
                if cur.key == key:
                    # update the value
                    cur.value = value
                    # exit method
                    return
                # move onto the next hash entry
                else:
                    cur = cur.next
            # if there are no matches
            # insert the hash entry at the head of the list
            self.buckets[index].insert_at_head(hash_obj)
            # update the entries
            self.entries += 1


            
        
    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # find the index
        index = self.hash_index(key)

        # is there anything there
        if self.buckets[index] is None:
            return None
        
        # if there is something there...
        cur = self.buckets[index].head
        while cur is not None:
            if cur.key == key:
                val = cur.value
                cur.value = None
                # decrement self.entries
                self.entries -= 1
                return val
            else:
                cur = cur.next
        print('Cannot delete: key not found!')


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        # is there anything there
        if self.buckets[index] is None:
            return None

        # if there is something there...
        # traverse the linked list until we find a matching key
        cur = self.buckets[index].head
        while cur is not None:
            # if cur.key is the same as the given key
            if cur.key == key:
                # return the value of cur    
                return cur.value
            else:
                cur = cur.next
        # if there are no matches, return none
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Create a new hash table with new_capacity
        new_table = HashTable(new_capacity)
        # loop through each linked list in the table
        for index in range(self.capacity):
            # if there is a linked list
            if self.buckets[index] is not None:
                # loop through it and put each hash entry 
                # into the new table at its proper index
                cur = self.buckets[index].head
                while cur is not None:
                    new_table.put(cur.key, cur.value)
                    cur = cur.next
        
        self = new_table
        self.capacity = new_capacity







if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
        # print(ht.get(f"line_{i}"))
    
    for i in range(ht.capacity):
        print(ht.buckets[i])

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")