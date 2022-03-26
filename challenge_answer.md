#Question:
```
1. Write a CLI that consumes the API and is able to do the following:
  - Shows the total CPU, memory, and disk space of each group and allows us to limit to top-k results (invdb group-resources --limit 5)
  - Checks for group overlap. Given two groups, print all nodes that are in both. (invdb group-overlap --groups foo,bar)
2. Extend each command in Part 1 with a feature that you think would add value.
3. (Discussion Only)
  - What would you add to the inventory API to make it more useful?
  - What is another feature you would add to the client to help examine the current inventory?
  - What other uses are there for this type of API in large-scale infrastructure?
```

#Answers.

```
 1. invdb CLI is written (See the README part of how to install)
 - invdb group-resources --limit 5 (works with default limit of 10) (Check README.md file on how to use it)
 - invdb group-overlap --groups foo,bar (Works with valid groups name, Error is also handled)

2.
 - first Argument is extended with sorting options so you can use `total_memory`, `total_disk`or `total_cpus`. (Check README.md for details)
 - 2nd Argument is extended with Unlimited number of groups (not just 2 groups)

3.
-  I would add rack-id of the Server, Expiry date of warranty to the API.
-  I would add argument to find all the nodes with specific OS like 'Ubuntu' or specific
Server model like product_name.
- The main Reason I see for this kind of API is to make a decision on what group/Nodes needs to be selected
for specific workload.

```