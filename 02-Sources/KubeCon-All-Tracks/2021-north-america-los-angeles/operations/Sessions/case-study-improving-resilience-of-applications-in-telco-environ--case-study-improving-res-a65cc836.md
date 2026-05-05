---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Operations"
themes: ["SRE Reliability"]
speakers: ["Uma Mukkara", "ChaosNative", "Samar Sidharth", "Orange"]
sched_url: https://kccncna2021.sched.com/event/lV0e/case-study-improving-resilience-of-applications-in-telco-environments-uma-mukkara-chaosnative-samar-sidharth-orange
youtube_search_url: https://www.youtube.com/results?search_query=Case+Study+%3A+Improving+Resilience+of+Applications+in+Telco+Environments+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Case Study : Improving Resilience of Applications in Telco Environments - Uma Mukkara, ChaosNative & Samar Sidharth, Orange

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Operations]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Uma Mukkara, ChaosNative, Samar Sidharth, Orange
- Schedule: https://kccncna2021.sched.com/event/lV0e/case-study-improving-resilience-of-applications-in-telco-environments-uma-mukkara-chaosnative-samar-sidharth-orange
- Busca YouTube: https://www.youtube.com/results?search_query=Case+Study+%3A+Improving+Resilience+of+Applications+in+Telco+Environments+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Case Study : Improving Resilience of Applications in Telco Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV0e/case-study-improving-resilience-of-applications-in-telco-environments-uma-mukkara-chaosnative-samar-sidharth-orange
- YouTube search: https://www.youtube.com/results?search_query=Case+Study+%3A+Improving+Resilience+of+Applications+in+Telco+Environments+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fOgDZfZrFGg
- YouTube title: Case Study : Improving Resilience of Applications in Telco Environme... Uma Mukkara & Samar Sidharth
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/case-study-improving-resilience-of-applications-in-telco-environments/fOgDZfZrFGg.txt
- Transcript chars: 24011
- Keywords: litmus, towards, experiment, application, running, testing, engineering, scenarios, probes, resources, openstack, injection, deleted, applications, created, passed, reliability, native

### Resumo baseado na transcript

hello welcome everyone to kubecon and to this session i am um ceo of chaos native i am also a maintainer on the of project litmus chaos along with me in this session we have a co-speaker summer siddharth from orange today we'll be talking about a case study of chaos engineering project litmus at orange how they're using to improve the resilience of the overall kubernetes based platform so we're going to talk uh the first challenges in general about reliability around kubernetes ecosystem today and i will be

### Excerpt da transcript

hello welcome everyone to kubecon and to this session i am um ceo of chaos native i am also a maintainer on the of project litmus chaos along with me in this session we have a co-speaker summer siddharth from orange today we'll be talking about a case study of chaos engineering project litmus at orange how they're using to improve the resilience of the overall kubernetes based platform so we're going to talk uh the first challenges in general about reliability around kubernetes ecosystem today and i will be talking about how litmus can help in incrementally tackling this challenge of reliability in kubernetes and cloud native environments in general and summer will talk through the challenges that they had seen for reliability in their kubernetes environment and why they chose litmus and how they're using litmus and of course he will be doing a detailed demo of a couple of scenarios so let's talk about uh the resilience in general we all know that uh cloud native is mainstream mighty and it's in deeper option phase so this also brings couple of challenges as far as the resilience or reliability in production or in use is concerned the reason why these challenges occur is there is proliferation of micro services there are too many of them and they are shipping quite fast they come to your environment faster than you would expect so this uh even though they are all individually reliable well tested when you all put together this micro services to form your application service the dependency matrix increases a lot and any fault anywhere really means that you may have a problem of availability in your service so you need to be able to be resilient to all these faulty scenarios that's really the reliability challenge and the solution to this bigger problem is adopt chaos engineering and chaos engineering has been on the rise for the last couple of years we are seeing a lot of people using chaos engineering or project litmus is an evidence to that and we are expecting that chaos engineering will be a mainstream uh solution or a tool set uh in the very near future and uh chaos engineering is being adopted for the overall devops not just for ops which is typically the case uh in the last decade or so but now we see chaos engineering being used uh both in pipelines qa environments uh reliability testing test beds all that stuff performance engineering so chaos engineering is emerging as a greater tool set for developers and devops in general so the whole idea of ch
