# Spotify-Drive

Projeto para baixar músicas do spotify e fazer upload direto para seu Google Drive.

## Configuração

**Apenas na primeira vez** serão necessários algumas configurações para o programa rodas normalmente.

### App Spotify developers

Primeira é necessário criar um app no Spotify developers. Basta ir até a [página](https://developer.spotify.com/dashboard/applications), logar com sua conta do Spotify e clicar em *my new app*.
Dê um nome a ele e uma descrição. 

Ao criar o app, você precisará adicionar seu usuário no app e pegar duas informações, o *client ID* e o *client secret* (clique em show *client secret*). Dentro do spotify.py você colocará essas informações nas seguintes variáveis:
```
client_id = "CHANGE IT"
client_secret = "CHANGE IT"
```
Para adicionar seu usuário basta ir em *user and acces* -> *add new user* -> preencher os campos -> clique em *add*

### Google Drive

Na primeira vez que rodar o programa, já com o app do Spotify Developers configurado, basta seguir os passos de login que o próprio programa irá pedir. **Deixando claro que isso será necessário somente na primeira vez que rodar o programa**

## Utilização
Ao rodar o programa ele irá pedir um nome para a pasta no Google Drive e o link da música/playlist que quer baixar
