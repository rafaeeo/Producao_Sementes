# Dashboard de Produção de Sementes

Este projeto é um dashboard interativo desenvolvido com Streamlit e Plotly para visualizar e analisar dados de produção de sementes. O dashboard permite filtrar os dados por várias categorias e exibir gráficos que ajudam a entender a sazonalidade das colheitas, a tendência da produção ao longo dos anos e o impacto das categorias na produtividade média.

## Funcionalidades

- **Filtros Interativos**: Filtre os dados por categoria, espécie, safra, estado (UF) e cidade.
- **Gráficos Interativos**:
  - Sazonalidade das Colheitas
  - Tendência da Produção Agrícola ao Longo dos Anos
  - Impacto da Categoria na Produtividade Média

## Instalação

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/rafaeeo/Producao_Sementes.git
   cd Producao_Sementes
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Certifique-se de que o arquivo sigefcamposproducaodesementes.xlsx esteja no diretório do projeto.

## Uso

1. Execute o aplicativo Streamlit:
   ```bash
   streamlit run dashboard.py

2.Abra o navegador e acesse http://localhost:8501 para visualizar o dashboard.

## Estrutura do Projeto

dashboard.py: Código principal do dashboard.
sigefcamposproducaodesementes.xlsx: Arquivo de dados utilizado no dashboard.
requirements.txt: Lista de dependências do projeto.
Filtros Disponíveis
Categoria: Filtre os dados por diferentes categorias de sementes.
Espécie: Filtre os dados por espécies específicas de sementes.
Safra: Filtre os dados por anos de safra.
Estado (UF): Filtre os dados por estados brasileiros.
Cidade: Filtre os dados por cidades específicas.
Gráficos Disponíveis
Sazonalidade das Colheitas: Exibe a quantidade de colheitas por mês.
Tendência da Produção Agrícola ao Longo dos Anos: Exibe a produção bruta ao longo dos anos de safra.
Impacto da Categoria na Produtividade Média: Exibe a produtividade média por categoria.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o projeto.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

### Download do README.md

Você pode baixar o arquivo `README.md` clicando [aqui](sandbox:/mnt/data/README.md).

Seguindo esses passos, você conseguirá resolver o problema de push e atualizar o repositório no GitHub com o novo `README.md`.
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
