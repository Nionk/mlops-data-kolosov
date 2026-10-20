# Отчет по практической работе

## Окружение и ссылки

Python: 3.12.7
pandas: 3.0.6
scikit-learn: 1.9.1
dvc: 3.67.1
clearml: 2.1.12

Git-репозиторий: https://github.com/Nionk/mlops-data-kolosov
DVC remote: ../dvc_remote_kolosov (локальная директория вне репозитория)

## Часть 2. DVC

### Git commits, tags и хэши data.dvc

1. Базовая версия (tag: data-v1)
Git commit: 6a21d86004a84423c7a0e416d62f6daecc0893a6
data.dvc:
outs:
- md5: bf5656de288a783265cb7b85509abc8e.dir
  size: 2635
  nfiles: 1
  hash: md5
  path: data

2. Ветка feature/wine
Git commit: 5d805ccc99da110003315aafa39e65dff056d341
data.dvc:
outs:
- md5: f8fe844935c3e7d61c8736baacbf1018.dir
  size: 13938
  nfiles: 2
  hash: md5
  path: data

3. Ветка feature/iris-features
Git commit: 57fb9728e0e43de5ae2fe3abeff80b117a283806
data.dvc:
outs:
- md5: c6a76d56d42022aa7753d44fd7e84d6a.dir
  size: 4230
  nfiles: 1
  hash: md5
  path: data

4. Итоговая ветка main (после слияния)
Git commit: f210f8f1c5e830e02b68b84e677c3d8b329a484e
data.dvc:
outs:
- md5: 957c42d7c9ecafed014287db892a5935.dir
  size: 15533
  nfiles: 2
  hash: md5
  path: data

### Хэши CSV

iris.csv (base):
SHA-256: 6d700503c9c2e2c71d187b889a87af8a8d3a6dd5bae1266d46f4ee4db5a6349f
Форма: 150 rows x 5 cols
Столбцы: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'target']

wine.csv (wine и итоговая main):
SHA-256: 38860ba04ace4d402242340bcf40be4bd6f4ebde9144a3dc89dc12c20f7f8e60
Форма: 178 rows x 14 cols
Столбцы: ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline', 'target']

iris.csv (iris_features и итоговая main):
SHA-256: 3e1ba63f55da2aabc432d00b1670140f5162bf9ef34b837598ec2fc176c9ff26
Форма: 150 rows x 7 cols
Столбцы: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'target', 'sepal_area', 'petal_area']

### Результат восстановления из чистого clone

Вывод check_data.py после git clone и dvc pull:

Относительный путь: data/iris.csv
SHA-256: 3e1ba63f55da2aabc432d00b1670140f5162bf9ef34b837598ec2fc176c9ff26
Строк и столбцов: 150 rows x 7 cols
Список столбцов: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'target', 'sepal_area', 'petal_area']
Пропущенных знач.: 0
Относительный путь: data/wine.csv
SHA-256: 38860ba04ace4d402242340bcf40be4bd6f4ebde9144a3dc89dc12c20f7f8e60
Строк и столбцов: 178 rows x 14 cols
Список столбцов: ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline', 'target']
Пропущенных знач.: 0
Успех

## Часть 3. ClearML Dataset

Project: MIIT/MLOps/practice_3/kolosov
Dataset name: sklearn-tabular-kolosov

BASE_ID: 345416da8e98412ba18c09727a9d8efa
WINE_ID: 8cad7646de6f45a59946db9bc050b37c
IRIS_FEATURES_ID: aabd640b0b2e473ea48c9ea1264c73ff

### Dependency graph и состав трех скачанных версий

Метка             : BASE_ID
Dataset ID        : 345416da8e98412ba18c09727a9d8efa
Version           : 1.0.0
Dependency Graph  : {'345416da8e98412ba18c09727a9d8efa': []}
All files         : ['iris.csv']
Added files       : ['iris.csv']
Modified files    : []
Removed files     : []
  -> Файл: iris.csv
     SHA-256 : 6d700503c9c2e2c71d187b889a87af8a8d3a6dd5bae1266d46f4ee4db5a6349f
     Shape   : 150 rows x 5 cols
     Columns : ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'target']

Метка             : WINE_ID
Dataset ID        : 8cad7646de6f45a59946db9bc050b37c
Version           : 1.1.0
Dependency Graph  : {'345416da8e98412ba18c09727a9d8efa': [], '8cad7646de6f45a59946db9bc050b37c': ['345416da8e98412ba18c09727a9d8efa']}
All files         : ['iris.csv', 'wine.csv']
Added files       : ['wine.csv']
Modified files    : []
Removed files     : []
  -> Файл: iris.csv
     SHA-256 : 6d700503c9c2e2c71d187b889a87af8a8d3a6dd5bae1266d46f4ee4db5a6349f
     Shape   : 150 rows x 5 cols
     Columns : ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'target']
  -> Файл: wine.csv
     SHA-256 : 38860ba04ace4d402242340bcf40be4bd6f4ebde9144a3dc89dc12c20f7f8e60
     Shape   : 178 rows x 14 cols
     Columns : ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline', 'target']

