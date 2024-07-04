#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    listint_t *head = NULL;
    listint_t *new_node;

    /* Adding nodes to the end of the list */
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);

    /* Printing the original list */
    printf("Original list:\n");
    print_listint(head);
    printf("\n");

    /* Inserting a new node */
    new_node = insert_node(&head, 27);
    if (new_node == NULL) {
        printf("Error: Could not insert new node\n");
        free_listint(head);
        return (1);
    }

    /* Printing the modified list */
    printf("Modified list with 27 inserted:\n");
    print_listint(head);

    /* Freeing the list */
    free_listint(head);

    return (0);
}
