# RSSFeedParser
Skrypt sprawdza czy istnieje nowy odcinek podcastu na temat języka Python. Jeśli tak to wysłany zostaje email z powiadomieniem. 

Działanie:
1. Przy pierwszym uruchomieniu skryptu, na dysku tworzony i konfigurowane jest plik bazodanowy 'data.db'
2. Skrypt zapisuje do niego kilkanaście ostatnich odcinów znalezionych pod adresem: https://talkpython.fm/episodes/rss
3. Następnie cyklicznie uruchamia się ponowne sprawdzenie czy znaleziono nowy content
4. Jeśli tak to dane nowego podcastu zostają zapisane do bazy
5. Tworzony jest email wysyłany na zdefiniowane wcześniej konto z powiadomieniem
6. Powiadomienie zawiera: Numer odcinka, tytuł a także link do podcastu

UWAGA:
Aby skrypt działał poprawnie wymagane jest uzyskanie kodu autoryzacyjnego dla adresu email Google i wpisanie tych danych do pliku: config.py

