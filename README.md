# Клиентно и серверное взаимодействие
Клиент и сервер взаимодействую друг с другом в сети Интернет или в любой другой компьютерной сети 
при помощи различных сетевых протоколов, например, IP протокол, HTTP протокол, FTP и другие. Протоколов 
на самом деле очень много и каждый протокол позволяет оказывать ту или иную услугу. Например, при помощи 
HTTP протокола браузер отправляет специальное HTTP сообщение, в котором указано какую информацию и в каком
виде он хочет получить от сервера, сервер, получив такое сообщение, отсылает браузеру в ответ похожее по структуре
сообщение (или несколько сообщений), в котором содержится нужная информация, обычно это HTML документ.

Сообщения, которые посылают клиенты получили названия HTTP запросы. Запросы имеют специальные методы, которые
говорят серверу о том, как обрабатывать сообщение. А сообщения, которые посылает сервер получили название HTTP ответы,
они содержат помимо полезной информации еще и специальные коды состояния, которые позволяют браузеру узнать то, как 
сервер понял его запрос.
Сейчас мы схематично описали, как взаимодействуют клиент и сервер на седьмом уровне модели OSI, но, на самом деле это
взаимодействие происходит на всех семи уровнях. Когда клиент отправляет запрос, сообщение упаковывается, можно представить,
что сообщение заворачивается в семь оберток (хотя их может быть намного больше или же меньше), а когда сообщение получает
сервер, он начинает эти обертки разворачивать.
Также стоит заметить, что в основе взаимодействия клиент-сервер лежит принцип того, что такое взаимодействие начинает клиент,
сервер лишь отвечает клиенту и сообщает о том может ли он предоставить услугу клиенту и если может, то на каких условиях. 
Клиентское программное обеспечение и серверное программное обеспечение обычно установлено на разных машинах, но также они могут
работать и на одном компьютере.

Данная концепция взаимодействия была разработана в первую очередь для того, чтобы разделить нагрузку между участниками процесса
обмена информацией, а также для того, чтобы разделить программный код поставщика и заказчика.

В даном разделе расположены мои решения разных задач при реализации клиент серверных взаимодействий.
