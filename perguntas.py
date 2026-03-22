import streamlit as st


@st.cache_data
def carregar_perguntas():
    return [
        {
            "pergunta": "O que é o Scrum?",
            "opcoes": [
                "Uma metodologia rígida de desenvolvimento",
                "Um conjunto de ferramentas de gestão tradicional",
                "Um framework ágil para desenvolvimento de produtos complexos",
                "Uma linguagem de programação"
            ],
            "resposta_correta": 2,
            "explicacao": "Scrum é um framework ágil, leve, iterativo e incremental."
        },
        {
            "pergunta": "Qual dos itens abaixo NÃO é um valor do Scrum?",
            "opcoes": ["Coragem", "Foco", "Hierarquia", "Comprometimento"],
            "resposta_correta": 2,
            "explicacao": "Os valores do Scrum são: coragem, foco, comprometimento, respeito e abertura."
        },
        {
            "pergunta": "Em qual guia são definidos os princípios e práticas do Scrum?",
            "opcoes": ["Scrum Manifesto", "Scrum Guide", "Agile Book", "Sprint Manual"],
            "resposta_correta": 1,
            "explicacao": "O Scrum Guide é o guia oficial do framework."
        },
        {
            "pergunta": "O Scrum é baseado em qual abordagem?",
            "opcoes": ["Cascata", "Iterativa e incremental", "Prototipagem rápida", "Processo linear"],
            "resposta_correta": 1,
            "explicacao": "Scrum entrega valor por meio de ciclos iterativos e incrementais chamados Sprints."
        },
        {
            "pergunta": "Qual é a duração máxima recomendada para uma Sprint?",
            "opcoes": ["1 mês", "3 meses", "2 dias", "6 semanas"],
            "resposta_correta": 0,
            "explicacao": "A Sprint deve durar no máximo 1 mês."
        },
        {
            "pergunta": "Qual é o papel responsável por maximizar o valor do produto?",
            "opcoes": ["Scrum Master", "Time de Desenvolvimento", "Product Owner", "Gerente de Projeto"],
            "resposta_correta": 2,
            "explicacao": "O Product Owner é o responsável por maximizar o valor do produto."
        },
        {
            "pergunta": "Qual das responsabilidades abaixo pertence ao Scrum Master?",
            "opcoes": [
                "Gerenciar o projeto",
                "Garantir que o Scrum seja compreendido e aplicado",
                "Priorizar o backlog",
                "Codificar funcionalidades"
            ],
            "resposta_correta": 1,
            "explicacao": "O Scrum Master garante a aplicação do framework Scrum."
        },
        {
            "pergunta": "O time de desenvolvimento no Scrum é responsável por:",
            "opcoes": [
                "Revisar o backlog",
                "Criar incrementos funcionais a cada sprint",
                "Validar os testes do usuário",
                "Aprovar o orçamento"
            ],
            "resposta_correta": 1,
            "explicacao": "O time constrói e entrega incrementos funcionais do produto."
        },
        {
            "pergunta": "Quantas pessoas geralmente compõem um Time Scrum (Dev Team)?",
            "opcoes": ["De 3 a 9 pessoas", "De 1 a 3 pessoas", "Mais de 10 pessoas", "Apenas 1 pessoa"],
            "resposta_correta": 0,
            "explicacao": "O ideal é de 3 a 9 desenvolvedores para promover colaboração e agilidade."
        },
        {
            "pergunta": "Quem decide quando uma tarefa está “pronta”?",
            "opcoes": [
                "Product Owner",
                "Scrum Master",
                "Time de Desenvolvimento, com base na Definition of Done",
                "Cliente"
            ],
            "resposta_correta": 2,
            "explicacao": "A Definition of Done é acordada pelo time e usada para validar entregas."
        },
        {
            "pergunta": "O que é realizado na Daily Scrum?",
            "opcoes": [
                "Entrega do produto",
                "Priorização do backlog",
                "Reunião diária de 15 minutos para inspecionar e planejar o dia",
                "Testes de regressão"
            ],
            "resposta_correta": 2,
            "explicacao": "A Daily Scrum é uma reunião rápida para alinhamento diário."
        },
        {
            "pergunta": "O que acontece no Sprint Review?",
            "opcoes": [
                "O Product Owner aprova o projeto",
                "O cliente valida o produto entregue",
                "O time apresenta o incremento ao cliente e stakeholders",
                "O Scrum Master define novas tarefas"
            ],
            "resposta_correta": 2,
            "explicacao": "É a reunião de demonstração e coleta de feedback do produto."
        },
        {
            "pergunta": "Qual é o objetivo da Sprint Retrospective?",
            "opcoes": [
                "Corrigir erros técnicos",
                "Planejar novas funcionalidades",
                "Refletir e melhorar o processo de trabalho",
                "Avaliar performance individual"
            ],
            "resposta_correta": 2,
            "explicacao": "A Retrospectiva busca melhorias no processo de trabalho da equipe."
        },
        {
            "pergunta": "Qual evento dá início à Sprint?",
            "opcoes": ["Daily", "Sprint Planning", "Sprint Review", "Grooming"],
            "resposta_correta": 1,
            "explicacao": "A Sprint Planning define o objetivo e os itens do backlog que serão trabalhados."
        },
        {
            "pergunta": "Quem participa da Sprint Planning?",
            "opcoes": [
                "Apenas o Product Owner",
                "Apenas o time de desenvolvimento",
                "Product Owner, Scrum Master e Time de Desenvolvimento",
                "O cliente"
            ],
            "resposta_correta": 2,
            "explicacao": "Todos os membros do Scrum participam da Sprint Planning."
        },
        {
            "pergunta": "O que é o Product Backlog?",
            "opcoes": [
                "Lista de bugs",
                "Lista de tarefas para o Scrum Master",
                "Lista priorizada de requisitos e funcionalidades do produto",
                "Agenda das reuniões"
            ],
            "resposta_correta": 2,
            "explicacao": "O Product Backlog contém tudo o que precisa ser feito no produto."
        },
        {
            "pergunta": "O que representa o Sprint Backlog?",
            "opcoes": [
                "Conjunto de sprints anteriores",
                "Lista de pendências financeiras",
                "Itens selecionados para a Sprint atual",
                "Tarefas feitas no trimestre"
            ],
            "resposta_correta": 2,
            "explicacao": "É a lista dos itens do Product Backlog que foram selecionados para a Sprint."
        },
        {
            "pergunta": "O que é o Incremento no Scrum?",
            "opcoes": [
                "Resultado da Retrospectiva",
                "Documento de planejamento",
                "Conjunto de todos os itens do backlog entregues em uma Sprint",
                "Total de tarefas não entregues"
            ],
            "resposta_correta": 2,
            "explicacao": "O Incremento é a soma de todos os entregáveis da Sprint, prontos para entrega."
        },
        {
            "pergunta": "Qual artefato define o que é considerado “pronto”?",
            "opcoes": ["Burn-down Chart", "Sprint Goal", "Definition of Done", "Product Backlog"],
            "resposta_correta": 2,
            "explicacao": "A Definition of Done é o critério para aceitar uma entrega como completa."
        },
        {
            "pergunta": "O que é o Sprint Goal?",
            "opcoes": [
                "Objetivo estratégico da empresa",
                "Meta de desempenho do time",
                "Meta da Sprint que orienta o trabalho da equipe",
                "Valor estimado do produto"
            ],
            "resposta_correta": 2,
            "explicacao": "O Sprint Goal é o objetivo comum da Sprint e guia o trabalho do time."
        }
    ]
