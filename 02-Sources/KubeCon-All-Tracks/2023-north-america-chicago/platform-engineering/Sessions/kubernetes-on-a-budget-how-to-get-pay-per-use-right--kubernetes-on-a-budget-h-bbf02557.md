---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Vasuki Prasad", "Karim Lakhani", "Intuit"]
sched_url: https://kccncna2023.sched.com/event/1R2vf/kubernetes-on-a-budget-how-to-get-pay-per-use-right-vasuki-prasad-karim-lakhani-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+on+a+Budget%3A+How+to+Get+Pay-per-Use+Right+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kubernetes on a Budget: How to Get Pay-per-Use Right - Vasuki Prasad & Karim Lakhani, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Vasuki Prasad, Karim Lakhani, Intuit
- Schedule: https://kccncna2023.sched.com/event/1R2vf/kubernetes-on-a-budget-how-to-get-pay-per-use-right-vasuki-prasad-karim-lakhani-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+on+a+Budget%3A+How+to+Get+Pay-per-Use+Right+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kubernetes on a Budget: How to Get Pay-per-Use Right.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vf/kubernetes-on-a-budget-how-to-get-pay-per-use-right-vasuki-prasad-karim-lakhani-intuit
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+on+a+Budget%3A+How+to+Get+Pay-per-Use+Right+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=e_juDe90Ftg
- YouTube title: Kubernetes on a Budget: How to Get Pay-per-Use Right - Vasuki Prasad & Karim Lakhani, Intuit
- Match score: 0.825
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kubernetes-on-a-budget-how-to-get-pay-per-use-right/e_juDe90Ftg.txt
- Transcript chars: 32365
- Keywords: cost, capacity, gateway, metrics, cluster, scaling, started, operate, compute, instance, saving, application, requests, target, wanted, running, getting, always

### Resumo baseado na transcript

so hi everyone Welcome to our talk thanks for attending my name is kareim Lani and today we'll be talking about kubernetes on a budget how to get paper use right so as I mentioned I'm kareim Lani I'm a senior staff software engineer at int and I'm here with basuki prad who a staff engineer so our agenda for today we'll be discussing our context our in API Gateway and our journey into Cloud native Technologies be discussing our cost overruns as we migrated our workloads and PR pre-production

### Excerpt da transcript

so hi everyone Welcome to our talk thanks for attending my name is kareim Lani and today we'll be talking about kubernetes on a budget how to get paper use right so as I mentioned I'm kareim Lani I'm a senior staff software engineer at int and I'm here with basuki prad who a staff engineer so our agenda for today we'll be discussing our context our in API Gateway and our journey into Cloud native Technologies be discussing our cost overruns as we migrated our workloads and PR pre-production and then our challenges learnings and solutions and finally we'll close with our takeaways so into it is a fintech company that operates on a large scale as you can see we have over 1 million active cores over 28,000 name spaces over 25,000 services and over 300 kubernetes clusters and we P specifically work on the intu API Gateway so what is our in API Gateway St work it's the front door for all the requests that come into into it and a lot of servico service communication also goes through the in API gway so our service mes Journey started about three years ago but even before that we started our microservices journey and so the in API gway was used for service to service and it continues to be used for a lot of service to service communication so what is the a in an AP gway provider it provides routing Security in the form of authentication and authorization of both the application and the user it produces metrics that are used to feed our golden signals which provides availability error rates for all the services behind API gway as well as it provides detailed access logging of all the requests and responses flowing through our system and finally it provides quality of service features including rate limiting and traffic dialing and a few benefits and stats of our Gateway it's highly scalable at Peak we handle over 30 billion requests per day over 1 million requests per second and our infrastructure is about 30 plus clusters and 250 plus name spaces it's highly available with 49es of availability highly reliable it has to be trusted it has has to be up all the time it has to provide correct metrics it's low latency we target 30 milliseconds of overhead at the P99 and it has deep uh self-service capabilities it's integrated into our developer portal and so onboarding configuration management is all self-service um we're supporting over 2,000 developers uh on using our API Gateway add into it so our in AP Gateway was built in house uh I want to discuss quickly why so
