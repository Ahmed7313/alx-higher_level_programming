#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: double pointer to the start of the list.
 * Return: pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the start of the list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head, *slow = *head, *temp, *rev;

    if (!*head || !(*head)->next)
        return (1);

    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    rev = reverse_listint(&slow);
    temp = *head;

    while (rev)
    {
        if (temp->n != rev->n)
            return (0);
        temp = temp->next;
        rev = rev->next;
    }

    return (1);
}
