---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Doron Caspin", "Valentina Rodriguez Sosa", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27Fcr/aligning-enterprise-ai-security-with-mitre-atlas-using-open-source-technologies-doron-caspin-valentina-rodriguez-sosa-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Aligning+Enterprise+AI+Security+With+MITRE+ATLAS+Using+Open+Source+Technologies+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Aligning Enterprise AI Security With MITRE ATLAS Using Open Source Technologies - Doron Caspin & Valentina Rodriguez Sosa, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Doron Caspin, Valentina Rodriguez Sosa, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27Fcr/aligning-enterprise-ai-security-with-mitre-atlas-using-open-source-technologies-doron-caspin-valentina-rodriguez-sosa-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Aligning+Enterprise+AI+Security+With+MITRE+ATLAS+Using+Open+Source+Technologies+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Aligning Enterprise AI Security With MITRE ATLAS Using Open Source Technologies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fcr/aligning-enterprise-ai-security-with-mitre-atlas-using-open-source-technologies-doron-caspin-valentina-rodriguez-sosa-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Aligning+Enterprise+AI+Security+With+MITRE+ATLAS+Using+Open+Source+Technologies+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Va45Tx0RifI
- YouTube title: Aligning Enterprise AI Security With MITRE ATLAS Using Op... Doron Caspin & Valentina Rodriguez Sosa
- Match score: 0.804
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/aligning-enterprise-ai-security-with-mitre-atlas-using-open-source-tec/Va45Tx0RifI.txt
- Transcript chars: 27951
- Keywords: security, models, cluster, course, policies, attack, container, process, runtime, creating, network, source, session, protect, processes, identity, coming, working

### Resumo baseado na transcript

I know it's hard to be on the last session but we'll try to make it short and interesting and uh feel free to ask question during this session. We are not we try to do to be interactive as we can and let's start right Valentina go ahead introduce yourself. We are focused on AI security all kind of a mil malicious attempt to harm our models or and how to protect AI models from people of course and people and processes and of course AI processes that try to harm other AI systems. So we are seeing of course you see everywhere AI is exponential race exponential rise a lot of AI models a lot of LLM models deploy in Kubernetes or other models most of the LLMs that you see out there in the in the wild are deploy on Kubernetes we have additional capabilities that keep exploring LLMD other tools that come bring VLM that bring easier way to deploy LLM models on on Kubernetes and we have our traditional way to protect our Kubernetes environment and again these tools are not enough are not enough to to protect our LML models and we need to attack and build a model around how we really protect the AI model as part of our story of of the the the evaluation of of security and um yeah

### Excerpt da transcript

Thank you for coming for for this le for this session. I know it's hard to be on the last session but we'll try to make it short and interesting and uh feel free to ask question during this session. We are not we try to do to be interactive as we can and let's start right Valentina go ahead introduce yourself. >> Yeah of course um so I'm Valentina Rodriguez. I'm a principal architect at Red Hat. I'm also a Qflow project maintainer. >> I'm Dan Kaspin. I'm product manager at Treat currently managing the security products and um working with Valentina on different projects and you know all the AI AI issues AI stuff are coming our way and we try to find things and make some order in our world and in our today's session so it's this session come from from real world problems so we try to understand the problem, try to understand the issues and um so and we'll talk about this is our agenda today. We talk about AI safety versus AI security. We talk we talk about meter attack and meter um atlas the two frameworks that leading the market today.

all kind of other AI framework um risk convergence between AI and regular security um all kind of open source tooling that can help us uh support and protect our AI workloads and of course demo in the end and um I hope we'll have a lot of time for demos and questions. So let's start. Okay, this session is about mostly about I don't want to we don't want to confuse between AI security and safety. So AI safety is all about unintended harm, right? We try to ask question for for LLM model and we get the wrong answers or giving a toxic output or we try to ask questions that are not really something that are legit, right? >> [snorts] >> So and um this is all about AI safety and this is not the area that we try to to address today. It's complicated and it's um again not in the area or most of us as a techn technologies handle on the day today. Of course there are tools that we try to use but it's not focused today. We are focused on AI security all kind of a mil malicious attempt to harm our models or and how to protect AI models from people of course and people and processes and of course AI processes that try to harm other AI systems.

H so our focus today is aligning with meter atlas. I will talk about meter atlas a little bit what is all about and how we can use it for our benefit. So we are seeing of course you see everywhere AI is exponential race exponential rise a lot of AI models a lot of LLM models deploy in Kubernetes o
