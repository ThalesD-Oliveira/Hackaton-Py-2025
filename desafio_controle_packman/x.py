import asyncio
import websockets

async def conectar_websocket():
    # Define o endereço do servidor
    uri = "ws://192.168.1.101:8765"
    
    print(f"Tentando conectar a {uri}...")

    try:
        # Abre a conexão com o servidor
        async with websockets.connect(uri) as websocket:
            print("Conectado com sucesso!")

            # Exemplo: Enviar uma mensagem para o servidor
            mensagem_envio = "Olá, Servidor!"
            await websocket.send(mensagem_envio)
            print(f"> Enviado: {mensagem_envio}")

            # Exemplo: Aguardar e receber uma resposta do servidor
            # O script vai pausar aqui até receber algo
            resposta = await websocket.recv()
            print(f"< Recebido: {resposta}")

            # O loop abaixo manteria a conexão viva ouvindo continuamente:
            # while True:
            #     msg = await websocket.recv()
            #     print(f"Recebido: {msg}")

    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar. O servidor está rodando neste IP e porta?")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executa o loop de eventos assíncronos
if __name__ == "__main__":
    asyncio.run(conectar_websocket())