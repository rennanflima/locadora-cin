# language:pt

Funcionalidade: Consulta de acervo

    Cenário: Consulta de acervo por título
    Dado que estou na página de busca da locadora
    Quando digitar pelo nome do filme no campo nome
    E clicar no botão 'Pesquisar'
    Então será exibida a página de resultado

    Cenário: Consulta de acervo por gênero
    Dado que estou na página de busca da locadora
    Quando digitar pelo gênero do filme no campo apropriado
    E clicar no botão 'Pesquisar'
    Então será exibida a página de resultado

    Cenário: Consulta de acervo por ator
    Dado que estou na página de busca da locadora
    Quando digitar pelo ator no campo apropriado
    E clicar no botão 'Pesquisar'
    Então será exibida a página de resultado

    Cenário: Consulta de acervo por nacionalidade
    Dado que estou na página de busca da locadora
    Quando digitar pela nacionalidade do filme no campo apropriado
    E clicar no botão 'Pesquisar'
    Então será exibida a página de resultado
