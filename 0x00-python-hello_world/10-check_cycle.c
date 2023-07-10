#include "list.h"

/**
 * check_cycle - function to check if the linked list contain a cycle
 * @list: list to check
 * Return: 1 list is a cycle, 0 if it's not a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fast = list;

	if (list == NULL)
	{
		return (0);
	}

	while (slw && fast && fast->next)
	{
		slw = slw->next;
		fast = fast->next->next;

		if (slw == fast)
		{
			return (1);
		}
	}
	return (0);
}
