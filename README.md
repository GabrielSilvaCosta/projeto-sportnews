Resumo do Projeto "News"

O projeto "News" é uma aplicação web que gerencia notícias, categorias e usuários. Foi desenvolvido utilizando o framework Django para o backend, incluindo Django REST Framework para a criação de uma API, e templates HTML para o frontend.

Tecnologias Utilizadas:

Django: Um framework web em Python que facilita o desenvolvimento rápido e limpo de aplicações.

Django REST Framework (DRF): Uma extensão poderosa do Django para construção de APIs.

HTML e Templates Django: Para a criação das páginas web e a exibição dinâmica de dados.

Banco de Dados MySQL: utilizamos o banco de dados MYSQL como banco de dados da nossa aplicação

Modelos: Foram criados modelos para Category (categorias), User (usuários) e News (notícias) no backend.

Validação de Dados: Foi implementada uma validação customizada para o título das notícias, garantindo que contenham pelo menos duas palavras.

API Django REST Framework: Foram criadas APIs para os modelos Category, User e News utilizando o Django REST Framework. Cada API fornece operações CRUD básicas.

Serializadores: Foram criados serializadores para transformar objetos Python em formatos que podem ser facilmente renderizados em JSON, essenciais para as APIs.

Views Django e APIs: Foram criadas views Django para renderizar páginas HTML, e views baseadas em classes para manipular requisições e respostas da API.

Templates HTML: Foram criados templates HTML para a exibição de páginas como a página inicial, detalhes da notícia e formulários de criação de notícias.

Formulários Django: Foram criados formulários Django para as entidades Category e News, facilitando a coleta de dados do usuário.

Integração de Mídia: Adicionou-se a capacidade de fazer upload de imagens para as notícias.

Roteamento e URLs: Configurou-se roteamento e URLs para diferentes páginas e APIs utilizando o Django.

Static Files: Gerenciou-se arquivos estáticos como folhas de estilo CSS.

Observações:

O projeto segue as melhores práticas do Django, como organização de código em apps separados, uso de migrações para evolução do banco de dados, e configuração de URLs.
