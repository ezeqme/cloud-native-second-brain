---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Machine Learning + Data"
themes: ["AI ML", "Observability", "Storage Data", "GitOps Delivery"]
speakers: ["Vigith Maurice", "Amit Kalamkar", "Intuit"]
sched_url: https://kccncna2022.sched.com/event/182Hs/observability-in-argocdrollouts-using-streaming-ml-for-reducing-mttr-vigith-maurice-amit-kalamkar-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Observability+In+ArgoCD%2FRollouts+Using+Streaming+ML+For+Reducing+MTTR+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Observability In ArgoCD/Rollouts Using Streaming ML For Reducing MTTR - Vigith Maurice & Amit Kalamkar, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Observability]], [[Storage Data]], [[GitOps Delivery]]
- País/cidade: United States / Detroit
- Speakers: Vigith Maurice, Amit Kalamkar, Intuit
- Schedule: https://kccncna2022.sched.com/event/182Hs/observability-in-argocdrollouts-using-streaming-ml-for-reducing-mttr-vigith-maurice-amit-kalamkar-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Observability+In+ArgoCD%2FRollouts+Using+Streaming+ML+For+Reducing+MTTR+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Observability In ArgoCD/Rollouts Using Streaming ML For Reducing MTTR.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Hs/observability-in-argocdrollouts-using-streaming-ml-for-reducing-mttr-vigith-maurice-amit-kalamkar-intuit
- YouTube search: https://www.youtube.com/results?search_query=Observability+In+ArgoCD%2FRollouts+Using+Streaming+ML+For+Reducing+MTTR+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-YGS1hmd60E
- YouTube title: Observability In ArgoCD/Rollouts Using Streaming ML For Reducing MTTR - Vigith Maurice & A Kalamkar
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/observability-in-argocd-rollouts-using-streaming-ml-for-reducing-mttr/-YGS1hmd60E.txt
- Transcript chars: 24309
- Keywords: streaming, anomaly, change, argo, metrics, application, deployment, processing, platform, canary, stream, rollouts, matrix, meaning, write, systems, operational, whether

### Resumo baseado na transcript

today we wanted to talk how we integrated observability into Argo CD and Argo rollouts which is backed by AI Ops and how that's helping into it reduce mptd and mttr my name is Amit kalamkar I lead observability and analytics at Intuit I have with me visit Morris he is a principal engineer for that that tech tech track here's the agenda for today we will talk about a specific problem that is change induced incident and how we resolved it using aiops we have a demo both for flow you will learn more about this project as we go through the presentation one of the core principles at Intuit is innovation we want to make sure we innovate and We Know It Fast we do over Thousand Villages per day in production and training training such as the data from Prometheus and it stores it in model storage model storage out of the box we do ml flow and training is our overflows but this is how the streaming system works and this has been the streaming system at conceptual streaming system at Intuit for last four years since we have been streaming doing streaming for a while we ran into a couple of challenges to do real-time streaming the problem number one is a lot of boilerplate code for streaming what it

### Excerpt da transcript

today we wanted to talk how we integrated observability into Argo CD and Argo rollouts which is backed by AI Ops and how that's helping into it reduce mptd and mttr my name is Amit kalamkar I lead observability and analytics at Intuit I have with me visit Morris he is a principal engineer for that that tech tech track here's the agenda for today we will talk about a specific problem that is change induced incident and how we resolved it using aiops we have a demo both for Argo CD and Argo rollouts and then we'll talk about Mima paraj which is our open source aios project and how that's powering all this and if time permitting we will do some questions most of you should know into it from our Flagship products QuickBooks Turbo Tax Credit Karma all these products are powered by these five platform areas internally these platform areas ensure that we provide value to customers as well as we accelerate innovation me and widget belongs to developer experiences and platforms our group is responsible for all build time and runtime add into it just to give you a idea about scale we run around 2000 plus services on kubernetes and the investment we have done on modernization of the internal platforms have resulted in 6X Improvement in development velocity at into it into it is very much bought into open source uh we not only use it but we have active contributors and maintenance for a lot of CNC projects including arvo istio and others we are also one of the largest end user company and with the new capability we are open sourcing like new map Raj We are continuing the collaboration with other end user companies let me first start with giving you guys an idea about tech ecosystem at Intuit we started the modernization of this platform in 2018.

we pretty much modernized everything front-end platforms back-end platforms we moved all our container payloads as part of this two kubernetes we also created paved roads both for serverless and services that gave our developers end-to-end determination from commit to deploy as part of this automation we made a deliberate effort to instrument all layers of our platform instead of structure and applications out of box so we get real-time events from all over the place and we store it in the operational data Lake this data we use to derive actionable insight for different areas like operational excellence cost security and so forth to derive this actionable Insight at scale we needed a platform a IRS platform that can scale and
