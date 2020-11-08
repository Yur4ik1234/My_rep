 1 . Write info to file
 
 2 . Result of `python .`
 
 ```
We are in the __main__
2020-11-07 21:53:07.893325
win32
```
 3 . Result of  `python . -h`
 ```
 usage: _main_.py [-h] [-o OPT] [-l]

Приклад передачі аргументів у Python програму.

optional arguments:
  -h, --help            show this help message and exit
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.
  -l, --logs            Якщо виконати команду з цим параметром будуть виводитись логи.
```

 4 . Result of  `python . -o "Цей текст також має вивестись"`
 ```
 We are in the __main__
2020-11-07 21:57:41.107362
win32
З консолі було передано аргумент
 ========== >> Цей текст також має вивестись << ==========
```

 5 . Result of `python . --logs`
 ```
 2020-11-07 22:00:21,515 root INFO: Тут буде просто інформативне повідомлення
2020-11-07 22:00:21,516 root WARNING: Це Warning повідомлення
2020-11-07 22:00:21,517 root ERROR: Це повідомлення про помилку
```