#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - check if cycle is repeated
 * @list: head of linked list
 *
 * Return: 1 if cycled, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
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
