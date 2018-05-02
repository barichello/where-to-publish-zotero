# where to publish - zotero

A common advice for those starting to publich academic papers is to go for the journals you read more frequently. So, this script reads your library on Zotero e does the work for you.

The script identifies all the names of journals stored in the database and then counts how many items you have for each journal title.

# Limitations

The script is not case-sensitive, but it is sensitive to variations in typing. My suggestion is to use the script to identify these small variations, correct it manually (good to keep your library organized) and then run again.

The script only considers the "publication" field, which is only valid for "journal articles".

# How to use

Save the py file in the same folder as the zotero.sqlite file and run it. It depends on python-tk and sqlite3 libraries.

Zotero should be closed when you run the script, otherwise the database will be locked.

# To-do list

- Add the possibility to serach the most frequent author, publisher, etc.
- Reduce the sensitivity to small variations in the strings (do not know how though)
