Отчёт о построении **графика заражения коронавирусом в РФ**
1. Чтобы построить график, мне нужно было найти базу данных. Первоначальной идеей было построить график заражения в России по датам. Однако найти такую базу данных не удалось. Однако было найдено довольно много информации про количество заражённых, вылечившихся и погибших на территории РФ. 
2. Я изменил первоначальную задачу на то, чтобы построить график "Статистики заражения по регионам РФ"
3. Для того, чтобы построить график, я загнал данные в excel и сохранил их в формате **csv**. Затем по этим данным была построена таблица на Python  использованием библиотеки matplotlib
4. ##### Получив конечный результат, я понял, что он имеет определённые плюсы: 
График отражает статистику не в общем, а в каждом регионе отдельно, что важно, тк ситуация во всех регионах разная и нельзя применять одинаковые меры ко всем регионам вместе.
Можно наблюдать, как развивается ситуация в более и менее развитых регионах
##### Также во время работы я заметил, что программу можно улучшить
Во-первых, значения на горизонтальной оси сливаются, потому можно писать их горизонтально
Во-вторых, можно добавить надпись, которая указывает, каким цветом что обозначено.

4. В итоге, получился вот такой график ![clipboard](https://i.imgur.com/ZtCEien.png) Синим цветом показано общее число заражённых, зелёным-вылечившиеся, а желтым - погибшие от коронавируса по официальным данным