#include "lists.h"

listint_t *reverse(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse - Function to reverse a linked list
 * @head: pointer to starting of node of the list
 * Return: pointer to the head of reversed list
 */

listint_t *reverse(listint_t **head)
{
	listint_t *node = *head, *prev, *next = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Function that checks if list is palindrome
 * @head: pointer to head of the list
 * Return: 0 if list is not palindrome, -1
 * if list is palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tm, revs, *middle;
	size_t len = 0;
	size_t x;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tm = *head;
	while (tm)
	{
		len++;
		tm = tm->next;
	}
	tm = *head;
	for (x = 0; x < (len / 2) - 1; x++)
		tm = tm->next;
	if ((len % 2) == 0 && tm->next != tm->next->next)
		return (0);
	tm = tm->next->next;
	revs = reverse(&tm);
	middle = revs;
	tm = *head;

	while (revs)
	{
		if (tm->next != rev->next)
			return (0);
		tm = tm->next;
		revs = revs->next;
	}
	reverse(&middle);

	return (1);
}
