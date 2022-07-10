#include "lists.h"

/**
* check_cycle - check if list is cycle
* @list: type listint_t
* Return: always int
* case: 1 true, 0 false
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	/* Slow pointer will move one node per iteration whereas 
        fast node will move two nodes per iteration */
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
