#include "list.h"

/**
 * check_cycle - function to check if the linked list contain a cycle
 * @list: list to check
 * Return: 1 list is a cycle, 0 if it's not a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
	{
		return (0);
	}

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