Метка             : IRIS_FEATURES_ID
Dataset ID        : aabd640b0b2e473ea48c9ea1264c73ff
Version           : 2.0.0
Dependency Graph  : {'aabd640b0b2e473ea48c9ea1264c73ff': ['345416da8e98412ba18c09727a9d8efa']}
All files         : ['iris.csv']
Added files       : []
Modified files    : ['iris.csv']
Removed files     : []
  -> Файл: iris.csv
     SHA-256 : 3e1ba63f55da2aabc432d00b1670140f5162bf9ef34b837598ec2fc176c9ff26
     Shape   : 150 rows x 7 cols
     Columns : ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'target', 'sepal_area', 'petal_area']

## Часть 4. Сравнение

### 14. Сравнительная таблица

| Параметр | DVC | ClearML Dataset |
| --- | --- | --- |
| Идентификатор версии | Git commit и md5-хэш в data.dvc (например, 957c42d7c9ecafed014287db892a5935.dir) | Dataset ID на сервере (например, 345416da8e98412ba18c09727a9d8efa) и номер версии (1.0.0) |
| Расположение метаданных | Файл data.dvc и .dvc/config внутри Git-репозитория | На сервере ClearML, запрашиваются методами SDK (list_files, get_dependency_graph) |
| Расположение файлов | Локальный .dvc/cache и папка DVC remote (../dvc_remote_kolosov) | На ClearML File Server (files.clear.ml) в архивах и в локальном кэше при скачивании |
| Способ создания дочерней версии | Изменение файлов в папке data/, запуск dvc add data и git commit | Dataset.create с параметром parent_datasets=[base_id], затем add_files, upload и finalize |
| Способ переключения версии | Команда git switch <ветка> и затем dvc checkout | Вызов Dataset.get(dataset_id=...) и скачивание в нужную папку |
| Способ восстановления на чистой машине | git clone репозитория и команда dvc pull | Настройка clearml-init и вызов get_mutable_local_copy по Dataset ID |
| Поведение при ветвлении | Создаются отдельные ветки Git (feature/wine, feature/iris-features) со своими data.dvc | Создаются новые версии (1.1.0 и 2.0.0), у которых в parent_datasets указан один и тот же BASE_ID |
| Поведение при слиянии | git merge веток с помощью DVC merge driver и обновление data.dvc (nfiles: 2) | Создание новой версии с передачей нескольких ID в список parent_datasets |
| Связь версии данных с Git | Прямая: data.dvc хранится в самом Git-коммите | Косвенная: версии живут на сервере отдельно от Git, в отчете нужно вручную записывать Dataset ID |
| Доступность через UI | Нет встроенного UI, проверка через консоль | Доступно в веб-интерфейсе app.clear.ml (видны файлы, lineage, логи и размеры) |

### 15. Вывод

1. Какой объект однозначно определяет версию данных в DVC?
Версию данных задает файл data.dvc — внутри него записан точный MD5-хэш папки data. Когда мы делаем Git-коммит, мы привязываем этот хэш к конкретной точке в истории кода.

2. Почему одного Git-коммита недостаточно без DVC remote?
Git не хранит сами таблицы (папка data/ находится в .gitignore), он запоминает только легкий файл-указатель data.dvc. Если не отправить сами файлы в общее хранилище через dvc push, они останутся только в локальном кэше на компьютере автора, и при клонировании репозитория на другую машину скачать данные будет неоткуда.   

3. Чем Dataset version отличается от Dataset ID в ClearML?
Dataset version (например, 1.0.0) — это просто понятный человеку номер версии, который легко можно продублировать в другом проекте. А Dataset ID (например, 345416da8e98412ba18c09727a9d8efa) — это уникальный системный идентификатор на сервере, по которому всегда можно безошибочно достать нужный слепок данных.   

4. Почему finalize() нельзя считать созданием следующей версии?
Вызов finalize() не создает ничего нового — он просто запечатывает текущую версию, переводя ее в статус Completed. После этого менять файлы в ней больше нельзя. Чтобы сделать новую версию, нужно заново вызвать Dataset.create().   

5. Как доказать, что ClearML version 2.0.0 создана от базы, а не от 1.1.0?
В графе зависимостей (get_dependency_graph()) у версии 2.0.0 единственным родителем числится BASE_ID, а WINE_ID там вообще нет. В списке файлов версии 2.0.0 лежит только iris.csv без wine.csv, и при этом список удаленных файлов (list_removed_files()) пуст. Если бы мы делали ее от 1.1.0, файл wine.csv либо перешел бы по наследству, либо отобразился бы как удаленный.   

6. Что произойдёт, если после git switch не выполнить DVC checkout?
При переключении ветки Git обновит только текстовый файл data.dvc, а сами CSV-таблицы в папке data/ останутся от старой ветки. В итоге рабочая папка разойдется с метаданными, и скрипт будет работать не с теми данными.

7. В каком сценарии этой работы удобнее DVC, а в каком ClearML Dataset?
DVC оказался удобнее, когда нужно вести версии данных параллельно с кодом в Git и сливать разные ветки изменений через git merge. ClearML Dataset удобнее, когда нужно быстро скачать сразу несколько разных версий в отдельные папки по их ID (без постоянных переключений веток туда-сюда) и наглядно посмотреть историю изменений в веб-интерфейсе.