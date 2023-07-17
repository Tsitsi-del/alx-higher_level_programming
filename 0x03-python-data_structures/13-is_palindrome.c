#include "lists.h"

void *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Function to reverse a linked list
 * @head: pointer to starting of node of the list
 * Return: pointer to the head of reverse
 */
void *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *node = *head;
	listint_t *next = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
}

/**
 * is_palindrome - Function that checks if list is palindrome
 * @head: pointer to head of the list
 * Return: 0 if list is not palindrome, -1
 * if list is palindrome
 */

int is_palindrome(listint_t **head)
{
        listint_t *sl = *head, *fs = *head, *tm = *head, *duplicate = NULL;

        if (*head == NULL || (*head)->next == NULL)
        {
                return (1) }
        while (1)
        {
                fs = fs->next->next;
                if (!fs)
                {
                        duplicate = sl->next;
                        break; }
                if (!fs->next)
                {
                        duplicate = sl->next->next;
			break; }
		sl = sl->next; }
	reverse_listint(&duplicate);

	while (duplicate && tm)
	{
		if (tm->n == duplicate->n)
		{
			duplicate = duplicate->next;
			tm = tm->next; }
		else
			return (0);
	}
	if (!duplicate)
	{
		return (1); }
	return (0);
}
