> 🟢 **Live Demo:** [Clique aqui para acessar o Dashboard Interativo](https://sports-analytics-portfolio-acawxiqbei6nufak6app6nq.streamlit.app/)

## Criação de um dashboard interativo para análise estratégica de um projeto de jogadores sub-17 ##

Dados foram gerados de maneira fictícia, já que esse projeto foi para apresentação na ARS Academy - empresa iniciando o processo
de desenvolvimento de jogadores com foco em negociações com o futebol europeu, já que sua sede é na Polônia.

Portanto, todos os dados dos CSVs importados no código são fictícios, desde estatísticas de jogo - ABA 1 Perfil Técnico Consolidado
à telemetria de GPS - ABA 2 Telemetria Física e GPS.

## ABA 1 ##
<img width="1386" height="675" alt="image" src="https://github.com/user-attachments/assets/8fd16052-36a1-415d-87e0-933a03c6871f" />

## ABA 2 ##
<img width="1342" height="754" alt="image" src="https://github.com/user-attachments/assets/40c918e6-4a97-4f56-90ce-543b7641f7d4" />

## 🚀 Funcionalidades Principais

O dashboard foi projetado para que diferentes níveis da comissão técnica tomem decisões rápidas:
* **Filtro Dinâmico por Atleta:** Atualização de todas as métricas táticas e físicas de acordo com o jogador selecionado.
* **Gráfico de Radar Interativo (Scout):** Separação visual clara entre métricas ofensivas/criação e defensivas/combate, facilitando a identificação do perfil do atleta (Percentil vs. Média da Categoria).
* **Mapeamento de Ambidestria:** Análise do volume de passes com o pé dominante e não dominante para avaliar a previsibilidade do jogador sob pressão.
* **Telemetria Física Integrada:** Monitoramento de carga com distância total percorrida e sprints de alta intensidade.
* **Mapa de Calor de Ocupação Espacial:** Visualização através de densidade das zonas de maior atividade do atleta no campo.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python** (Linguagem base)
* **Streamlit** (Construção da interface web e deploy)
* **Plotly** (Gráficos de radar dinâmicos e interativos)
* **Pandas & Openpyxl** (Manipulação, tratamento e leitura das bases de dados em Excel/CSV)
* **Mplsoccer & Matplotlib** (Renderização do campo de futebol oficial e plotagem do mapa de calor do GPS)

## 📊 Métricas Analisadas no Dashboard

Para alinhar a análise ao mercado atual, o painel monitora KPIs estratégicos de desempenho:
* **Ofensivas/Criação:** xG (Gols Esperados), Ações na Área Rival, Passes para o Terço Final, Passes Progressivos e Conduções Progressivas.
* **Defensivas/Combate:** Recuperações no Terço Rival, Duelos Ganhos (%), Interceptações e Desarmes.

## 💻 Como Rodar o Projeto Localmente

Se desejar clonar o repositório e executar o painel na sua máquina, siga os passos abaixo no terminal:

1. Clone o repositório:
   ```bash
   git clone [https://github.com/jeancarlocorreia/sports-analytics-portfolio.git](https://github.com/jeancarlocorreia/sports-analytics-portfolio.git)

2. Acesse a pasta do projeto:
   ```bash
   cd sports-analytics-portfolio

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt

4. Execute a aplicação do Streamlit
   ```bash
   streamlit run app2.py

## 👋 Desenvolvido por Jeancarlo Camargo Correia - Contato www.linkedin.com/in/jeancarlocamargo

