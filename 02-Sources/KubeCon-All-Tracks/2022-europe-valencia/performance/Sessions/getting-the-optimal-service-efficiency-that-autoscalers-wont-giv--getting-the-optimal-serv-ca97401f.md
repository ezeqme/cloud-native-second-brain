---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Performance"
themes: ["SRE Reliability"]
speakers: ["Mauro Pessina", "Moviri"]
sched_url: https://kccnceu2022.sched.com/event/ytmr/getting-the-optimal-service-efficiency-that-autoscalers-wont-give-you-mauro-pessina-moviri
youtube_search_url: https://www.youtube.com/results?search_query=Getting+the+Optimal+Service+Efficiency+That+Autoscalers+Won%E2%80%99t+Give+You+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Getting the Optimal Service Efficiency That Autoscalers Won’t Give You - Mauro Pessina, Moviri

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Mauro Pessina, Moviri
- Schedule: https://kccnceu2022.sched.com/event/ytmr/getting-the-optimal-service-efficiency-that-autoscalers-wont-give-you-mauro-pessina-moviri
- Busca YouTube: https://www.youtube.com/results?search_query=Getting+the+Optimal+Service+Efficiency+That+Autoscalers+Won%E2%80%99t+Give+You+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Getting the Optimal Service Efficiency That Autoscalers Won’t Give You.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytmr/getting-the-optimal-service-efficiency-that-autoscalers-wont-give-you-mauro-pessina-moviri
- YouTube search: https://www.youtube.com/results?search_query=Getting+the+Optimal+Service+Efficiency+That+Autoscalers+Won%E2%80%99t+Give+You+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Z-G6yMavQrU
- YouTube title: Getting the Optimal Service Efficiency That Autoscalers Won’t Give You - Mauro Pessina, Moviri
- Match score: 0.948
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/getting-the-optimal-service-efficiency-that-autoscalers-wont-give-you/Z-G6yMavQrU.txt
- Transcript chars: 30989
- Keywords: application, configuration, performance, memory, cost, request, limits, container, approach, resource, resources, parameters, baseline, efficiency, optimization, applications, response, higher

### Resumo baseado na transcript

this is mauro pecina and welcome to my session which is getting the optimal service efficiency that auto skaters won't give you these are the contents we will cover today we start by discussing the problem we are going to address and the kubernetes challenges for ensuring application performance and reliability we will then introduce the new approach we implemented in moviri which leverages ai to automate the optimization process and we'll do by they do that by providing real world examples finally we will conclude with the some take or decreased and that multiple parameters at kubernetes and jvm level also need to be tuned accordingly this is a clear clearly a confirmation of the perceived complexity of tuning kubernetes microservices applications as we we're here just discussing just one micro services but think about tuning hundreds of microservices in terms of customer result what did we get uh the red sizing of the service spots allowed a huge cost reduction in the kubernetes environment but where's more we allowed them to automate the tuning of their services or

### Excerpt da transcript

this is mauro pecina and welcome to my session which is getting the optimal service efficiency that auto skaters won't give you these are the contents we will cover today we start by discussing the problem we are going to address and the kubernetes challenges for ensuring application performance and reliability we will then introduce the new approach we implemented in moviri which leverages ai to automate the optimization process and we'll do by they do that by providing real world examples finally we will conclude with the some take away the quiz before proceeding please allow me to introduce myself my name is mauro and i'm the head of performance engineering services align in mobility and performance engineering has always been my passion since i graduated so let's start with a quick introduction about what the problem is as you all know applications are evolving monoliths are quickly disappearing and modern and cloud native applications are features dozens or even hundreds of microservices spanning over a wide set of technologies all these technologies comes with the tunable parameters and option themselves and as a result we must deal with hydrate of on of thousands of possible configurations so how do you find the configuration that that best suits our workload speaking of kubernetes itself there are more and more stories about how difficult it is to ensure performance and stability for kubernetes application as you may have seen also on speeches before mine the kubernetes fellow stories for example is a website that was specifically created to check kubernetes incident reports with the goal to learn how to prevent them many of these stories describe teams that are struggling with kubernetes application performance and stability issues such as unexpected cpu slowdowns or even sudden container termination but why is it so difficult to manage application performance stability and efficiency on kubernetes the simple answer is that kubernetes is a great platform to run containerized applications but it requires applications to be carefully configured to ensure high performance and stability let's now get back to the fundamentals and see how kubernetes resource management works to better understand the main parameters that impact kubernetes application performance stability and cost efficiency we will go through the six main key facts and their implication starting from the first which is resource request you may have heard many talks before mine talking a
