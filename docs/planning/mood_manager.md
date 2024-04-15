This class will manage my suggested routines when I'm facing a problem, feeling bored, or just want to have fun.
In this mode, I should be add the issue, and the routine will be suggested to me.
ex: Watch philosophical videos, read a book when you feel bored. -> it will be named "Nice to have" routine.
And the program should know that the above routine is related to "Boredom", so it can collect all helpful routines for this issue.

 ex:
 ```
 bardala> mode_manager
 >> Add
 >>> What's the routine?
 >> Watch philosophical videos.
 >>> What's the issue?
 >> Boredom
 >>> Done. ---it should be in a green color.
 >> /
 get out the mode_manager.
 bardala>
```

 ex:
 ```
 bardala> mode_manager
 >> I want to study, but I'm feeling lazy.
 >>> Oh, I think you should first get out of your phone, Then, you can start with a small task.
 >> Give me another suggestion.
 >>> Try to explore the topic you want to study, try to search for it on the internet.
 >> /
 get out the mode_manager.
 bardala>
```

 ex:

 ```
 bardala> mode_manager
 >> I'm feeling anxious.
 >>> Take a deep breath, and try to focus on your breath.
 >> Give me another suggestion.
 >>> Try to listen to calm music.
```



 ex:
 ```
 bardala> mode_manager
 >> Add this routine.
 >>> What's the routine?
 >> When you feel bored, watch philosophical videos.
 >>> What's the issue?
 >> Boredom
 >>> Done. ---it should be in a green color.
```

 ex:
 ```
 bardala> mode_manager
 >> I'm feeling bored.
 >>> Watch philosophical videos.
 >> Suggest me another routine.
 >>> Read a book.
 >> thank you.
 >>> You're welcome.
 >> /
 get out the mode_manager.
 bardala>
```

ex:
```
bardala> mode_manager
>> Add this routine.
>>> What's the routine?
>> When you feel bored, watch philosophical videos.
>>> What's the issue?
>> Boredom 
>>> Done.  --This should be displayed in a green color.
```
<!--  -->

## DadaBase Design
### Table: issues
| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| issue       | TEXT      | Not null    |
| created_at  | TEXT      |             |

---

### Table: routines
| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | INTEGER   | Primary key |
| issue_id    | INTEGER   | Foreign key referencing issues(id) |
| routine     | TEXT      | Not null    |
| created_at  | TEXT      |             |

---

## DataBase structure
### issues:
| id | issue
|----|------
| 1  | boredom
| 2  | laziness
| 3  | anxiety

---

### routines:
| id | issue_id | routine
|----|----------|--------
| 1  | 1        | Watch philosophical videos.
| 2  | 1        | Read a book.
| 3  | 2        | Get out of your phone.
| 4  | 2        | Start with a small task.
| 5  | 3        | Take a deep breath.
| 6  | 3        | Listen to calm music.

---


