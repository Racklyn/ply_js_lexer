# Analisador Léxico JS (básico) com PLY

Criação de um analisador léxico básico para a linguagem JavaScript. O analisador foi criado com a biblioteca PLY, em Python. <br>
O analisador reconhece apenas os tokens presentes no seguinte código JavaScript:
```js
function calc(op, a, b){
    if(op == "soma"){
        return a+b;
    }else if(op == "sub"){
        return a-b;
    }else if(op == "multi"){
        return a*b;
    }else if(op == "div"){
        return a/b;
    }
}

let operacoes = ["soma", "sub", "multi", "div"];

for(var i = 0; i < operacoes.length; i++ ){
    console.log(calc(operacoes[i], 10, 2))
}
```

## Executando:
1. Clone este repositório em sua máquina.
2. Para rodar, é necessário ter **Python3** e a biblioteca **Ply** instalados.
3. Para instalar a biblioteca Ply, você pode rodar o seguinte comando:
  ```shell
  pip install ply
  ```
4. Execute o programa navegando até o diretório clonado e rodando:
  ```shell
  python3 main.py
  ```
