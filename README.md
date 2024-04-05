Интернет магазин для любых товаров 
состоит из приложений usersApp, marketApp, mailingApp

usersApp
в users будет определено:
* модель пользователя с регистрацией по email и дефолтным 0 is_active только после отправки письма на почту is_active == 1
* контроллеры для регистрация, вход, выход, удаление, профиль, редактирование, и список пользователей
* шаблоны входа и регистрации, профиль, удаление, редактирования и списка пользователя
* права доступа 
level 1 (Администратор) - все права в том числе присвоение уровня доступа 
level 2 (Группа менеджеров) - возможность снимать с публикации
товар, доступ к списку публикация и пользователей, заходить в профиль пользователей, создавать категории продуктов
доступ к mailingApp. 
level 3(все авторизованные пользователи) создавать свой продукт, публиковать продукт, редактировать свой продукт, 
добавлять продукт в корзину, заходить в любой продукт и категорию без права редактирования

1) User
* avatar
* first_name 
* last_name
* email
* is_active

marketApp
* модели Category, Product, Version, Cart, Notes, draft
* контроллеры создания редактирования удаления список для всех моделей, а для Product + профиль 
* шаблоны создания удаление список для всех и профиль для product

1) Category
* name 
* description
* photo

2) Cart
* user
* product

3) Notes
* title
* body
* User

4)Version
* name
* description
* Product

5) draft
* user
* Product

6) Product
* name 
* description
* photo
* is_published
* at_created
* at_updated
* country
* owner

mailingApp
отправляет рекламу или сообщение по заданным настройкам пользователям которых выбрал администратор или менеджер
1) massage
* title
* body

2) status
* at_last_send
* status_send
* answer

2) settings
* massage
* at_start
* at_end
* period
* at_send
