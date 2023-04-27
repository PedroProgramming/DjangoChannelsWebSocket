# DjangoChannelsWebSocket

# Gerenciamento de Eventos

# Inicilização do para testar django-channels

# 1 - Excluir pasta 'venv'

      Criar outra utilizando: 
           Windows: python -m venv venv
           Linux: python3 -m venv venv
           
      Ativar 'venv'
           Windows: venv/Scripts/Activate
           Linux: source venv/bin/activate.

# 2 - Bibliotecas fornecidas - 'requirements.txt'
      Para instalar todas de uma só vez, basta digitar no seu terminal: 
      
      Windows: pip install -r requirements.txt
      Linux: python3 install -r requirements.txt
  
# 3 - Área administrativa
      Entrar na área administrativa para crair salas
      
      - Abra o terminal no vsCode
      - Windows: python manage.py createsuperuser
      - linux: python3 manage.py createsuperuser
      
      username: obrigatório (será logado por ele)
      e-mail: pode ignorar
      password: obrigatório
      
      - Rodar server:
           python manage.py runserver
           
      - abrir google(ou outro navegador)
          url: 127.0.0.1:8000/admin/
          
          - colocar username e password
          - vá em salas e crie uma nova
          - acesse url: 127.0.0.1:8000/entrar/
              depois só abrir outro navegado e trocar mensagens
          
 
 # Á seguir, explicação:

# Oque é Django?

      O Django é um framework web full stack open source (código aberto) baseado em Python, gratuito e de alto nível.
      Este framework foi criado com o objetivo de resolver todos os problemas mais comuns do processo de desenvolvimento de aplicações web
      como por exemplo autenticação, rotas, object relational mapper (ORM) e até migrations.

# Oque é Django-channels (canais)

      Por mais de uma década após o Django ter sido lançado em 2005, as páginas eram em sua maioria estáticas, AJAX era usado apenas em casos de uso limitados e as coisas eram relativamente simples.
      Nos últimos cinco anos, os aplicativos da web em tempo real evoluíram, tendendo para mais interação cliente-servidor e ponto a ponto.
      Este tipo de comunicação é alcançável com WebSockets , um novo protocolo que fornece comunicação full-duplex e mantém uma conexão aberta e persistente entre cliente e servidor.

      Channels Django facilita o suporte a WebSockets no Django de uma maneira semelhante às visualizações HTTP tradicionais.
      Ele envolve o suporte de visualização assíncrona nativa do Django, permitindo que os projetos do Django lidem não apenas com HTTP,
      mas também com protocolos que requerem conexões de longa duração, como WebSockets, MQTT, chatbots, etc.

 # Oque é WebSocket?
 
      WebSocket é uma tecnologia avançada para criar uma ligação entre um cliente e um servidor (browser e servidor) e permitir a comunicação entre eles em tempo real.
      A principal diferença com o WebSocket é que permite receber dados sem ter de enviar um pedido separado, como, por exemplo, acontece no HTTP.
      Uma vez estabelecida a ligação, os dados virão por si mesmos sem necessidade de enviar o pedido.
      
      # Como funciona o WebSockets?
      
      A ligação entre cliente e servidor permanece aberta até ser terminada por uma das partes ou ser encerrada por um timeout. Eles executam um aperto de mão para estabelecer uma ligação entre o cliente e o servidor. 
      Uma ligação estabelecida permanece aberta, e a comunicação é efectuada utilizando o mesmo canal até que a ligação seja terminada no lado do cliente ou do servidor.
      As mensagens são trocadas bidireccionalmente. O WebSocket permite encriptar os dados que são transmitidos.
 
# Pedro Dev | 2023
