---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Observability", "Kubernetes Core"]
speakers: ["Willem Berroubache", "Orange"]
sched_url: https://kccnceu2026.sched.com/event/2CW8F/from-logs-to-decisions-autonomous-ai-agents-for-real-time-kubernetes-threat-response-willem-berroubache-orange
youtube_search_url: https://www.youtube.com/results?search_query=From+Logs+to+Decisions%3A+Autonomous+AI+Agents+for+Real-Time+Kubernetes+Threat+Response+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From Logs to Decisions: Autonomous AI Agents for Real-Time Kubernetes Threat Response - Willem Berroubache, Orange

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Observability]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Willem Berroubache, Orange
- Schedule: https://kccnceu2026.sched.com/event/2CW8F/from-logs-to-decisions-autonomous-ai-agents-for-real-time-kubernetes-threat-response-willem-berroubache-orange
- Busca YouTube: https://www.youtube.com/results?search_query=From+Logs+to+Decisions%3A+Autonomous+AI+Agents+for+Real-Time+Kubernetes+Threat+Response+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From Logs to Decisions: Autonomous AI Agents for Real-Time Kubernetes Threat Response.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW8F/from-logs-to-decisions-autonomous-ai-agents-for-real-time-kubernetes-threat-response-willem-berroubache-orange
- YouTube search: https://www.youtube.com/results?search_query=From+Logs+to+Decisions%3A+Autonomous+AI+Agents+for+Real-Time+Kubernetes+Threat+Response+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XiNsfhUxO2Y
- YouTube title: From Logs to Decisions: Autonomous AI Agents for Real-Time Kubernetes Threat R... Willem Berroubache
- Match score: 0.969
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-logs-to-decisions-autonomous-ai-agents-for-real-time-kubernetes-t/XiNsfhUxO2Y.txt
- Transcript chars: 11050
- Keywords: security, environment, remediation, information, application, threat, improve, solution, cluster, container, response, against, threats, understand, operation, allows, crypto, logs

### Resumo baseado na transcript

In this session we're going to speak about AI agent security Kubernetes of course and how we can use all the solution against threats hacker and so on to protect our environment cluster and customers. Is there some people here who works on security topics and agent topics? So with all these problems we can have some breaches in our infrastructure and this a direct threat for customer trust user data and Orange environment. It could see the pod bridge the security issue but we need to understand to see how we can improve this automatic detection and have immediate remediation. So sometimes security and not only security operation could breaks at scale because we have a lot of logs we have lot of events lot of metrics alarm and so on and we can have some fatigue with because everything could fire. So we need to try the best product the best solution to improve our operation our security operation and detect the threats.

### Excerpt da transcript

In this session we're going to speak about AI agent security Kubernetes of course and how we can use all the solution against threats hacker and so on to protect our environment cluster and customers. Is there some people here who works on security topics and agent topics? No? Okay. Okay, great. So just to quickly introduce myself. I'm William Burbage. I'm working for Orange in Paris. Today I'm an architect. I'm designing some security solution for security monitoring detect threats attackers hackers to protect our customers infrastructure and I'm trying to add some AI security feature to protect and improve the security monitoring this architecture in our environment. In the past I I worked in 5G information system for network edge production Kubernetes cluster and I'm also the trainer for Orange Group one of the different trainer for Orange Group on Kubernetes and cloud native solution. So just a quick disclaimer. All the things you will see during this session is unfortunately if I can say it like that based on different true story and it's not a fairy tale.

So let's start. There is a big gap between what we expect about security from our partners and what we can have in our different environment and we all know this case where some people said yeah we are secure. Yeah, we are cloud native and so on. But if you check if you are looking what you can have behind all this environment solution and so on sometimes you can have legacy stack all feature and if you are going to check and audit what you can have you can for example have a lot of CVs. Okay? So you are going to check exactly how they can deploy the application the animal file the helm chart and so on and trust us sometimes it's not very beautiful. So with all these problems we can have some breaches in our infrastructure and this a direct threat for customer trust user data and Orange environment. So the audit is great. Okay? But runtime monitoring is non-negotiable because the audit say okay you're secure with this release in this version. But you need to prove you're real you're really secure in production.

So okay. During security audit you can check our bug CVs and so on. Okay, but the hackers can try to exploit your application to find some exploit. Okay? And for example destroy your application. So you will check the application the manifest the helm chart all the declarative information to deploy this application but it's just the map. Runtime events are the real world general. So we have
