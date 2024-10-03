# Trabalho 1

Simples exemplo de script para escaneamento de portas em uma máquina.

## Autores

- Lucas Ferreira de Almeida - 11262063

## Características do sistema

- Arquitetura x86-64
- Sistema operacional Ubuntu 22.04 LTS
- Processador AMD Ryzen 5 2600 Six-Core
- 2x Memória RAM 8GB 2666MhZ

## Dependências

- [Python 3.10.12](https://www.python.org/downloads/)

## Download

Para fazer o download do script de escaneamento de portas, execute:

```bash
curl https://raw.githubusercontent.com/lalmeida32/ssc0901/refs/heads/main/trabalho-1/scan.py -o scan.py
```

Para fazer o download do script que simula um servidor HTTP simples, execute:

```bash
curl https://raw.githubusercontent.com/lalmeida32/ssc0901/refs/heads/main/trabalho-1/http-server.py -o http-server.py
```

## Executando

Para realizar somente o escaneamento de portas, execute, após baixar o script de escaneamento de portas:

```bash
python scan.py
```

Para executar um servidor HTTP simples na porta 8080 e testar o script de escaneamento de portas, execute em um terminal:

```bash
python http-server.py
```

OBS: Para cancelar a execução deste servidor, selecione o terminal onde ele está executando e aperte as teclas CTRL + C ou CMD + C.

Em outro terminal, execute:

```bash
python scan.py
```

Você pode alterar, dentro do script `http-server.py`, a porta 8080 para a porta 80. No entanto, talvez seja necessário executar este script como administrador.
