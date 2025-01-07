import datetime
import time
import os

import streamlit as st
import pandas as pd
import transformers
import torch


st.set_page_config(
    page_title="Minimal Tech",
    page_icon="🎲", 
    layout="wide"
)

st.title("Minimal Tech")

st.image("src/assets/pixel_logo.png")
st.markdown("""

:blue[O máximo com o mínimo.]

### :green[Quem Somos]

Oferecemos solucoes em dados e tecnologia para atender demandas de alto impacto.

### :green[Objetivo] 


**Valores:**
- **Comprometimento:** Dedicamos nossa energia e habilidades para garantir o sucesso dos nossos clientes.
- **Inovação:** Acompanhamos as tendências e aplicamos o que há de mais avançado em IA.
- **Transparência:** Relacionamentos baseados na ética, clareza e honestidade.
- **Eficiência:** Resolver problemas com soluções diretas, ágeis e eficazes.
- **Parceria:** Trabalhamos lado a lado com nossos clientes, focando em suas necessidades específicas.

---

### Proposta de Valor

A MINIMAL TECH é uma consultoria de inteligência artificial focada em oferecer soluções 100% personalizadas para resolver problemas empresariais reais. Diferente das grandes empresas, nós:

- **Entendemos a fundo sua necessidade** através de um processo de discovery detalhado.
- **Adaptamos nossas soluções** para encaixá-las perfeitamente às suas demandas.
- **Praticamos preços competitivos,** permitindo que empresas de todos os tamanhos usufruam dos benefícios da IA.
- **Garantimos resultados medíveis,** usando cases reais como prova do nosso impacto.

Com a MINIMAL TECH, você não contrata apenas tecnologia, você ganha um parceiro na transformação dos seus processos.

---

### Benefícios de nos Contratar

1. **Customização Total:** Desenvolvemos soluções que atendem às necessidades específicas do seu negócio, indo além de soluções genéricas de mercado.
2. **Preços Agressivos:** Oferecemos valores acessíveis para viabilizar projetos de alto impacto.
3. **Descoberta Detalhada:** Antes de qualquer desenvolvimento, mergulhamos no seu problema para garantir que a solução entregue seja efetiva.
4. **Expertise Combinada:** Nossa equipe une conhecimento técnico profundo em IA com habilidades em gestão de produtos digitais e negociações.
5. **Flexibilidade:** Se necessário, contamos com freelancers para escalar nossa capacidade e garantir prazos.
6. **Transformação Real:** Nossos projetos geram resultados mensuráveis, melhorando processos, reduzindo custos e maximizando o impacto.

---

### Possíveis Cases de Uso

1. **Automatização de Processos:** Reduzir tarefas repetitivas e aumentar a produtividade por meio de IA.
2. **Análise de Dados:** Coletar e interpretar dados de forma inteligente para gerar insights acionáveis.
3. **Chatbots Personalizados:** Melhorar a experiência do cliente com atendentes virtuais eficientes.
4. **Validação e Controle:** Implementar sistemas de verificação automática para aumentar a qualidade e a segurança.
5. **Campanhas de Marketing Baseadas em Dados:** Maximizar o impacto de campanhas utilizando modelos preditivos.
6. **Previsão de Demandas:** Antecipar necessidades de mercado para melhor planejamento e alocação de recursos.

---

### Dados Relevantes sobre IA

- Empresas que utilizam IA aumentam a produtividade em até 40%.
- 77% dos processos corporativos podem ser otimizados com soluções baseadas em IA.
- Negócios que adotam IA alcançam ROI (Retorno sobre Investimento) 3 vezes mais rápido em comparação às empresas que não adotam.

---

"""
)