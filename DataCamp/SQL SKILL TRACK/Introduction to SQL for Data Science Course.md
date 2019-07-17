# Introduction to SQL for Data Science Course

## Keywords: Basic SQL,RDBMS

Course introduces to the Basics of what's a DB, SQL and DBMS

Focus of the course is to **QUERY the DB**

As a good practice **KEYWORDS** are written in **ALLCAPS** even though any RDBMS will identify the keywords.

In SQL:

-  **ROW** values are known as **Record or Observation**
- **Column** values are known as **Attributes or Field**

### Keywords introduced

|  #   | KEYWORD  | USE CASE                                                     |
| :--: | :------- | :----------------------------------------------------------- |
|  1   | SELECT   | Select the column,columns from the table                     |
|  2   | FROM     | To denote Table on which operation is done                   |
|  3   | LIMIT    | To limit the number of records returned based on the Query   |
|  4   | COUNT    | Count the number of entries of Specific Column               |
|  5   | DISTINCT | Returns the unique entries in the Specific Column            |
|  6   | WHERE    | Used to Filter the data based on condition specified         |
|  7   | AND      | Used along with WHERE to Filter data based on Multiple Columns |
|  8   | OR       | Used for this OR this Selection                              |
|  9   | BETWEEN  | Used with WHERE to select data between a specified range     |
|  10  | IN       | Used with WHERE to select the values matching the list of specified condition |
|  11  | NULL     | Represents the missing value in the observation              |
|  12  | IS NULL  | Count number of Entries that has NULL value                  |
|  13  | NOT NULL | To Filter out Non-Missing Values                             |
|  15  | LIKE     | Used for **Wildcard** Selection **%** - Select zero or one or more character missing and   **_** Missing One character |
|  14  | NOT LIKE | Doesn't match the given condition                            |
|  15  | AVG      | Aggregate function used for calculating **Average**          |
|  16  | SUM      | Aggregate function used for calculating **Sum**              |
|  17  | MIN      | Aggregate function used for calculating **Minimum Value**    |
|  18  | MAX      | Aggregate function used for calculating **Maximum Value**    |
|  19  | AS       | Used for Aliasing a Calculated field                         |
|  20  | ORDER BY | Sort the returned Data                                       |
|  21  | GROUP BY | Group the data based on the selected field                   |
|  22  | HAVING   | Used under **GROUP BY**  when meeting a certain condition    |

#### Points to Remember:

- **<>**  Symbol for **NOT EQUAL To **
- **' '** Single Quote is used to enclose strings in PostgreSQL
- **Division( / )** is like Python 2.xx so we should divide by a float to get a floating point value
- Default sort order in **ORDER BY** is Ascending to reverse **DESC** keyword is added
- SQL will throw an error if we tried to SELECT a field that is not in GROUP clause without using it to compute some kind of value about the entire group