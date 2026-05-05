---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Jianbo Sun", "Da Yin", "Alibaba Cloud"]
sched_url: https://kccnceu2023.sched.com/event/1K8nU/challenges-of-modern-application-delivery-a-retrospection-of-kubevela-highlight-technologies-jianbo-sun-da-yin-alibaba-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Challenges+of+Modern+Application+Delivery%3A+A+Retrospection+of+KubeVela+Highlight%C2%A0Technologies+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Challenges of Modern Application Delivery: A Retrospection of KubeVela Highlight Technologies - Jianbo Sun & Da Yin, Alibaba Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jianbo Sun, Da Yin, Alibaba Cloud
- Schedule: https://kccnceu2023.sched.com/event/1K8nU/challenges-of-modern-application-delivery-a-retrospection-of-kubevela-highlight-technologies-jianbo-sun-da-yin-alibaba-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Challenges+of+Modern+Application+Delivery%3A+A+Retrospection+of+KubeVela+Highlight%C2%A0Technologies+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Challenges of Modern Application Delivery: A Retrospection of KubeVela Highlight Technologies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1K8nU/challenges-of-modern-application-delivery-a-retrospection-of-kubevela-highlight-technologies-jianbo-sun-da-yin-alibaba-cloud
- YouTube search: https://www.youtube.com/results?search_query=Challenges+of+Modern+Application+Delivery%3A+A+Retrospection+of+KubeVela+Highlight%C2%A0Technologies+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ozsV6N7XNwY
- YouTube title: Challenges of Modern Application Delivery: A Retrospection of KubeVela Highli... Jianbo Sun & Da Yin
- Match score: 0.94
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/challenges-of-modern-application-delivery-a-retrospection-of-kubevela/ozsV6N7XNwY.txt
- Transcript chars: 23666
- Keywords: application, control, component, resources, covella, delivery, applications, version, resource, fields, platform, provides, deploy, deployment, google, definitions, possible, connect

### Resumo baseado na transcript

hello everyone engineer from Alibaba today I and my colleague girl Inda will share the topic for you I will introduce the first part and the rest will be introduced by my colleague okay let's start so kubela is a modern software platform that makes delivering and operating applications across today's hybrid multi-cloud environments easier faster and reliable it is an application-centric control plan and also familiar by the community as implementation of open application models it is a powerful glue engine on the left side it can connect with

### Excerpt da transcript

hello everyone engineer from Alibaba today I and my colleague girl Inda will share the topic for you I will introduce the first part and the rest will be introduced by my colleague okay let's start so kubela is a modern software platform that makes delivering and operating applications across today's hybrid multi-cloud environments easier faster and reliable it is an application-centric control plan and also familiar by the community as implementation of open application models it is a powerful glue engine on the left side it can connect with your traditional CI systems or the modern githubs then it provides infrastructure agnostic layer to render or straight deploy and manage your software and finally deploy to the right side of the picture both kubernetes clusters multi-cloud services or iot Edge scenarios and equivala is a control plan that can provide best practices for your platform engineering on the upside it can expose many ways to manage it provides API CLI and also a very user-friendly UI console and you can use skid Ops to connect with it and it provides fully observability for the whole platform the most important is it has a large catalog of add-ons that can connect to the whole community so here comes a question that why we built covela process improvements over the past two to three decades have significantly increased the eligibility of software application and product teams offering some flexible services for both infrastructure like compute Network and storage as well as develop services like builds tests delivery and obsibility the autonomy and the process Improvement has also has the effect of gradually shifting more and more responsibility for supporting services to protect teams forcing them to spend more and more time and the cognitive energy on infrastructure concerns and reducing their time to produce value relevant to their organization so here is is a workflow that in a usual application delivery pipeline they must need to concern effects workloads for different kinds and they have to learn observability and security details for better stability and avoid risks they need to handle rollout and traffic splitting and learn these complexity infrastructures but all of these things are hard to learn well for example one developer learns the Ingress with V1 beta1 API that can work well as a Gateway in kubernetes 1.21 version but it suddenly failed when the cluster upgraded to 1.22 due to the API duplication they shouldn't care about all
