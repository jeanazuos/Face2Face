# O que é o script?
Face2Face é um script feito em Python 3 de reconhecimento facial para realizar a comparação de faces humanas. 
O script é baseado em uma biblioteca chamada Face Recognition de Adam Geitgey e pode ser encontrado em "https://github.com/ageitgey/face_recognition".

# Para que serve?
Este projeto visa o estudo de tecnologias de reconhecimento facial em um modelo de machine learning pré-treinado utilizando bibliotecas gratuitas.

# Tecnologias utilizadas
* Python 3;
* Docker;
* Face Recognition;
* Dlib;
* Flask;
* Flask-swagger-ui;
* Numpy.


# Como executar?
 - Temos duas maneiras de executar, uma delas é via CLI (command-line interface) e a outra via API.

## API - Docker
 * Clone o repositório e entre no diretório raiz;
 * Faça o build da imagem com `docker build . -t face2face/flask:last_edition`;
 * Execute a imagem `docker run -d -p 5005:5000 face2face/flask:last_edition`;
 * Obs.: (*O nome da imagem pode ser alterado, este é apenas um exemplo);
 * Você pode conferir se a aplicação está de pé com o comando docker ps:
 * ![DockerUp](https://media.githubusercontent.com/media/jeanazuos/Face2Face/master/static/doc_media/docker_up.png)
 * Para acessar a url de teste você pode acessar através do seu navegador a url `http://0.0.0.0:5005/test` onde o valor `5005` representa a porta definida quando rodamos o container;

### Verificando faces através da API - Docker
 Após executar a aplicação através do docker, podemos enviar fotos de rostos humanos para serem comparados.
 Utilizamos o verbo 'POST' para enviarmos as imagens e através dele recebemos um payload com dois valores em caso de sucesso. Em nosso exemplo vamos utilizar o Postman para realizarmos essa requisição (o software pode ser encontrado para download gratuito em "https://www.postman.com/downloads/").
#### Montando a requisição via Postman
* Após ter realizado o download, abra o software (Postman) e crie a seguinte estrutura:
 * ![PostmanExamplePost](https://media.githubusercontent.com/media/jeanazuos/Face2Face/master/static/doc_media/postman_post_example.png)
* Resultado da requisição, em caso de sucesso é retornado um json contendo a informação de que foram encontrados as faces e se elas dão match:
 * ![PostmanExamplePostSuccess](https://media.githubusercontent.com/media/jeanazuos/Face2Face/master/static/doc_media/postman_post_result.png)

##### Observações:
* Lembrando que a porta `5005`é um exemplo e vai de acordo com o que você montou ao rodar o Docker nos passos anteriores.
* São aceitas as extensões: "png, jpg, jpeg e gif".
* É possível fazer comparação entre apenas duas imagens e obrigatóriamente elas devem possuir a face humana.
* Imagens que possuem mais de uma pessoa ainda não são tratadas, portanto, provavelmente a comparação poderá ser falha. (Isso é um ponto de melhoria).
* Foi implementado Swagger como documentação de apoio, acesse o endpoint `http://localhost:5005/swagger/`.
 
## (CLI)
 * Clone o repositório e entre no diretório raiz;
 * Crie um arquivo do tipo `.env` e insira o conteúdo presente no tópico "Variáveis de ambiente";
 * Instale as dependências do requirements.txt com `pip install -r requirements.txt`;
 * Acesse o diretório `cli/TESTE_DE_BIOMETRIA_FACIAL`;
 * Crie uma pasta respeitando a nomenclatura das já existentes, por exemplo `Item_4`;
 * Insira na pasta criada os arquivos a serem comparados respeitando a nomenclatura `Imagem_1.JPG` e `Imagem_2.JPG`;
   - Nota 1: Faça esse procedimento para todos os itens que deseja comparar, sempre criando um diretório para cada conjunto de comparações.
   - Nota 2: A comparação deverá sempre ser feita entre apenas 2 (dois) arquivos.
 * Volte para o diretório `cli` e execute o comando `python cli.py`;
 * Ao rodar a aplicação você será direcionado para um menu principal onde poderá inserir o nome da pasta que deseja analisar:
  * ![MenuCli](https://media.githubusercontent.com/media/jeanazuos/Face2Face/cli/static/doc_media/run_cli.gif)

# Variáveis de ambiente
`
ALLOWED_EXTENSIONS="{'png', 'jpg', 'jpeg', 'gif'}"
MAX_CONTENT_LENGTH=16777216
CLI_MAIN_PATH_CHECK="TESTE_DE_BIOMETRIA_FACIAL"
CLI_DEFAULT_IMAGE_NAME_ONE="Imagem_1.JPG"
CLI_DEFAULT_IMAGE_NAME_TWO="Imagem_2.JPG"
FLASK_PORT_API=5000
`

# Links interessantes
Aqui disponibilizo alguns links que julgo relevantes sobre o projeto e a biblioteca principal "Face Recognition":
- Posso retreinar o modelo? -> https://github.com/ageitgey/face_recognition/issues/331
- Reconhecimento facial com Deep Learning -> https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
- Perfil Github do criador da biblioteca -> https://github.com/ageitgey
