#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list to check
 * Return: 1 if there is cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *tort = list, *hare = list;

	if (list == NULL)
		return (0);

	while (hare && hare->next)
	{
		hare = hare->next->next;
		tort = tort->next;
		if (tort == hare)
			return (1);
	}
	return (0);
}
