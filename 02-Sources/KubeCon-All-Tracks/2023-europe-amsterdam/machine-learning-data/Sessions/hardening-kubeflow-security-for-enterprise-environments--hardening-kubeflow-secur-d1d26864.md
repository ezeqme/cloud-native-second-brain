---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Machine Learning + Data"
themes: ["AI ML", "Security", "Storage Data"]
speakers: ["Julius von Kohout", "DPDHL", "Diana Dimitrova Atanasova", "VMware"]
sched_url: https://kccnceu2023.sched.com/event/1HyY8/hardening-kubeflow-security-for-enterprise-environments-julius-von-kohout-dpdhl-diana-dimitrova-atanasova-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Hardening+Kubeflow+Security+for+Enterprise+Environments+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Hardening Kubeflow Security for Enterprise Environments - Julius von Kohout, DPDHL & Diana Dimitrova Atanasova, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Julius von Kohout, DPDHL, Diana Dimitrova Atanasova, VMware
- Schedule: https://kccnceu2023.sched.com/event/1HyY8/hardening-kubeflow-security-for-enterprise-environments-julius-von-kohout-dpdhl-diana-dimitrova-atanasova-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Hardening+Kubeflow+Security+for+Enterprise+Environments+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Hardening Kubeflow Security for Enterprise Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyY8/hardening-kubeflow-security-for-enterprise-environments-julius-von-kohout-dpdhl-diana-dimitrova-atanasova-vmware
- YouTube search: https://www.youtube.com/results?search_query=Hardening+Kubeflow+Security+for+Enterprise+Environments+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wQaOa4Kjxs0
- YouTube title: Hardening Kubeflow Security for Enterprise Environments - Julius Kohout & Diana Dimitrova Atanasova
- Match score: 0.813
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/hardening-kubeflow-security-for-enterprise-environments/wQaOa4Kjxs0.txt
- Transcript chars: 32800
- Keywords: security, namespace, pipelines, actually, containers, default, machine, course, working, companies, please, policies, within, access, authentication, components, cluster, namespaces

### Resumo baseado na transcript

so hello everyone and thank you for being here with us today at kubecon 2023 our talk is about hardening your flow security for Enterprises I'm Diana tanasova a software engineer at vmware's open source program office and I'm currently contributing to the kubeflow project today I have the pleasure to co-present together with Julius bonco heart who is a freelancer a DHL employee and who is contributing to the qflow ecosystem for over two years and he is also a founder of the cubeful security working group so that's

### Excerpt da transcript

so hello everyone and thank you for being here with us today at kubecon 2023 our talk is about hardening your flow security for Enterprises I'm Diana tanasova a software engineer at vmware's open source program office and I'm currently contributing to the kubeflow project today I have the pleasure to co-present together with Julius bonco heart who is a freelancer a DHL employee and who is contributing to the qflow ecosystem for over two years and he is also a founder of the cubeful security working group so that's enough for us or do you want to say something quite a few and okay maybe here and how many of you are planning to use kubeflow okay really the mining part everybody got their hands up amazing so yeah okay so we still will do here is the agenda so we will still do an overview of what Q4 project is and we will try to share the answers of who is using q102i uh then we will do a short introduction of the security working group we will share its main goals and initiatives then you to make sure that we are on the same page we will do an overview of the Q4 architecture and then we will share um we will discuss the authentication flow of kubernetes of cube flow then follows the interesting part we would have a discussion of different various security issues and we will end up with the conclusion we will wrap it up so what is keep flow keep flow is an open source machine learning cooperation platform based on kubernetes it enables data scientists and machine learning Engineers to build scale deploy orchestrate their machine learning workflows it tries to standardize and automate the iterative nature of machine learning workflow we can see a q flow as an orchestrator of commonly used machine learning platforms like Q4 pipelines which are reusable modular can be shared across the teams you can do hyper parameter tuning things to the cat component you can surf your model right in the cube flow thanks to the caser component users can spin up their favorite Ides they can do they can easily track their lineage of their pipelines and models and Etc the cube flow is it comprises of different components and it also has integration with different machine learning Frameworks like tensorflow by torch and very important is that it's abstract away the complexity of kubernetes so to summarize coupon helps teams to streamline their Pro their work it improves the collaboration it has it has a multi-ten tenancy support and as how it speeds up the time for developing their
