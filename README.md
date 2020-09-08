# O que é o script?
Face2Face é um script feito em Python 3 de reconhecimento facial para realizar a comparação de faces humanas. 
O script é baseado em uma biblioteca chamada Face Recognition de Adam Geitgey e pode ser encontrado em "https://github.com/ageitgey/face_recognition".

# Para que serve?
Este projeto visa o estudo de tecnologias de reconhecimento facial em um modelo de machine learning pré-treinado utilizando bibliotecas gratuitas.

# Tecnologias utilizadas
* Python 3;
* Face Recognition;
* Dlib;
* Flask;
* Flask-swagger-ui;
* Numpy;


# Como executar?
 - Temos duas maneiras de executar, uma delas é via CLI (command-line interface) e a outra via API.
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
    ![MenuCli](https://media.githubusercontent.com/media/jeanazuos/Face2Face/cli/static/doc_media/run_cli.gif)

# Links interessantes
Aqui disponibilizo alguns links que julgo relevantes sobre o projeto e a biblioteca principal "Face Recognition":
- Posso retreinar o modelo? -> https://github.com/ageitgey/face_recognition/issues/331
- Reconhecimento facial com Deep Learning -> https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
- Perfil Github do criador da biblioteca -> https://github.com/ageitgey
